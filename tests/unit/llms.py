"""Unit tests for LLMs parser and full compilation scripts.

Validates scripts/llms_to_xml.py (parse_llms_txt, generate_xml_context) and
scripts/generate_llms_txt.py (get_markdown_title, llms.txt & llms-full.txt generation).
"""

import importlib.util
import os
from pathlib import Path
import xml.etree.ElementTree as ET
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _import_script(module_name: str, relative_path: str):
    """
    Dynamically load a Python script from a repository-relative path.
    
    Parameters:
        module_name (str): Name to assign to the imported module.
        relative_path (str): Path to the script relative to the repository root.
    
    Returns:
        module: The dynamically imported Python module.
    """
    script_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_llms_txt2ctx_parser_api(tmp_path):
    """Test parse_llms_txt and generate_xml_context from scripts/llms_to_xml.py."""
    llms_to_xml = _import_script("llms_to_xml", "scripts/llms_to_xml.py")

    # 1. Test parse_llms_txt with synthetic input
    sample_llms_txt = tmp_path / "sample_llms.txt"
    sample_llms_txt.write_text(
        "# Header\n\n- [Sample Title](docs/sample.md)\n- [Another Title](openwiki/test.md)\n",
        encoding="utf-8",
    )

    paths = llms_to_xml.parse_llms_txt(sample_llms_txt)
    assert paths == ["docs/sample.md", "openwiki/test.md"]

    # 2. Test generate_xml_context with synthetic files
    doc_file = tmp_path / "docs/sample.md"
    doc_file.parent.mkdir(parents=True, exist_ok=True)
    doc_file.write_text("# Sample Content\n\nTest content for XML context.", encoding="utf-8")

    out_xml = tmp_path / "output_context.xml"
    llms_to_xml.generate_xml_context(tmp_path, ["docs/sample.md"], out_xml)

    assert out_xml.exists()
    tree = ET.parse(out_xml)
    root = tree.getroot()
    assert root.tag == "context"
    files = root.findall("file")
    assert len(files) == 1
    assert files[0].attrib["path"] == "docs/sample.md"

    # 3. Test parse_llms_txt on repo's llms.txt if present
    repo_llms_txt = REPO_ROOT / "llms.txt"
    if repo_llms_txt.exists():
        repo_paths = llms_to_xml.parse_llms_txt(repo_llms_txt)
        assert isinstance(repo_paths, list)
        assert len(repo_paths) > 0


def test_build_llms_full_compilation(tmp_path):
    """Test get_markdown_title and llms.txt / llms-full.txt compilation logic from scripts/generate_llms_txt.py."""
    generate_llms_txt = _import_script("generate_llms_txt", "scripts/generate_llms_txt.py")

    # 1. Test get_markdown_title
    md_with_h1 = tmp_path / "test_h1.md"
    md_with_h1.write_text("# Sovereign AI Document\n\nSome text.", encoding="utf-8")
    assert generate_llms_txt.get_markdown_title(md_with_h1) == "Sovereign AI Document"

    md_without_h1 = tmp_path / "no_h1.md"
    md_without_h1.write_text("Just text without H1 heading.", encoding="utf-8")
    assert generate_llms_txt.get_markdown_title(md_without_h1) == "no_h1.md"

    # 2. Test llms.txt and llms-full.txt in repository
    llms_txt = REPO_ROOT / "llms.txt"
    llms_full_txt = REPO_ROOT / "llms-full.txt"

    assert llms_txt.exists(), "llms.txt should exist in repository root."
    assert llms_full_txt.exists(), "llms-full.txt should exist in repository root."

    txt_content = llms_txt.read_text(encoding="utf-8")
    assert "# DSOM AI Knowledge Base" in txt_content
    assert "## Root Documents" in txt_content or "## Documentation" in txt_content

    full_content = llms_full_txt.read_text(encoding="utf-8")
    assert "# DSOM AI Knowledge Base (Full Content)" in full_content
    assert "<!-- BEGIN FILE:" in full_content
    assert "<!-- END FILE:" in full_content
