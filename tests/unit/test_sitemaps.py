"""Ujian unit untuk tests/unit/sitemaps.py (pengesah konfigurasi sitemap dan Context7)."""

import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_sitemaps_module():
    """Loads tests/unit/sitemaps.py dynamically for isolated testing.

    Returns:
        module: Loaded sitemaps test module instance.
    """
    module_path = REPO_ROOT / "tests" / "unit" / "sitemaps.py"
    spec = importlib.util.spec_from_file_location("unit_test_target_sitemaps", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sitemaps_mod = _load_sitemaps_module()

VALID_URLSET = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    "  <url><loc>https://example.org/</loc></url>\n"
    "</urlset>\n"
)

EMPTY_URLSET = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    "</urlset>\n"
)

VALID_CONTEXT_XML = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    "<context>\n"
    '  <file path="docs/sample.md">\n'
    "    <content>Sample</content>\n"
    "  </file>\n"
    "</context>\n"
)


def _setup_valid_sitemaps(tmp_path):
    """Creates temporary mock sitemap files for unit testing.

    Args:
        tmp_path (Path): Temporary directory path.
    """
    (tmp_path / "docs").mkdir(exist_ok=True)
    (tmp_path / "html" / "docs").mkdir(parents=True, exist_ok=True)
    (tmp_path / "docs" / "sitemap.xml").write_text(VALID_URLSET, encoding="utf-8")
    (tmp_path / "html" / "sitemap.xml").write_text(VALID_URLSET, encoding="utf-8")
    (tmp_path / "html" / "docs" / "sitemap.txt").write_text("https://example.org/\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# test_sitemaps_consistency()
# ---------------------------------------------------------------------------

def test_sitemaps_consistency_rejects_missing_files(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(AssertionError, match=r"(tidak wujud|does not exist)"):
        sitemaps_mod.test_sitemaps_consistency()


def test_sitemaps_consistency_accepts_valid_sitemaps(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _setup_valid_sitemaps(tmp_path)
    sitemaps_mod.test_sitemaps_consistency()


def test_sitemaps_consistency_rejects_wrong_root_element(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _setup_valid_sitemaps(tmp_path)
    (tmp_path / "docs" / "sitemap.xml").write_text(
        '<?xml version="1.0"?><sitemapindex></sitemapindex>', encoding="utf-8"
    )

    with pytest.raises(AssertionError, match=r"(root element must be 'urlset'|mestilah 'urlset')"):
        sitemaps_mod.test_sitemaps_consistency()


def test_sitemaps_consistency_rejects_docs_sitemap_with_no_locs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _setup_valid_sitemaps(tmp_path)
    (tmp_path / "docs" / "sitemap.xml").write_text(EMPTY_URLSET, encoding="utf-8")

    with pytest.raises(AssertionError, match=r"(contains no valid|tidak mengandungi elemen <loc>)"):
        sitemaps_mod.test_sitemaps_consistency()


def test_sitemaps_consistency_rejects_empty_sitemap_txt(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _setup_valid_sitemaps(tmp_path)
    (tmp_path / "html" / "docs" / "sitemap.txt").write_text("", encoding="utf-8")

    with pytest.raises(AssertionError, match=r"(is empty|adalah kosong)"):
        sitemaps_mod.test_sitemaps_consistency()


# ---------------------------------------------------------------------------
# test_context7_configuration()
# ---------------------------------------------------------------------------

def test_context7_configuration_rejects_missing_mkdocs_yml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(AssertionError, match=r"(MkDocs configuration file missing|tidak wujud)"):
        sitemaps_mod.test_context7_configuration()


def test_context7_configuration_accepts_valid_mkdocs_yml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text(
        "site_name: My Docs\ndocs_dir: docs\n", encoding="utf-8"
    )
    sitemaps_mod.test_context7_configuration()


def test_context7_configuration_rejects_mkdocs_yml_missing_site_name(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text("docs_dir: docs\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="site_name"):
        sitemaps_mod.test_context7_configuration()


def test_context7_configuration_rejects_mkdocs_yml_missing_docs_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text("site_name: My Docs\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="docs_dir"):
        sitemaps_mod.test_context7_configuration()


def test_context7_configuration_accepts_valid_context_xml(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text(
        "site_name: My Docs\ndocs_dir: docs\n", encoding="utf-8"
    )
    (tmp_path / "llms_context.xml").write_text(VALID_CONTEXT_XML, encoding="utf-8")

    sitemaps_mod.test_context7_configuration()


def test_context7_configuration_rejects_context_xml_wrong_root(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text(
        "site_name: My Docs\ndocs_dir: docs\n", encoding="utf-8"
    )
    (tmp_path / "llms_context.xml").write_text(
        '<?xml version="1.0"?><notcontext></notcontext>', encoding="utf-8"
    )

    with pytest.raises(AssertionError, match=r"(root element must be <context>|mestilah <context>)"):
        sitemaps_mod.test_context7_configuration()


def test_context7_configuration_rejects_context_xml_with_no_file_entries(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text(
        "site_name: My Docs\ndocs_dir: docs\n", encoding="utf-8"
    )
    (tmp_path / "llms_context.xml").write_text(
        '<?xml version="1.0"?><context></context>', encoding="utf-8"
    )

    with pytest.raises(AssertionError, match=r"(contains no <file> entries|tidak mengandungi sebarang entri <file>)"):
        sitemaps_mod.test_context7_configuration()


def test_context7_configuration_propagates_xml_parse_error_for_malformed_context_xml(
    tmp_path, monkeypatch
):
    """Penguraian XML tidak sah mesti menghasilkan ralat ParseError."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "mkdocs.yml").write_text(
        "site_name: My Docs\ndocs_dir: docs\n", encoding="utf-8"
    )
    (tmp_path / "llms_context.xml").write_text("<context><unclosed>", encoding="utf-8")

    with pytest.raises(ET.ParseError):
        sitemaps_mod.test_context7_configuration()
