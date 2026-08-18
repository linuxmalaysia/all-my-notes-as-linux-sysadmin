"""Unit tests for the tests/unit package initializer (tests/unit/__init__.py)."""

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INIT_PATH = REPO_ROOT / "tests" / "unit" / "__init__.py"


def test_unit_package_init_file_exists():
    assert INIT_PATH.exists(), "tests/unit/__init__.py must exist so 'tests.unit' is a package."


def test_unit_package_init_has_expected_docstring():
    spec = importlib.util.spec_from_file_location("tests_unit_init_module", INIT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert "DSOM NOSS Linux" in module.__doc__
    assert module.__doc__ == "Unit tests package for DSOM NOSS Linux project."


def test_unit_package_init_contains_only_the_docstring():
    """The initializer should be a no-op module: only a module docstring, no
    imports or side effects that could affect test discovery/collection."""
    content = INIT_PATH.read_text(encoding="utf-8").strip()
    assert content.startswith('"""') and content.endswith('"""')
    assert content == '"""Unit tests package for DSOM NOSS Linux project."""'
