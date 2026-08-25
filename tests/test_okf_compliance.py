"""Integration tests for OKF Markdown Compliance.

This test suite scans all markdown files across the repository to ensure
strict compliance with the Google OKF v0.2 YAML Frontmatter standard and
the mandatory Sovereign Markdown Palace dual-license footer.
"""

import glob
import os

import pytest

# Directories to scan
TARGET_DIRS = ["docs/**/*.md", "openwiki/**/*.md", "manual/**/*.md", ".agents/skills/*/SKILL.md"]
EXCLUDED_FILES = ["README.md", "CHANGELOG.md", "HISTORY.md", "AGENTS.md", "SUMMARY.md"]

def get_markdown_files():
    """Retrieve all markdown files matching the target directories."""
    files = []
    for pattern in TARGET_DIRS:
        files.extend(glob.glob(pattern, recursive=True))
        
    # Filter out excluded files
    return [f for f in files if os.path.basename(f) not in EXCLUDED_FILES]

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_okf_frontmatter(filepath):
    """Verify that the markdown file begins with valid OKF YAML frontmatter."""
    with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
        
    assert content.startswith("---"), f"File {filepath} must start with YAML frontmatter."
    
    parts = content.split("---", 2)
    assert len(parts) >= 3, f"File {filepath} has malformed or missing YAML closure '---'."
    
    frontmatter = parts[1].strip()
    
    # Check for mandatory OKF keys (depending on the domain, either okf_version or dsom_governance)
    has_okf = "okf_version:" in frontmatter or "dsom_governance:" in frontmatter
    assert has_okf, f"File {filepath} must contain OKF or DSOM metadata keys."
    assert "title:" in frontmatter or "name:" in frontmatter, f"File {filepath} is missing 'title' or 'name' in frontmatter."

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_sovereign_footer(filepath):
    """Verify that the markdown file ends with the Sovereign dual-license footer."""
    with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read().strip()
        
    # The exact footer varies slightly depending on date, but must contain key phrases
    assert "Harisfazillah Jamel" in content or "LinuxMalaysia" in content, f"File {filepath} missing Author attribution in footer."
    assert "Dwi-Lesen" in content or "Dual-License" in content or "CC BY-SA 4.0" in content or "GNU" in content, f"File {filepath} missing Licensing standard in footer."
