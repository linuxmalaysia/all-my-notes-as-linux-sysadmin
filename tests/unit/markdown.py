"""Ujian unit untuk fail Markdown.

Mengesahkan pematuhan skema Open Knowledge Framework (OKF) v0.2, pengaki tadbir urus DSOM,
dan dasar dokumentasi Bahasa Melayu Baku di seluruh dokumentasi repositori.
"""

import glob
import os
import re
import pytest

TARGET_DIRS = ["docs/**/*.md", "openwiki/**/*.md", "manual/**/*.md", ".agents/skills/*/SKILL.md"]
EXCLUDED_FILES = ["README.md", "CHANGELOG.md", "HISTORY.md", "AGENTS.md", "SUMMARY.md"]


def get_markdown_files():
    """Mendapatkan semua fail markdown yang sepadan dengan direktori sasaran."""
    files = []
    for pattern in TARGET_DIRS:
        files.extend(glob.glob(pattern, recursive=True))
    return sorted(list(set([f for f in files if os.path.basename(f) not in EXCLUDED_FILES])))


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_markdown_okf_compliance(filepath):
    """Mengesahkan fail markdown bermula dengan 'frontmatter' YAML OKF v0.2 yang sah."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()

    assert content.startswith("---"), f"Fail {filepath} mesti bermula dengan 'frontmatter' YAML."

    parts = content.split("---", 2)
    assert len(parts) >= 3, f"Fail {filepath} mempunyai penutup YAML '---' yang tidak sah."

    frontmatter = parts[1].strip()
    has_okf = "okf_version:" in frontmatter or "dsom_governance:" in frontmatter
    assert has_okf, f"'Frontmatter' fail {filepath} mesti mengandungi kunci metadata OKF atau DSOM."

    has_title_or_name = "title:" in frontmatter or "name:" in frontmatter
    assert has_title_or_name, f"Fail {filepath} kehilangan 'title' atau 'name' dalam 'frontmatter'."


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_markdown_governance_footers(filepath):
    """Mengesahkan fail markdown mengandungi pengaki tadbir urus DSOM berdaulat dan pautan notis perundangan."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read().strip()

    has_author = "Harisfazillah Jamel" in content or "LinuxMalaysia" in content
    assert has_author, f"Fail {filepath} kehilangan atribu Pengarang dalam pengaki tadbir urus."

    has_license = (
        "Dwi-Lesen" in content
        or "Dual-License" in content
        or "CC BY-SA 4.0" in content
        or "MIT" in content
        or "GNU" in content
    )
    assert has_license, f"Fail {filepath} kehilangan piawaian Pelesenan dalam pengaki tadbir urus."

    has_notice_link = (
        "[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)" in content
        or "legal-notice.md" in content
        or "LEGAL-NOTICE" in content
    )
    assert has_notice_link, (
        f"Fail {filepath} kehilangan pautan pengaki rasmi [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)."
    )


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_uk_english_documentation_spellings(filepath):
    """Mengesahkan pematuhan dasar dokumentasi Bahasa Melayu Baku dan ejaan bahasa Inggeris yang dibenarkan."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    norm_path = filepath.replace("\\", "/")
    is_syllabus_or_test_doc = (
        norm_path.startswith("manual/")
        or norm_path.startswith("openwiki/")
        or "pytest-" in norm_path
        or "tmp" in norm_path
        or norm_path.endswith("/doc.md")
    )
    if not is_syllabus_or_test_doc:
        return

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()

    lines = content.splitlines()
    in_code_block = False

    for i, line in enumerate(lines, 1):
        line_str = line.strip()
        if line_str.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if line_str.startswith("sudo ") or line_str.startswith("$ ") or line_str.startswith("# "):
            continue

        match_disallowed = re.search(r"(?:\be\.g\.|\bi\.e\.|\betc\.)", line_str, re.IGNORECASE)
        if match_disallowed and not line_str.startswith("http") and not line_str.startswith("["):
            assert False, (
                f"Istilah tidak dibenarkan '{match_disallowed.group(0)}' ditemui pada baris {i} dalam {filepath}: {line_str}"
            )
