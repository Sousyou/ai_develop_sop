from __future__ import annotations

import argparse
from pathlib import Path
import sys

from . import __version__
from .starter import format_report, init_target, read_starter_version, read_target_version, update_target


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
    init_parser.add_argument(
        "--with-sandbox",
        "--with-sanbox",
        dest="with_sandbox",
        action="store_true",
        help="Also create a root sandbox/ directory for isolated tests or experiments.",
    )
    init_parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    init_parser.add_argument("--yes", action="store_true", help="Skip the interactive confirmation prompt.")
    init_parser.set_defaults(handler=handle_init)

    update_parser = subparsers.add_parser("update", help="Update starter-owned SOP assets in a target directory.")
    update_parser.add_argument("target", nargs="?", default=".", help="Target directory. Defaults to the current directory.")
    update_parser.add_argument(
        "--force",
        action="store_true",
        help="Fallback to full overwrite when a standardized entrypoint merge cannot be applied cleanly.",
    )
    update_parser.add_argument(
        "--force-seed",
        action="store_true",
        help="Also overwrite project-owned seed files such as control files and project rule indexes.",
    )
    update_parser.add_argument(
        "--with-sandbox",
        "--with-sanbox",
        dest="with_sandbox",
        action="store_true",
        help="Also create a root sandbox/ directory for isolated tests or experiments.",
    )
    update_parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files.")
    update_parser.add_argument("--yes", action="store_true", help="Skip the interactive confirmation prompt.")
    update_parser.set_defaults(handler=handle_update)

    return parser


def handle_version(_args: argparse.Namespace) -> int:
    print(read_starter_version())
    return 0


def handle_init(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    starter_version = read_starter_version()
    target_version = read_target_version(target)
    if not confirm_operation(
        command="init",
        target=target,
        starter_version=starter_version,
        target_version=target_version,
        force=args.force,
        force_seed=False,
        dry_run=args.dry_run,
        with_sandbox=args.with_sandbox,
        assume_yes=args.yes,
    ):
        return 1
    report = init_target(
        target,
        force=args.force,
        dry_run=args.dry_run,
        with_sandbox=args.with_sandbox,
    )
    print(format_report(report))
    return 2 if report.has_conflicts else 0


def handle_update(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    starter_version = read_starter_version()
    target_version = read_target_version(target)
    if not confirm_operation(
        command="update",
        target=target,
        starter_version=starter_version,
        target_version=target_version,
        force=args.force,
        force_seed=args.force_seed,
        dry_run=args.dry_run,
        with_sandbox=args.with_sandbox,
        assume_yes=args.yes,
    ):
        return 1
    report = update_target(
        target,
        force=args.force,
        force_seed=args.force_seed,
        dry_run=args.dry_run,
        with_sandbox=args.with_sandbox,
    )
    print(format_report(report))
    return 2 if report.has_conflicts else 0


def confirm_operation(
    *,
    command: str,
    target: Path,
    starter_version: str,
    target_version: str | None,
    force: bool,
    force_seed: bool,
    dry_run: bool,
    with_sandbox: bool,
    assume_yes: bool,
) -> bool:
    if assume_yes:
        return True
    if not sys.stdin.isatty():
        print(
            "This command requires interactive confirmation. Re-run with --yes to skip the prompt.",
            file=sys.stderr,
        )
        return False

    print(f"About to run: dev-sop {command}")
    print(f"Target: {target}")
    print(f"Starter SOP version: {starter_version}")
    print(f"Target SOP version: {target_version or 'unversioned'}")
    print(
        "Workspace directories: "
        + ("product/, dev/, sandbox/" if with_sandbox else "product/, dev/")
    )
    print(f"Force overwrite: {'yes' if force else 'no'}")
    if command == "update":
        print(f"Force seed overwrite: {'yes' if force_seed else 'no'}")
    print(f"Dry run: {'yes' if dry_run else 'no'}")
    response = input("Proceed? [y/N]: ").strip().lower()
    if response in {"y", "yes"}:
        return True
    print("Cancelled.")
    return False


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
