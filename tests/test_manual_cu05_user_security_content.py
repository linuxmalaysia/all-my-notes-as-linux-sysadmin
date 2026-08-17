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
  - .agents/skills/index.md (Master Palace Registry rows for the two skills above)
  - openwiki/topic-05-linux-security.md
  - html/manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html
  - html/manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html
  - html/manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html
  - html/openwiki/topic-05-linux-security.html
  - html/search/search_index.json
"""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """
    Read a repository file as UTF-8 text, removing any leading byte-order mark.
    
    Parameters:
    	relative_path (str): Path to the file relative to the repository root.
    
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

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


def split_frontmatter(content):
    """Split a markdown file's content into (frontmatter, body)."""
    assert content.startswith("---"), "File must start with YAML frontmatter."
    parts = content.split("---", 2)
    assert len(parts) >= 3, "File has malformed or missing YAML closure '---'."
    return parts[1].strip(), parts[2]

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


# ---------------------------------------------------------------------------
# Manual knowledge nodes (manual/cu05) - frontmatter & structure
# ---------------------------------------------------------------------------

MANUAL_NODES = [
    "manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md",
    "manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md",
    "manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md",
]


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_exists(relpath):
    assert (REPO_ROOT / relpath).is_file()


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_okf_frontmatter(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    assert "okf_version: 0.1" in frontmatter
    assert "type: knowledge-node" in frontmatter
    assert "title:" in frontmatter
    assert 'timestamp: "2026-08-17T00:00:00Z"' in frontmatter
    assert "topics:" in frontmatter
    assert "tags:" in frontmatter
    assert "description:" in frontmatter


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_resource_matches_file_location(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'resource:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} missing 'resource' frontmatter key."
    assert match.group(1) == f"file:///{relpath}"


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_learning_objectives_and_checklist(relpath):
    content = read(relpath)
    assert "Objektif Pembelajaran" in content
    assert "Senarai Semak Kompetensi" in content
    assert re.search(r"^- \[ \] ", content, re.MULTILINE), (
        f"{relpath} should contain at least one unchecked checklist item."
    )


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_sovereign_footer_dated_2026_08_17(relpath):
    content = read(relpath).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content
    assert "Notis Perundangan" in content
    assert "CC BY-SA 4.0" in content


def test_manual_cu05_main_node_has_six_numbered_top_level_sections():
    content = read(MANUAL_NODES[0])
    for n in range(1, 7):
        assert re.search(rf"^## .*{n}\. ", content, re.MULTILINE), (
            f"Main CU05 node should have a numbered top-level section '{n}.'."
        )
    # No stray 7th top-level numbered section.
    assert not re.search(r"^## .*7\. ", content, re.MULTILINE)


def test_manual_cu05_main_node_covers_identity_and_navigation_topics():
    content = read(MANUAL_NODES[0])
    for keyword in [
        "/etc/group", "/etc/gshadow", "groupadd", "umask 027",
        "SUID", "SGID", "Sticky Bit", "plocate", "man 5 shadow",
        "/etc/profile.d/timeout.sh", "faillock.conf",
    ]:
        assert keyword in content, f"Main CU05 node should mention '{keyword}'."


def test_manual_cu05_wa01_node_has_four_numbered_sections():
    content = read(MANUAL_NODES[1])
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu05-wa01 manual node should have numbered section {n}."
        )
    assert not re.search(r"^### 5\. ", content, re.MULTILINE)


def test_manual_cu05_wa01_node_covers_uid0_and_shadow_audit():
    content = read(MANUAL_NODES[1])
    for keyword in [
        'awk -F: \'($3 == "0")', "/etc/shadow", "sudo -l -U ahmad",
        "sudo faillock --user ahmad --reset",
    ]:
        assert keyword in content, f"cu05-wa01 manual node should mention '{keyword}'."


def test_manual_cu05_wa05_node_has_four_numbered_sections():
    content = read(MANUAL_NODES[2])
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu05-wa05 manual node should have numbered section {n}."
        )
    assert not re.search(r"^### 5\. ", content, re.MULTILINE)


def test_manual_cu05_wa05_node_covers_grub_and_shutdown_procedures():
    content = read(MANUAL_NODES[2])
    for keyword in [
        "grub2-setpassword", "grub2-mkconfig", "readonly TMOUT=900",
        "maxlogins       3", "sudo systemctl poweroff",
    ]:
        assert keyword in content, f"cu05-wa05 manual node should mention '{keyword}'."


# ---------------------------------------------------------------------------
# AI Agent Skills (.agents/skills/cu05-wa01.../SKILL.md, cu05-wa05.../SKILL.md)
# ---------------------------------------------------------------------------

SKILL_FILES = {
    "cu05-wa01": ".agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md",
    "cu05-wa05": ".agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md",
}


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_file_exists(relpath):
    assert (REPO_ROOT / relpath).is_file()


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_file_has_no_leading_byte_order_mark(relpath):
    """Previously these files started with a UTF-8 BOM before '---'; the
    revamped skill files must start directly with the frontmatter fence."""
    raw = (REPO_ROOT / relpath).read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf"), f"{relpath} should not start with a BOM."
    assert raw.startswith(b"---"), f"{relpath} should start directly with '---'."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_is_well_formed(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    assert "name:" in frontmatter, f"{relpath} missing name key."
    assert "description:" in frontmatter, f"{relpath} missing description key."
    assert "title:" in frontmatter, f"{relpath} missing title key."
    assert "topics:" in frontmatter, f"{relpath} missing topics key."
    assert "tags:" in frontmatter, f"{relpath} missing tags key."
    assert "okf_version: 0.1" in frontmatter, f"{relpath} must declare okf_version: 0.1."
    assert "type: skill" in frontmatter, f"{relpath} should declare type: skill."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_no_longer_uses_placeholder_type(relpath):
    """The previous scaffold used 'type: procedural_skill'; this PR upgrades
    it to the canonical 'type: skill'."""
    frontmatter, _ = split_frontmatter(read(relpath))
    assert "procedural_skill" not in frontmatter, (
        f"{relpath} should no longer use the placeholder 'procedural_skill' type."
    )


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_timestamp_is_valid(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} is missing a timestamp field."
    assert TIMESTAMP_RE.match(match.group(1))


@pytest.mark.parametrize("name,relpath", SKILL_FILES.items())
def test_skill_frontmatter_name_matches_folder(name, relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'name:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} missing quoted 'name' field."
    assert match.group(1).startswith(name)


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_resource_matches_file_location(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'resource:\s*"([^"]+)"', frontmatter)
    assert match, f"{relpath} missing 'resource' frontmatter key."
    assert match.group(1) == f"file:///{relpath}"


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_procedure_no_longer_a_stub(relpath):
    content = read(relpath)
    assert "Pending implementation based on JTPS 2 document." not in content, (
        f"{relpath} still contains the unimplemented stub placeholder."
    )
    assert "```bash" in content, f"{relpath} should contain executable bash examples."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_has_audit_verification_checklist(relpath):
    content = read(relpath)
    assert "Audit Verification Checklist" in content
    assert re.search(r"^- \[ \] ", content, re.MULTILINE), (
        f"{relpath} should contain at least one unchecked checklist item."
    )


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_has_sovereign_footer_dated_2026_08_17(relpath):
    content = read(relpath).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content, f"{relpath} footer should be dated 2026-08-17."
    assert "Notis Perundangan" in content


def test_skill_cu05_wa01_covers_full_audit_workflow():
    content = read(SKILL_FILES["cu05-wa01"])
    for keyword in [
        'awk -F: \'($3 == "0" && $1 != "root")',
        "sudo pwck -r", "sudo grpck -r", "sudo visudo -c",
        "sudo -l -U <username>", "find / -perm -4000 -type f -ls",
        "sudo setfacl -m u:zarith:rw-", "sudo faillock --user <username> --reset",
    ]:
        assert keyword in content, f"cu05-wa01 skill should mention '{keyword}'."


def test_skill_cu05_wa05_covers_full_lockdown_workflow():
    content = read(SKILL_FILES["cu05-wa05"])
    for keyword in [
        "grub2-setpassword", "grub2-mkconfig -o /boot/grub2/grub.cfg",
        "readonly TMOUT=900", "hard    core            0",
        "hard    maxlogins       3", "sudo shutdown -h +2",
        "sudo systemctl poweroff",
    ]:
        assert keyword in content, f"cu05-wa05 skill should mention '{keyword}'."


# ---------------------------------------------------------------------------
# Master Palace Registry (.agents/skills/index.md)
# ---------------------------------------------------------------------------

SKILLS_INDEX = ".agents/skills/index.md"


def test_skills_index_timestamp_updated_and_valid():
    frontmatter, _ = split_frontmatter(read(SKILLS_INDEX))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "Master Palace Registry is missing a timestamp field."
    assert TIMESTAMP_RE.match(match.group(1))
    assert match.group(1) == "2026-08-17T04:28:15Z"


def test_skills_index_no_longer_lists_placeholder_descriptions_for_updated_skills():
    content = read(SKILLS_INDEX)
    for name in SKILL_FILES:
        row_match = re.search(rf"\*\*`{name}[^\n]*\n", content)
        assert row_match, f"Expected a registry row referencing '{name}'."
        assert "No description provided." not in row_match.group(0), (
            f"Registry row for '{name}' should have a real description now."
        )
        assert "N/A" not in row_match.group(0), (
            f"Registry row for '{name}' should list real topics/scope now."
        )


@pytest.mark.parametrize(
    "fragment",
    [
        "Executes NOSS Work Activity CU05-WA01: Audit user accounts, group "
        "memberships, authentication files (/etc/passwd, /etc/shadow), "
        "sudoers configuration, file permissions, POSIX ACLs, and faillock.",
        "Executes NOSS Work Activity CU05-WA05: Manage physical endpoint "
        "lockdowns, bootloader GRUB2 password protection, session timeout "
        "(TMOUT), virtual terminal limits, and safe shutdown procedures.",
    ],
)
def test_skills_index_contains_updated_descriptions(fragment):
    content = read(SKILLS_INDEX)
    assert fragment in content, f"Registry should contain description fragment: {fragment!r}"


def test_skills_index_wa01_row_has_expected_title_and_topics():
    content = read(SKILLS_INDEX)
    row_match = re.search(r"\*\*`cu05-wa01[^\n]*\n", content)
    assert row_match
    row = row_match.group(0)
    assert "Perform User Account and Permission Audits (CU05-WA01)" in row
    assert '"visudo"' in row
    assert '"faillock"' in row


def test_skills_index_wa05_row_has_expected_title_and_topics():
    content = read(SKILLS_INDEX)
    row_match = re.search(r"\*\*`cu05-wa05[^\n]*\n", content)
    assert row_match
    row = row_match.group(0)
    assert "Manage Physical Endpoint Security Lockdowns (CU05-WA05)" in row
    assert '"grub"' in row
    assert '"tmout"' in row


def test_skills_index_unrelated_cu05_rows_are_unaffected():
    """Only the wa01 and wa05 rows were updated; sibling rows in the same
    unit should remain untouched placeholders."""
    content = read(SKILLS_INDEX)
    for name in [
        "cu05-wa02-configure-endpoint-antivirus-anti-malware-defences",
        "cu05-wa03-configure-client-firewall-profiles",
        "cu05-wa04-conduct-application-security-patching",
    ]:
        row_match = re.search(rf"\*\*`{name}[^\n]*\n", content)
        assert row_match, f"Expected a registry row referencing '{name}'."
        assert "No description provided." in row_match.group(0)
        assert "N/A" in row_match.group(0)


def test_skills_index_total_modules_indexed_unchanged():
    content = read(SKILLS_INDEX)
    assert "**Total Modules Indexed:** `122`" in content


# ---------------------------------------------------------------------------
# openwiki/topic-05-linux-security.md
# ---------------------------------------------------------------------------

OPENWIKI_TOPIC_05 = "openwiki/topic-05-linux-security.md"


def test_openwiki_topic05_frontmatter_is_valid():
    frontmatter, _ = split_frontmatter(read(OPENWIKI_TOPIC_05))
    assert "okf_version: 0.1" in frontmatter
    assert "type: documentation" in frontmatter
    assert 'timestamp: "2026-08-17T00:00:00Z"' in frontmatter
    assert "cu05" in frontmatter.lower()


def test_openwiki_topic05_has_eight_numbered_syllabus_sections():
    content = read(OPENWIKI_TOPIC_05)
    for n in range(1, 9):
        assert re.search(rf"^{n}\. \*\*", content, re.MULTILINE), (
            f"Expected numbered syllabus item '{n}. **...' in topic-05."
        )
    assert not re.search(r"^9\. \*\*", content, re.MULTILINE)


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_openwiki_topic05_links_to_each_manual_node(relpath):
    content = read(OPENWIKI_TOPIC_05)
    assert relpath in content or f"../{relpath}" in content


def test_openwiki_topic05_noss_mapping_lists_wa01_and_wa05_skills():
    content = read(OPENWIKI_TOPIC_05)
    assert "cu05-wa01-perform-user-account-and-permission-audits" in content
    assert "cu05-wa05-manage-physical-endpoint-security-lockdowns" in content
    assert "cu05-wa03-configure-client-firewall-profiles" in content


def test_openwiki_topic05_has_sovereign_footer_dated_2026_08_17():
    content = read(OPENWIKI_TOPIC_05).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content
    assert "Notis Perundangan" in content


# ---------------------------------------------------------------------------
# Rebuilt static HTML manual pages (html/manual/cu05/*.html)
# ---------------------------------------------------------------------------

HTML_MANUAL_PAGES = {
    "html/manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html": {
        "title": "Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01) - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali audit akaun pengguna, pemeriksaan /etc/passwd dan "
            "/etc/shadow, pengurusan privilesej sudoers, kebenaran UGO/POSIX "
            "ACL, serta penguncian faillock."
        ),
        "h1_id": "audit-akaun-pengguna-kebenaran-akses-linux-cu05-wa01",
        "header_topic": "Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01)",
    },
    "html/manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html": {
        "title": "Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05) - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali kawalan keselamatan fizikal, penguncian bootloader "
            "GRUB2, kawalan konsol maya VT, tamat masa sesi TMOUT, dan "
            "penutupan selamat."
        ),
        "h1_id": "kawalan-keselamatan-fizikal-persekitaran-console-endpoint-linux-cu05-wa05",
        "header_topic": "Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05)",
    },
    "html/manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html": {
        "title": "Pentadbiran Pengguna, Kebenaran Fail & Kawalan Akses Endpoint Linux - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali komprehesif pentadbiran pengguna, kumpulan, "
            "/etc/shadow, visudo, kebenaran fail chmod/chown, "
            "SUID/SGID/Sticky bit, POSIX ACL, faillock, FHS, dan penutupan "
            "sistem selamat."
        ),
        "h1_id": "pentadbiran-pengguna-kebenaran-fail-kawalan-akses-endpoint-linux",
        "header_topic": "Pentadbiran Pengguna, Kebenaran Fail & Kawalan Akses Endpoint Linux",
    },
}


@pytest.mark.parametrize("relpath", HTML_MANUAL_PAGES.keys())
def test_html_manual_page_exists(relpath):
    assert (REPO_ROOT / relpath).is_file()


@pytest.mark.parametrize("relpath,expected", HTML_MANUAL_PAGES.items())
def test_html_manual_page_title_tag(relpath, expected):
    content = read(relpath)
    assert f"<title>{expected['title']}</title>" in content


@pytest.mark.parametrize("relpath,expected", HTML_MANUAL_PAGES.items())
def test_html_manual_page_meta_description(relpath, expected):
    content = read(relpath)
    assert f'<meta name="description" content="{expected["description"]}">' in content


@pytest.mark.parametrize("relpath,expected", HTML_MANUAL_PAGES.items())
def test_html_manual_page_h1_and_skip_link_ids_match(relpath, expected):
    content = read(relpath)
    h1_id = expected["h1_id"]
    assert f'<h1 id="{h1_id}">' in content
    assert f'<a href="#{h1_id}" class="md-skip">' in content


@pytest.mark.parametrize("relpath,expected", HTML_MANUAL_PAGES.items())
def test_html_manual_page_header_topic_matches_title(relpath, expected):
    content = read(relpath)
    idx = content.find('data-md-component="header-topic"')
    assert idx != -1, f"{relpath} missing header-topic component."
    snippet = content[idx: idx + 400]
    assert expected["header_topic"] in snippet


def test_html_wa01_page_renamed_procedure_section_anchors():
    content = read("html/manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html")
    assert 'href="#prosedur-arahan-amali"' in content
    assert 'href="#1-audit-integriti-fail-pengguna-kumpulan-etcpasswd-etcshadow"' in content
    assert 'href="#2-audit-pengurusan-kebenaran-privilesej-pentadbir-visudo"' in content
    assert 'href="#3-audit-kebenaran-fail-posix-acl"' in content
    assert 'href="#4-semakan-pemulihan-penguncian-akaun-faillock"' in content
    # Old generic procedure heading should no longer be present.
    assert 'href="#garis-panduan-amali-prosedur"' not in content


def test_html_wa05_page_renamed_procedure_section_anchors():
    content = read("html/manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html")
    assert 'href="#prosedur-arahan-amali"' in content
    assert 'href="#1-perlindungan-bootloader-grub2-dengan-kata-laluan"' in content
    assert 'href="#2-penguatkuasaan-tamat-masa-sesi-terminal-otomatik-tmout"' in content
    assert 'href="#3-kawalan-penggunaan-had-proses-konsol-maya"' in content
    assert 'href="#4-prosedur-penutupan-ulang-but-selamat"' in content
    assert 'href="#garis-panduan-amali-prosedur"' not in content


def test_html_pentadbiran_page_has_all_top_level_section_anchors():
    content = read("html/manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html")
    for anchor in [
        "1-pentadbiran-pengguna-kumpulan-sistem",
        "2-polisi-kebolehan-keistimewaan-sistem-visudo-dasar-kata-laluan-faillock",
        "3-kebenaran-fail-asas-bit-khas-suid-sgid-sticky-bit",
        "4-senarai-kawalan-akses-posix-posix-acl-getfacl-setfacl",
        "5-navigasi-fhs-pencarian-fail-dokumentasi-find-plocate-man-db",
        "6-kawalan-keselamatan-sesi-penutupan-selamat-tmout-limitsconf-systemctl",
    ]:
        assert f'href="#{anchor}"' in content, f"Missing TOC anchor for section '{anchor}'."


def test_html_openwiki_topic05_links_to_all_three_manual_pages():
    content = read("html/openwiki/topic-05-linux-security.html")
    assert '<a href="../manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html">' in content
    assert '<a href="../manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html">' in content
    assert '<a href="../manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html">' in content


def test_html_openwiki_topic05_title_and_h1():
    content = read("html/openwiki/topic-05-linux-security.html")
    assert "<title>Topik 5: Keselamatan Linux & Kawalan Akses (CU05) - NOSS Linux Malaysia (DSOM)</title>" in content
    assert '<h1 id="topik-5-keselamatan-linux-kawalan-akses-endpoint-cu05">' in content


# ---------------------------------------------------------------------------
# html/search/search_index.json
# ---------------------------------------------------------------------------

SEARCH_INDEX_PATH = "html/search/search_index.json"


@pytest.fixture(scope="module")
def search_index():
    with open(REPO_ROOT / SEARCH_INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_search_index_is_valid_json_with_docs_list(search_index):
    assert isinstance(search_index, dict)
    assert "docs" in search_index
    assert isinstance(search_index["docs"], list)
    assert len(search_index["docs"]) > 0


def test_search_index_locations_are_unique(search_index):
    locations = [doc["location"] for doc in search_index["docs"]]
    duplicates = {loc for loc in locations if locations.count(loc) > 1}
    assert not duplicates, f"Search index has duplicate location entries: {duplicates}"


def test_search_index_contains_new_pentadbiran_page_entry(search_index):
    matches = [
        doc for doc in search_index["docs"]
        if doc["location"] == "manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html"
    ]
    assert matches, "Expected a top-level search entry for the new pentadbiran manual page."
    assert matches[0]["title"] == (
        "Pentadbiran Pengguna, Kebenaran Fail &amp; Kawalan Akses Endpoint Linux"
    )


@pytest.mark.parametrize(
    "location,expected_title",
    [
        (
            "manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html",
            "Audit Akaun Pengguna &amp; Kebenaran Akses Linux (CU05-WA01)",
        ),
        (
            "manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html",
            "Kawalan Keselamatan Fizikal &amp; Persekitaran Console Endpoint Linux (CU05-WA05)",
        ),
        (
            "openwiki/topic-05-linux-security.html",
            "Topik 5: Keselamatan Linux &amp; Kawalan Akses Endpoint (CU05)",
        ),
    ],
)
def test_search_index_contains_updated_page_titles(search_index, location, expected_title):
    matches = [doc for doc in search_index["docs"] if doc["location"] == location]
    assert matches, f"Expected search index entry for location {location!r}."
    assert matches[0]["title"] == expected_title


def test_search_index_contains_wa01_renamed_section_anchors(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    base = "manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.html"
    for anchor in [
        "#prosedur-arahan-amali",
        "#1-audit-integriti-fail-pengguna-kumpulan-etcpasswd-etcshadow",
        "#4-semakan-pemulihan-penguncian-akaun-faillock",
    ]:
        assert f"{base}{anchor}" in locations, f"Missing search entry for anchor '{anchor}'."


def test_search_index_contains_wa05_renamed_section_anchors(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    base = "manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.html"
    for anchor in [
        "#prosedur-arahan-amali",
        "#1-perlindungan-bootloader-grub2-dengan-kata-laluan",
        "#4-prosedur-penutupan-ulang-but-selamat",
    ]:
        assert f"{base}{anchor}" in locations, f"Missing search entry for anchor '{anchor}'."


def test_search_index_pentadbiran_page_has_all_numbered_section_anchors(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    base = "manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.html"
    for anchor in [
        "#1-pentadbiran-pengguna-kumpulan-sistem",
        "#2-polisi-kebolehan-keistimewaan-sistem-visudo-dasar-kata-laluan-faillock",
        "#3-kebenaran-fail-asas-bit-khas-suid-sgid-sticky-bit",
        "#4-senarai-kawalan-akses-posix-posix-acl-getfacl-setfacl",
        "#5-navigasi-fhs-pencarian-fail-dokumentasi-find-plocate-man-db",
        "#6-kawalan-keselamatan-sesi-penutupan-selamat-tmout-limitsconf-systemctl",
    ]:
        assert f"{base}{anchor}" in locations, f"Missing search entry for anchor '{anchor}'."
