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

import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_manual_cu03_wa04_has_required_systemd_concepts():
    content = read("manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md")
    assert re.search(r'`systemctl`|\bsystemctl\b', content)
    assert re.search(r'`journalctl`|\bjournalctl\b', content)
    assert re.search(r'`timedatectl`|\btimedatectl\b', content)
    assert re.search(r'`chrony`|\bchrony\b|\bchronyd\b', content)
    assert re.search(r'`man`|\bman\b', content)
    assert re.search(r'`apropos`|\bapropos\b', content)
    assert re.search(r'`whatis`|\bwhatis\b', content)
    assert "Asia/Kuala_Lumpur" in content

def test_manual_cu06_wa05_has_required_process_concepts():
    content = read("manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md")
    assert re.search(r'`ps aux`|\bps aux\b', content)
    assert re.search(r'`top`|\btop\b', content)
    assert re.search(r'`htop`|\bhtop\b', content)
    assert re.search(r'`vmstat`|\bvmstat\b', content)
    assert re.search(r'`iostat`|\biostat\b', content)
    assert "SIGTERM" in content
    assert "SIGKILL" in content
    assert re.search(r'`nice`|\bnice\b', content)
    assert re.search(r'`renice`|\brenice\b', content)
    assert "cgroups" in content or "systemd-run" in content

def test_skill_cu03_wa04_type_skill_and_content():
    content = read(".agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md")
    assert "type: skill" in content
    assert re.search(r'`systemctl`|\bsystemctl\b', content)
    assert re.search(r'`journalctl`|\bjournalctl\b', content)
    assert re.search(r'`timedatectl`|\btimedatectl\b', content)
    assert re.search(r'`chrony`|\bchrony\b|\bchronyd\b', content)

def test_skill_cu06_wa05_type_skill_and_content():
    content1 = read(".agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md")
    assert "type: skill" in content1
    assert re.search(r'`ps aux`|\bps aux\b', content1)
    assert re.search(r'`vmstat`|\bvmstat\b', content1)
    assert "SIGTERM" in content1

    content2 = read(".agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md")
    assert "type: skill" in content2
    assert re.search(r'`ps aux`|\bps aux\b', content2)
    assert re.search(r'`vmstat`|\bvmstat\b', content2)
    assert "SIGTERM" in content2

def test_openwiki_topics_links_and_structure():
    content3 = read("openwiki/topic-03-linux-server-administration.md")
    assert "cu03-wa04-konfigurasi-teras-pelayan.md" in content3
    assert "cu03-wa04-perform-core-server-configurations" in content3

    content6 = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md" in content6
    assert "cu06-wa05-perform-system-optimisation-and-disk-management" in content6

    # Verify that every mapped manual file exists on disk
    manual_targets = [
        "manual/cu03/cu03-wa01-persediaan-pemasangan-pelayan.md",
        "manual/cu03/cu03-wa02-pelaksanaan-pemasangan-fizikal-pelayan.md",
        "manual/cu03/cu03-wa03-pemasangan-sistem-operasi-pelayan.md",
        "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md",
        "manual/cu03/cu03-wa05-pelaksanaan-peranan-dan-servis-pelayan.md",
        "manual/cu03/cu03-wa06-pengurusan-perkakasan-dan-antaramuka-pelayan.md",
        "manual/cu06/cu06-wa01-keperluan-perkhidmatan-sokongan-pengguna.md",
        "manual/cu06/cu06-wa02-pengendalian-aduan-dan-insiden-pengguna.md",
        "manual/cu06/cu06-wa03-diagnostik-dan-troubleshooting-perkakasan.md",
        "manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md",
        "manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md",
        "manual/cu06/cu06-wa06-pengurusan-tiket-sokongan-dan-sla.md",
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md",
    ]
    for rel_path in manual_targets:
        assert (REPO_ROOT / rel_path).is_file(), f"Missing manual file target: {rel_path}"

    # Verify that every mapped skill directory contains SKILL.md
    skill_targets = [
        ".agents/skills/cu03-wa01-prepare-server-setup/SKILL.md",
        ".agents/skills/cu03-wa02-carry-out-server-installation/SKILL.md",
        ".agents/skills/cu03-wa03-install-server-operating-system/SKILL.md",
        ".agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md",
        ".agents/skills/cu03-wa05-implement-server-roles-and-services/SKILL.md",
        ".agents/skills/cu03-wa06-manage-server-hardware/SKILL.md",
        ".agents/skills/cu06-wa01-prepare-end-user-support-service-requirements/SKILL.md",
        ".agents/skills/cu06-wa02-handle-end-user-requests-and-incidents/SKILL.md",
        ".agents/skills/cu06-wa03-support-hardware-troubleshooting/SKILL.md",
        ".agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md",
        ".agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md",
        ".agents/skills/cu06-wa06-manage-support-tickets-and-slas/SKILL.md",
        ".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md",
    ]
    for rel_path in skill_targets:
        assert (REPO_ROOT / rel_path).is_file(), f"Missing skill file target: {rel_path}"
