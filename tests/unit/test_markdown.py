"""Ujian unit untuk tests/unit/markdown.py (pengesah pematuhan markdown OKF/DSOM)."""

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_markdown_module():
    module_path = REPO_ROOT / "tests" / "unit" / "markdown.py"
    spec = importlib.util.spec_from_file_location("unit_test_target_markdown", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


markdown_mod = _load_markdown_module()


# ---------------------------------------------------------------------------
# get_markdown_files()
# ---------------------------------------------------------------------------

def test_get_markdown_files_discovers_expected_patterns(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    expected = [
        "docs/sub/a.md",
        "openwiki/b.md",
        "manual/cu01/c.md",
        ".agents/skills/skillA/SKILL.md",
    ]
    for rel in expected:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("content", encoding="utf-8")

    # Should NOT match: .agents/skills/*/SKILL.md is not a wildcard for other filenames.
    other_skill_file = tmp_path / ".agents/skills/skillA/other.md"
    other_skill_file.write_text("content", encoding="utf-8")

    found = markdown_mod.get_markdown_files()

    assert sorted(found) == sorted(expected)
    assert ".agents/skills/skillA/other.md" not in found


def test_get_markdown_files_excludes_configured_filenames(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    kept = tmp_path / "docs" / "kept.md"
    kept.parent.mkdir(parents=True, exist_ok=True)
    kept.write_text("content", encoding="utf-8")

    for excluded_name in ["README.md", "CHANGELOG.md", "HISTORY.md", "AGENTS.md", "SUMMARY.md"]:
        excluded_path = tmp_path / "docs" / excluded_name
        excluded_path.write_text("content", encoding="utf-8")

    found = markdown_mod.get_markdown_files()

    assert found == ["docs/kept.md"]


def test_get_markdown_files_returns_empty_list_when_nothing_matches(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert markdown_mod.get_markdown_files() == []


# ---------------------------------------------------------------------------
# test_markdown_okf_compliance()
# ---------------------------------------------------------------------------

def test_okf_compliance_accepts_okf_version_and_title(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text(
        "---\nokf_version: 0.2\ntitle: Sample Document\n---\n\nBody content.\n",
        encoding="utf-8",
    )
    markdown_mod.test_markdown_okf_compliance(str(md))


def test_okf_compliance_accepts_dsom_governance_and_name(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text(
        "---\ndsom_governance: true\nname: Sample Skill\n---\n\nBody content.\n",
        encoding="utf-8",
    )
    markdown_mod.test_markdown_okf_compliance(str(md))


def test_okf_compliance_rejects_missing_file():
    with pytest.raises(AssertionError, match=r"(Markdown file missing|tidak wujud)"):
        markdown_mod.test_markdown_okf_compliance("no/such/doc.md")


def test_okf_compliance_rejects_file_without_leading_frontmatter(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("# Just a heading\n\nNo frontmatter here.\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(must start with YAML frontmatter|mesti bermula dengan 'frontmatter')"):
        markdown_mod.test_markdown_okf_compliance(str(md))


def test_okf_compliance_rejects_malformed_frontmatter_closure(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("---\nokf_version: 0.2\ntitle: X\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(malformed YAML closure|penutup YAML '---' yang tidak sah)"):
        markdown_mod.test_markdown_okf_compliance(str(md))


def test_okf_compliance_rejects_missing_okf_or_dsom_keys(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("---\ntitle: X\n---\n\nBody.\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(OKF or DSOM|OKF atau DSOM)"):
        markdown_mod.test_markdown_okf_compliance(str(md))


def test_okf_compliance_rejects_missing_title_or_name(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("---\nokf_version: 0.2\n---\n\nBody.\n", encoding="utf-8")
    with pytest.raises(AssertionError) as excinfo:
        markdown_mod.test_markdown_okf_compliance(str(md))
    assert "title" in str(excinfo.value) and "name" in str(excinfo.value)


# ---------------------------------------------------------------------------
# test_markdown_governance_footers()
# ---------------------------------------------------------------------------

def test_governance_footer_accepts_author_and_cc_license(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Body.\n\nAuthor: Harisfazillah Jamel — CC BY-SA 4.0\n[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)\n", encoding="utf-8")
    markdown_mod.test_markdown_governance_footers(str(md))


def test_governance_footer_accepts_linuxmalaysia_and_gnu_license(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Body.\n\n(c) LinuxMalaysia — GNU license\n[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)\n", encoding="utf-8")
    markdown_mod.test_markdown_governance_footers(str(md))


def test_governance_footer_rejects_missing_author(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Body.\n\nCC BY-SA 4.0\n[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(Author attribution|Pengarang dalam pengaki)"):
        markdown_mod.test_markdown_governance_footers(str(md))


def test_governance_footer_rejects_missing_license(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Body.\n\nAuthor: Harisfazillah Jamel\n[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)\n", encoding="utf-8")
    with pytest.raises(AssertionError, match=r"(Licensing standard|Pelesenan dalam pengaki)"):
        markdown_mod.test_markdown_governance_footers(str(md))


def test_governance_footer_rejects_missing_file():
    with pytest.raises(AssertionError, match=r"(Markdown file missing|tidak wujud)"):
        markdown_mod.test_markdown_governance_footers("no/such/doc.md")


# ---------------------------------------------------------------------------
# test_uk_english_documentation_spellings()
# ---------------------------------------------------------------------------

def _write_doc(tmp_path, name, content):
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return str(path)


def test_uk_english_spellings_passes_when_all_terms_present(tmp_path, monkeypatch):
    doc = _write_doc(
        tmp_path,
        "doc.md",
        "This covers virtualisation, optimisation, organisation, licence and behaviour.\n",
    )
    markdown_mod.test_uk_english_documentation_spellings(doc)


def test_uk_english_spellings_fails_when_disallowed_term_present(tmp_path):
    doc = _write_doc(
        tmp_path,
        "doc.md",
        "Prosa mengandungi e.g. istilah yang tidak dibenarkan.\n",
    )
    with pytest.raises(AssertionError, match=r"(e\.g\.|Istilah tidak dibenarkan)"):
        markdown_mod.test_uk_english_documentation_spellings(doc)


def test_uk_english_spellings_is_case_insensitive(tmp_path):
    doc = _write_doc(
        tmp_path,
        "doc.md",
        "VIRTUALISATION, Optimisation, ORGANISATION, Licence, BEHAVIOUR.\n",
    )
    markdown_mod.test_uk_english_documentation_spellings(doc)
