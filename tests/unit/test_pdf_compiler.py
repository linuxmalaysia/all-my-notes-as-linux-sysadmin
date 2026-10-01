"""Unit tests for the PDF compiler script (tools/compile_pdf.py)."""

from pathlib import Path
import pytest
import tools.compile_pdf as pdf_compiler

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def test_clean_markdown_strips_frontmatter_and_footers(tmp_path):
    """Verify clean_markdown strips OKF frontmatter and DSOM footers."""
    src_file = tmp_path / "test.md"
    src_file.write_text(
        "---\nokf_version: '0.2'\ntitle: Test\n---\n\n# Heading\nContent\n---\n*Linux for NOSS Malaysia*\n",
        encoding="utf-8",
    )
    cleaned = pdf_compiler.clean_markdown(src_file, tmp_path)
    content = cleaned.read_text(encoding="utf-8")
    assert "okf_version" not in content
    assert "# Heading" in content
    assert "Content" in content


def test_write_css_generates_pure_white_css(tmp_path):
    """Verify write_css creates CSS with mandated A4 margins and pure white background."""
    css_file = pdf_compiler.write_css(tmp_path)
    assert css_file.exists()
    css_content = css_file.read_text(encoding="utf-8")
    assert "#FFFFFF !important" in css_content
    assert "margin: 10mm 10mm 12mm 10mm;" in css_content


def test_generated_pdf_artifact_exists_and_exceeds_min_size():
    """Verify the generated PDF ebook in docs/dist exists and exceeds 10KB."""
    pdf_path = REPO_ROOT / "docs" / "dist" / "terminal-cloud-pdf-compilation-guide.pdf"
    assert pdf_path.is_file()
    assert pdf_path.stat().st_size > 10240
