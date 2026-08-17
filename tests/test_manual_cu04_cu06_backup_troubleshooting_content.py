"""Tests for CU04 & CU06 Backup, Recovery, External Storage, Text Processing, and Agent Skills content.

Covers:
  - manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md
  - manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md
  - manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md
  - manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md
  - .agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md
  - .agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md
  - .agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md
  - .agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md
  - openwiki/topic-04-automation-and-backup.md
  - openwiki/topic-06-troubleshooting-and-logs.md
"""

import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_manual_cu04_wa02_has_required_backup_concepts():
    content = read("manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md")
    assert re.search(r'`tar`|\btar\b', content)
    assert re.search(r'`zstd`|\bzstd\b', content)
    assert re.search(r'`gzip`|\bgzip\b', content)
    assert re.search(r'`rsync`|\brsync\b', content)
    assert re.search(r'`cron`|\bcron\b|\bcrontab\b', content)
    assert "systemd.timer" in content or "systemd" in content
    assert "3-2-1" in content
    assert "RequiresMountsFor" in content

def test_manual_cu04_wa04_has_required_recovery_concepts():
    content = read("manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md")
    assert re.search(r'`sha256sum`|\bsha256sum\b', content)
    assert re.search(r'`tar`|\btar\b', content)
    assert "bare-metal" in content.lower() or "baremetal" in content.lower()
    assert "/tmp/recovery_staging" in content
    assert "grub2-mkconfig" in content

def test_manual_cu06_wa04_has_required_mount_concepts():
    content = read("manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md")
    assert re.search(r'`mount`|\bmount\b', content)
    assert re.search(r'`umount`|\bumount\b', content)
    assert re.search(r'`findmnt`|\bfindmnt\b', content)
    assert "/etc/fstab" in content
    assert "nodev" in content and "nosuid" in content and "noexec" in content
    assert "nofail" in content
    assert "udisksctl" in content

def test_manual_cu06_wa07_has_required_text_filter_and_rca_concepts():
    content = read("manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md")
    assert re.search(r'`grep`|\bgrep\b', content)
    assert re.search(r'`sed`|\bsed\b', content)
    assert re.search(r'`awk`|\bawk\b', content)
    assert re.search(r'`cut`|\bcut\b', content)
    assert re.search(r'`sort`|\bsort\b', content)
    assert re.search(r'`uniq`|\buniq\b', content)
    assert re.search(r'`vim`|\bvim\b', content)
    assert re.search(r'`nano`|\bnano\b', content)
    assert "RCA" in content or "Root Cause Analysis" in content
    assert "sshd -t" in content

def test_skill_cu04_type_skill_and_content():
    content_wa02 = read(".agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md")
    assert "type: skill" in content_wa02
    assert re.search(r'`tar`|\btar\b', content_wa02)
    assert re.search(r'`rsync`|\brsync\b', content_wa02)
    assert "RequiresMountsFor" in content_wa02

    content_wa04 = read(".agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md")
    assert "type: skill" in content_wa04
    assert re.search(r'`sha256sum`|\bsha256sum\b', content_wa04)

def test_skill_cu06_type_skill_and_content():
    content_wa04 = read(".agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md")
    assert "type: skill" in content_wa04
    assert re.search(r'`mount`|\bmount\b', content_wa04)
    assert "/etc/fstab" in content_wa04
    assert "nofail" in content_wa04

    content_wa07 = read(".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md")
    assert "type: skill" in content_wa07
    assert re.search(r'`grep`|\bgrep\b', content_wa07)
    assert "RCA" in content_wa07
    assert "sshd -t" in content_wa07

def test_openwiki_topics_links_and_structure_cu04_cu06():
    content4 = read("openwiki/topic-04-automation-and-backup.md")
    assert "cu04-wa02-operasi-sandaran-tempatan.md" in content4
    assert "cu04-wa02-perform-local-backup-operations" in content4

    content6 = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md" in content6
    assert "cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md" in content6

    # Verify Palace Registry index entries
    palace_index = read(".agents/skills/index.md")
    assert "cu04-wa02-perform-local-backup-operations" in palace_index
    assert "cu04-wa04-restore-endpoint-data" in palace_index

    # Verify mapped manual targets exist
    manual_targets = [
        "manual/cu04/cu04-wa01-persediaan-alatan-sandaran-dan-pemulihan.md",
        "manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md",
        "manual/cu04/cu04-wa03-sandaran-berasaskan-rangkaian.md",
        "manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md",
        "manual/cu04/cu04-wa05-pemulihan-bare-metal-endpoint.md",
        "manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md",
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md",
    ]
    for rel_path in manual_targets:
        assert (REPO_ROOT / rel_path).is_file(), f"Missing manual file target: {rel_path}"

    # Verify mapped skill targets exist
    skill_targets = [
        ".agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md",
        ".agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md",
        ".agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md",
        ".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md",
    ]
    for rel_path in skill_targets:
        assert (REPO_ROOT / rel_path).is_file(), f"Missing skill file target: {rel_path}"
