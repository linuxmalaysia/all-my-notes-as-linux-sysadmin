"""Ujian untuk konfigurasi pytest.ini repositori.

Mengesahkan bahawa pytest.ini mengisytiharkan corak python_files / python_functions
yang diperlukan untuk menemui modul ujian pematuhan tests/unit/*.py (ansible.py,
containers.py, markdown.py, sitemaps.py, llms.py), yang secara sengaja tidak
menggunakan awalan nama fail konvensional 'test_'.
"""

import configparser
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PYTEST_INI = REPO_ROOT / "pytest.ini"


def _read_pytest_ini() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(PYTEST_INI)
    return config


def test_pytest_ini_exists_at_repo_root():
    assert PYTEST_INI.exists(), "pytest.ini mesti wujud di punca repositori."


def test_pytest_ini_has_pytest_section():
    config = _read_pytest_ini()
    assert config.has_section("pytest"), "pytest.ini mesti mengandungi seksyen [pytest]."


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
    """Setiap modul di bawah tests/unit yang tidak bermula dengan 'test_' (dan bukan
    penyulita pakej) mesti disenaraikan secara eksplisit dalam python_files, jika tidak
    peraturan penemuan lalai pytest akan melangkaunya secara senyap."""
    config = _read_pytest_ini()
    python_files = set(config.get("pytest", "python_files").split())

    unit_dir = REPO_ROOT / "tests" / "unit"
    custom_modules = [
        p.name
        for p in unit_dir.glob("*.py")
        if p.name != "__init__.py" and not p.name.startswith("test_")
    ]

    assert custom_modules, "Dijangkakan sekurang-kurangnya satu modul tanpa awalan 'test_' di bawah tests/unit."
    for module_name in custom_modules:
        assert module_name in python_files, (
            f"{module_name} tidak disenaraikan dalam python_files pytest.ini dan tidak akan ditemui."
        )


def test_pytest_ini_enables_discovery_of_non_test_prefixed_module(tmp_path):
    """Semakan fungsi/integrasi: menjalankan pytest dengan pytest.ini yang tepat ini
    sebenarnya mengumpul modul tanpa awalan 'test_' seperti 'ansible.py', manakala
    modul yang tidak disenaraikan dan tidak sepadan dengan 'test_*.py' kekal tidak ditemui.
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
    """Fungsi pembantu seperti 'get_playbook_files' (yang digunakan oleh ansible.py) mesti
    tidak dikumpul sebagai ujian, walaupun fail yang mengandunginya dikumpul."""
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
