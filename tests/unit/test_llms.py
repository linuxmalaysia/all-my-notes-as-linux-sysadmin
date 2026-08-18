"""Ujian unit tambahan untuk kes sempadan/negatif bagi scripts/llms_to_xml.py dan
scripts/generate_llms_txt.py.
"""

import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_script(module_name: str, relative_path: str):
    """Pembantu untuk mengimport skrip di luar laluan pakej python secara dinamik."""
    script_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def llms_to_xml():
    return _import_script("llms_to_xml_edge_cases", "scripts/llms_to_xml.py")


@pytest.fixture(scope="module")
def generate_llms_txt():
    return _import_script("generate_llms_txt_edge_cases", "scripts/generate_llms_txt.py")


# ---------------------------------------------------------------------------
# parse_llms_txt() boundary/negative cases
# ---------------------------------------------------------------------------

def test_parse_llms_txt_ignores_links_to_non_markdown_targets(tmp_path, llms_to_xml):
    llms_txt = tmp_path / "llms.txt"
    llms_txt.write_text(
        "# Header\n\n"
        "- [HTML Page](html/page.html)\n"
        "- [Markdown Doc](docs/doc.md)\n",
        encoding="utf-8",
    )

    paths = llms_to_xml.parse_llms_txt(llms_txt)

    assert paths == ["docs/doc.md"]


def test_parse_llms_txt_captures_full_urls_ending_in_md(tmp_path, llms_to_xml):
    """Corak pautan regex hanya memerlukan sasaran berakhir dengan '.md'."""
    llms_txt = tmp_path / "llms.txt"
    llms_txt.write_text("- [External](https://example.org/readme.md)\n", encoding="utf-8")

    paths = llms_to_xml.parse_llms_txt(llms_txt)

    assert paths == ["https://example.org/readme.md"]


def test_parse_llms_txt_returns_empty_list_for_file_with_no_links(tmp_path, llms_to_xml):
    llms_txt = tmp_path / "llms.txt"
    llms_txt.write_text("# Header\n\nJust prose, no markdown links here.\n", encoding="utf-8")

    assert llms_to_xml.parse_llms_txt(llms_txt) == []


def test_parse_llms_txt_only_captures_first_link_per_line(tmp_path, llms_to_xml):
    """parse_llms_txt menggunakan re.search setiap baris."""
    llms_txt = tmp_path / "llms.txt"
    llms_txt.write_text(
        "- [First](docs/first.md) and also [Second](docs/second.md)\n",
        encoding="utf-8",
    )

    paths = llms_to_xml.parse_llms_txt(llms_txt)

    assert paths == ["docs/first.md"]


def test_parse_llms_txt_strips_leading_whitespace_inside_link_target(tmp_path, llms_to_xml):
    """Laluan yang ditangkap dibersihkan dengan .strip()."""
    llms_txt = tmp_path / "llms.txt"
    llms_txt.write_text("- [Padded](  docs/padded.md)\n", encoding="utf-8")

    paths = llms_to_xml.parse_llms_txt(llms_txt)

    assert paths == ["docs/padded.md"]


# ---------------------------------------------------------------------------
# generate_xml_context() boundary/negative cases
# ---------------------------------------------------------------------------

def test_generate_xml_context_skips_missing_referenced_files(tmp_path, llms_to_xml, capsys):
    existing = tmp_path / "docs" / "exists.md"
    existing.parent.mkdir(parents=True, exist_ok=True)
    existing.write_text("# Exists\n\nContent.", encoding="utf-8")

    out_xml = tmp_path / "output_context.xml"
    llms_to_xml.generate_xml_context(
        tmp_path, ["docs/exists.md", "docs/missing.md"], out_xml
    )

    tree = ET.parse(out_xml)
    root = tree.getroot()
    files = root.findall("file")
    assert len(files) == 1
    assert files[0].attrib["path"] == "docs/exists.md"

    captured = capsys.readouterr()
    assert "Warning: File not found docs/missing.md" in captured.out


def test_generate_xml_context_escapes_special_xml_characters(tmp_path, llms_to_xml):
    doc_file = tmp_path / "special.md"
    doc_file.write_text("<script>alert('x')</script> & more", encoding="utf-8")

    out_xml = tmp_path / "output_context.xml"
    llms_to_xml.generate_xml_context(tmp_path, ["special.md"], out_xml)

    raw_output = out_xml.read_text(encoding="utf-8")
    assert "&lt;script&gt;" in raw_output
    assert "&amp;" in raw_output

    # Output terlepas mesti kekal XML yang sah.
    ET.parse(out_xml)


def test_generate_xml_context_with_empty_file_list_produces_empty_context(tmp_path, llms_to_xml):
    out_xml = tmp_path / "output_context.xml"
    llms_to_xml.generate_xml_context(tmp_path, [], out_xml)

    tree = ET.parse(out_xml)
    root = tree.getroot()
    assert root.tag == "context"
    assert root.findall("file") == []


# ---------------------------------------------------------------------------
# get_markdown_title() boundary/negative cases
# ---------------------------------------------------------------------------

def test_get_markdown_title_returns_filename_fallback_for_missing_file(tmp_path, generate_llms_txt):
    """Pengujian cawangan 'except' sandaran."""
    missing_path = tmp_path / "missing.md"

    title = generate_llms_txt.get_markdown_title(missing_path)

    assert title == "missing.md"


def test_get_markdown_title_ignores_leading_blank_lines(tmp_path, generate_llms_txt):
    md = tmp_path / "leading_blank.md"
    md.write_text("\n\n# Real Title\n\nBody.\n", encoding="utf-8")

    assert generate_llms_txt.get_markdown_title(md) == "Real Title"


def test_get_markdown_title_uses_first_h1_when_multiple_present(tmp_path, generate_llms_txt):
    md = tmp_path / "multi_h1.md"
    md.write_text("# First Title\n\n# Second Title\n", encoding="utf-8")

    assert generate_llms_txt.get_markdown_title(md) == "First Title"


def test_get_markdown_title_ignores_h2_and_deeper_headings(tmp_path, generate_llms_txt):
    md = tmp_path / "h2_only.md"
    md.write_text("## Not An H1\n\nBody text.\n", encoding="utf-8")

    assert generate_llms_txt.get_markdown_title(md) == "h2_only.md"
