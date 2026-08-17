"""Tests for CU03 & CU06 Core Server Configurations, Process Management, Monitoring and Agent Skills content.

Covers:
  - manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md
  - manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md
  - .agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md
  - .agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md
  - .agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md
  - .agents/skills/index.md
  - openwiki/topic-03-linux-server-administration.md
  - openwiki/topic-06-troubleshooting-and-logs.md
  - html/manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html
  - html/manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.html
  - html/openwiki/topic-03-linux-server-administration.html
  - html/openwiki/topic-06-troubleshooting-and-logs.html
  - html/search/search_index.json
"""

import json
import re
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


def get_frontmatter(content):
    """Extract and return the raw YAML frontmatter block from Markdown content.

    Parameters:
        content: Full text of a Markdown file starting with '---' delimited
            frontmatter.

    Returns:
        The frontmatter text located between the first pair of '---' markers.
    """
    parts = content.split("---", 2)
    assert len(parts) >= 3, "Frontmatter must be delimited by '---' on both ends."
    return parts[1]

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


# ---------------------------------------------------------------------------
# manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md — detailed content
# ---------------------------------------------------------------------------

MANUAL_CU03_PATH = "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md"


def test_manual_cu03_wa04_frontmatter_fields():
    content = read(MANUAL_CU03_PATH)
    frontmatter = get_frontmatter(content)
    assert "okf_version: 0.1" in frontmatter
    assert 'title: "Konfigurasi Teras Pelayan Linux & Pengurusan Perkhidmatan Systemd"' in frontmatter
    assert "type: knowledge-node" in frontmatter
    assert '"cu03"' in frontmatter
    assert '"wa04"' in frontmatter
    assert "resource: \"file:///manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md\"" in frontmatter


def test_manual_cu03_wa04_systemctl_service_management_section():
    content = read(MANUAL_CU03_PATH)
    assert "sudo systemctl status sshd" in content
    assert "sudo systemctl enable --now sshd" in content
    assert "sudo systemctl mask legacy-service" in content
    assert "sudo systemctl unmask legacy-service" in content
    assert "systemctl get-default" in content
    assert "sudo systemctl set-default multi-user.target" in content
    assert "sudo systemctl isolate multi-user.target" in content


def test_manual_cu03_wa04_custom_unit_file_hardening_directives():
    content = read(MANUAL_CU03_PATH)
    assert "/etc/systemd/system/myapp.service" in content
    for directive in (
        "ProtectSystem=strict",
        "ProtectHome=true",
        "PrivateTmp=true",
        "NoNewPrivileges=true",
        "CapabilityBoundingSet=CAP_NET_BIND_SERVICE",
        "ReadWritePaths=/var/log/myapp /var/lib/myapp",
    ):
        assert directive in content
    assert "sudo useradd -r -s /sbin/nologin nossapp" in content
    assert "sudo systemctl daemon-reload" in content


def test_manual_cu03_wa04_journalctl_audit_commands():
    content = read(MANUAL_CU03_PATH)
    assert "sudo journalctl -u sshd -f" in content
    assert "--since" in content and "--until" in content
    assert "-p err..emerg" in content
    assert "sudo journalctl -b" in content
    assert "sudo journalctl --disk-usage" in content
    assert "sudo journalctl --vacuum-size=500M" in content


def test_manual_cu03_wa04_time_sync_and_chrony_config():
    content = read(MANUAL_CU03_PATH)
    assert "sudo timedatectl set-timezone Asia/Kuala_Lumpur" in content
    assert "sudo timedatectl set-ntp true" in content
    assert "server my.pool.ntp.org iburst" in content
    assert "driftfile /var/lib/chrony/drift" in content
    assert "makestep 1.0 3" in content
    assert "chronyc sources -v" in content
    assert "chronyc tracking" in content


def test_manual_cu03_wa04_man_pages_navigation_section():
    content = read(MANUAL_CU03_PATH)
    assert "man systemctl" in content
    assert "man 5 fstab" in content
    assert "man 8 useradd" in content
    assert 'apropos "systemctl"' in content
    assert "whatis chronyd" in content
    assert "whereis chronyc" in content
    assert "sudo updatedb" in content
    assert "plocate chrony.conf" in content


def test_manual_cu03_wa04_security_hardening_and_checklist():
    content = read(MANUAL_CU03_PATH)
    assert "Prinsip Perkhidmatan Minimum (Service Minimisation)" in content
    assert "Pengasingan Hak Akses Unit Servis" in content
    assert "Audit Log Berpusat" in content
    checklist_items = re.findall(r"^- \[ \] .+", content, re.MULTILINE)
    assert len(checklist_items) >= 6


def test_manual_cu03_wa04_no_longer_contains_placeholder_procedure():
    """Regression: the old generic placeholder procedure text must be replaced."""
    content = read(MANUAL_CU03_PATH)
    assert "Pending implementation based on JTPS 2 document." not in content
    assert "Melakukan semakan status dan kesediaan perkakasan" not in content


def test_manual_cu03_wa04_footer_attribution():
    content = read(MANUAL_CU03_PATH)
    assert "Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17" in content
    assert "CC BY-SA 4.0" in content


# ---------------------------------------------------------------------------
# manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md — detailed
# ---------------------------------------------------------------------------

MANUAL_CU06_PATH = "manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md"


def test_manual_cu06_wa05_frontmatter_fields():
    content = read(MANUAL_CU06_PATH)
    frontmatter = get_frontmatter(content)
    assert "okf_version: 0.1" in frontmatter
    assert 'title: "Pengoptimuman Prestasi Sistem, Pemantauan Proses & Kawalan Sumber"' in frontmatter
    assert "type: knowledge-node" in frontmatter
    assert '"cu06"' in frontmatter
    assert '"wa05"' in frontmatter


def test_manual_cu06_wa05_process_monitoring_commands():
    content = read(MANUAL_CU06_PATH)
    assert "ps aux --sort=-%mem | head -n 10" in content
    assert "ps aux --sort=-%cpu | head -n 10" in content
    assert "ps axjf" in content
    assert "pstree -p" in content


def test_manual_cu06_wa05_resource_diagnostics_commands():
    content = read(MANUAL_CU06_PATH)
    assert "uptime" in content
    assert "free -h" in content
    assert "vmstat 1 5" in content
    assert "iostat -xz 1 5" in content
    assert "sudo pidstat -d 1 5" in content


def test_manual_cu06_wa05_posix_signal_table():
    content = read(MANUAL_CU06_PATH)
    assert "SIGHUP" in content
    assert "SIGINT" in content
    assert "SIGKILL" in content
    assert "SIGTERM" in content
    assert "kill -15 4821" in content
    assert "kill -9 4821" in content
    assert "sudo kill -1 1024" in content
    assert 'sudo killall -15 nginx' in content
    assert 'sudo pkill -f "python3 script.py"' in content


def test_manual_cu06_wa05_nice_renice_ionice_priority_tuning():
    content = read(MANUAL_CU06_PATH)
    assert "-20 (Keutamaan Tertinggi)" in content
    assert "19 (Keutamaan Terendah)" in content
    assert "sudo nice -n -10 /usr/local/bin/heavy-data-process.sh" in content
    assert "nice -n 15 /usr/local/bin/backup.sh &" in content
    assert "sudo renice -n 5 -p 4821" in content
    assert "sudo ionice -c 3 /usr/local/bin/backup-job.sh" in content


def test_manual_cu06_wa05_cgroups_v2_resource_control():
    content = read(MANUAL_CU06_PATH)
    assert "sudo systemd-run --scope -p MemoryMax=500M -p CPUQuota=50%" in content
    assert "/etc/systemd/system/myapp.service.d/override.conf" in content
    assert "MemoryMax=1G" in content
    assert "MemoryHigh=800M" in content
    assert "CPUQuota=200%" in content
    assert "IOWeight=50" in content


def test_manual_cu06_wa05_security_hardening_and_checklist():
    content = read(MANUAL_CU06_PATH)
    assert "Perlindungan Terhadap DoS & Fork Bomb" in content
    assert "/etc/security/limits.conf" in content
    assert "Pengawasan Proses Luar Biasa" in content
    checklist_items = re.findall(r"^- \[ \] .+", content, re.MULTILINE)
    assert len(checklist_items) >= 5


def test_manual_cu06_wa05_no_longer_contains_placeholder_procedure():
    """Regression: the old generic placeholder procedure text must be replaced."""
    content = read(MANUAL_CU06_PATH)
    assert "Pending implementation based on JTPS 2 document." not in content
    assert "Melakukan semakan status dan kesediaan perkakasan" not in content


# ---------------------------------------------------------------------------
# .agents/skills/*/SKILL.md — frontmatter & structural detail
# ---------------------------------------------------------------------------

SKILL_CU03_PATH = ".agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md"
SKILL_CU06_OPTIMIZE_PATH = ".agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md"
SKILL_CU06_PERFORM_PATH = ".agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md"


def test_skill_cu03_wa04_frontmatter_fields():
    content = read(SKILL_CU03_PATH)
    frontmatter = get_frontmatter(content)
    assert "okf_version: 0.1" in frontmatter
    assert "name: cu03-wa04-perform-core-server-configurations" in frontmatter
    assert 'title: "CU03 WA04: Perform Core Server Configurations"' in frontmatter
    assert "type: skill" in frontmatter
    assert "K622-XXX-3:2026-C03 WA04" in frontmatter
    assert (
        "resource: \"file:///.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md\""
        in frontmatter
    )
    # No leading BOM/mojibake artefact from earlier revisions.
    assert not content.startswith("\ufeff")
    assert not content.lstrip("\ufeff").startswith("\ufeff")


def test_skill_cu03_wa04_covers_all_five_execution_sections():
    content = read(SKILL_CU03_PATH)
    assert "### 1. Systemd Service Unit Management (`systemctl`)" in content
    assert "### 2. Custom Unit File Creation" in content
    assert "### 3. Journal Audit Logging (`journalctl`)" in content
    assert "### 4. Time Synchronization & Timezone (`timedatectl` & `chronyd`)" in content
    assert "### 5. System Documentation Navigation" in content
    assert "sudo systemctl mask telnet.service" in content
    assert "sudo journalctl --vacuum-size=500M" in content
    assert "sudo timedatectl set-timezone Asia/Kuala_Lumpur" in content


def test_skill_cu06_wa05_optimize_frontmatter_fields():
    content = read(SKILL_CU06_OPTIMIZE_PATH)
    frontmatter = get_frontmatter(content)
    assert "name: cu06-wa05-optimize-system-performance-and-storage" in frontmatter
    assert 'title: "CU06 WA05: Optimize System Performance and Storage"' in frontmatter
    assert "type: skill" in frontmatter
    assert (
        "resource: \"file:///.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md\""
        in frontmatter
    )


def test_skill_cu06_wa05_perform_frontmatter_fields():
    content = read(SKILL_CU06_PERFORM_PATH)
    frontmatter = get_frontmatter(content)
    assert "name: cu06-wa05-perform-system-optimisation-and-disk-management" in frontmatter
    assert 'title: "CU06 WA05: Perform System Optimisation and Disk Management"' in frontmatter
    assert "type: skill" in frontmatter
    assert (
        "resource: \"file:///.agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md\""
        in frontmatter
    )


def test_skill_cu06_wa05_variants_share_identical_command_body():
    """Both cu06-wa05 skill files should teach the same command set even
    though they carry distinct names/titles (renamed/duplicated skill)."""
    optimize_content = read(SKILL_CU06_OPTIMIZE_PATH)
    perform_content = read(SKILL_CU06_PERFORM_PATH)

    # Body (everything after frontmatter closing '---') should be identical
    # except for the title/heading lines which legitimately differ.
    optimize_body = optimize_content.split("---", 2)[2]
    perform_body = perform_content.split("---", 2)[2]

    shared_snippets = [
        "sudo systemd-run --scope -p MemoryMax=500M -p CPUQuota=50% /usr/local/bin/heavy-app",
        "sudo renice -n 5 -p <PID>",
        "sudo ionice -c 3 /usr/local/bin/backup-job.sh",
        "sudo pidstat -d 1 5",
    ]
    for snippet in shared_snippets:
        assert snippet in optimize_body
        assert snippet in perform_body


def test_skill_cu03_and_cu06_have_no_placeholder_procedure_left():
    for path in (SKILL_CU03_PATH, SKILL_CU06_OPTIMIZE_PATH, SKILL_CU06_PERFORM_PATH):
        content = read(path)
        assert "Pending implementation based on JTPS 2 document." not in content


# ---------------------------------------------------------------------------
# .agents/skills/index.md — registry table
# ---------------------------------------------------------------------------

INDEX_PATH = ".agents/skills/index.md"


def test_index_total_modules_updated():
    content = read(INDEX_PATH)
    assert "**Total Modules Indexed:** `123`" in content


def test_index_registers_cu03_wa04_with_description():
    content = read(INDEX_PATH)
    assert (
        "| **`cu03-wa04-perform-core-server-configurations`** <br> "
        "*CU03 WA04: Perform Core Server Configurations* | "
        "Executes NOSS Work Activity K622-XXX-3:2026-C03 WA04: Perform Core Server Configurations "
        "including systemd service management, custom service units, journalctl audit logging, "
        "timedatectl/chrony time sync, and system man pages."
    ) in content
    assert "No description provided" not in content.split(
        "cu03-wa04-perform-core-server-configurations"
    )[1].split("\n")[0]


def test_index_registers_both_cu06_wa05_skill_rows():
    content = read(INDEX_PATH)
    assert "cu06-wa05-optimize-system-performance-and-storage" in content
    assert "CU06 WA05: Optimize System Performance and Storage" in content
    assert "cu06-wa05-perform-system-optimisation-and-disk-management" in content
    assert "CU06 WA05: Perform System Optimisation and Disk Management" in content
    # Confirm the two skills are on separate table rows.
    optimize_line = next(
        line for line in content.splitlines()
        if "cu06-wa05-optimize-system-performance-and-storage" in line
    )
    perform_line = next(
        line for line in content.splitlines()
        if "cu06-wa05-perform-system-optimisation-and-disk-management" in line and line.strip().startswith("|")
    )
    assert optimize_line != perform_line


def test_index_timestamp_bumped():
    content = read(INDEX_PATH)
    assert 'timestamp: "2026-08-17T05:31:00Z"' in content


# ---------------------------------------------------------------------------
# openwiki/topic-03 & topic-06 — expanded syllabus content
# ---------------------------------------------------------------------------

OPENWIKI_CU03_PATH = "openwiki/topic-03-linux-server-administration.md"
OPENWIKI_CU06_PATH = "openwiki/topic-06-troubleshooting-and-logs.md"


def test_openwiki_topic03_title_and_frontmatter():
    content = read(OPENWIKI_CU03_PATH)
    frontmatter = get_frontmatter(content)
    assert 'title: "Topik 3: Pentadbiran Pelayan Linux (CU03)"' in frontmatter
    assert "# Topik 3: Pentadbiran Pelayan Linux (CU03)" in content


def test_openwiki_topic03_syllabus_mentions_systemd_workflow():
    content = read(OPENWIKI_CU03_PATH)
    assert "Konfigurasi Teras Pelayan & Systemd" in content
    assert "`systemctl`" in content
    assert "`journalctl`" in content
    assert "`timedatectl`" in content
    assert "`chronyd`" in content
    assert "`man`" in content


def test_openwiki_topic06_title_and_frontmatter():
    content = read(OPENWIKI_CU06_PATH)
    frontmatter = get_frontmatter(content)
    assert 'title: "Topik 6: Penyelesaian Masalah, Pemantauan Prestasi & Analisis Log (CU06)"' in frontmatter
    assert "# Topik 6: Penyelesaian Masalah, Pemantauan Prestasi & Analisis Log (CU06)" in content


def test_openwiki_topic06_syllabus_mentions_process_and_signal_concepts():
    content = read(OPENWIKI_CU06_PATH)
    assert "Kitaran Hayat Proses & Penalaan Keutamaan" in content
    assert "SIGTERM" in content
    assert "SIGKILL" in content
    assert "SIGHUP" in content
    assert "`nice`, `renice`" in content
    assert "`cgroups v2`" in content


# ---------------------------------------------------------------------------
# Generated HTML pages — title / meta description / heading consistency
# ---------------------------------------------------------------------------

HTML_MANUAL_CU03_PATH = "html/manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html"
HTML_MANUAL_CU06_PATH = "html/manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.html"
HTML_OPENWIKI_CU03_PATH = "html/openwiki/topic-03-linux-server-administration.html"
HTML_OPENWIKI_CU06_PATH = "html/openwiki/topic-06-troubleshooting-and-logs.html"


def test_html_manual_cu03_title_and_meta_description():
    content = read(HTML_MANUAL_CU03_PATH)
    assert (
        "<title>Konfigurasi Teras Pelayan Linux & Pengurusan Perkhidmatan Systemd "
        "- NOSS Linux Malaysia (DSOM)</title>" in content
    )
    assert (
        'content="Panduan amali konfigurasi teras pelayan Linux, pengurusan unit '
        'perkhidmatan systemd, audit log journalctl, penyegerakan masa timedatectl/chrony, '
        'dan sistem dokumentasi man."' in content
    )
    assert 'id="konfigurasi-teras-pelayan-linux-pengurusan-perkhidmatan-systemd"' in content


def test_html_manual_cu03_skip_link_matches_new_heading_anchor():
    content = read(HTML_MANUAL_CU03_PATH)
    assert '<a href="#konfigurasi-teras-pelayan-linux-pengurusan-perkhidmatan-systemd" class="md-skip">' in content


def test_html_manual_cu06_title_and_meta_description():
    content = read(HTML_MANUAL_CU06_PATH)
    assert (
        "<title>Pengoptimuman Prestasi Sistem, Pemantauan Proses & Kawalan Sumber "
        "- NOSS Linux Malaysia (DSOM)</title>" in content
    )
    assert (
        'content="Panduan amali pemantauan proses sistem, analisis penggunaan CPU/memori/I-O, '
        'kawalan keutamaan nice/renice, penamatan isyarat proses SIGTERM/SIGKILL, '
        'dan pengurusan sumber cgroups v2."' in content
    )
    assert 'id="pengoptimuman-prestasi-sistem-pemantauan-proses-kawalan-sumber"' in content


def test_html_openwiki_topic03_title_updated_from_slug():
    content = read(HTML_OPENWIKI_CU03_PATH)
    assert "<title>Topik 3: Pentadbiran Pelayan Linux (CU03) - NOSS Linux Malaysia (DSOM)</title>" in content
    # Regression: the raw filename slug must no longer leak into the title.
    assert "<title>topic-03-linux-server-administration - NOSS Linux Malaysia (DSOM)</title>" not in content


def test_html_openwiki_topic06_meta_description_present():
    content = read(HTML_OPENWIKI_CU06_PATH)
    assert (
        'content="Silibus penyelesaian masalah sistem, pemantauan prestasi & proses, '
        'analisis log journalctl, dan sokongan pengguna dipetakan kepada NOSS CU06."' in content
    )
    assert "Topik 6: Penyelesaian Masalah, Pemantauan Prestasi &amp; Analisis Log (CU06)" in content


def test_html_manual_pages_reference_systemctl_and_journalctl_code_blocks():
    cu03_content = read(HTML_MANUAL_CU03_PATH)
    assert "systemctl" in cu03_content
    assert "journalctl" in cu03_content
    assert "chronyc" in cu03_content

    cu06_content = read(HTML_MANUAL_CU06_PATH)
    assert "vmstat" in cu06_content
    assert "SIGTERM" in cu06_content
    assert "cgroups" in cu06_content or "systemd-run" in cu06_content


# ---------------------------------------------------------------------------
# html/search/search_index.json — generated MkDocs search index
# ---------------------------------------------------------------------------

SEARCH_INDEX_PATH = "html/search/search_index.json"


@pytest.fixture(scope="module")
def search_index():
    """Load and parse the generated MkDocs search index once per test module."""
    path = REPO_ROOT / SEARCH_INDEX_PATH
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_search_index_is_valid_json_with_expected_shape(search_index):
    assert isinstance(search_index, dict)
    assert "config" in search_index
    assert "docs" in search_index
    assert isinstance(search_index["docs"], list)
    assert len(search_index["docs"]) > 0


def test_search_index_contains_manual_cu03_wa04_entry(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    assert HTML_MANUAL_CU03_PATH.replace("html/", "", 1) in locations

    top_level = next(
        doc for doc in search_index["docs"]
        if doc["location"] == HTML_MANUAL_CU03_PATH.replace("html/", "", 1)
    )
    assert "Konfigurasi Teras Pelayan Linux" in top_level["title"]
    assert "Systemd" in top_level["title"]


def test_search_index_contains_manual_cu06_wa05_entry(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    assert HTML_MANUAL_CU06_PATH.replace("html/", "", 1) in locations

    top_level = next(
        doc for doc in search_index["docs"]
        if doc["location"] == HTML_MANUAL_CU06_PATH.replace("html/", "", 1)
    )
    assert "Pengoptimuman Prestasi Sistem" in top_level["title"]
    assert "Kawalan Sumber" in top_level["title"]


def test_search_index_contains_openwiki_topic_entries(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    assert HTML_OPENWIKI_CU03_PATH.replace("html/", "", 1) in locations
    assert HTML_OPENWIKI_CU06_PATH.replace("html/", "", 1) in locations


def test_search_index_manual_cu03_has_new_systemd_subsections(search_index):
    """New subsection headings introduced by this PR must be searchable."""
    cu03_base = HTML_MANUAL_CU03_PATH.replace("html/", "", 1)
    subsection_anchors = {
        doc["location"] for doc in search_index["docs"]
        if doc["location"].startswith(cu03_base + "#")
    }
    expected_anchor = cu03_base + "#2-pengurusan-perkhidmatan-unit-servis-dengan-systemctl"
    assert expected_anchor in subsection_anchors


def test_search_index_manual_cu06_has_new_process_subsections(search_index):
    cu06_base = HTML_MANUAL_CU06_PATH.replace("html/", "", 1)
    subsection_anchors = {
        doc["location"] for doc in search_index["docs"]
        if doc["location"].startswith(cu06_base + "#")
    }
    expected_anchor = cu06_base + "#4-pengurusan-isyarat-posix-penamatan-proses"
    assert expected_anchor in subsection_anchors
