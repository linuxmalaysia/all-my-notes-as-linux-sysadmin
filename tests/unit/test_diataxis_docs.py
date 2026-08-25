"""Ujian unit untuk scripts/build_diataxis_docs.py (pembina struktur Diátaxis)."""

import importlib.util
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_diataxis_docs_script() -> ModuleType:
    """Muatkan skrip build_diataxis_docs.py secara dinamik untuk ujian terasing.

    Returns:
        ModuleType: Instans modul build_diataxis_docs yang dimuatkan.
    """
    script_path = REPO_ROOT / "scripts" / "build_diataxis_docs.py"
    spec = importlib.util.spec_from_file_location("diataxis_docs_mod", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


diataxis_mod = _import_diataxis_docs_script()


def test_get_doc_type_infers_quadrant_correctly():
    """Mengesahkan penentuan jenis kuadran Diátaxis berdasarkan laluan fail."""
    assert diataxis_mod.get_doc_type("docs/tutorials/start.md") == "tutorial"
    assert diataxis_mod.get_doc_type("docs/how-to/deploy.md") == "guide"
    assert diataxis_mod.get_doc_type("docs/reference/api.md") == "reference"
    assert diataxis_mod.get_doc_type("docs/explanation/concept.md") == "concept"


def test_get_yaml_template_generates_valid_frontmatter():
    """Mengesahkan penjanaan templat YAML frontmatter Diátaxis."""
    yaml_str = diataxis_mod.get_yaml_template(
        title="Ujian Tajuk",
        description="Penerangan ujian.",
        doc_type="guide",
        file_id="docs/how-to/test.md",
    )
    assert 'title: "Ujian Tajuk"' in yaml_str
    assert 'type: "guide"' in yaml_str
    assert 'id: "docs/how-to/test.md"' in yaml_str


def test_strip_old_frontmatter_removes_leading_yaml():
    """Mengesahkan penyingkiran YAML frontmatter lama daripada kandungan Markdown."""
    content = "---\ntitle: Old\n---\n# Body\n\nProsa."
    body = diataxis_mod.strip_old_frontmatter(content)
    assert body.startswith("# Body")
    assert "title: Old" not in body
