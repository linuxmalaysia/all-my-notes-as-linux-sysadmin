"""Unit tests for the Enterprise HA Database solution PDF compiler script (tools/compile_ha_db_pdf.py)."""

from pathlib import Path

import tools.compile_ha_db_pdf as ha_pdf_compiler

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def test_clean_markdown_strips_frontmatter_and_footers(tmp_path):
    """Verify clean_markdown strips OKF frontmatter and DSOM footers."""
    src_file = tmp_path / "ha_db.md"
    src_file.write_text(
        "---\nokf_version: '0.2'\ntitle: 'Title'\n---\n\n# Heading\nContent\n---\n*Linux for NOSS Malaysia (Sovereign Manual)*\n*Standard: UK English*",
        encoding="utf-8",
    )
    cleaned = ha_pdf_compiler.clean_markdown(src_file, tmp_path)
    content = cleaned.read_text(encoding="utf-8")
    assert "okf_version" not in content
    assert "# Heading" in content
    assert "Content" in content
    assert "Linux for NOSS Malaysia" not in content


def test_write_css_generates_pure_white_css(tmp_path):
    """Verify write_css creates CSS with mandated A4 margins and pure white background."""
    css_file = ha_pdf_compiler.write_css(tmp_path)
    assert css_file.exists()
    css_content = css_file.read_text(encoding="utf-8")
    assert "#FFFFFF !important" in css_content
    assert "margin: 10mm 10mm 12mm 10mm;" in css_content


def test_generated_ha_db_pdf_artifact_exists_and_exceeds_min_size():
    """Verify the generated HA Database PDF in docs/dist exists and exceeds 10KB."""
    pdf_path = REPO_ROOT / "docs" / "dist" / "solusi-pangkalan-data-kebolehseediaan-tinggi.pdf"
    assert pdf_path.is_file()
    assert pdf_path.stat().st_size > 10240
