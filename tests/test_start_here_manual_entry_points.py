"""Tests for the "Di Mana Mahu Bermula Untuk Manual Linux?" onboarding section.

Covers the new manual entry-points guide added to START-HERE.md and propagated
into the generated knowledge-base mirrors:
  - START-HERE.md (source)
  - html/START-HERE.html (rendered MkDocs output)
  - llms-full.txt / html/llms-full.txt (compiled knowledge base)
  - llms_context.xml / html/llms_context.xml (Context7 XML export)
  - html/search/search_index.json (MkDocs search index)

Also covers the renumbering of sections 5-8 in
docs/how-to/deploy-and-serve-html.md as reflected in the compiled llms-full.txt
/ llms_context.xml mirrors (new section 5: "Pengehosan GitHub Pages &
Automasi Bina Semula"), and basic structural sanity checks for
html/sitemap.xml.gz.
"""

import gzip
import json
import re
from pathlib import Path

import defusedxml.ElementTree as ET
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

HEADING_MD = "## 📖 Di Mana Mahu Bermula Untuk Manual Linux?"
HEADING_HTML_ID = "di-mana-mahu-bermula-untuk-manual-linux"
HEADING_HTML_TEXT = "📖 Di Mana Mahu Bermula Untuk Manual Linux?"

# (source .md link, rendered .html href) pairs expected inside the new section.
EXPECTED_LINK_TARGETS = [
    ("manual/index.md", "manual/index.html"),
    ("manual/cu01/index.md", "manual/cu01/index.html"),
    ("manual/cu02/index.md", "manual/cu02/index.html"),
    ("manual/cu03/index.md", "manual/cu03/index.html"),
    ("manual/cu04/index.md", "manual/cu04/index.html"),
    ("manual/cu05/index.md", "manual/cu05/index.html"),
    ("manual/cu06/index.md", "manual/cu06/index.html"),
    ("docs/tutorials/getting-started.md", "docs/tutorials/getting-started.html"),
]

CU_LABELS = [
    "CU01: Persediaan Sistem Komputer & Desktop Linux",
    "CU02: Pengurusan Storan & Hipervisor Pemayaan",
    "CU03: Pentadbiran & Perkhidmatan Pelayan Linux",
    "CU04: Automasi, Sandaran & Pemulihan Sistem",
    "CU05: Kawalan Keselamatan Endpoint & Pengerasan Sistem",
    "CU06: Sokongan Pengguna & Penyelesaian Masalah",
]


def read(relative_path):
    """Reads a file relative to repository root into string.

    Args:
        relative_path (str): Relative path from repo root.

    Returns:
        str: UTF-8 file content string.
    """
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# START-HERE.md (source markdown)
# ---------------------------------------------------------------------------

def test_start_here_md_contains_manual_entry_points_heading():
    content = read("START-HERE.md")
    assert HEADING_MD in content


@pytest.mark.parametrize("md_link,_html_link", EXPECTED_LINK_TARGETS)
def test_start_here_md_links_to_expected_target(md_link, _html_link):
    content = read("START-HERE.md")
    assert f"]({md_link})" in content, f"START-HERE.md should link to {md_link}."


@pytest.mark.parametrize("md_link,_html_link", EXPECTED_LINK_TARGETS)
def test_start_here_md_link_targets_exist_on_disk(md_link, _html_link):
    """Regression: every markdown link added in the new section must resolve
    to a real file in the repository (no dangling links)."""
    assert (REPO_ROOT / md_link).is_file(), f"Linked file {md_link} does not exist."


@pytest.mark.parametrize("label", CU_LABELS)
def test_start_here_md_mentions_all_cu_labels(label):
    content = read("START-HERE.md")
    assert label in content, f"START-HERE.md missing CU label: {label}"


def test_start_here_md_new_section_between_entry_points_and_why_sections():
    """The new section must sit between '🌐 Entry Points' and
    '🌟 Kenapa Linux NOSS & DSOM?' as introduced by this PR."""
    content = read("START-HERE.md")
    entry_points_idx = content.index("## 🌐 Titik Masuk (Entry Points)")
    new_section_idx = content.index(HEADING_MD)
    why_idx = content.index("## 🌟 Kenapa Linux NOSS & DSOM?")
    assert entry_points_idx < new_section_idx < why_idx


def test_start_here_md_new_section_mentions_six_competency_units():
    content = read("START-HERE.md")
    section_start = content.index(HEADING_MD)
    section_end = content.index("## 🌟 Kenapa Linux NOSS & DSOM?")
    section = content[section_start:section_end]
    assert "6 Unit Kompetensi (CU01 hingga CU06)" in section


# ---------------------------------------------------------------------------
# Compiled knowledge-base mirrors: llms-full.txt & html/llms-full.txt
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_llms_full_txt_contains_manual_entry_points_section(relpath):
    content = read(relpath)
    assert HEADING_MD in content, f"{relpath} missing the manual entry-points heading."


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
@pytest.mark.parametrize("md_link,_html_link", EXPECTED_LINK_TARGETS)
def test_llms_full_txt_contains_expected_links(relpath, md_link, _html_link):
    content = read(relpath)
    assert f"]({md_link})" in content, f"{relpath} should link to {md_link}."


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_llms_full_txt_wraps_start_here_between_begin_end_markers(relpath):
    content = read(relpath)
    begin_idx = content.index("<!-- BEGIN FILE: START-HERE.md -->")
    end_idx = content.index("<!-- END FILE: START-HERE.md -->")
    heading_idx = content.index(HEADING_MD)
    assert begin_idx < heading_idx < end_idx, (
        f"{relpath}: manual entry-points heading must appear inside the "
        "START-HERE.md file block."
    )


# ---------------------------------------------------------------------------
# Section renumbering in docs/how-to/deploy-and-serve-html.md mirrors
# ---------------------------------------------------------------------------

RENUMBERED_SECTIONS = [
    "## 5. Pengehosan GitHub Pages & Automasi Bina Semula (GitHub Actions Workflow)",
    "## 6. Automasi Penyebaran Menggunakan Ansible Playbook",
    "## 7. Prosedur Mengemas Kini & Membina Semula HTML (Untuk Penulis/Penyumbang)",
    "## 8. Pengesahan Kualiti Sebelum Komit (Quality Gate)",
]


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_deploy_doc_sections_are_renumbered_in_order(relpath):
    content = read(relpath)
    indices = []
    for heading in RENUMBERED_SECTIONS:
        assert heading in content, f"{relpath} missing renumbered heading: {heading}"
        indices.append(content.index(heading))
    assert indices == sorted(indices), (
        f"{relpath}: renumbered sections 5-8 must appear in ascending order."
    )


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_deploy_doc_no_longer_has_stale_section_five_title(relpath):
    """Regression: the old '## 5. Automasi Penyebaran Menggunakan Ansible
    Playbook' heading must not remain, since section 5 was renumbered to 6
    and replaced by the new GitHub Pages section."""
    content = read(relpath)
    assert "## 5. Automasi Penyebaran Menggunakan Ansible Playbook" not in content


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_deploy_doc_github_pages_section_mentions_workflow_file(relpath):
    content = read(relpath)
    section_start = content.index("## 5. Pengehosan GitHub Pages")
    section_end = content.index("## 6. Automasi Penyebaran Menggunakan Ansible Playbook")
    section = content[section_start:section_end]
    assert ".github/workflows/static.yml" in section
    assert "uv run scripts/serve_mkdocs.py --build-only" in section
    assert ".nojekyll" in section


# ---------------------------------------------------------------------------
# llms_context.xml & html/llms_context.xml (Context7 XML export)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_llms_context_xml_is_well_formed(relpath):
    content = read(relpath)
    sanitized = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", content)
    root = ET.fromstring(sanitized)
    assert root.tag == "context"
    assert len(root.findall("file")) > 0


@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_llms_context_xml_start_here_entry_contains_new_section(relpath):
    content = read(relpath)
    begin_idx = content.index('<file path="START-HERE.md">')
    end_idx = content.index("</file>", begin_idx)
    entry = content[begin_idx:end_idx]
    assert HEADING_MD in entry
    # XML entity-escaped ampersand form used throughout llms_context.xml
    assert "Laluan Mengikut Tahap &amp; Keperluan" in entry


@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_llms_context_xml_deploy_doc_sections_renumbered(relpath):
    content = read(relpath)
    expected = [
        "## 5. Pengehosan GitHub Pages &amp; Automasi Bina Semula (GitHub Actions Workflow)",
        "## 6. Automasi Penyebaran Menggunakan Ansible Playbook",
        "## 7. Prosedur Mengemas Kini &amp; Membina Semula HTML (Untuk Penulis/Penyumbang)",
        "## 8. Pengesahan Kualiti Sebelum Komit (Quality Gate)",
    ]
    indices = []
    for heading in expected:
        assert heading in content, f"{relpath} missing renumbered heading: {heading}"
        indices.append(content.index(heading))
    assert indices == sorted(indices)


# ---------------------------------------------------------------------------
# html/START-HERE.html (rendered MkDocs output)
# ---------------------------------------------------------------------------

def test_start_here_html_has_new_section_heading_with_permalink():
    content = read("html/START-HERE.html")
    assert (
        f'<h2 id="{HEADING_HTML_ID}">{HEADING_HTML_TEXT}'
        f'<a class="headerlink" href="#{HEADING_HTML_ID}"' in content
    )


def test_start_here_html_nav_includes_new_section_twice():
    """MkDocs Material renders the same nav entry in both the top-level TOC
    and the on-page TOC sidebar, so it should appear exactly twice as a
    nav link (plus heading id + headerlink anchor = 4 total occurrences)."""
    content = read("html/START-HERE.html")
    nav_link_count = content.count(
        f'<a href="#{HEADING_HTML_ID}" class="md-nav__link">'
    )
    assert nav_link_count == 2


@pytest.mark.parametrize("md_link,html_link", EXPECTED_LINK_TARGETS)
def test_start_here_html_renders_html_links_not_markdown(md_link, html_link):
    content = read("html/START-HERE.html")
    assert f'href="{html_link}"' in content, (
        f"html/START-HERE.html should link to rendered target {html_link}."
    )
    # use_directory_urls: false means markdown links must be rewritten to .html
    assert f'href="{md_link}"' not in content


@pytest.mark.parametrize("_md_link,html_link", EXPECTED_LINK_TARGETS)
def test_start_here_html_link_targets_exist_on_disk(_md_link, html_link):
    """Regression: rendered .html link targets must exist under html/."""
    assert (REPO_ROOT / "html" / html_link).is_file(), (
        f"Rendered target html/{html_link} does not exist."
    )


def test_start_here_html_escapes_ampersands_in_cu_labels():
    content = read("html/START-HERE.html")
    assert "CU01: Persediaan Sistem Komputer &amp; Desktop Linux" in content
    assert "CU01: Persediaan Sistem Komputer & Desktop Linux" not in content


# ---------------------------------------------------------------------------
# html/search/search_index.json
# ---------------------------------------------------------------------------

def _load_search_index():
    return json.loads(
        (REPO_ROOT / "html/search/search_index.json").read_text(encoding="utf-8")
    )


def test_search_index_json_is_valid_and_has_docs():
    data = _load_search_index()
    assert "docs" in data
    assert isinstance(data["docs"], list)
    assert len(data["docs"]) > 0


def test_search_index_json_has_entry_for_new_section():
    data = _load_search_index()
    matches = [
        doc
        for doc in data["docs"]
        if doc.get("location") == f"START-HERE.html#{HEADING_HTML_ID}"
    ]
    assert len(matches) == 1, (
        "Expected exactly one search index entry for the new manual "
        "entry-points section."
    )
    assert matches[0]["title"] == HEADING_HTML_TEXT


def test_search_index_json_new_entry_text_mentions_manual_and_cu01():
    data = _load_search_index()
    matches = [
        doc
        for doc in data["docs"]
        if doc.get("location") == f"START-HERE.html#{HEADING_HTML_ID}"
    ]
    assert matches, "Expected a search index entry for the new section."
    text = matches[0]["text"]
    assert "manual/index.md" in text
    assert "CU01" in text


# ---------------------------------------------------------------------------
# html/sitemap.xml.gz
# ---------------------------------------------------------------------------

def test_sitemap_xml_gz_decompresses_to_valid_xml():
    gz_path = REPO_ROOT / "html/sitemap.xml.gz"
    assert gz_path.is_file(), "html/sitemap.xml.gz must exist."

    with gzip.open(gz_path, "rb") as f:
        decompressed = f.read()

    root = ET.fromstring(decompressed)
    assert root.tag.endswith("urlset")


def test_sitemap_xml_gz_matches_uncompressed_sitemap():
    """The gzip-compressed sitemap and the plain html/sitemap.xml file should
    describe the same document (both are produced by the same MkDocs build
    step)."""
    gz_path = REPO_ROOT / "html/sitemap.xml.gz"
    plain_path = REPO_ROOT / "html/sitemap.xml"
    assert plain_path.is_file(), "html/sitemap.xml must exist for comparison."

    with gzip.open(gz_path, "rb") as f:
        decompressed = f.read().decode("utf-8")

    plain_content = plain_path.read_text(encoding="utf-8")
    assert decompressed.strip() == plain_content.strip()


def test_sitemap_xml_gz_is_not_empty_gzip_stream():
    gz_path = REPO_ROOT / "html/sitemap.xml.gz"
    raw_bytes = gz_path.read_bytes()
    # gzip magic number
    assert raw_bytes[:2] == b"\x1f\x8b"
    assert len(raw_bytes) > 0