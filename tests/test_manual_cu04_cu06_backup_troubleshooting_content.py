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
  - .agents/skills/index.md
"""

import html as html_module
import json
import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def html_to_text(raw_html):
    """Strip HTML tags (incl. Pygments syntax-highlighting spans) and unescape entities,
    so that multi-token shell commands can be matched as plain substrings."""
    text = re.sub(r"<[^>]+>", "", raw_html)
    return html_module.unescape(text)

def extract_frontmatter(content):
    """Return the raw YAML frontmatter block delimited by leading '---' markers."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert match, "Expected YAML frontmatter delimited by '---' markers"
    return match.group(1)

def frontmatter_field(content, field):
    fm = extract_frontmatter(content)
    match = re.search(rf'^{field}:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    assert match, f"Frontmatter field '{field}' not found"
    return match.group(1).strip()

@pytest.fixture(scope="module")
def search_index():
    return json.loads(read("html/search/search_index.json"))

def find_doc(search_index, location):
    matches = [d for d in search_index["docs"] if d.get("location") == location]
    assert matches, f"No search_index.json doc entry found for location={location!r}"
    return matches[0]

def test_manual_cu04_wa02_has_required_backup_concepts():
    content = read("manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md")
    assert re.search(r'`tar`|\btar\b', content)
    assert re.search(r'`zstd`|\bzstd\b', content)
    assert re.search(r'`gzip`|\bgzip\b', content)
    assert re.search(r'`rsync`|\brsync\b', content)
    assert re.search(r'`cron`|\bcron\b|\bcrontab\b', content)
    assert "systemd.timer" in content or "systemd" in content
    assert "3-2-1" in content

def test_manual_cu04_wa04_has_required_recovery_concepts():
    content = read("manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md")
    assert re.search(r'`sha256sum`|\bsha256sum\b', content)
    assert re.search(r'`tar`|\btar\b', content)
    assert "bare-metal" in content.lower() or "baremetal" in content.lower()

def test_manual_cu06_wa04_has_required_mount_concepts():
    content = read("manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md")
    assert re.search(r'`mount`|\bmount\b', content)
    assert re.search(r'`umount`|\bumount\b', content)
    assert re.search(r'`findmnt`|\bfindmnt\b', content)
    assert "/etc/fstab" in content
    assert "nodev" in content and "nosuid" in content and "noexec" in content

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

def test_skill_cu04_type_skill_and_content():
    content_wa02 = read(".agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md")
    assert "type: skill" in content_wa02
    assert re.search(r'`tar`|\btar\b', content_wa02)
    assert re.search(r'`rsync`|\brsync\b', content_wa02)

    content_wa04 = read(".agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md")
    assert "type: skill" in content_wa04
    assert re.search(r'`sha256sum`|\bsha256sum\b', content_wa04)

def test_skill_cu06_type_skill_and_content():
    content_wa04 = read(".agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md")
    assert "type: skill" in content_wa04
    assert re.search(r'`mount`|\bmount\b', content_wa04)
    assert "/etc/fstab" in content_wa04

    content_wa07 = read(".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md")
    assert "type: skill" in content_wa07
    assert re.search(r'`grep`|\bgrep\b', content_wa07)
    assert "RCA" in content_wa07

def test_openwiki_topics_links_and_structure_cu04_cu06():
    content4 = read("openwiki/topic-04-automation-and-backup.md")
    assert "cu04-wa02-operasi-sandaran-tempatan.md" in content4
    assert "cu04-wa02-perform-local-backup-operations" in content4

    content6 = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md" in content6
    assert "cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md" in content6

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


# ---------------------------------------------------------------------------
# Deeper Markdown manual content checks: frontmatter integrity & exact command
# snippets introduced by this PR.
# ---------------------------------------------------------------------------

MANUAL_MD_PATHS = {
    "cu04-wa02": "manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md",
    "cu04-wa04": "manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md",
    "cu06-wa04": "manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md",
    "cu06-wa07": "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md",
}


@pytest.mark.parametrize("key,rel_path", MANUAL_MD_PATHS.items())
def test_manual_md_frontmatter_is_well_formed(key, rel_path):
    content = read(rel_path)
    assert frontmatter_field(content, "okf_version") == "0.1"
    assert frontmatter_field(content, "type") == "knowledge-node"
    timestamp = frontmatter_field(content, "timestamp")
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp), timestamp
    resource = frontmatter_field(content, "resource")
    assert resource == f"file:///{rel_path}"
    title = frontmatter_field(content, "title")
    # The rendered H1 must reproduce the frontmatter title.
    assert f"# {title}" in content


def test_manual_cu04_wa02_exact_command_snippets():
    content = read(MANUAL_MD_PATHS["cu04-wa02"])
    assert "sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/logs_backup_$(date +%Y%m%d).tar.zst /var/log" in content
    assert "tar -tvf /mnt/backup/logs_backup_*.tar.zst" in content
    assert "sudo tar -I zstd -xvf /mnt/backup/logs_backup_*.tar.zst -C /tmp/restored_logs/" in content
    assert "tar -czvf /mnt/backup/etc_backup.tar.gz /etc" in content
    assert "tar -cJvf /mnt/backup/etc_backup.tar.xz /etc" in content
    assert "sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/" in content
    assert "tar -I zstd -cvf - /etc | gpg --symmetric --cipher-algo AES256 -o /mnt/backup/etc_encrypted.tar.zst.gpg" in content
    assert "0 2 * * * /usr/local/bin/system_backup.sh >> /var/log/backup.log 2>&1" in content
    assert "OnCalendar=*-*-* 02:00:00" in content
    assert "sudo systemctl enable --now local-backup.timer" in content


def test_manual_cu04_wa04_exact_command_snippets():
    content = read(MANUAL_MD_PATHS["cu04-wa04"])
    assert "sha256sum /mnt/backup/etc_backup_20260817.tar.zst > /mnt/backup/etc_backup_20260817.tar.zst.sha256" in content
    assert "sha256sum -c etc_backup_20260817.tar.zst.sha256" in content
    assert 'tar -tvf /mnt/backup/etc_backup_20260817.tar.zst | grep "netplan"' in content
    assert "sudo tar -I zstd --same-owner -p -xvf /mnt/backup/etc_backup_20260817.tar.zst -C /" in content
    assert "gpg --decrypt /mnt/backup/etc_encrypted.tar.zst.gpg | sudo tar -I zstd -xvf - -C /tmp/recovery_staging/" in content
    assert "sudo cryptsetup luksOpen /dev/nvme0n1p3 cryptroot" in content
    assert "grub-install /dev/nvme0n1" in content


def test_manual_cu06_wa04_exact_command_snippets():
    content = read(MANUAL_MD_PATHS["cu06-wa04"])
    assert "lsblk -f" in content
    assert "sudo blkid /dev/sdb1" in content
    assert "sudo mount -t ext4 /dev/sdb1 /mnt/usb_flash" in content
    assert "sudo umount /mnt/usb_flash" in content
    assert "eject /dev/sr0" in content
    assert "UUID=550e8400-e29b-41d4-a716-446655440000 /mnt/sec_storage   ext4    defaults,nodev,nosuid,noexec  0       2" in content
    assert "sudo mount -a" in content


def test_manual_cu06_wa07_exact_command_snippets():
    content = read(MANUAL_MD_PATHS["cu06-wa07"])
    assert 'grep -in "failed" /var/log/auth.log' in content
    assert 'grep "Failed password" /var/log/auth.log | cut -d\' \' -f11 | sort | uniq -c | sort -nr' in content
    assert "sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config" in content
    assert "awk '{print $1, $5}' /var/log/syslog | head -n 10" in content
    assert "sudo systemctl status nginx 2>&1 | tee /tmp/nginx_error_audit.log" in content
    # IO redirection reference table operators
    for operator in [">", ">>", "<", "2>&1", "tee"]:
        assert operator in content


def test_manual_md_competency_checklists_are_non_generic():
    """Regression: the old placeholder checklist items must have been replaced
    with content-specific competency items."""
    generic_items = [
        "Memahami teori dan konsep asas yang terlibat.",
        "Berjaya melaksanakan prosedur kerja secara amali tanpa ralat.",
        "Menyediakan rekod verifikasi atau dokumentasi penyerahan tugas.",
    ]
    for rel_path in MANUAL_MD_PATHS.values():
        content = read(rel_path)
        for generic_item in generic_items:
            assert generic_item not in content, f"{rel_path} still contains generic placeholder checklist item"
        # Each file must have at least 3 concrete checklist entries.
        checklist_items = re.findall(r"^- \[ \] .+$", content, re.MULTILINE)
        assert len(checklist_items) >= 3, rel_path


def test_manual_md_ai_prompts_section_has_three_prompts():
    for rel_path in MANUAL_MD_PATHS.values():
        content = read(rel_path)
        prompts_section = content.split("Eksplorasi Lanjut bersama AI")[1]
        prompts_section = prompts_section.split("---", 1)[0]
        numbered_prompts = re.findall(r"^\d+\. \*\".+\"\*$", prompts_section, re.MULTILINE)
        assert len(numbered_prompts) == 3, rel_path


def test_manual_md_footer_signature_dated_2026_08_17():
    for rel_path in MANUAL_MD_PATHS.values():
        content = read(rel_path)
        assert "Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17" in content
        assert "Sovereign Manual" in content


# ---------------------------------------------------------------------------
# SKILL.md checks
# ---------------------------------------------------------------------------

SKILL_MD_PATHS = {
    "cu04-wa02": ".agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md",
    "cu04-wa04": ".agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md",
    "cu06-wa04": ".agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md",
    "cu06-wa07": ".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md",
}

SKILL_NAMES = {
    "cu04-wa02": "cu04-wa02-perform-local-backup-operations",
    "cu04-wa04": "cu04-wa04-restore-endpoint-data",
    "cu06-wa04": "cu06-wa04-configure-and-troubleshoot-peripheral-connections",
    "cu06-wa07": "cu06-wa07-resolve-system-anomalies-and-document-rca",
}


@pytest.mark.parametrize("key,rel_path", SKILL_MD_PATHS.items())
def test_skill_md_no_leading_byte_order_mark(key, rel_path):
    """Regression: previous revisions started with a stray UTF-8 BOM (\ufeff)
    before the frontmatter delimiter; this must not regress."""
    raw_bytes = (REPO_ROOT / rel_path).read_bytes()
    assert not raw_bytes.startswith(b"\xef\xbb\xbf"), f"{rel_path} still has a leading BOM"
    assert raw_bytes.startswith(b"---\n"), f"{rel_path} must start directly with frontmatter delimiter"


@pytest.mark.parametrize("key,rel_path", SKILL_MD_PATHS.items())
def test_skill_md_frontmatter_fields(key, rel_path):
    content = read(rel_path)
    assert frontmatter_field(content, "okf_version") == "0.1"
    assert frontmatter_field(content, "type") == "skill"
    assert frontmatter_field(content, "name") == SKILL_NAMES[key]
    # description should be a substantive sentence, not the old generic placeholder.
    description = frontmatter_field(content, "description")
    assert description.startswith("Executes NOSS Work Activity")
    assert len(description) > 60
    timestamp = frontmatter_field(content, "timestamp")
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp), timestamp
    resource = frontmatter_field(content, "resource")
    assert resource == f"file:///{rel_path}"


def test_skill_md_no_longer_procedural_skill_type():
    """Regression: old frontmatter used `type: procedural_skill`; verify it was
    migrated to `type: skill` and the placeholder body text is gone."""
    for rel_path in SKILL_MD_PATHS.values():
        content = read(rel_path)
        assert "type: procedural_skill" not in content
        assert "Pending implementation based on JTPS 2 document." not in content


def test_skill_cu04_wa02_execution_procedure_detail():
    content = read(SKILL_MD_PATHS["cu04-wa02"])
    assert "K622-001-3:2026-C04 WA02" in content
    assert "sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/system_config_$(date +%Y%m%d).tar.zst /etc /var/log" in content
    assert "sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/" in content
    assert "OnCalendar=*-*-* 02:00:00" in content
    assert "sudo systemctl daemon-reload" in content
    assert "3-2-1 backup strategy" in content
    assert "gpg --symmetric" in content


def test_skill_cu04_wa04_execution_procedure_detail():
    content = read(SKILL_MD_PATHS["cu04-wa04"])
    assert "K622-001-3:2026-C04 WA04" in content
    assert "sha256sum -c system_config_20260817.tar.zst.sha256" in content
    assert "etc/netplan/01-netcfg.yaml" in content
    assert "gpg --decrypt /mnt/backup/backup_encrypted.tar.zst.gpg" in content
    assert "Reinstall GRUB bootloader via chroot." in content


def test_skill_cu06_wa04_execution_procedure_detail():
    content = read(SKILL_MD_PATHS["cu06-wa04"])
    assert "K622-001-3:2026-C06 WA04" in content
    assert "lsblk -f" in content
    assert "sudo mount -t ext4 /dev/sdb1 /mnt/external_usb" in content
    assert "sudo umount /mnt/external_usb" in content
    assert "eject /dev/sr0" in content
    assert "defaults,nodev,nosuid,noexec 0 2" in content


def test_skill_cu06_wa07_execution_procedure_detail():
    content = read(SKILL_MD_PATHS["cu06-wa07"])
    assert "K622-001-3:2026-C06 WA07" in content
    assert 'grep -in "failed" /var/log/auth.log' in content
    assert "sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config" in content
    assert "awk '{print $1, $5}' /var/log/syslog | head -n 10" in content
    assert "sudo systemctl status nginx 2>&1 | tee /tmp/nginx_error_audit.log" in content
    assert "Root Cause Analysis (RCA) Report Structure" in content


def test_skill_md_footer_signature_dated_2026_08_17():
    for rel_path in SKILL_MD_PATHS.values():
        content = read(rel_path)
        assert "Sovereign AI Skill" in content
        assert "Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17" in content


# ---------------------------------------------------------------------------
# Skills registry (.agents/skills/index.md) checks
# ---------------------------------------------------------------------------

def test_skills_index_timestamp_updated():
    content = read(".agents/skills/index.md")
    timestamp = frontmatter_field(content, "timestamp")
    assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", timestamp)


@pytest.mark.parametrize("skill_name,expected_snippet", [
    ("cu04-wa02-perform-local-backup-operations",
     "Executes NOSS Work Activity CU04-WA02 - Perform Local Backup Operations including tar archive with zstd compression"),
    ("cu04-wa04-restore-endpoint-data",
     "Executes NOSS Work Activity CU04-WA04 - Restore Endpoint Data and Filesystem Recovery including sha256sum checksum validation"),
    ("cu06-wa04-configure-and-troubleshoot-peripheral-connections",
     "Executes NOSS Work Activity CU06-WA04 - Configure and Troubleshoot Peripheral Connections including storage mounting"),
    ("cu06-wa07-resolve-system-anomalies-and-document-rca",
     "Executes NOSS Work Activity CU06-WA07 - Resolve System Anomalies and Document RCA using text filters"),
])
def test_skills_index_entries_no_longer_placeholder(skill_name, expected_snippet):
    content = read(".agents/skills/index.md")
    # Locate this skill's table row.
    row_match = re.search(rf"^\|\s*\*\*`{re.escape(skill_name)}`\*\*.*$", content, re.MULTILINE)
    assert row_match, f"Row for {skill_name} not found in registry"
    row = row_match.group(0)
    assert "No description provided." not in row
    assert "N/A" not in row
    assert expected_snippet in row


def test_skills_index_unrelated_rows_remain_untouched():
    """Sanity check that unrelated, not-yet-documented skills in this PR's diff
    scope are still marked as placeholders (this PR only touched 4 rows)."""
    content = read(".agents/skills/index.md")
    untouched_row = re.search(
        r"^\|\s*\*\*`cu04-wa01-prepare-backup-recovery-tools`\*\*.*$", content, re.MULTILINE
    )
    assert untouched_row
    assert "No description provided." in untouched_row.group(0)


# ---------------------------------------------------------------------------
# OpenWiki topic pages: deeper structural checks
# ---------------------------------------------------------------------------

def test_openwiki_topic04_syllabus_and_reading_list():
    content = read("openwiki/topic-04-automation-and-backup.md")
    assert "NOSS CU04 (Backup & Recovery Tools)" in content
    assert "zstd" in content and "rsync" in content and "cron" in content
    assert "3-2-1" in content
    assert "[GNU Tar Official Manual](https://www.gnu.org/software/tar/manual/)" in content
    assert re.search(r"^\d+\. \*\".+\"\*$", content, re.MULTILINE)


def test_openwiki_topic06_syllabus_and_reading_list():
    content = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "NOSS CU06 (End-User Support & System Maintenance)" in content
    assert "nodev,nosuid,noexec" in content
    assert "grep" in content and "sed" in content and "awk" in content
    assert "Root Cause Analysis" in content
    assert "[Systemd Journalctl User Guide](https://www.freedesktop.org/software/systemd/man/journalctl.html)" in content


# ---------------------------------------------------------------------------
# Generated HTML checks: titles/meta descriptions must reflect the Markdown
# content produced by this PR (and must not regress to the previous copy).
# ---------------------------------------------------------------------------

HTML_MANUAL_PATHS = {
    "cu04-wa02": "html/manual/cu04/cu04-wa02-operasi-sandaran-tempatan.html",
    "cu04-wa04": "html/manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.html",
    "cu06-wa04": "html/manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.html",
    "cu06-wa07": "html/manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html",
}

HTML_EXPECTED_TITLES = {
    "cu04-wa02": "Pelaksanaan Operasi Sandaran Tempatan & Pemampatan Data",
    "cu04-wa04": "Pemulihan Data & Verifikasi Integriti Sistem Fail",
    "cu06-wa04": "Konfigurasi Pelekapan Storan, Peranti Luaran & Pengoperasian Media",
    "cu06-wa07": "Pemprosesan Teks Aluran, Saluran Paip, Editor CLI & Analisis Punca Utama (RCA)",
}

HTML_EXPECTED_ANCHOR_IDS = {
    "cu04-wa02": "pelaksanaan-operasi-sandaran-tempatan-pemampatan-data",
    "cu04-wa04": "pemulihan-data-verifikasi-integriti-sistem-fail",
    "cu06-wa04": "konfigurasi-pelekapan-storan-peranti-luaran-pengoperasian-media",
    "cu06-wa07": "pemprosesan-teks-aluran-saluran-paip-editor-cli-analisis-punca-utama-rca",
}


@pytest.mark.parametrize("key,rel_path", HTML_MANUAL_PATHS.items())
def test_html_manual_title_matches_markdown_title(key, rel_path):
    html_content = read(rel_path)
    title_match = re.search(r"<title>(.*?)</title>", html_content, re.DOTALL)
    assert title_match, rel_path
    title_text = title_match.group(1).strip()
    assert title_text == f"{HTML_EXPECTED_TITLES[key]} - NOSS Linux Malaysia (DSOM)"


@pytest.mark.parametrize("key,rel_path", HTML_MANUAL_PATHS.items())
def test_html_manual_meta_description_matches_markdown_description(key, rel_path):
    html_content = read(rel_path)
    md_content = read(MANUAL_MD_PATHS[key])
    md_description = frontmatter_field(md_content, "description")
    desc_match = re.search(r'<meta name="description" content="([^"]*)">', html_content)
    assert desc_match, rel_path
    assert desc_match.group(1) == md_description


@pytest.mark.parametrize("key,rel_path", HTML_MANUAL_PATHS.items())
def test_html_manual_h1_anchor_id_updated(key, rel_path):
    html_content = read(rel_path)
    expected_id = HTML_EXPECTED_ANCHOR_IDS[key]
    assert f'<h1 id="{expected_id}">' in html_content
    assert f'href="#{expected_id}" class="md-skip"' in html_content


@pytest.mark.parametrize("key,rel_path", HTML_MANUAL_PATHS.items())
def test_html_manual_body_contains_new_command_snippets(key, rel_path):
    html_content = read(rel_path)
    text = html_to_text(html_content)
    if key == "cu04-wa02":
        assert "sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/logs_backup_$(date +%Y%m%d).tar.zst /var/log" in text
        assert "sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/" in text
    elif key == "cu04-wa04":
        assert "sha256sum -c etc_backup_20260817.tar.zst.sha256" in text
        assert "grub-install /dev/nvme0n1" in text
    elif key == "cu06-wa04":
        assert "sudo mount -t ext4 /dev/sdb1 /mnt/usb_flash" in text
        assert "nodev,nosuid,noexec" in text
    elif key == "cu06-wa07":
        assert 'grep -in "failed" /var/log/auth.log' in text
        assert "sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config" in text


def test_html_openwiki_topic_pages_exist_and_reference_updated_manuals():
    content4 = read("html/openwiki/topic-04-automation-and-backup.html")
    text4 = html_to_text(content4)
    assert "NOSS CU04" in text4
    assert "zstd" in text4

    content6 = read("html/openwiki/topic-06-troubleshooting-and-logs.html")
    text6 = html_to_text(content6)
    assert "NOSS CU06" in text6
    assert "nodev,nosuid,noexec" in text6 or "nodev" in text6


# ---------------------------------------------------------------------------
# Search index (html/search/search_index.json) checks
# ---------------------------------------------------------------------------

def test_search_index_json_has_expected_top_level_structure(search_index):
    assert "config" in search_index
    assert "docs" in search_index
    assert isinstance(search_index["docs"], list)
    assert len(search_index["docs"]) > 0
    for doc in search_index["docs"][:5]:
        assert "location" in doc
        assert "title" in doc


@pytest.mark.parametrize("key,rel_path", HTML_MANUAL_PATHS.items())
def test_search_index_manual_titles_reflect_pr_content(key, rel_path, search_index):
    html_location = rel_path.split("html/", 1)[1]
    doc = find_doc(search_index, html_location)
    expected_title_html_escaped = html_module.escape(HTML_EXPECTED_TITLES[key], quote=False)
    assert doc["title"] == expected_title_html_escaped


def test_search_index_openwiki_topics_present(search_index):
    doc4 = find_doc(search_index, "openwiki/topic-04-automation-and-backup.html")
    assert "CU04" in doc4["title"]

    doc6 = find_doc(search_index, "openwiki/topic-06-troubleshooting-and-logs.html")
    assert "CU06" in doc6["title"]


def test_search_index_manual_cu04_wa02_tags_match_frontmatter(search_index):
    doc = find_doc(search_index, "manual/cu04/cu04-wa02-operasi-sandaran-tempatan.html")
    for expected_tag in ["cu04", "zstd", "rsync", "systemd"]:
        assert expected_tag in doc.get("tags", []), doc.get("tags")


def test_search_index_manual_cu06_wa07_tags_match_frontmatter(search_index):
    doc = find_doc(search_index, "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html")
    for expected_tag in ["grep", "sed", "awk", "vim", "nano", "rca"]:
        assert expected_tag in doc.get("tags", []), doc.get("tags")
