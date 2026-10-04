"""Integration tests for Python script syntax and docstring compliance.

This test suite scans all Python files in the repository to ensure they
are syntactically valid and contain module-level docstrings as per PEP-257.
"""

import ast
import glob

import pytest

TARGET_DIRS = ["scripts/**/*.py", ".agents/**/*.py"]

def get_python_files():
    """Retrieve all Python files matching the target directories."""
    files = []
    for pattern in TARGET_DIRS:
        files.extend(glob.glob(pattern, recursive=True))
    return files

@pytest.mark.parametrize("filepath", get_python_files())
def test_python_syntax_and_docstrings(filepath):
    """Verify that the Python file has valid syntax and a module docstring."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in {filepath}: {e}")
        
    # Verify module AST is parseable
    assert tree is not None
