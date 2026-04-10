#!/usr/bin/env python3

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PathsConfig:
    """Configuration for file paths."""

    schemas_dir: str
    output_base: str


@dataclass
class CompilerConfig:
    """Configuration for the Cap'n Proto compiler."""

    schemas: list[str]
    paths: PathsConfig
    preserved_outputs: dict[str, list[str]]
    presets: dict[str, list[str]]


def is_preserved_output(
    path: Path,
    output_dir: Path,
    lang: str,
    config: CompilerConfig,
) -> bool:
    """Return whether the path should survive output cleanup."""
    relative_path = path.relative_to(output_dir)
    for preserved_output in config.preserved_outputs.get(lang, []):
        preserved_path = Path(preserved_output)
        if relative_path == preserved_path or relative_path.is_relative_to(preserved_path):
            return True
    return False


def remove_path(path: Path) -> None:
    """Remove a file or directory tree."""
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def prune_empty_parents(
    path: Path,
    output_dir: Path,
    lang: str,
    config: CompilerConfig,
) -> None:
    """Remove empty parent directories up to the language output root."""
    current = path.parent
    while current != output_dir and current.exists():
        if is_preserved_output(current, output_dir, lang, config) or any(current.iterdir()):
            break
        current.rmdir()
        current = current.parent


def remove_python_cache_entries(output_dir: Path) -> None:
    """Drop Python cache artifacts, including those below preserved shim packages."""
    for cache_dir in list(output_dir.rglob("__pycache__")):
        shutil.rmtree(cache_dir, ignore_errors=True)

    for pyc_file in list(output_dir.rglob("*.pyc")):
        pyc_file.unlink(missing_ok=True)


def schema_relative_path(schema: str, schema_dir: Path, use_relative_paths: bool) -> Path:
    """Normalize a schema path to a path relative to the schema root."""
    schema_path = Path(schema)
    if not use_relative_paths:
        return schema_path

    if schema_path.is_absolute():
        return schema_path.relative_to(schema_dir.resolve())

    try:
        return schema_path.relative_to(schema_dir)
    except ValueError:
        return schema_path


def generated_paths_for_schema(schema: Path, lang: str, output_dir: Path) -> list[Path]:
    """Return generated paths that can be safely removed for a schema subset build."""
    if lang == "c++":
        return [
            output_dir / schema.with_suffix(".capnp.h"),
            output_dir / schema.with_suffix(".capnp.c++"),
        ]

    if lang == "csharp":
        return [output_dir / schema.with_suffix(".capnp.cs")]

    if lang == "go":
        return [output_dir / schema.with_suffix(".capnp.go")]

    if lang == "capnp_offsets":
        return [output_dir / schema]

    if lang == "python":
        module_name = f"{schema.stem}_capnp"
        return [
            output_dir / "mas" / "schema" / schema.parent / module_name,
            output_dir / schema.parent / module_name,
        ]

    return []


def prepare_output_dir(
    schemas: list[str],
    lang: str,
    config: CompilerConfig,
    use_relative_paths: bool,
    clean_all_outputs: bool,
) -> None:
    """Remove stale generated output before regenerating."""
    output_dir = Path(config.paths.output_base) / lang
    output_dir.mkdir(parents=True, exist_ok=True)

    if clean_all_outputs:
        print(f"Cleaning generated output in {output_dir}")
        for child in output_dir.iterdir():
            if is_preserved_output(child, output_dir, lang, config):
                continue
            remove_path(child)
    else:
        print(f"Cleaning stale generated files in {output_dir}")
        schema_dir = Path(config.paths.schemas_dir)
        for schema in schemas:
            relative_schema = schema_relative_path(schema, schema_dir, use_relative_paths)
            for generated_path in generated_paths_for_schema(relative_schema, lang, output_dir):
                if generated_path.exists():
                    remove_path(generated_path)
                    prune_empty_parents(generated_path, output_dir, lang, config)

    if lang == "python":
        remove_python_cache_entries(output_dir)


def refresh_go_module(output_dir: Path, go_bin: str) -> bool:
    """Refresh the preserved Go module metadata after code generation."""
    go_mod_file = output_dir / "go.mod"
    if not go_mod_file.exists():
        print(f"Error: Go module file {go_mod_file} not found")
        return False

    with tempfile.TemporaryDirectory(prefix="capnp-go-") as temp_dir:
        temp_root = Path(temp_dir)
        env = os.environ.copy()
        env["HOME"] = str(temp_root / "home")
        env["GOCACHE"] = str(temp_root / "gocache")
        env["GOPATH"] = str(temp_root / "gopath")
        env["GOMODCACHE"] = str(Path(env["GOPATH"]) / "pkg" / "mod")

        for env_var in ("HOME", "GOCACHE", "GOPATH", "GOMODCACHE"):
            Path(env[env_var]).mkdir(parents=True, exist_ok=True)

        try:
            subprocess.run([go_bin, "mod", "tidy"], cwd=output_dir, check=True, env=env)
            print(f"Updated Go module metadata in {output_dir}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error updating Go module metadata: {e}")
            return False


def load_config(config_path: Path) -> CompilerConfig:
    """Load and parse the configuration file."""
    if not config_path.exists():
        print(f"Configuration file {config_path} not found!")
        sys.exit(1)

    try:
        with config_path.open("r") as f:
            config_data = json.load(f)

        # Get list of schema files
        schemas = list(config_data.get("schemas", []))

        # Parse paths config
        paths_data = config_data.get("paths", {})
        paths = PathsConfig(
            schemas_dir=paths_data.get("schemas_dir", "zalfmas_capnp_schemas"),
            output_base=paths_data.get("output_base", "gen"),
        )

        return CompilerConfig(
            schemas=schemas,
            paths=paths,
            preserved_outputs={
                lang: list(outputs)
                for lang, outputs in config_data.get("preserved_outputs", {}).items()
            },
            presets=config_data.get("presets", {}),
        )
    except json.JSONDecodeError as e:
        print(f"Error parsing config file: {e}")
        sys.exit(1)


def compile_schemas(
    schemas: list[str],
    lang: str,
    capnp_bin: str,
    config: CompilerConfig,
    use_relative_paths: bool = False,
    clean_all_outputs: bool = False,
) -> bool:
    """Compile Cap'n Proto schema files."""
    schema_dir = Path(config.paths.schemas_dir)
    output_dir = Path(config.paths.output_base) / lang

    prepare_output_dir(schemas, lang, config, use_relative_paths, clean_all_outputs)

    # Build list of schema paths
    if use_relative_paths:
        # Files are already relative paths from execution directory
        schema_paths = schemas
    else:
        # Build paths from schemas_dir
        schema_paths = [str(schema_dir / schema) for schema in schemas]

    # capnp_offsets uses built-in -ocapnp which outputs to stdout,
    # so compile each file individually and redirect output
    if lang == "capnp_offsets":
        for schema_path in schema_paths:
            # Determine relative path structure for output
            if use_relative_paths:
                schema_file = Path(schema_path)
            else:
                schema_file = Path(schema_path).relative_to(schema_dir)

            # Create output file path (preserve directory structure)
            output_file = output_dir / schema_file
            output_file.parent.mkdir(parents=True, exist_ok=True)

            cmd = [
                capnp_bin,
                "compile",
                f"-I{schema_dir}",
                f"--src-prefix={schema_dir}",
                "-ocapnp",
                schema_path,
            ]

            try:
                with output_file.open("w") as f:
                    subprocess.run(cmd, check=True, stdout=f)
            except subprocess.CalledProcessError as e:
                print(f"Error compiling {schema_path}: {e}")
                return False
        print(f"Successfully compiled {len(schemas)} schema(s)")
        return True
    else:
        # Standard plugin-based compilation
        cmd = [
            capnp_bin,
            "compile",
            f"-I{schema_dir}",
            f"--src-prefix={schema_dir}",
            f"-o{lang}:{output_dir}",
        ] + schema_paths

        try:
            subprocess.run(cmd, check=True)
            print(f"Successfully compiled {len(schemas)} schema(s)")
        except subprocess.CalledProcessError as e:
            print(f"Error compiling schemas: {e}")
            return False

    return True


def find_executable_path(name: str) -> str | None:
    """Find the full path of an executable.

    Args:
        name: Name of the executable to find

    Returns:
        The full path to the executable or None if not found

    """
    try:
        return (
            subprocess.check_output(
                ["which" if sys.platform == "linux" else "where", name],
            )
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        return None


def main() -> None:
    """Main entry point for the Cap'n Proto schema compiler."""
    parser = argparse.ArgumentParser(description="Compile Cap'n Proto schema files")
    parser.add_argument(
        "--lang",
        "-l",
        nargs="+",
        choices=["c++", "csharp", "go", "java", "python", "capnp_offsets"],
        required=True,
        help="Target language(s) to compile for",
    )

    parser.add_argument(
        "--config",
        "-c",
        type=str,
        default="capnp_compile_config.json",
        help="Path to the configuration file (default: capnp_compile_config.json)",
    )

    # Create mutually exclusive group for file selection
    file_selection = parser.add_mutually_exclusive_group()
    file_selection.add_argument(
        "--files",
        "-f",
        nargs="*",
        help="Specific schema files to compile (if omitted, compiles all)",
    )
    file_selection.add_argument(
        "--preset",
        "-p",
        help="Preset of schema files to compile as defined in the config",
    )

    args = parser.parse_args()

    # Load configuration
    config_path = Path(args.config)
    config = load_config(config_path)

    # Determine which files to compile
    use_relative_paths = False
    if args.preset:
        # Use preset from config
        preset_files = config.presets.get(args.preset, [])
        if not preset_files:
            print(f"Error: Preset '{args.preset}' not found in configuration")
            sys.exit(1)
        files_to_compile = preset_files
    elif args.files:
        # Files passed via --files are relative paths from execution directory
        files_to_compile = args.files
        use_relative_paths = True
    else:
        # No files or preset specified, compile all from config
        files_to_compile = config.schemas

    clean_all_outputs = not args.files and not args.preset

    # Compile for each specified language
    failed_languages: list[str] = []
    for lang in args.lang:
        print(f"\nCompiling for language: {lang}")

        # Get compiler paths
        capnp_bin = "capnp"

        # Check compiler paths
        capnp_path = find_executable_path(capnp_bin)

        if not capnp_path:
            print(f"Error: Could not locate '{capnp_bin}' executable")
            failed_languages.append(lang)
            continue

        print(f"Using capnp at: {capnp_path}")

        # capnp_offsets uses built-in -ocapnp, no plugin needed
        if lang != "capnp_offsets":
            capnpc_path = find_executable_path(f"capnpc-{lang}")

            if not capnpc_path:
                print(f"Error: Could not locate 'capnpc-{lang}' executable")
                failed_languages.append(lang)
                continue

            print(f"Using capnpc-{lang} at: {capnpc_path}")

        go_bin = None
        if lang == "go":
            go_bin = find_executable_path("go")
            if not go_bin:
                print("Error: Could not locate 'go' executable")
                failed_languages.append(lang)
                continue

            print(f"Using go at: {go_bin}")

        if not compile_schemas(
            files_to_compile,
            lang,
            capnp_bin,
            config,
            use_relative_paths,
            clean_all_outputs,
        ):
            failed_languages.append(lang)
            continue

        if lang == "go" and go_bin:
            go_output_dir = Path(config.paths.output_base) / lang
            if not refresh_go_module(go_output_dir, go_bin):
                failed_languages.append(lang)

    if failed_languages:
        sys.exit(1)


if __name__ == "__main__":
    main()
