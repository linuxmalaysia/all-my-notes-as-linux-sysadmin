"""Tests for CU03 & CU06 Core Server Configurations, Process Management, Monitoring and Agent Skills content.

Covers:
  - manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md
  - manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md
  - .agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md
  - .agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md
  - .agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md
  - openwiki/topic-03-linux-server-administration.md
  - openwiki/topic-06-troubleshooting-and-logs.md
"""

from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """Read a repository file as UTF-8 text, removing an optional byte-order mark.
    
    Parameters:
    	relative_path: Path to the file relative to the repository root.
    
    Returns:
    	The file contents as a string.
    """
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_manual_cu03_wa04_has_required_systemd_concepts():
    content = read("manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md")
    assert "systemctl" in content
    assert "journalctl" in content
    assert "timedatectl" in content
    assert "chrony" in content or "chronyd" in content
    assert "man" in content
    assert "apropos" in content
    assert "whatis" in content
    assert "Asia/Kuala_Lumpur" in content

def test_manual_cu06_wa05_has_required_process_concepts():
    content = read("manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md")
    assert "ps aux" in content
    assert "top" in content
    assert "htop" in content
    assert "vmstat" in content
    assert "iostat" in content
    assert "SIGTERM" in content
    assert "SIGKILL" in content
    assert "nice" in content
    assert "renice" in content
    assert "cgroups" in content or "systemd-run" in content

def test_skill_cu03_wa04_type_skill_and_content():
    content = read(".agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md")
    assert "type: skill" in content
    assert "systemctl" in content
    assert "journalctl" in content
    assert "timedatectl" in content
    assert "chrony" in content or "chronyd" in content

def test_skill_cu06_wa05_type_skill_and_content():
    content1 = read(".agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md")
    assert "type: skill" in content1
    assert "ps aux" in content1
    assert "vmstat" in content1
    assert "SIGTERM" in content1

    content2 = read(".agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md")
    assert "type: skill" in content2
    assert "ps aux" in content2
    assert "vmstat" in content2
    assert "SIGTERM" in content2

def test_openwiki_topics_links_and_structure():
    content3 = read("openwiki/topic-03-linux-server-administration.md")
    assert "cu03-wa04-konfigurasi-teras-pelayan.md" in content3
    assert "cu03-wa04-perform-core-server-configurations" in content3

    content6 = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md" in content6
    assert "cu06-wa05-perform-system-optimisation-and-disk-management" in content6
