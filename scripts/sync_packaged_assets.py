from __future__ import annotations

from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = REPO_ROOT / "src" / "dev_sop_cli" / "assets" / "starter"
PACKAGED_ROOT_README = Path(__file__).resolve().parent / "packaged-root-README.md"
PRODUCT_ROOT = REPO_ROOT / "product"


def main() -> None:
    if ASSET_ROOT.exists():
        shutil.rmtree(ASSET_ROOT)

    ASSET_ROOT.mkdir(parents=True, exist_ok=True)

    for name in ("AGENTS.md", "CLAUDE.md", "README.md"):
        source = REPO_ROOT / name
        if name == "README.md":
            source = PACKAGED_ROOT_README
        shutil.copyfile(source, ASSET_ROOT / name)

    shutil.copytree(PRODUCT_ROOT, ASSET_ROOT / "dev_sop")

    backup_dir = ASSET_ROOT / "dev_sop" / "_backup"
    if backup_dir.exists():
        shutil.rmtree(backup_dir)


if __name__ == "__main__":
    main()
