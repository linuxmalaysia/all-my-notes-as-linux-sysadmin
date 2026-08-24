"""Ujian pengesahan bagi Migrasi Bab 8: Pemasangan, Pengurusan Pakej RPM/Debian/Source & Kemas Kini Perisian.

Merangkumi:
  - manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
  - manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md
  - openwiki/topic-01-linux-desktop-and-basics.md
  - openwiki/topic-05-linux-security.md
  - .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md
  - .agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def test_manual_cu01_wa05_rpm_and_source_compilation_concepts():
    content = read("manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md")
    assert "rpm -Uvh" in content
    assert "rpm -qi" in content
    assert "rpm -V" in content
    assert "--rebuilddb" in content
    assert "--nodeps" in content
    assert "rpmbuild --rebuild" in content
    assert "./configure" in content
    assert "make -j" in content


def test_manual_cu05_wa04_automated_patching_and_integrity_concepts():
    content = read("manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md")
    assert "unattended-upgrades" in content
    assert "dnf-automatic" in content
    assert "rpm -Va" in content
    assert "dpkg --verify" in content


def test_openwiki_topics_package_management_mentions():
    content01 = read("openwiki/topic-01-linux-desktop-and-basics.md")
    assert "RPM" in content01
    assert "DEB" in content01
    assert "Tarball" in content01

    content05 = read("openwiki/topic-05-linux-security.md")
    assert "unattended-upgrades" in content05
    assert "dnf-automatic" in content05
    assert "rpm -V" in content05


def test_skill_cu01_wa05_rpm_enhancements():
    content = read(".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md")
    assert "rpm -Uvh" in content
    assert "rpmbuild --rebuild" in content
    assert "./configure" in content


def test_skill_cu05_wa04_patching_enhancements():
    content = read(".agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md")
    assert "unattended-upgrades" in content
    assert "dnf-automatic" in content
    assert "rpm -Va" in content


# ---------------------------------------------------------------------------
# Additional comprehensive coverage
# ---------------------------------------------------------------------------

import json

import pytest

TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def split_frontmatter(content):
    """Split a markdown/skill file's content into (frontmatter, body)."""
    assert content.startswith("---") or content.lstrip("\ufeff").startswith("---")
    content = content.lstrip("\ufeff")
    parts = content.split("---", 2)
    assert len(parts) >= 3, "File has malformed or missing YAML closure '---'."
    return parts[1].strip(), parts[2]


CU05_WA04_SKILL = ".agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md"
CU01_WA05_SKILL = ".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md"
CU01_WA05_MANUAL = "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"
CU05_WA04_MANUAL = "manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md"
OPENWIKI_TOPIC_01 = "openwiki/topic-01-linux-desktop-and-basics.md"
OPENWIKI_TOPIC_05 = "openwiki/topic-05-linux-security.md"
SKILLS_INDEX = ".agents/skills/index.md"


# ---------------------------------------------------------------------------
# .agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md
# (upgraded frontmatter + implemented Procedure, replacing the stub)
# ---------------------------------------------------------------------------

def test_skill_cu05_wa04_frontmatter_upgraded_fields():
    frontmatter, _ = split_frontmatter(read(CU05_WA04_SKILL))
    assert "name: cu05-wa04-conduct-application-security-patching" in frontmatter
    assert 'description: "Executes NOSS Work Activity: Conduct Application Security Patching' in frontmatter
    assert "okf_version: 0.1" in frontmatter
    assert "type: skill" in frontmatter
    assert 'title: "Conduct Application Security Patching"' in frontmatter
    assert 'timestamp: "2026-08-17T00:00:00Z"' in frontmatter
    assert (
        'resource: "file:///.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md"'
        in frontmatter
    )


def test_skill_cu05_wa04_frontmatter_timestamp_is_valid_iso8601():
    frontmatter, _ = split_frontmatter(read(CU05_WA04_SKILL))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "cu05-wa04 SKILL.md must declare a timestamp."
    assert TIMESTAMP_RE.match(match.group(1))


def test_skill_cu05_wa04_frontmatter_topics_and_tags_include_new_keywords():
    frontmatter, _ = split_frontmatter(read(CU05_WA04_SKILL))
    for keyword in ["security-patching", "unattended-upgrades", "dnf-automatic"]:
        assert keyword in frontmatter, f"topics/tags should mention '{keyword}'."


def test_skill_cu05_wa04_no_longer_uses_placeholder_type():
    content = read(CU05_WA04_SKILL)
    assert "procedural_skill" not in content, (
        "cu05-wa04 SKILL.md should no longer use the placeholder 'procedural_skill' type."
    )


def test_skill_cu05_wa04_procedure_no_longer_a_stub():
    content = read(CU05_WA04_SKILL)
    assert "Pending implementation based on JTPS 2 document." not in content
    assert "## Overview" in content
    assert "## Procedure" in content
    assert content.count("```bash") >= 3


def test_skill_cu05_wa04_overview_mentions_compliance_standards():
    content = read(CU05_WA04_SKILL)
    overview_start = content.index("## Overview")
    procedure_start = content.index("## Procedure")
    overview = content[overview_start:procedure_start]
    assert "NOSS Level 3" in overview
    assert "ISO/IEC 27001" in overview


def test_skill_cu05_wa04_debian_ubuntu_automation_commands():
    content = read(CU05_WA04_SKILL)
    section_start = content.index("### 1. Automated Security Patching")
    section_end = content.index("### 2. Package Integrity & Security Auditing")
    section = content[section_start:section_end]
    for command in [
        "sudo apt update",
        "sudo apt install -y unattended-upgrades apt-config-auto-update",
        "sudo dpkg-reconfigure --priority=low unattended-upgrades",
        "sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log",
    ]:
        assert command in section, f"Debian/Ubuntu automation subsection missing: {command!r}"


def test_skill_cu05_wa04_redhat_automation_commands():
    content = read(CU05_WA04_SKILL)
    section_start = content.index("### 1. Automated Security Patching")
    section_end = content.index("### 2. Package Integrity & Security Auditing")
    section = content[section_start:section_end]
    for command in [
        "sudo dnf install -y dnf-automatic",
        "sudo sed -i 's/upgrade_type = default/upgrade_type = security/' /etc/dnf/automatic.conf",
        "sudo sed -i 's/apply_updates = no/apply_updates = yes/' /etc/dnf/automatic.conf",
        "sudo systemctl enable --now dnf-automatic.timer",
    ]:
        assert command in section, f"Red Hat automation subsection missing: {command!r}"


def test_skill_cu05_wa04_integrity_auditing_commands():
    content = read(CU05_WA04_SKILL)
    section = content[content.index("### 2. Package Integrity & Security Auditing"):]
    for command in ["sudo rpm -Va", "sudo rpm -V openssh-server", "sudo dnf updateinfo list security", "sudo dpkg --verify"]:
        assert command in section, f"Package integrity subsection missing: {command!r}"


def test_skill_cu05_wa04_footer_retains_attribution():
    content = read(CU05_WA04_SKILL).strip()
    assert "Harisfazillah Jamel" in content
    assert "Notis Perundangan" in content


# ---------------------------------------------------------------------------
# .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md
# (new "RPM Package Operations & Source Compilation" subsection)
# ---------------------------------------------------------------------------

def test_skill_cu01_wa05_rpm_subsection_heading_present():
    content = read(CU01_WA05_SKILL)
    assert "**RPM Package Operations & Source Compilation:**" in content


def test_skill_cu01_wa05_rpm_subsection_commands():
    content = read(CU01_WA05_SKILL)
    section_start = content.index("**RPM Package Operations & Source Compilation:**")
    section_end = content.index("### 2. Universal Containerized Packaging")
    section = content[section_start:section_end]
    for command in [
        "sudo rpm -Uvh nmap-7.95-1.x86_64.rpm",
        "rpm -qi nmap",
        "rpm -ql nmap",
        "rpm -V nmap",
        "rpmbuild --rebuild openssh-9.8p1-1.src.rpm",
        "tar -xvf sample-app-1.0.tar.gz",
        "cd sample-app-1.0",
        "./configure --prefix=/usr/local",
        "make -j$(nproc)",
        "sudo make install",
    ]:
        assert command in section, f"RPM/source-compilation subsection missing: {command!r}"


def test_skill_cu01_wa05_rpm_subsection_is_within_native_package_management_section():
    """The new subsection must sit inside '### 1. Native Package Management',
    after DNF5 and before Universal Containerized Packaging."""
    content = read(CU01_WA05_SKILL)
    native_idx = content.index("### 1. Native Package Management")
    dnf_idx = content.index("AlmaLinux 10 / Fedora 43 (DNF5)")
    rpm_idx = content.index("**RPM Package Operations & Source Compilation:**")
    containerized_idx = content.index("### 2. Universal Containerized Packaging")
    assert native_idx < dnf_idx < rpm_idx < containerized_idx


# ---------------------------------------------------------------------------
# .agents/skills/index.md (Master Palace Registry)
# ---------------------------------------------------------------------------

def test_skills_index_timestamp_bumped_to_2026_08_23():
    frontmatter, _ = split_frontmatter(read(SKILLS_INDEX))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "Master Palace Registry is missing a timestamp field."
    assert match.group(1) == "2026-08-23T23:25:24Z"


def test_skills_index_footer_dated_2026_08_23():
    content = read(SKILLS_INDEX).strip()
    assert content.endswith(
        "*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | "
        "Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | "
        "[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*"
    )
    assert "Harisfazillah Jamel (LinuxMalaysia) | 2026-08-23" in content
    assert "Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17" not in content


def test_skills_index_still_lists_cu05_wa04_skill_row():
    """Regression: the registry row for cu05-wa04 must continue to exist even
    though only the timestamp/footer date were bumped in this change."""
    content = read(SKILLS_INDEX)
    assert "cu05-wa04-conduct-application-security-patching" in content


# ---------------------------------------------------------------------------
# manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
# (new Section "C. Pengurusan Pakej RPM & Kompilasi Kod Sumber")
# ---------------------------------------------------------------------------

def test_manual_cu01_wa05_rpm_section_heading_and_position():
    content = read(CU01_WA05_MANUAL)
    heading = "#### C. Pengurusan Pakej RPM & Kompilasi Kod Sumber (Red Hat Package Manager & Tarball)"
    assert heading in content
    section_b_idx = content.index("#### B. Red Hat/AlmaLinux/Fedora (DNF5 / DNF)")
    section_c_idx = content.index(heading)
    section_2_idx = content.index("### 2. Pemasangan Pakej Universal (Flatpak & Snap)")
    assert section_b_idx < section_c_idx < section_2_idx


def test_manual_cu01_wa05_rpm_option_flags_documented():
    content = read(CU01_WA05_MANUAL)
    section_start = content.index("#### C. Pengurusan Pakej RPM")
    section_end = content.index("### 2. Pemasangan Pakej Universal")
    section = content[section_start:section_end]
    for flag in ["`-i`", "`-U`", "`-F`", "`-q`", "`-V`", "`-e`", "`--rebuilddb`", "`--nodeps`"]:
        assert flag in section, f"RPM option flag {flag} should be documented."


def test_manual_cu01_wa05_rpm_examples_and_source_compilation_commands():
    content = read(CU01_WA05_MANUAL)
    section_start = content.index("#### C. Pengurusan Pakej RPM")
    section_end = content.index("### 2. Pemasangan Pakej Universal")
    section = content[section_start:section_end]
    for command in [
        "sudo rpm -Uvh nmap-7.95-1.x86_64.rpm",
        "rpm -qi nmap",
        "rpm -ql nmap",
        "rpm -qf /usr/bin/nmap",
        "rpm -V nmap",
        "sudo dnf install -y rpm-build rpmdevtools gcc make",
        "rpmbuild --rebuild openssh-9.8p1-1.src.rpm",
        "tar -xvf sampel-aplikasi-1.0.tar.gz",
        "./configure --prefix=/usr/local",
        "make -j$(nproc)",
        "sudo make install",
    ]:
        assert command in section, f"RPM/source compilation section missing: {command!r}"


def test_manual_cu01_wa05_still_has_four_numbered_top_level_sections():
    """Regression: adding subsection C must not disturb the four top-level
    numbered '### N.' sections of the manual node."""
    content = read(CU01_WA05_MANUAL)
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu01-wa05 manual node should still have numbered section {n}."
        )
    assert not re.search(r"^### 5\. ", content, re.MULTILINE)


# ---------------------------------------------------------------------------
# manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md
# (replacing the generic verification stub with real procedures)
# ---------------------------------------------------------------------------

def test_manual_cu05_wa04_stub_verification_commands_removed():
    """Regression: the previous generic placeholder commands must no longer
    be present now that real automation/audit procedures were added."""
    content = read(CU05_WA04_MANUAL)
    assert "# Contoh arahan verifikasi status sistem" not in content
    assert "uname -r\nsystemctl status" not in content


def test_manual_cu05_wa04_automation_section_headings_and_order():
    content = read(CU05_WA04_MANUAL)
    heading_automation = "### 2. Automasi Tampalan Keselamatan Pakej (Unattended Upgrades & DNF Automatic)"
    heading_integrity = "### 3. Semakan Integriti Fail Pakej & Audit CVE (`rpm -V` & `dpkg --verify`)"
    assert heading_automation in content
    assert heading_integrity in content
    steps_idx = content.index("### 2. Langkah-Langkah Operasi")
    automation_idx = content.index(heading_automation)
    integrity_idx = content.index(heading_integrity)
    assert steps_idx < automation_idx < integrity_idx


def test_manual_cu05_wa04_debian_and_redhat_automation_subsections():
    content = read(CU05_WA04_MANUAL)
    section_start = content.index("### 2. Automasi Tampalan Keselamatan Pakej")
    section_end = content.index("### 3. Semakan Integriti Fail Pakej")
    section = content[section_start:section_end]
    assert "#### A. Debian / Ubuntu (unattended-upgrades)" in section
    assert "#### B. Red Hat / AlmaLinux / Fedora (dnf-automatic)" in section
    for command in [
        "sudo apt install -y unattended-upgrades apt-config-auto-update",
        "sudo dpkg-reconfigure --priority=low unattended-upgrades",
        "cat /etc/apt/apt.conf.d/20auto-upgrades",
        "sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log",
        "sudo dnf install -y dnf-automatic",
        "sudo systemctl enable --now dnf-automatic.timer",
        "sudo systemctl status dnf-automatic.timer",
    ]:
        assert command in section, f"Automation section missing: {command!r}"


def test_manual_cu05_wa04_integrity_audit_commands():
    content = read(CU05_WA04_MANUAL)
    section = content[content.index("### 3. Semakan Integriti Fail Pakej"):]
    for command in [
        "sudo rpm -Va",
        "sudo rpm -V openssh-server",
        "sudo dpkg --verify",
        "sudo dnf updateinfo list security",
    ]:
        assert command in section, f"Integrity audit section missing: {command!r}"


# ---------------------------------------------------------------------------
# openwiki/topic-01-linux-desktop-and-basics.md
# ---------------------------------------------------------------------------

def test_openwiki_topic01_section7_covers_packaging_format_comparison():
    content = read(OPENWIKI_TOPIC_01)
    section_start = content.index(
        "### 7. Pemasangan Aplikasi, Pemacu Peranti & Persekitaran Shell (CU01-WA05)"
    )
    section_end = content.index(
        "### 8. Konfigurasi Sambungan Rangkaian Endpoint (CU01-WA06)"
    )
    section = content[section_start:section_end]
    assert "**Perbandingan Format Pembungkusan**" in section
    for keyword in [
        ".deb", ".rpm", "dnf5", "-ivh", "-Uvh", "--rebuilddb", "--nodeps",
        "Flatpak", "Snap", ".tar.gz", ".tar.zst",
        "./configure && make && make install", ".src.rpm", "rpmbuild --rebuild",
        "$EDITOR", "$VISUAL", "/etc/profile.d/editor.sh",
        "lspci", "ubuntu-drivers", "akmod-nvidia",
    ]:
        assert keyword in section, f"topic-01 section 7 should mention '{keyword}'."


def test_openwiki_topic01_section7_still_links_to_manual_node():
    content = read(OPENWIKI_TOPIC_01)
    assert "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md" in content


# ---------------------------------------------------------------------------
# openwiki/topic-05-linux-security.md
# ---------------------------------------------------------------------------

def test_openwiki_topic05_new_syllabus_item_9_content():
    content = read(OPENWIKI_TOPIC_05)
    item_9 = "9. **Automasi Tampalan Keselamatan & Audit Integriti Pakej (CU05-WA04)**:"
    assert item_9 in content
    section_start = content.index(item_9)
    section_end = content.index("## Modul Amali Terkait")
    section = content[section_start:section_end]
    assert "`unattended-upgrades`" in section
    assert "`dnf-automatic`" in section
    assert "`rpm -V`" in section
    assert "`rpm -Va`" in section
    assert "`dpkg --verify`" in section


def test_openwiki_topic05_related_modules_list_includes_cu05_wa04_between_wa01_and_wa05():
    content = read(OPENWIKI_TOPIC_05)
    wa01_idx = content.index("Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01)")
    wa04_idx = content.index(
        "[Pengurusan Tampalan & Kemas Kini Keselamatan (CU05-WA04)]"
        "(../manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md)"
    )
    wa05_idx = content.index(
        "Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05)"
    )
    assert wa01_idx < wa04_idx < wa05_idx


def test_openwiki_topic05_syllabus_still_has_nine_numbered_items_in_order():
    content = read(OPENWIKI_TOPIC_05)
    section = content[content.index("## Silibus Utama"):content.index("## Modul Amali Terkait")]
    indices = []
    for n in range(1, 10):
        pattern = rf"^{n}\. \*\*"
        match = re.search(pattern, section, re.MULTILINE)
        assert match, f"topic-05 syllabus should have numbered item {n}."
        indices.append(match.start())
    assert indices == sorted(indices)


# ---------------------------------------------------------------------------
# START-HERE.md and compiled mirrors: heading/label rewording regression
# ---------------------------------------------------------------------------

OLD_ENTRY_POINTS_HEADING = "Titik Mula (Entry Points)"
NEW_ENTRY_POINTS_HEADING = "Entry Points (Titik Masuk)"
OLD_CU05_LABEL = "CU05: Kawalan Keselamatan Endpoint & Pengerasan Sistem"
NEW_CU05_LABEL = "CU05: Kawalan Keselamatan Endpoint & Hardening"
OLD_CU06_LABEL = "CU06: Sokongan Pengguna & Penyelesaian Masalah"
NEW_CU06_LABEL = "CU06: Sokongan Pengguna & Troubleshooting"


@pytest.mark.parametrize(
    "relpath",
    ["START-HERE.md", "llms-full.txt", "html/llms-full.txt"],
)
def test_start_here_entry_points_heading_reworded(relpath):
    content = read(relpath)
    assert f"## 🌐 {NEW_ENTRY_POINTS_HEADING}" in content
    assert OLD_ENTRY_POINTS_HEADING not in content


@pytest.mark.parametrize(
    "relpath",
    ["START-HERE.md", "llms-full.txt", "html/llms-full.txt"],
)
def test_start_here_cu05_cu06_labels_reworded(relpath):
    content = read(relpath)
    assert NEW_CU05_LABEL in content
    assert NEW_CU06_LABEL in content
    assert OLD_CU05_LABEL not in content
    assert OLD_CU06_LABEL not in content


@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_start_here_cu05_cu06_labels_reworded_xml_escaped(relpath):
    content = read(relpath)
    assert NEW_CU05_LABEL.replace("&", "&amp;") in content
    assert NEW_CU06_LABEL.replace("&", "&amp;") in content
    assert OLD_CU05_LABEL.replace("&", "&amp;") not in content
    assert OLD_CU06_LABEL.replace("&", "&amp;") not in content


def test_start_here_html_entry_points_anchor_reworded():
    content = read("html/START-HERE.html")
    assert 'id="entry-points-titik-masuk"' in content
    assert 'id="titik-mula-entry-points"' not in content
    assert NEW_CU05_LABEL.replace("&", "&amp;") in content
    assert NEW_CU06_LABEL.replace("&", "&amp;") in content


# ---------------------------------------------------------------------------
# Rebuilt static HTML pages: html/manual/cu01/... & html/manual/cu05/...
# ---------------------------------------------------------------------------

HTML_CU01_WA05 = "html/manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
HTML_CU05_WA04 = "html/manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.html"


def test_html_cu01_wa05_has_new_rpm_section_heading_and_nav_link():
    content = read(HTML_CU01_WA05)
    anchor_id = "c-pengurusan-pakej-rpm-kompilasi-kod-sumber-red-hat-package-manager-tarball"
    assert f'<h4 id="{anchor_id}">' in content
    assert f'href="#{anchor_id}" class="md-nav__link"' in content


def test_html_cu01_wa05_rpm_section_code_blocks_present():
    content = read(HTML_CU01_WA05)
    # Pygments syntax highlighting wraps each token/whitespace run in its own
    # <span>, so compare against the tag-stripped plain text instead of the
    # raw HTML (which never contains the literal multi-word command string).
    text = re.sub(r"<[^>]+>", "", content)
    assert "rpm -Uvh nmap-7.95-1.x86_64.rpm" in text
    assert "rpmbuild --rebuild openssh-9.8p1-1.src.rpm" in text
    assert "sampel-aplikasi-1.0.tar.gz" in text


def test_html_cu05_wa04_has_new_section_headings_and_nav_links():
    content = read(HTML_CU05_WA04)
    automation_id = "2-automasi-tampalan-keselamatan-pakej-unattended-upgrades-dnf-automatic"
    integrity_id = "3-semakan-integriti-fail-pakej-audit-cve-rpm-v-dpkg-verify"
    for anchor_id, tag in [(automation_id, "h3"), (integrity_id, "h3")]:
        assert f'<{tag} id="{anchor_id}">' in content
        assert f'href="#{anchor_id}" class="md-nav__link"' in content


def test_html_cu05_wa04_debian_and_redhat_subsection_anchors_present():
    content = read(HTML_CU05_WA04)
    assert '<h4 id="a-debian-ubuntu-unattended-upgrades">' in content
    assert '<h4 id="b-red-hat-almalinux-fedora-dnf-automatic">' in content


def test_html_cu05_wa04_stub_commands_removed():
    content = read(HTML_CU05_WA04)
    assert "# Contoh arahan verifikasi status sistem" not in content


def test_html_openwiki_topic05_lists_cu05_wa04_related_module_link():
    content = read("html/openwiki/topic-05-linux-security.html")
    assert (
        'href="../manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.html"'
        in content
    )
    assert "Automasi Tampalan Keselamatan &amp; Audit Integriti Pakej (CU05-WA04)" in content


def test_html_openwiki_topic01_section7_reflects_packaging_format_comparison():
    content = read("html/openwiki/topic-01-linux-desktop-and-basics.html")
    section_start = content.index(
        '<h3 id="7-pemasangan-aplikasi-pemacu-peranti-persekitaran-shell-cu01-wa05">'
    )
    section_end = content.index(
        '<h3 id="8-konfigurasi-sambungan-rangkaian-endpoint-cu01-wa06">'
    )
    section = content[section_start:section_end]
    assert "Perbandingan Format Pembungkusan" in section
    assert "rpmbuild --rebuild" in section
    assert "akmod-nvidia" in section


# ---------------------------------------------------------------------------
# html/search/search_index.json
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def search_index_data():
    with open(REPO_ROOT / "html/search/search_index.json", "r", encoding="utf-8") as f:
        return json.load(f)


def _doc_for_location(data, location):
    matches = [doc for doc in data["docs"] if doc.get("location") == location]
    assert matches, f"Expected exactly one search index entry for {location!r}."
    return matches[0]


def test_search_index_has_entry_for_new_cu01_wa05_rpm_subsection():
    with open(REPO_ROOT / "html/search/search_index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    doc = _doc_for_location(
        data,
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
        "#c-pengurusan-pakej-rpm-kompilasi-kod-sumber-red-hat-package-manager-tarball",
    )
    assert doc["title"] == "C. Pengurusan Pakej RPM &amp; Kompilasi Kod Sumber (Red Hat Package Manager &amp; Tarball)"


def test_search_index_has_entries_for_new_cu05_wa04_subsections():
    with open(REPO_ROOT / "html/search/search_index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    automation_doc = _doc_for_location(
        data,
        "manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.html"
        "#2-automasi-tampalan-keselamatan-pakej-unattended-upgrades-dnf-automatic",
    )
    assert "Unattended Upgrades" in automation_doc["title"]
    assert "DNF Automatic" in automation_doc["title"]

    integrity_doc = _doc_for_location(
        data,
        "manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.html"
        "#3-semakan-integriti-fail-pakej-audit-cve-rpm-v-dpkg-verify",
    )
    assert "Semakan Integriti Fail Pakej" in integrity_doc["title"]


def test_search_index_locations_unique_for_updated_pages():
    with open(REPO_ROOT / "html/search/search_index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    locations = [
        doc["location"]
        for doc in data["docs"]
        if doc["location"].startswith("manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html")
        or doc["location"].startswith(
            "manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.html"
        )
    ]
    duplicates = {loc for loc in locations if locations.count(loc) > 1}
    assert not duplicates, f"Duplicate search index locations found: {duplicates}"


# ---------------------------------------------------------------------------
# llms-full.txt / html/llms-full.txt: embedded SKILL.md file blocks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_llms_full_txt_embeds_upgraded_cu05_wa04_skill_file(relpath):
    content = read(relpath)
    begin_marker = (
        "<!-- BEGIN FILE: .agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md -->"
    )
    end_marker = (
        "<!-- END FILE: .agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md -->"
    )
    begin_idx = content.index(begin_marker)
    end_idx = content.index(end_marker)
    section = content[begin_idx:end_idx]
    assert "type: skill" in section
    assert "procedural_skill" not in section
    assert "## Overview" in section
    assert "unattended-upgrades" in section
    assert "dnf-automatic" in section


@pytest.mark.parametrize("relpath", ["llms-full.txt", "html/llms-full.txt"])
def test_llms_full_txt_embeds_upgraded_cu01_wa05_skill_file(relpath):
    content = read(relpath)
    begin_marker = (
        "<!-- BEGIN FILE: .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md -->"
    )
    end_marker = (
        "<!-- END FILE: .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md -->"
    )
    begin_idx = content.index(begin_marker)
    end_idx = content.index(end_marker)
    section = content[begin_idx:end_idx]
    assert "RPM Package Operations & Source Compilation" in section
    assert "rpmbuild --rebuild openssh-9.8p1-1.src.rpm" in section


@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_llms_context_xml_embeds_upgraded_cu05_wa04_skill_file(relpath):
    content = read(relpath)
    begin_idx = content.index(
        '<file path=".agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md">'
    )
    end_idx = content.index("</file>", begin_idx)
    section = content[begin_idx:end_idx]
    assert "type: skill" in section
    assert "procedural_skill" not in section
    assert "unattended-upgrades" in section
    assert "dnf-automatic" in section


@pytest.mark.parametrize("relpath", ["llms_context.xml", "html/llms_context.xml"])
def test_llms_context_xml_topic01_section7_uses_escaped_shell_operators(relpath):
    content = read(relpath)
    assert "./configure &amp;&amp; make &amp;&amp; make install" in content
