"""Tests for the Bab 2 (CU01) content in manual/cu01/.

Covers:
  - The four Sovereign Manual knowledge nodes under manual/cu01/
    (hardware/UEFI, installation procedure, LUKS2 encryption, post-install).
  - The updated openwiki/topic-01-linux-desktop-and-basics.md syllabus, which
    now links to the four new nodes and references 2026 canonical distros.
  - The Master Palace Registry (.agents/skills/index.md) timestamp update.
"""

import os
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

NEW_MANUAL_NODES = [
    "manual/cu01/keperluan-perkakasan-dan-bios-uefi.md",
    "manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md",
    "manual/cu01/penyulitan-cakera-luks2-pejabat.md",
    "manual/cu01/pasca-pemasangan-dan-driver.md",
]

OPENWIKI_TOPIC_01 = "openwiki/topic-01-linux-desktop-and-basics.md"
SKILLS_INDEX = ".agents/skills/index.md"

TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")


def split_frontmatter(content):
    """Split a markdown file's content into (frontmatter, body)."""
    assert content.startswith("---"), "File must start with YAML frontmatter."
    parts = content.split("---", 2)
    assert len(parts) >= 3, "File has malformed or missing YAML closure '---'."
    return parts[1].strip(), parts[2]


# ---------------------------------------------------------------------------
# New manual/cu01 knowledge nodes
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("relpath", NEW_MANUAL_NODES)
def test_new_manual_node_exists(relpath):
    assert (REPO_ROOT / relpath).is_file(), f"Expected knowledge node {relpath} to exist."


@pytest.mark.parametrize("relpath", NEW_MANUAL_NODES)
def test_new_manual_node_has_okf_frontmatter(relpath):
    content = read(relpath)
    frontmatter, _ = split_frontmatter(content)

    assert "okf_version:" in frontmatter, f"{relpath} missing okf_version key."
    assert "type: knowledge_node" in frontmatter or "type: knowledge-node" in frontmatter, f"{relpath} should be type: knowledge_node."
    assert "title:" in frontmatter, f"{relpath} missing title key."
    assert "timestamp:" in frontmatter, f"{relpath} missing timestamp key."
    assert "resource:" in frontmatter, f"{relpath} missing resource key."


@pytest.mark.parametrize("relpath", NEW_MANUAL_NODES)
def test_new_manual_node_timestamp_is_valid_iso8601(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} timestamp value must be a quoted ISO8601 string."
    assert TIMESTAMP_RE.match(match.group(1)), (
        f"{relpath} timestamp '{match.group(1)}' is not in YYYY-MM-DDTHH:MM:SSZ format."
    )


@pytest.mark.parametrize("relpath", NEW_MANUAL_NODES)
def test_new_manual_node_resource_path_matches_file_location(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'resource:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} is missing a resource: URI."
    expected = f"file:///{relpath}"
    assert match.group(1) == expected, (
        f"{relpath} resource URI '{match.group(1)}' does not match expected '{expected}'."
    )


@pytest.mark.parametrize("relpath", NEW_MANUAL_NODES)
def test_new_manual_node_has_sovereign_footer(relpath):
    content = read(relpath).strip()
    assert "Harisfazillah Jamel" in content or "LinuxMalaysia" in content, (
        f"{relpath} missing author attribution footer."
    )
    assert "Dwi-Lesen" in content or "CC BY-SA 4.0" in content, (
        f"{relpath} missing dual-license footer."
    )
    assert "Notis Perundangan" in content, f"{relpath} missing legal notice link in footer."


def test_hardware_bios_uefi_node_mentions_canonical_2026_distros():
    content = read("manual/cu01/keperluan-perkakasan-dan-bios-uefi.md")
    for distro in ["Ubuntu 26.04 LTS", "Fedora 43", "AlmaLinux 10"]:
        assert distro in content, f"Hardware/BIOS node should reference '{distro}'."
    assert "UEFI" in content
    assert "Secure Boot" in content
    assert "Ventoy" in content


def test_installation_procedure_node_covers_lvm_and_target_distros():
    content = read("manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md")
    assert "LVM" in content
    for distro in ["Ubuntu 26.04 LTS", "AlmaLinux 10", "Fedora 43"]:
        assert distro in content, f"Installation node should reference '{distro}'."


def test_luks2_encryption_node_covers_key_compliance_topics():
    content = read("manual/cu01/penyulitan-cakera-luks2-pejabat.md")
    assert "LUKS2" in content
    assert "cryptsetup" in content
    assert "ISO/IEC 27001" in content
    assert "MAMPU" in content
    assert "key slots" in content.lower() or "slot kunci" in content.lower()


def test_post_install_node_covers_package_management_and_hardening():
    content = read("manual/cu01/pasca-pemasangan-dan-driver.md")
    for tool in ["apt", "dnf", "ufw", "firewalld", "sshd"]:
        assert tool in content, f"Post-install node should reference '{tool}'."


# ---------------------------------------------------------------------------
# Updated openwiki topic-01 syllabus
# ---------------------------------------------------------------------------

def test_openwiki_topic01_frontmatter_updated_for_2026():
    frontmatter, _ = split_frontmatter(read(OPENWIKI_TOPIC_01))
    assert "2026" in frontmatter
    assert "luks2" in frontmatter.lower()


def test_openwiki_topic01_title_reflects_2026_update():
    content = read(OPENWIKI_TOPIC_01)
    assert "Dikemaskini 2026" in content
    assert "Dikemaskini 2024" not in content


@pytest.mark.parametrize(
    "expected_link",
    [
        "manual/cu01/keperluan-perkakasan-dan-bios-uefi.md",
        "manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md",
        "manual/cu01/penyulitan-cakera-luks2-pejabat.md",
        "manual/cu01/penegasan-keselamatan-sistem.md",
    ],
)
def test_openwiki_topic01_links_to_new_nodes(expected_link):
    content = read(OPENWIKI_TOPIC_01)
    assert expected_link in content, f"Syllabus should link to {expected_link}."


def test_openwiki_topic01_has_numbered_sections():
    content = read(OPENWIKI_TOPIC_01)
    for n in range(1, 11):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"Expected numbered section heading '### {n}. ...' in syllabus."
        )


def test_openwiki_topic01_mentions_canonical_2026_distros():
    content = read(OPENWIKI_TOPIC_01)
    for distro in ["Ubuntu 26.04 LTS", "Fedora 43", "AlmaLinux 10"]:
        assert distro in content


def test_openwiki_topic01_no_longer_references_stale_2024_distro_versions():
    content = read(OPENWIKI_TOPIC_01)
    for stale in ["Ubuntu 24.04", "Fedora 41", "RHEL 9.4", "GNOME 46"]:
        assert stale not in content, f"Stale reference '{stale}' should have been removed."


# ---------------------------------------------------------------------------
# Master Palace Registry timestamp
# ---------------------------------------------------------------------------

def test_skills_index_timestamp_is_valid_iso8601():
    frontmatter, _ = split_frontmatter(read(SKILLS_INDEX))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "Master Palace Registry is missing a timestamp field."
    assert TIMESTAMP_RE.match(match.group(1)), (
        f"Master Palace Registry timestamp '{match.group(1)}' is not valid ISO8601 UTC."
    )


def test_skills_index_title_unchanged():
    frontmatter, _ = split_frontmatter(read(SKILLS_INDEX))
    assert 'title: "Master Palace Registry"' in frontmatter
