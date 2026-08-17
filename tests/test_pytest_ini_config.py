"""Tests for the repository's pytest.ini configuration.

Validates that pytest.ini declares the python_files / python_functions patterns
required to discover the tests/unit/*.py compliance-test modules (ansible.py,
containers.py, markdown.py, sitemaps.py, llms.py), which intentionally do not
use the conventional 'test_' filename prefix.
"""

import configparser
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PYTEST_INI = REPO_ROOT / "pytest.ini"


def _read_pytest_ini():
    config = configparser.ConfigParser()
    config.read(PYTEST_INI)
    return config


def test_pytest_ini_exists_at_repo_root():
    assert PYTEST_INI.exists(), "pytest.ini must exist at the repository root."


def test_pytest_ini_has_pytest_section():
    config = _read_pytest_ini()
    assert config.has_section("pytest"), "pytest.ini must contain a [pytest] section."


def test_pytest_ini_declares_expected_python_files_patterns():
    config = _read_pytest_ini()
    python_files = set(config.get("pytest", "python_files").split())

    expected_patterns = {
        "test_*.py",
        "ansible.py",
        "containers.py",
        "markdown.py",
        "sitemaps.py",
        "llms.py",
    }
    assert python_files == expected_patterns


def test_pytest_ini_declares_expected_python_functions_pattern():
    config = _read_pytest_ini()
    assert config.get("pytest", "python_functions").strip() == "test_*"


def test_pytest_ini_python_files_cover_every_non_test_prefixed_unit_module():
    """Every module under tests/unit that does not start with 'test_' (and is not
    the package initializer) must be explicitly listed in python_files, otherwise
    pytest's default discovery rules would silently skip it."""
    config = _read_pytest_ini()
    python_files = set(config.get("pytest", "python_files").split())

    unit_dir = REPO_ROOT / "tests" / "unit"
    custom_modules = [
        p.name
        for p in unit_dir.glob("*.py")
        if p.name != "__init__.py" and not p.name.startswith("test_")
    ]

    assert custom_modules, "Expected at least one non-'test_'-prefixed module under tests/unit."
    for module_name in custom_modules:
        assert module_name in python_files, (
            f"{module_name} is not listed in pytest.ini's python_files and would not be discovered."
        )


def test_pytest_ini_enables_discovery_of_non_test_prefixed_module(tmp_path):
    """Functional/integration check: running pytest with this exact pytest.ini
    actually collects a non-'test_'-prefixed module such as 'ansible.py', while a
    module that isn't listed and doesn't match 'test_*.py' remains undiscovered.
    """
    (tmp_path / "pytest.ini").write_text(PYTEST_INI.read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "ansible.py").write_text(
        "def test_dummy_check():\n    assert 1 + 1 == 2\n",
        encoding="utf-8",
    )
    (tmp_path / "not_discovered.py").write_text(
        "def test_should_not_be_collected():\n    assert False\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "ansible.py::test_dummy_check" in result.stdout
    assert "not_discovered.py" not in result.stdout


def test_pytest_ini_python_functions_pattern_ignores_non_test_prefixed_functions(tmp_path):
    """A helper function such as 'get_playbook_files' (used by ansible.py) must
    not itself be collected as a test, even though its containing file is."""
    (tmp_path / "pytest.ini").write_text(PYTEST_INI.read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "markdown.py").write_text(
        "def get_markdown_files():\n"
        "    return []\n\n"
        "def test_uses_helper():\n"
        "    assert get_markdown_files() == []\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "markdown.py::test_uses_helper" in result.stdout
    assert "::get_markdown_files" not in result.stdout