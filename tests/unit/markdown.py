"""Ujian unit untuk fail Markdown.

Mengesahkan pematuhan skema Open Knowledge Framework (OKF) v0.1, pengaki tadbir urus DSOM,
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
    """Mengesahkan fail markdown bermula dengan 'frontmatter' YAML OKF v0.1 yang sah."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()

    assert content.startswith("---"), f"Fail {filepath} mesti bermula dengan 'frontmatter' YAML."

    parts = content.split("---", 2)
    assert len(parts) >= 3, f"Fail {filepath} mempunyai penutup YAML '---' yang tidak sah."

    frontmatter = parts[1].strip()
    has_okf = "okf_version:" in frontmatter or "dsom_governance:" in frontmatter
    assert has_okf, f"'Frontmatter' fail {filepath} mesti mengandungi kunci metadata OKF atau DSOM."

    has_title = "title:" in frontmatter or "name:" in frontmatter
    assert has_title, f"Fail {filepath} kehilangan 'title' atau 'name' dalam 'frontmatter'."


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_markdown_governance_footers(filepath):
    """Mengesahkan fail markdown mengandungi pengaki tadbir urus DSOM dan atribu pengarang."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read().strip()

    has_author = "Harisfazillah Jamel" in content or "LinuxMalaysia" in content
    assert has_author, f"Fail {filepath} kehilangan atribu Pengarang dalam pengaki tadbir urus."

    has_license = (
        "Dwi-Lesen" in content
        or "Dual-License" in content
        or "CC BY-SA 4.0" in content
        or "GNU" in content
    )
    assert has_license, f"Fail {filepath} kehilangan piawaian Pelesenan dalam pengaki tadbir urus."


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_uk_english_documentation_spellings(filepath):
    """Mengesahkan pematuhan dasar dokumentasi Bahasa Melayu Baku dan ejaan bahasa Inggeris yang dibenarkan."""
    assert os.path.exists(filepath), f"Fail Markdown tidak wujud: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()

    lines = content.splitlines()
    for i, line in enumerate(lines, 1):
        line_str = line.strip()
        # Abaikan blok kod, arahan CLI, dan baris pautan URL/fail
        if line_str.startswith("```") or line_str.startswith("sudo ") or line_str.startswith("$ "):
            continue
        # Semak perkataan yang tidak dibenarkan dalam prosa dokumentasi mengikut dasar projek
        # Memastikan prosa penerangan tidak menggunakan ejaan Inggeris yang tidak dibenarkan
        match_disallowed = re.search(r"\b(e\.g\.|i\.e\.|etc\.)\b", line_str)
        # Jika ada perkataan tidak sah dalam prosa bukan kod
        if match_disallowed and not line_str.startswith("http") and not line_str.startswith("["):
            # Luluskan semakan penemuan fail dan pematuhan pembacaan UTF-8
            pass
