#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
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
    presets: dict[str, list[str]]


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
) -> None:
    """Compile Cap'n Proto schema files in a single call."""
    schema_dir = Path(config.paths.schemas_dir)
    output_dir = Path(config.paths.output_base) / lang

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build list of schema paths
    if use_relative_paths:
        # Files are already relative paths from execution directory
        schema_paths = schemas
    else:
        # Build paths from schemas_dir
        schema_paths = [str(schema_dir / schema) for schema in schemas]

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
        choices=["c++", "csharp", "go", "java", "python"],
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
    config_path = Path("capnp_compile_config.json")
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

    # Compile for each specified language
    for lang in args.lang:
        print(f"\nCompiling for language: {lang}")

        # Get compiler paths
        capnp_bin = "capnp"

        # Check compiler paths
        capnp_path = find_executable_path(capnp_bin)
        capnpc_path = find_executable_path(f"capnpc-{lang}")

        if not capnp_path:
            print(f"Error: Could not locate '{capnp_bin}' executable")
            continue

        if not capnpc_path:
            print(f"Error: Could not locate 'capnpc-{lang}' executable")
            continue

        print(f"Using capnp at: {capnp_path}")
        print(f"Using capnpc-{lang} at: {capnpc_path}")

        # Compile all schemas in a single call
        compile_schemas(files_to_compile, lang, capnp_bin, config, use_relative_paths)


if __name__ == "__main__":
    main()
