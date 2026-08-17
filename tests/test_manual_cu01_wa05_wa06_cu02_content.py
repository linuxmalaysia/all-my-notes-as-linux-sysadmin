"""Tests for the CU01-WA05, CU01-WA06, and CU02 storage content added/updated
in this change set.

Covers:
  - The upgraded AI Agent Skills:
      .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md
      .agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md
      .agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md
  - The Master Palace Registry (.agents/skills/index.md) description/tag updates
    for the three skills above.
  - The expanded Sovereign Manual knowledge nodes:
      manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
      manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md
      manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md
  - The updated openwiki syllabus documents (topic-01, topic-02) that link to
    the nodes above.
  - The rebuilt static HTML pages for the manual nodes and openwiki topics.
  - The regenerated html/search/search_index.json search index.
"""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

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
# AI Agent Skills (.agents/skills/*/SKILL.md)
# ---------------------------------------------------------------------------

SKILL_FILES = {
    "cu01-wa05": ".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md",
    "cu01-wa06": ".agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md",
    "cu02-wa01": ".agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md",
}


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_file_exists(relpath):
    assert (REPO_ROOT / relpath).is_file(), f"Expected skill file {relpath} to exist."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_is_well_formed(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    assert "name:" in frontmatter, f"{relpath} missing name key."
    assert "description:" in frontmatter, f"{relpath} missing description key."
    assert "topics:" in frontmatter, f"{relpath} missing topics key."
    assert "tags:" in frontmatter, f"{relpath} missing tags key."
    assert "okf_version: 0.1" in frontmatter, f"{relpath} must declare okf_version: 0.1."
    assert "type: skill" in frontmatter, f"{relpath} should declare type: skill."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_frontmatter_no_longer_placeholder_type(relpath):
    """The previous scaffold used 'type: procedural_skill'; this PR upgrades
    it to the canonical 'type: skill'."""
    frontmatter, _ = split_frontmatter(read(relpath))
    assert "procedural_skill" not in frontmatter, (
        f"{relpath} should no longer use the placeholder 'procedural_skill' type."
    )


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_has_overview_and_governance_sections(relpath):
    content = read(relpath)
    assert "## Overview" in content, f"{relpath} missing '## Overview' section."
    assert "## Procedure" in content, f"{relpath} missing '## Procedure' section."
    assert "## Security & Governance" in content, (
        f"{relpath} missing '## Security & Governance' section."
    )


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_procedure_no_longer_a_stub(relpath):
    content = read(relpath)
    assert "Pending implementation based on JTPS 2 document." not in content, (
        f"{relpath} still contains the unimplemented stub placeholder."
    )
    # At least one fenced bash code block with an actual command should exist.
    assert "```bash" in content, f"{relpath} should contain executable bash examples."


@pytest.mark.parametrize("relpath", SKILL_FILES.values())
def test_skill_has_sovereign_footer_dated_2026_08_17(relpath):
    content = read(relpath).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content, f"{relpath} footer should be dated 2026-08-17."
    assert "Notis Perundangan" in content


def test_cu01_wa05_skill_covers_package_managers_and_drivers():
    content = read(SKILL_FILES["cu01-wa05"])
    for keyword in ["apt", "dnf", "flatpak", "snap", "nvidia-smi", "lspci"]:
        assert keyword in content, f"cu01-wa05 skill should mention '{keyword}'."


def test_cu01_wa06_skill_covers_networkmanager_workflow():
    content = read(SKILL_FILES["cu01-wa06"])
    for keyword in ["nmcli", "ip route show", "resolvectl", "wifi connect", "ipv4.method"]:
        assert keyword in content, f"cu01-wa06 skill should mention '{keyword}'."


def test_cu02_wa01_skill_covers_gpt_lvm_and_filesystem():
    content = read(SKILL_FILES["cu02-wa01"])
    for keyword in ["parted", "pvcreate", "vgcreate", "lvcreate", "mkfs.xfs", "fstab"]:
        assert keyword in content, f"cu02-wa01 skill should mention '{keyword}'."


# ---------------------------------------------------------------------------
# Master Palace Registry (.agents/skills/index.md)
# ---------------------------------------------------------------------------

SKILLS_INDEX = ".agents/skills/index.md"


def test_skills_index_no_longer_lists_placeholder_descriptions_for_updated_skills():
    content = read(SKILLS_INDEX)
    for name in SKILL_FILES:
        # The row for each updated skill must not use the generic placeholder.
        row_match = re.search(rf"\*\*`{name}[^\n]*\n", content)
        assert row_match, f"Expected a registry row referencing '{name}'."
        assert "No description provided." not in row_match.group(0), (
            f"Registry row for '{name}' should have a real description now."
        )


@pytest.mark.parametrize(
    "fragment",
    [
        "Executes NOSS Work Activity: Install Computer Applications And Device Drivers (APT, DNF5, Flatpak, Snap, GPU Drivers)",
        "Executes NOSS Work Activity: Configure Endpoint Network Connectivity (NetworkManager, nmcli, iproute2, Static IP, DHCP, Wi-Fi, DNS)",
        "Executes NOSS Work Activity: Identify Virtualisation Infrastructure & Storage Partitioning Requirements (GPT, LVM2, Filesystems)",
    ],
)
def test_skills_index_contains_updated_descriptions(fragment):
    content = read(SKILLS_INDEX)
    assert fragment in content, f"Registry should contain description fragment: {fragment!r}"


def test_skills_index_timestamp_updated_and_valid():
    frontmatter, _ = split_frontmatter(read(SKILLS_INDEX))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "Master Palace Registry is missing a timestamp field."
    assert TIMESTAMP_RE.match(match.group(1))
    assert match.group(1) == "2026-08-16T23:36:31Z"


# ---------------------------------------------------------------------------
# Manual knowledge nodes (manual/cu01, manual/cu02)
# ---------------------------------------------------------------------------

MANUAL_NODES = [
    "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md",
    "manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md",
    "manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md",
]


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_exists(relpath):
    assert (REPO_ROOT / relpath).is_file()


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_okf_frontmatter(relpath):
    content = read(relpath)
    frontmatter, _ = split_frontmatter(content)
    assert "okf_version: 0.1" in frontmatter
    assert "type: knowledge-node" in frontmatter
    assert "title:" in frontmatter
    assert 'timestamp: "2026-08-17T00:00:00Z"' in frontmatter
    assert "resource:" in frontmatter


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_resource_matches_file_location(relpath):
    frontmatter, _ = split_frontmatter(read(relpath))
    match = re.search(r'resource:\s*"([^"]+)"', frontmatter)
    assert match
    assert match.group(1) == f"file:///{relpath}"


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_learning_objectives_and_checklist(relpath):
    content = read(relpath)
    assert "Objektif Pembelajaran" in content
    assert "Senarai Semak Kompetensi" in content
    # Checklist items should be unchecked task-list items.
    assert re.search(r"^- \[ \] ", content, re.MULTILINE), (
        f"{relpath} should contain at least one unchecked checklist item."
    )


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_security_governance_section(relpath):
    content = read(relpath)
    assert "Pematuhan Keselamatan JDN / MAMPU" in content
    assert "ISO/IEC 27001" in content


@pytest.mark.parametrize("relpath", MANUAL_NODES)
def test_manual_node_has_sovereign_footer_dated_2026_08_17(relpath):
    content = read(relpath).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content
    assert "Notis Perundangan" in content


def test_cu01_wa05_manual_node_covers_apt_dnf5_flatpak_snap_and_nvidia():
    content = read(MANUAL_NODES[0])
    for keyword in [
        "APT", "DNF5", "Flatpak", "Snap", "NVIDIA",
        "ubuntu-drivers", "akmod-nvidia", "gpgcheck=1",
    ]:
        assert keyword in content, f"cu01-wa05 manual node should mention '{keyword}'."


def test_cu01_wa06_manual_node_covers_nmcli_static_dhcp_wifi_dns():
    content = read(MANUAL_NODES[1])
    for keyword in [
        "nmcli", "Pejabat-Statik",
        "ipv4.method manual", "ipv4.method auto", "nmcli device wifi connect",
        "resolvectl", "dig www.jdn.gov.my",
    ]:
        assert keyword in content, f"cu01-wa06 manual node should mention '{keyword}'."


def test_cu02_storage_manual_node_covers_gpt_lvm_fs_and_luks2():
    content = read(MANUAL_NODES[2])
    for keyword in [
        "gdisk", "parted", "pvcreate", "vgcreate", "lvcreate", "lvextend",
        "mkfs.ext4", "mkfs.xfs", "mkfs.btrfs", "/etc/fstab", "cryptsetup luksFormat",
        "LUKS2",
    ]:
        assert keyword in content, f"cu02 storage manual node should mention '{keyword}'."


def test_cu01_wa05_manual_node_numbered_sections_present():
    content = read(MANUAL_NODES[0])
    for n in range(1, 4):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu01-wa05 manual node should have numbered section {n}."
        )


def test_cu01_wa06_manual_node_numbered_sections_present():
    content = read(MANUAL_NODES[1])
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu01-wa06 manual node should have numbered section {n}."
        )


def test_cu02_storage_manual_node_numbered_sections_present():
    content = read(MANUAL_NODES[2])
    for n in range(1, 6):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu02 storage manual node should have numbered section {n}."
        )


# ---------------------------------------------------------------------------
# openwiki/topic-01-linux-desktop-and-basics.md
# ---------------------------------------------------------------------------

OPENWIKI_TOPIC_01 = "openwiki/topic-01-linux-desktop-and-basics.md"


def test_openwiki_topic01_has_ten_numbered_syllabus_sections():
    content = read(OPENWIKI_TOPIC_01)
    for n in range(1, 11):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"Expected numbered section heading '### {n}. ...' in syllabus."
        )
    # No stray 11th section should exist.
    assert not re.search(r"^### 11\. ", content, re.MULTILINE)


def test_openwiki_topic01_section_7_is_wa05_and_section_8_is_wa06():
    content = read(OPENWIKI_TOPIC_01)
    assert "### 7. Pemasangan Aplikasi & Pemacu Peranti Linux (CU01-WA05)" in content
    assert "### 8. Konfigurasi Sambungan Rangkaian Endpoint (CU01-WA06)" in content


def test_openwiki_topic01_hardening_and_faq_renumbered_to_9_and_10():
    content = read(OPENWIKI_TOPIC_01)
    assert "### 9. Tugasan Pasca-Pemasangan & Hardening" in content
    assert "### 10. Soal Jawab (FAQ) & Direktori Perisian Alternatif" in content
    # The old numbering for these sections should no longer exist.
    assert "### 7. Tugasan Pasca-Pemasangan" not in content
    assert "### 8. Soal Jawab (FAQ)" not in content


@pytest.mark.parametrize(
    "expected_link",
    [
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md",
        "manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md",
    ],
)
def test_openwiki_topic01_links_to_new_wa_nodes(expected_link):
    content = read(OPENWIKI_TOPIC_01)
    assert expected_link in content


def test_openwiki_topic01_noss_mapping_table_includes_wa05_and_wa06():
    content = read(OPENWIKI_TOPIC_01)
    assert "CU01-WA05" in content
    assert "CU01-WA06" in content
    assert (
        ".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md"
        in content
    )
    assert (
        ".agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md" in content
    )


# ---------------------------------------------------------------------------
# openwiki/topic-02-storage-and-virtualisation.md
# ---------------------------------------------------------------------------

OPENWIKI_TOPIC_02 = "openwiki/topic-02-storage-and-virtualisation.md"


def test_openwiki_topic02_exists_with_okf_frontmatter():
    content = read(OPENWIKI_TOPIC_02)
    frontmatter, _ = split_frontmatter(content)
    assert "okf_version: 0.1" in frontmatter
    assert "type: documentation" in frontmatter
    assert 'timestamp: "2026-08-17T00:00:00Z"' in frontmatter
    assert "cu02" in frontmatter.lower()


def test_openwiki_topic02_has_five_numbered_syllabus_sections():
    content = read(OPENWIKI_TOPIC_02)
    for n in range(1, 6):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE)


def test_openwiki_topic02_links_to_cu02_storage_manual_node():
    content = read(OPENWIKI_TOPIC_02)
    assert "manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md" in content


def test_openwiki_topic02_noss_mapping_table_includes_cu02_wa01():
    content = read(OPENWIKI_TOPIC_02)
    assert "CU02-WA01" in content
    assert (
        ".agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md"
        in content
    )


def test_openwiki_topic02_covers_gpt_lvm2_filesystems_and_luks2():
    content = read(OPENWIKI_TOPIC_02)
    for keyword in ["GPT", "LVM2", "EXT4", "XFS", "Btrfs", "LUKS2", "KVM"]:
        assert keyword in content, f"topic-02 syllabus should mention '{keyword}'."


# ---------------------------------------------------------------------------
# Rebuilt static HTML pages
# ---------------------------------------------------------------------------

HTML_MANUAL_PAGES = {
    "html/manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html": {
        "title": "CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali NOSS CU01-WA05 bagi pengurusan pakej perisian "
            "(APT, DNF, Flatpak, Snap) dan pemasangan pemacu peranti "
            "GPU/pemacu proprietari di Linux."
        ),
        "h1_id": "cu01-wa05-pemasangan-aplikasi-pemacu-peranti-linux",
        "header_topic": "CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux",
    },
    "html/manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.html": {
        "title": "CU01-WA06: Konfigurasi Sambungan Rangkaian Endpoint Linux - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali NOSS CU01-WA06 bagi konfigurasi NetworkManager, "
            "IP statik, DHCP, Wi-Fi, dan DNS pada sistem endpoint Linux."
        ),
        "h1_id": "cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint-linux",
        "header_topic": "CU01-WA06: Konfigurasi Sambungan Rangkaian Endpoint Linux",
    },
    "html/manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.html": {
        "title": "CU02: Pengurusan Storan, Partisi GPT, LVM2 & Sistem Fail Linux - NOSS Linux Malaysia (DSOM)",
        "description": (
            "Panduan amali komprehesif bagi pengurusan storan fizikal dan "
            "logikal, jadual partisi GPT, LVM2 (PV/VG/LV), sistem fail "
            "EXT4/XFS/Btrfs, /etc/fstab, dan penyulitan LUKS2 mengikut NOSS CU02."
        ),
        "h1_id": "cu02-pengurusan-storan-partisi-gpt-lvm2-sistem-fail-linux",
        "header_topic": "CU02: Pengurusan Storan, Partisi GPT, LVM2 & Sistem Fail Linux",
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
    assert expected["header_topic"] in content
    # The header topic span must appear inside the dedicated header-topic component.
    idx = content.find('data-md-component="header-topic"')
    assert idx != -1, f"{relpath} missing header-topic component."
    snippet = content[idx: idx + 400]
    assert expected["header_topic"] in snippet


def test_html_openwiki_topic01_nav_has_renumbered_sections():
    content = read("html/openwiki/topic-01-linux-desktop-and-basics.html")
    assert 'href="#7-pemasangan-aplikasi-pemacu-peranti-linux-cu01-wa05"' in content
    assert 'href="#8-konfigurasi-sambungan-rangkaian-endpoint-cu01-wa06"' in content
    assert 'href="#9-tugasan-pasca-pemasangan-hardening"' in content
    assert 'href="#10-soal-jawab-faq-direktori-perisian-alternatif"' in content


def test_html_openwiki_topic02_exists_and_has_expected_title():
    content = read("html/openwiki/topic-02-storage-and-virtualisation.html")
    assert (
        "<title>Topik 2: Pengurusan Storan, Partisi & Pengmayaan (CU02) "
        "\u2014 Dikemaskini 2026 - NOSS Linux Malaysia (DSOM)</title>" in content
    )
    assert '<h1 id="topik-2-pengurusan-storan-pengmayaan-cu02">' in content


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


@pytest.mark.parametrize(
    "location,expected_title",
    [
        (
            "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html",
            "CU01-WA05: Pemasangan Aplikasi &amp; Pemacu Peranti Linux",
        ),
        (
            "manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.html",
            "CU01-WA06: Konfigurasi Sambungan Rangkaian Endpoint Linux",
        ),
        (
            "manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.html",
            "CU02: Pengurusan Storan, Partisi GPT, LVM2 &amp; Sistem Fail Linux",
        ),
    ],
)
def test_search_index_contains_updated_manual_page_titles(search_index, location, expected_title):
    matches = [doc for doc in search_index["docs"] if doc["location"] == location]
    assert matches, f"Expected search index entry for location {location!r}."
    assert matches[0]["title"] == expected_title


def test_search_index_contains_new_skill_reference_entries(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    assert "docs/reference/skills/cu01-wa05-install-computer-applications-and-device-drivers.html" in locations
    assert "docs/reference/skills/cu01-wa06-configure-endpoint-network-connectivity.html" in locations


def test_search_index_contains_topic01_renumbered_section_anchors(search_index):
    locations = {doc["location"] for doc in search_index["docs"]}
    assert (
        "openwiki/topic-01-linux-desktop-and-basics.html#7-pemasangan-aplikasi-pemacu-peranti-linux-cu01-wa05"
        in locations
    )
    assert (
        "openwiki/topic-01-linux-desktop-and-basics.html#8-konfigurasi-sambungan-rangkaian-endpoint-cu01-wa06"
        in locations
    )