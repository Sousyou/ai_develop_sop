from __future__ import annotations

import argparse
from pathlib import Path
import sys

from . import __version__
from .starter import format_report, init_target, read_starter_version, update_target


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dev-sop",
        description="Initialize or update the AI Engineering SOP starter in a target directory.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    version_parser = subparsers.add_parser("version", help="Print the packaged starter version.")
    version_parser.set_defaults(handler=handle_version)

    init_parser = subparsers.add_parser("init", help="Copy the starter surface into a target directory.")
    init_parser.add_argument("target", nargs="?", default=".", help="Target directory. Defaults to the current directory.")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing files instead of skipping them.")
    init_parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    init_parser.set_defaults(handler=handle_init)

    update_parser = subparsers.add_parser("update", help="Update starter-owned SOP assets in a target directory.")
    update_parser.add_argument("target", nargs="?", default=".", help="Target directory. Defaults to the current directory.")
    update_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite conflicting starter-owned files such as AGENTS.md or files under .dev_sop/core/.",
    )
    update_parser.add_argument(
        "--force-seed",
        action="store_true",
        help="Also overwrite seed files such as control and project-surface README files.",
    )
    update_parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    update_parser.set_defaults(handler=handle_update)

    return parser


def handle_version(_args: argparse.Namespace) -> int:
    print(read_starter_version())
    return 0


def handle_init(args: argparse.Namespace) -> int:
    report = init_target(Path(args.target).resolve(), force=args.force, dry_run=args.dry_run)
    print(format_report(report))
    return 0


def handle_update(args: argparse.Namespace) -> int:
    report = update_target(
        Path(args.target).resolve(),
        force=args.force,
        force_seed=args.force_seed,
        dry_run=args.dry_run,
    )
    print(format_report(report))
    return 2 if report.has_conflicts and not args.force else 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
