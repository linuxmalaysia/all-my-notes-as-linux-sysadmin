"""Tests for CU02 Storage Management and Agent Skills content.

Covers:
  - manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md
  - .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md
  - .agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md
  - .agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md
  - openwiki/topic-02-storage-and-virtualisation.md
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """Reads a file relative to repository root into string.

    Args:
        relative_path (str): Relative path from repo root.

    Returns:
        str: UTF-8 file content string.
    """
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_cu02_storage_manual_has_destructive_warning_and_key_procedures():
    content = read("manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md")
    assert "AMARAN OPERASI MEMUSNAHKAN DATA" in content
    assert "gdisk" in content
    assert "parted" in content
    assert "pvcreate" in content
    assert "vgcreate" in content
    assert "lvcreate" in content
    assert "mkfs.ext4" in content
    assert "mkfs.xfs" in content
    assert "mkfs.btrfs" in content
    assert "UUID=" in content
    assert "mount -a" in content
    assert "cryptsetup" in content
    assert "/etc/crypttab" in content

def test_skill_cu01_wa05_has_correct_keyrings_and_codename():
    content = read(".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md")
    assert "Resolute Raccoon" in content
    assert "/etc/apt/keyrings/" in content or "signed-by=" in content
    assert "check-upgrade" in content
    assert "rpmfusion" in content

def test_skill_cu01_wa06_has_dhcp_cleanup_and_wifi_prompt():
    content = read(".agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md")
    assert 'ipv4.addresses ""' in content
    assert 'ipv4.gateway ""' in content
    assert 'ipv4.dns ""' in content
    assert "--ask" in content or "Personal" in content

def test_skill_cu02_wa01_has_warning_and_uuid_check():
    content = read(".agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md")
    assert "DESTRUCTIVE OPERATION WARNING" in content
    assert "parted" in content
    assert "pvcreate" in content
    assert "grep -q" in content
    assert "mount -a" in content

def test_openwiki_topic02_reclassifies_kvm_as_type_1():
    content = read("openwiki/topic-02-storage-and-virtualisation.md")
    assert "Type-1" in content or "Jenis-1" in content
    assert "KVM" in content
    assert "VirtualBox" in content
