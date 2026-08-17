"""Tests for CU05 User Administration, Permissions, Security Lockdowns and Agent Skills content.

Covers:
  - manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md
  - manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md
  - manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md
  - .agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md
  - .agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md
  - openwiki/topic-05-linux-security.md
"""

from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """
    Read a repository file as UTF-8 text, removing any leading byte-order mark.
    
    Parameters:
    	relative_path (str): Path to the file relative to the repository root.
    
    Returns:
    	str: The file contents.
    """
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_manual_cu05_main_node_has_required_concepts():
    content = read("manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md")
    assert "/etc/passwd" in content
    assert "/etc/shadow" in content
    assert "useradd" in content
    assert "usermod" in content
    assert "visudo" in content
    assert "faillock" in content
    assert "chmod" in content
    assert "chown" in content
    assert "getfacl" in content
    assert "setfacl" in content
    assert "TMOUT" in content
    assert "/etc/security/limits.conf" in content
    assert "systemctl poweroff" in content or "shutdown" in content

def test_manual_cu05_wa01_node_has_audit_commands():
    content = read("manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md")
    assert "pwck" in content
    assert "visudo -c" in content
    assert "getfacl" in content
    assert "faillock" in content

def test_manual_cu05_wa05_node_has_lockdown_commands():
    content = read("manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md")
    assert "grub" in content.lower()
    assert "TMOUT" in content
    assert "limits.conf" in content
    assert "systemctl poweroff" in content or "shutdown" in content

def test_skill_cu05_wa01_type_skill_and_content():
    content = read(".agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md")
    assert "type: skill" in content
    assert "pwck" in content
    assert "visudo -c" in content
    assert "faillock" in content

def test_skill_cu05_wa05_type_skill_and_content():
    content = read(".agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md")
    assert "type: skill" in content
    assert "TMOUT" in content
    assert "limits.conf" in content
    assert "grub" in content.lower()

def test_openwiki_topic05_links_and_structure():
    content = read("openwiki/topic-05-linux-security.md")
    assert "pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md" in content
    assert "cu05-wa01-perform-user-account-and-permission-audits" in content
    assert "cu05-wa05-manage-physical-endpoint-security-lockdowns" in content
