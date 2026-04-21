from __future__ import annotations

import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from dev_sop_cli.cli import build_parser  # noqa: E402
from dev_sop_cli.starter import init_target, update_target  # noqa: E402


class StarterWorkspaceLayoutTests(unittest.TestCase):
    def test_init_creates_default_workspace_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)

            report = init_target(target)

            self.assertTrue((target / "product").is_dir())
            self.assertTrue((target / "dev").is_dir())
            self.assertFalse((target / "sandbox").exists())
            self.assertIn("product/", report.created_workspace_directories)
            self.assertIn("dev/", report.created_workspace_directories)

    def test_init_creates_sandbox_when_requested(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)

            report = init_target(target, with_sandbox=True)

            self.assertTrue((target / "sandbox").is_dir())
            self.assertIn("sandbox/", report.created_workspace_directories)

    def test_update_backfills_missing_workspace_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)

            report = update_target(target)

            self.assertTrue((target / "product").is_dir())
            self.assertTrue((target / "dev").is_dir())
            self.assertFalse((target / "sandbox").exists())
            self.assertTrue(report.version_updated)

    def test_existing_file_blocks_workspace_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)
            (target / "product").write_text("blocking file", encoding="utf-8")

            report = init_target(target)

            self.assertIn("product/", report.workspace_directory_conflicts)
            self.assertTrue(report.has_conflicts)

    def test_cli_accepts_canonical_sandbox_flag(self) -> None:
        parser = build_parser()

        init_args = parser.parse_args(["init", ".", "--with-sandbox"])
        update_args = parser.parse_args(["update", ".", "--with-sandbox"])

        self.assertTrue(init_args.with_sandbox)
        self.assertTrue(update_args.with_sandbox)

    def test_cli_rejects_legacy_flag_with_migration_hint(self) -> None:
        parser = build_parser()

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as context:
                parser.parse_args(["init", ".", "--with-sanbox"])

        self.assertEqual(context.exception.code, 2)
        message = stderr.getvalue()
        self.assertIn("--with-sanbox", message)
        self.assertIn("--with-sandbox", message)
        self.assertIn("no longer supported", message)


if __name__ == "__main__":
    unittest.main()
