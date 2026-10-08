"""Integration tests for OKF v0.2 Markdown Compliance.

This test suite scans all markdown files across the repository to ensure
strict compliance with the Google OKF v0.2 YAML Frontmatter standard,
trust signals, sources provenance (internal docs & public internet URLs),
and the mandatory Sovereign Markdown Palace dual-license footer.
"""

import os

import pytest
import yaml

EXCLUDED_DIRS = {"build", "html", "node_modules", ".git", ".pytest_cache", "scratch"}

def get_markdown_files():
    """Retrieve all markdown files in the repository except excluded directories."""
    files = []
    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(os.path.join(root, filename))
    return sorted(files)

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_okf_v02_frontmatter(filepath):
    """Verify that the markdown file begins with valid OKF v0.2 YAML frontmatter and trust signals."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    norm_path = filepath.replace("\\", "/")
    filename = os.path.basename(norm_path)
    if filename in ["index.md", "log.md"] and norm_path not in ["./index.md", "index.md"]:
        # Reserved files in subdirectories MUST NOT carry frontmatter per OKF v0.2 §3.1 & §8
        assert not content.startswith("---"), f"Reserved file {filepath} must not carry YAML frontmatter per OKF v0.2 §3.1 & §8."
        return
        
    assert content.startswith("---"), f"File {filepath} must start with YAML frontmatter '---'."
    
    parts = content.split("---", 2)
    assert len(parts) >= 3, f"File {filepath} has malformed or missing YAML closure '---'."
    
    raw_fm = parts[1].strip()
    data = yaml.safe_load(raw_fm)
    assert isinstance(data, dict), f"File {filepath} frontmatter must be a valid YAML object."

    # Assert OKF v0.2 version indicators
    version = str(data.get("okf_version") or data.get("spec_version") or "")
    assert version == "0.2", f"File {filepath} must specify okf_version or spec_version as '0.2'."

    # Assert basic metadata
    assert "type" in data, f"File {filepath} missing 'type' functional classification."
    assert "title" in data or "name" in data, f"File {filepath} missing 'title' or 'name'."
    assert "description" in data, f"File {filepath} missing 'description'."

    # Assert Trust Signals
    assert "status" in data, f"File {filepath} missing 'status' lifecycle indicator."
    assert "stale_after" in data, f"File {filepath} missing 'stale_after' freshness date."
    assert "generated" in data, f"File {filepath} missing 'generated' provenance record."

    # Assert Sources (Internal Document Reference & Public Internet URL)
    assert "sources" in data and isinstance(data["sources"], list), f"File {filepath} must contain a list of 'sources'."
    sources = data["sources"]
    assert len(sources) >= 1, f"File {filepath} 'sources' must contain at least one source entry."

    has_internal_ref = False
    has_public_url = False

    for src in sources:
        if isinstance(src, dict):
            res = str(src.get("url") or src.get("resource") or "")
            if res.startswith(("http://", "https://")):
                has_public_url = True
            elif res.endswith(".md") or "/" in res or res.startswith("file:"):
                has_internal_ref = True

    assert has_internal_ref, f"File {filepath} sources must include an internal document reference."
    assert has_public_url, f"File {filepath} sources must include a public internet URL."

@pytest.mark.parametrize("filepath", get_markdown_files())
def test_sovereign_footer(filepath):
    """Verify that the markdown file ends with the Sovereign dual-license footer."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        
    assert "Harisfazillah Jamel" in content or "LinuxMalaysia" in content, f"File {filepath} missing Author attribution in footer."
    assert "Dwi-Lesen" in content or "Dual-License" in content or "CC BY-SA 4.0" in content or "GNU" in content, f"File {filepath} missing Licensing standard in footer."
