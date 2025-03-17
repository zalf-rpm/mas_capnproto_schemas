#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, List


@dataclass
class SchemaConfig:
    """Configuration for a schema file."""

    output_dir: str
    base_path: str = ""


@dataclass
class PathsConfig:
    """Configuration for file paths."""

    schemas_dir: str
    output_base: str


@dataclass
class CompilerConfig:
    """Configuration for the Cap'n Proto compiler."""

    schemas: Dict[str, SchemaConfig]
    paths: PathsConfig
    presets: Dict[str, List[str]]


def load_config(config_path: Path) -> CompilerConfig:
    """Load and parse the configuration file."""
    if not config_path.exists():
        print(f"Configuration file {config_path} not found!")
        sys.exit(1)

    try:
        with config_path.open("r") as f:
            config_data = json.load(f)

        # Parse schema configs
        schemas = {
            key: SchemaConfig(
                output_dir=schema_data.get("output_dir", ""),
                base_path=schema_data.get("base_path", ""),
            )
            for key, schema_data in config_data.get("schemas", {}).items()
        }

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


def compile_schema(
    schema: str,
    lang: str,
    capnp_bin: str,
    schema_config: SchemaConfig,
    config: CompilerConfig,
) -> None:
    """Compile a Cap'n Proto schema file."""
    # Create paths
    schema_dir = Path(config.paths.schemas_dir)
    output_dir = Path(config.paths.output_base) / lang
    if schema_config.output_dir:
        output_dir /= schema_config.output_dir

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Handle schema path and source prefix
    src_prefix = schema_dir
    if schema_config.base_path:
        src_prefix /= schema_config.base_path
        schema_path = Path(schema_config.base_path) / schema
    else:
        schema_path = schema

    full_schema_path = schema_dir / schema_path

    cmd = [
        capnp_bin,
        "compile",
        f"-I{schema_dir}",
        f"--src-prefix={src_prefix}",
        f"-o{lang}:{output_dir}",
        f"{full_schema_path}",
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully compiled {schema_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {schema_path}: {e}")


def find_executable_path(name: str) -> Optional[str]:
    """Find the full path of an executable.

    Args:
        name: Name of the executable to find

    Returns:
        The full path to the executable or None if not found
    """
    try:
        return subprocess.check_output(["which", name]).decode().strip()
    except subprocess.CalledProcessError:
        return None


def main() -> None:
    """Main entry point for the Cap'n Proto schema compiler."""
    parser = argparse.ArgumentParser(description="Compile Cap'n Proto schema files")
    parser.add_argument(
        "--lang",
        "-l",
        nargs="+",
        choices=["c++", "csharp", "go", "java"],
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
    all_available_files = set(config.schemas.keys())
    if args.preset:
        preset_files = config.presets.get(args.preset, [])
        files_to_compile = set(preset_files)
    else:
        files_to_compile = set(args.files) if args.files else all_available_files

    # Validate requested files
    invalid_files = files_to_compile - all_available_files
    if invalid_files:
        for file in invalid_files:
            print(f"Warning: '{file}' not found in configuration file")

    # Get valid files to compile
    valid_files = files_to_compile & all_available_files

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

        # Compile schemas
        for file in valid_files:
            schema_config = config.schemas[file]
            compile_schema(file, lang, capnp_bin, schema_config, config)


if __name__ == "__main__":
    main()
