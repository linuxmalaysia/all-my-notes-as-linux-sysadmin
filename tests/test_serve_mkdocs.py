"""Unit tests for scripts/serve_mkdocs.py.

This module verifies the cross-platform symlink/hardlink helper functions
and the docs_dir preparation + MkDocs invocation logic introduced to support
Linux (POSIX) symlinks in addition to the existing Windows junction/hardlink
behaviour.
"""

import importlib.util
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "serve_mkdocs.py"


def _load_module():
    """Dynamically import scripts/serve_mkdocs.py as a standalone module.

    The script is a standalone `uv` script (not part of a package), so it is
    loaded via importlib rather than a normal package import.
    """
    spec = importlib.util.spec_from_file_location("serve_mkdocs", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def serve_mkdocs():
    return _load_module()


def _is_link_or_junction(path: Path) -> bool:
    """Helper to check if a path is a symlink or junction across Windows and POSIX."""
    if path.is_symlink():
        return True
    if hasattr(path, "is_junction") and path.is_junction():
        return True
    return False


# ---------------------------------------------------------------------------
# create_junction
# ---------------------------------------------------------------------------

class TestCreateJunction:
    def test_creates_symlink_when_dest_missing(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_dir"
        src.mkdir()
        dest = tmp_path / "dest_link"

        serve_mkdocs.create_junction(src, dest)

        assert _is_link_or_junction(dest)
        assert dest.resolve() == src.resolve()

    def test_replaces_existing_symlink_dest(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_dir"
        src.mkdir()
        other = tmp_path / "other_dir"
        other.mkdir()
        dest = tmp_path / "dest_link"
        serve_mkdocs.create_junction(other, dest)

        serve_mkdocs.create_junction(src, dest)

        assert _is_link_or_junction(dest)
        assert dest.resolve() == src.resolve()

    def test_removes_existing_file_dest(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_dir"
        src.mkdir()
        dest = tmp_path / "dest_file"
        dest.write_text("stale content")

        serve_mkdocs.create_junction(src, dest)

        assert _is_link_or_junction(dest)
        assert dest.resolve() == src.resolve()

    def test_removes_existing_empty_directory_dest(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_dir"
        src.mkdir()
        dest = tmp_path / "dest_dir"
        dest.mkdir()

        serve_mkdocs.create_junction(src, dest)

        assert _is_link_or_junction(dest)
        assert dest.resolve() == src.resolve()

    def test_removes_existing_nonempty_directory_dest(self, serve_mkdocs, tmp_path):
        """A non-empty directory at dest should be removed via shutil.rmtree
        fallback (since os.rmdir only works on empty directories)."""
        src = tmp_path / "src_dir"
        src.mkdir()
        dest = tmp_path / "dest_dir"
        dest.mkdir()
        (dest / "leftover.txt").write_text("leftover")

        serve_mkdocs.create_junction(src, dest)

        assert _is_link_or_junction(dest)
        assert dest.resolve() == src.resolve()

    def test_windows_uses_mklink_junction_command(self, serve_mkdocs, tmp_path, monkeypatch):
        src = tmp_path / "src_dir"
        dest = tmp_path / "dest_link"
        monkeypatch.setattr(serve_mkdocs.sys, "platform", "win32")
        fake_run = MagicMock()
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        serve_mkdocs.create_junction(src, dest)

        fake_run.assert_called_once()
        called_cmd = fake_run.call_args[0][0]
        assert called_cmd[:3] == ["cmd", "/c", "mklink"]
        assert "/J" in called_cmd
        assert str(dest) in called_cmd
        assert str(src) in called_cmd


# ---------------------------------------------------------------------------
# create_hardlink
# ---------------------------------------------------------------------------

class TestCreateHardlink:
    def test_creates_hardlink_when_dest_missing(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_file.txt"
        src.write_text("hello")
        dest = tmp_path / "dest_file.txt"

        serve_mkdocs.create_hardlink(src, dest)

        assert dest.exists()
        assert dest.read_text() == "hello"
        # Confirm it is actually a hardlink (same inode) on POSIX systems.
        if not sys.platform.startswith("win"):
            assert dest.stat().st_ino == src.stat().st_ino

    def test_replaces_existing_dest(self, serve_mkdocs, tmp_path):
        src = tmp_path / "src_file.txt"
        src.write_text("new content")
        dest = tmp_path / "dest_file.txt"
        dest.write_text("stale content")

        serve_mkdocs.create_hardlink(src, dest)

        assert dest.read_text() == "new content"

    def test_falls_back_to_symlink_on_oserror(self, serve_mkdocs, tmp_path, monkeypatch):
        """If os.link fails (e.g. cross-device link), the function should
        fall back to creating a symlink instead."""
        src = tmp_path / "src_file.txt"
        src.write_text("hello")
        dest = tmp_path / "dest_file.txt"
        monkeypatch.setattr(serve_mkdocs.sys, "platform", "linux")

        def raise_oserror(_src, _dest):
            raise OSError("Invalid cross-device link")

        monkeypatch.setattr(serve_mkdocs.os, "link", raise_oserror)
        mock_symlink = MagicMock()
        monkeypatch.setattr(serve_mkdocs.os, "symlink", mock_symlink)

        serve_mkdocs.create_hardlink(src, dest)

        mock_symlink.assert_called_once_with(src.resolve(), dest)

    def test_windows_uses_mklink_hardlink_command(self, serve_mkdocs, tmp_path, monkeypatch):
        src = tmp_path / "src_file.txt"
        dest = tmp_path / "dest_file.txt"
        monkeypatch.setattr(serve_mkdocs.sys, "platform", "win32")
        fake_run = MagicMock()
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        serve_mkdocs.create_hardlink(src, dest)

        fake_run.assert_called_once()
        called_cmd = fake_run.call_args[0][0]
        assert called_cmd[:3] == ["cmd", "/c", "mklink"]
        assert "/H" in called_cmd
        assert str(dest) in called_cmd
        assert str(src) in called_cmd


# ---------------------------------------------------------------------------
# prepare_docs_dir
# ---------------------------------------------------------------------------

class TestPrepareDocsDir:
    def test_creates_build_dir_if_missing(self, serve_mkdocs, tmp_path):
        root_dir = tmp_path / "root"
        root_dir.mkdir()
        build_dir = root_dir / "mkdocs_src"

        assert not build_dir.exists()
        serve_mkdocs.prepare_docs_dir(root_dir, build_dir)
        assert build_dir.is_dir()

    def test_does_not_error_if_build_dir_already_exists(self, serve_mkdocs, tmp_path):
        root_dir = tmp_path / "root"
        root_dir.mkdir()
        build_dir = root_dir / "mkdocs_src"
        build_dir.mkdir()

        # Should not raise even though the directory already exists.
        serve_mkdocs.prepare_docs_dir(root_dir, build_dir)
        assert build_dir.is_dir()

    def test_links_only_existing_source_directories(self, serve_mkdocs, tmp_path):
        root_dir = tmp_path / "root"
        root_dir.mkdir()
        # Only create a subset of the expected directories.
        (root_dir / "docs").mkdir()
        (root_dir / "palace").mkdir()
        build_dir = root_dir / "mkdocs_src"

        serve_mkdocs.prepare_docs_dir(root_dir, build_dir)

        assert _is_link_or_junction(build_dir / "docs")
        assert _is_link_or_junction(build_dir / "palace")
        # Directories that were never created at the source should not
        # appear as broken links in the destination.
        assert not (build_dir / "openwiki").exists()
        assert not (build_dir / ".agents").exists()
        assert not (build_dir / "assets").exists()

    def test_hardlinks_only_existing_files(self, serve_mkdocs, tmp_path):
        root_dir = tmp_path / "root"
        root_dir.mkdir()
        (root_dir / "README.md").write_text("# Readme")
        build_dir = root_dir / "mkdocs_src"

        serve_mkdocs.prepare_docs_dir(root_dir, build_dir)

        assert (build_dir / "README.md").exists()
        assert (build_dir / "README.md").read_text() == "# Readme"
        # Files that don't exist at the source (e.g. CHANGELOG.md) should be
        # silently skipped rather than raising an error.
        assert not (build_dir / "CHANGELOG.md").exists()

    def test_all_expected_dirs_linked_when_present(self, serve_mkdocs, tmp_path):
        root_dir = tmp_path / "root"
        root_dir.mkdir()
        for d in ["docs", "openwiki", "palace", ".agents", "assets"]:
            (root_dir / d).mkdir()
        build_dir = root_dir / "mkdocs_src"

        serve_mkdocs.prepare_docs_dir(root_dir, build_dir)

        for d in ["docs", "openwiki", "palace", ".agents", "assets"]:
            assert _is_link_or_junction(build_dir / d)
            assert (build_dir / d).resolve() == (root_dir / d).resolve()


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------

class TestMain:
    def test_default_invokes_serve_command(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py"])
        fake_result = MagicMock(returncode=0)
        fake_run = MagicMock(return_value=fake_result)
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        serve_mkdocs.main()

        fake_run.assert_called_once()
        cmd = fake_run.call_args[0][0]
        assert cmd == ["uvx", "--with", "mkdocs-material", "mkdocs", "serve", "-f", "mkdocs.yml"]

    def test_build_only_flag_uses_build_command_and_adds_clean(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py", "--build-only"])
        fake_result = MagicMock(returncode=0)
        fake_run = MagicMock(return_value=fake_result)
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        serve_mkdocs.main()

        cmd = fake_run.call_args[0][0]
        assert "build" in cmd
        assert "--build-only" not in cmd
        assert "--clean" in cmd
        assert "serve" not in cmd

    def test_build_only_does_not_duplicate_clean_flag(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py", "--build-only", "--clean"])
        fake_result = MagicMock(returncode=0)
        fake_run = MagicMock(return_value=fake_result)
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        serve_mkdocs.main()

        cmd = fake_run.call_args[0][0]
        assert cmd.count("--clean") == 1

    def test_nonzero_return_code_causes_system_exit(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py"])
        fake_result = MagicMock(returncode=42)
        fake_run = MagicMock(return_value=fake_result)
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", fake_run)

        with pytest.raises(SystemExit) as exc_info:
            serve_mkdocs.main()

        assert exc_info.value.code == 42

    def test_keyboard_interrupt_exits_cleanly(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py"])

        def raise_keyboard_interrupt(*args, **kwargs):
            raise KeyboardInterrupt()

        monkeypatch.setattr(serve_mkdocs.subprocess, "run", raise_keyboard_interrupt)

        with pytest.raises(SystemExit) as exc_info:
            serve_mkdocs.main()

        assert exc_info.value.code == 0

    def test_prepares_docs_dir_under_current_working_directory(self, serve_mkdocs, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(sys, "argv", ["serve_mkdocs.py"])
        (tmp_path / "docs").mkdir()
        mock_prepare = MagicMock()
        monkeypatch.setattr(serve_mkdocs, "prepare_docs_dir", mock_prepare)
        fake_result = MagicMock(returncode=0)
        monkeypatch.setattr(serve_mkdocs.subprocess, "run", MagicMock(return_value=fake_result))

        serve_mkdocs.main()

        mock_prepare.assert_called_once_with(tmp_path, tmp_path / "mkdocs_src")