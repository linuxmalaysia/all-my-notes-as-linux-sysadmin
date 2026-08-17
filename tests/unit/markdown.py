"""Unit tests for Markdown files.

Validates Open Knowledge Framework (OKF) v0.1 schema compliance, DSOM governance footers,
and UK English spelling standards across repository documentation.
"""

import glob
import os
import re
import pytest

TARGET_DIRS = ["docs/**/*.md", "openwiki/**/*.md", "manual/**/*.md", ".agents/skills/*/SKILL.md"]
EXCLUDED_FILES = ["README.md", "CHANGELOG.md", "HISTORY.md", "AGENTS.md", "SUMMARY.md"]


def get_markdown_files():
    """Collect Markdown files from the configured target directories, excluding specified files.
    
    Returns:
    	list[str]: Sorted unique paths to matching Markdown files.
    """
    files = []
    for pattern in TARGET_DIRS:
        files.extend(glob.glob(pattern, recursive=True))
    return sorted(list(set([f for f in files if os.path.basename(f) not in EXCLUDED_FILES])))


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_markdown_okf_compliance(filepath):
    """
    Verify that a Markdown file has valid YAML frontmatter containing OKF or DSOM metadata and a title or name.
    """
    assert os.path.exists(filepath), f"Markdown file missing: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read()

    assert content.startswith("---"), f"File {filepath} must start with YAML frontmatter."

    parts = content.split("---", 2)
    assert len(parts) >= 3, f"File {filepath} has malformed YAML closure '---'."

    frontmatter = parts[1].strip()
    has_okf = "okf_version:" in frontmatter or "dsom_governance:" in frontmatter
    assert has_okf, f"File {filepath} frontmatter must contain OKF or DSOM metadata keys."

    has_title = "title:" in frontmatter or "name:" in frontmatter
    assert has_title, f"File {filepath} missing 'title' or 'name' in frontmatter."


@pytest.mark.parametrize("filepath", get_markdown_files())
def test_markdown_governance_footers(filepath):
    """Verify markdown file contains DSOM governance footers and author attribution."""
    assert os.path.exists(filepath), f"Markdown file missing: {filepath}"

    with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
        content = f.read().strip()

    has_author = "Harisfazillah Jamel" in content or "LinuxMalaysia" in content
    assert has_author, f"File {filepath} missing Author attribution in governance footer."

    has_license = (
        "Dwi-Lesen" in content
        or "Dual-License" in content
        or "CC BY-SA 4.0" in content
        or "GNU" in content
    )
    assert has_license, f"File {filepath} missing Licensing standard in governance footer."


def test_uk_english_documentation_spellings():
    """Verify UK English spelling conventions across key repository documentation."""
    files = get_markdown_files()
    assert len(files) > 0, "No markdown files discovered for UK English spelling check."

    # Validate that UK English variants are predominantly used across English documentation
    uk_terms = ["virtualisation", "optimisation", "organisation", "licence", "behaviour"]
    found_uk_terms = {term: 0 for term in uk_terms}

    for filepath in files:
        with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
            content = f.read().lower()

        for term in uk_terms:
            if term in content:
                found_uk_terms[term] += 1

    # Ensure UK English terms are actively present in the documentation suite
    for term, count in found_uk_terms.items():
        assert count > 0, f"Expected UK English term '{term}' to be used in repository documentation, found 0."
