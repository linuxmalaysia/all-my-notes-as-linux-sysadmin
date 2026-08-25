"""Ujian unit untuk scripts/generate_html_site.py (penjana tapak web statik HTML)."""

import importlib.util
from pathlib import Path

import pytest

markdown = pytest.importorskip("markdown")
jinja2 = pytest.importorskip("jinja2")

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_html_site_script():
    """Muat naik skrip generate_html_site.py secara dinamik untuk ujian terasing.

    Returns:
        module: Instans modul generate_html_site yang dimuatkan.
    """
    script_path = REPO_ROOT / "scripts" / "generate_html_site.py"
    spec = importlib.util.spec_from_file_location("html_site_mod", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


html_mod = _import_html_site_script()


def test_parse_llms_txt_extracts_links(tmp_path):
    """Mengesahkan pautan fail Markdown diekstrak secara betul daripada llms.txt."""
    llms_file = tmp_path / "llms.txt"
    llms_file.write_text("- [Tajuk](docs/index.md)\n- [Lain](manual/cu01/file.md)\n", encoding="utf-8")

    paths = html_mod.parse_llms_txt(llms_file)
    assert paths == ["docs/index.md", "manual/cu01/file.md"]


def test_fix_internal_links_replaces_md_with_html():
    """Mengesahkan penukar pautan dalaman menukar .md kepada .html."""
    md_text = "Rujuk [Panduan](docs/guide.md) dan [Seksi](docs/guide.md#section)."
    fixed = html_mod.fix_internal_links(md_text)
    assert "[Panduan](docs/guide.html)" in fixed
    assert "[Seksi](docs/guide.html#section)" in fixed


def test_strip_frontmatter_and_get_title_from_frontmatter():
    """Mengesahkan pengekstrakan tajuk daripada YAML frontmatter."""
    raw_md = '---\ntitle: "Tajuk Utama"\n---\n# Subheading\n\nKandungan.'
    title, clean, fm = html_mod.strip_frontmatter_and_get_title(raw_md, "default.md")
    assert title == "Tajuk Utama"
    assert "title: \"Tajuk Utama\"" in fm
    assert clean.startswith("# Subheading")


def test_strip_frontmatter_and_get_title_fallback_to_h1():
    """Mengesahkan pengekstrakan tajuk daripada tajuk H1 pertama jika tiada frontmatter."""
    raw_md = "# Tajuk H1 Pertama\n\nKandungan prosa."
    title, clean, fm = html_mod.strip_frontmatter_and_get_title(raw_md, "default.md")
    assert title == "Tajuk H1 Pertama"
    assert fm == ""
