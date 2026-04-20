from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
import re
import shutil
from typing import Iterable

from . import __version__

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "starter"
PACKAGED_DEV_SOP_DIR = PurePosixPath("dev_sop")
VERSION_FILE = PurePosixPath(".dev_sop/VERSION.md")

SEED_ONLY_FILES = {
    PurePosixPath("README.md"),
    PurePosixPath(".dev_sop/control/CURRENT.md"),
    PurePosixPath(".dev_sop/control/DOC_MAP.md"),
    PurePosixPath(".dev_sop/project-rules/README.md"),
    PurePosixPath(".dev_sop/project-rules/rule-index.md"),
    PurePosixPath(".dev_sop/project-rules/exceptions.md"),
    PurePosixPath(".dev_sop/project-specs/README.md"),
    PurePosixPath(".dev_sop/project-facts/README.md"),
}
MANAGED_ROOT_FILES = {
    PurePosixPath("AGENTS.md"),
    PurePosixPath("CLAUDE.md"),
    PurePosixPath(".dev_sop/README.md"),
}
MANAGED_DIR_PREFIXES = (
    PurePosixPath(".dev_sop/core"),
    PurePosixPath(".dev_sop/upgrades"),
)
VERSION_RE = re.compile(r"`(\d+\.\d+\.\d+)`")
UPGRADE_RE = re.compile(r"v(\d+\.\d+\.\d+)\.md$")


@dataclass
class OperationReport:
    command: str
    target: Path
    starter_version: str
    target_version: str | None = None
    created: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    version_updated: bool = False
    applicable_upgrades: list[str] = field(default_factory=list)

    @property
    def has_conflicts(self) -> bool:
        return bool(self.conflicts)


def starter_root() -> Path:
    if not ASSET_ROOT.exists():
        raise FileNotFoundError(f"Packaged starter assets not found: {ASSET_ROOT}")
    return ASSET_ROOT


def iter_starter_files() -> Iterable[PurePosixPath]:
    root = starter_root()
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield _target_relative_from_asset(PurePosixPath(path.relative_to(root).as_posix()))


def read_asset_text(relative_path: PurePosixPath) -> str:
    return _source_path(relative_path).read_text(encoding="utf-8")


def read_starter_version() -> str:
    version = extract_version(read_asset_text(VERSION_FILE))
    if version != __version__:
        raise ValueError(
            "Packaged starter version mismatch: "
            f"package={__version__}, assets={version}"
        )
    return version


def read_target_version(target_root: Path) -> str | None:
    path = target_root / Path(VERSION_FILE.as_posix())
    if not path.exists():
        return None
    return extract_version(path.read_text(encoding="utf-8"))


def extract_version(text: str) -> str:
    match = VERSION_RE.search(text)
    if not match:
        raise ValueError("Could not extract semantic version from VERSION.md")
    return match.group(1)


def version_key(version: str) -> tuple[int, int, int]:
    parts = version.split(".")
    return tuple(int(part) for part in parts)  # type: ignore[return-value]


def starter_upgrade_notes() -> list[str]:
    notes_dir = _source_path(PurePosixPath(".dev_sop/upgrades"))
    notes: list[str] = []
    for path in sorted(notes_dir.glob("v*.md")):
        match = UPGRADE_RE.fullmatch(path.name)
        if match:
            notes.append(match.group(1))
    return sorted(notes, key=version_key)


def applicable_upgrade_notes(target_version: str | None, starter_version: str) -> list[str]:
    if target_version is None:
        return [f"v{version}.md" for version in starter_upgrade_notes()]
    current = version_key(target_version)
    latest = version_key(starter_version)
    if current >= latest:
        return []
    return [
        f"v{version}.md"
        for version in starter_upgrade_notes()
        if current < version_key(version) <= latest
    ]


def classify_update_path(relative_path: PurePosixPath) -> str:
    if relative_path == VERSION_FILE:
        return "version"
    if relative_path in SEED_ONLY_FILES:
        return "seed"
    if relative_path in MANAGED_ROOT_FILES:
        return "managed"
    if any(_is_relative_to(relative_path, prefix) for prefix in MANAGED_DIR_PREFIXES):
        return "managed"
    raise ValueError(f"Unhandled starter path in update manifest: {relative_path}")


def init_target(target_root: Path, *, force: bool = False, dry_run: bool = False) -> OperationReport:
    starter_version = read_starter_version()
    target_root.mkdir(parents=True, exist_ok=True)
    report = OperationReport(
        command="init",
        target=target_root,
        starter_version=starter_version,
        target_version=read_target_version(target_root),
    )
    for relative_path in iter_starter_files():
        source = _source_path(relative_path)
        destination = target_root / Path(relative_path.as_posix())
        if not destination.exists():
            _write_file(source, destination, dry_run=dry_run)
            report.created.append(relative_path.as_posix())
            continue
        if _same_file(source, destination):
            report.unchanged.append(relative_path.as_posix())
            continue
        if force:
            _write_file(source, destination, dry_run=dry_run)
            report.updated.append(relative_path.as_posix())
        else:
            report.skipped.append(relative_path.as_posix())
    return report


def update_target(
    target_root: Path,
    *,
    force: bool = False,
    force_seed: bool = False,
    dry_run: bool = False,
) -> OperationReport:
    starter_version = read_starter_version()
    target_root.mkdir(parents=True, exist_ok=True)
    current_version = read_target_version(target_root)
    report = OperationReport(
        command="update",
        target=target_root,
        starter_version=starter_version,
        target_version=current_version,
        applicable_upgrades=applicable_upgrade_notes(current_version, starter_version),
    )

    for relative_path in iter_starter_files():
        classification = classify_update_path(relative_path)
        if classification == "version":
            continue

        source = _source_path(relative_path)
        destination = target_root / Path(relative_path.as_posix())

        if not destination.exists():
            _write_file(source, destination, dry_run=dry_run)
            report.created.append(relative_path.as_posix())
            continue

        if _same_file(source, destination):
            report.unchanged.append(relative_path.as_posix())
            continue

        if classification == "seed":
            if force_seed:
                _write_file(source, destination, dry_run=dry_run)
                report.updated.append(relative_path.as_posix())
            else:
                report.skipped.append(relative_path.as_posix())
            continue

        if force:
            _write_file(source, destination, dry_run=dry_run)
            report.updated.append(relative_path.as_posix())
        else:
            report.conflicts.append(relative_path.as_posix())

    if not report.has_conflicts or force:
        source = _source_path(VERSION_FILE)
        destination = target_root / Path(VERSION_FILE.as_posix())
        if not destination.exists():
            _write_file(source, destination, dry_run=dry_run)
            report.created.append(VERSION_FILE.as_posix())
        elif not _same_file(source, destination):
            _write_file(source, destination, dry_run=dry_run)
            report.updated.append(VERSION_FILE.as_posix())
        else:
            report.unchanged.append(VERSION_FILE.as_posix())
        report.version_updated = True

    return report


def format_report(report: OperationReport) -> str:
    lines = [
        f"{report.command} target: {report.target}",
        f"starter version: {report.starter_version}",
    ]
    if report.command == "update":
        lines.append(f"target version: {report.target_version or 'unversioned'}")
        if report.applicable_upgrades:
            lines.append("applicable upgrade notes: " + ", ".join(report.applicable_upgrades))
        else:
            lines.append("applicable upgrade notes: none")

    lines.extend(
        [
            f"created: {len(report.created)}",
            f"updated: {len(report.updated)}",
            f"unchanged: {len(report.unchanged)}",
            f"skipped: {len(report.skipped)}",
            f"conflicts: {len(report.conflicts)}",
        ]
    )

    if report.skipped:
        lines.append("skipped existing files:")
        lines.extend(f"  - {path}" for path in report.skipped[:20])
        if len(report.skipped) > 20:
            lines.append(f"  - ... and {len(report.skipped) - 20} more")

    if report.conflicts:
        lines.append("conflicting starter-owned files:")
        lines.extend(f"  - {path}" for path in report.conflicts[:20])
        if len(report.conflicts) > 20:
            lines.append(f"  - ... and {len(report.conflicts) - 20} more")
        lines.append("rerun with --force to overwrite starter-owned files.")

    if report.command == "update" and not report.version_updated:
        lines.append("VERSION.md was not updated because starter-owned conflicts remain.")

    return "\n".join(lines)


def _write_file(source: Path, destination: Path, *, dry_run: bool) -> None:
    if dry_run:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def _same_file(source: Path, destination: Path) -> bool:
    return source.read_bytes() == destination.read_bytes()


def _is_relative_to(path: PurePosixPath, prefix: PurePosixPath) -> bool:
    try:
        path.relative_to(prefix)
        return True
    except ValueError:
        return False


def _source_path(relative_path: PurePosixPath) -> Path:
    return starter_root() / Path(_asset_relative_from_target(relative_path).as_posix())


def _asset_relative_from_target(relative_path: PurePosixPath) -> PurePosixPath:
    if _is_relative_to(relative_path, PurePosixPath(".dev_sop")):
        suffix = relative_path.relative_to(PurePosixPath(".dev_sop"))
        return PACKAGED_DEV_SOP_DIR / suffix
    return relative_path


def _target_relative_from_asset(relative_path: PurePosixPath) -> PurePosixPath:
    if _is_relative_to(relative_path, PACKAGED_DEV_SOP_DIR):
        suffix = relative_path.relative_to(PACKAGED_DEV_SOP_DIR)
        return PurePosixPath(".dev_sop") / suffix
    return relative_path
