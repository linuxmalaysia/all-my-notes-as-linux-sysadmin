"""Ujian regresi bagi migrasi Bab 9: GNOME, Nautilus dan tarball."""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

WA04_MANUAL = "manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md"
WA05_MANUAL = "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"
TOPIC_01 = "openwiki/topic-01-linux-desktop-and-basics.md"
WA04_SKILL = (
    ".agents/skills/cu01-wa04-install-computer-desktop-operating-systems/SKILL.md"
)
WA05_SKILL = (
    ".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md"
)


def read(relative_path):
    """Baca fail UTF-8 relatif daripada punca repositori."""
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8-sig")


def frontmatter(relative_path):
    """Dapatkan blok frontmatter dan pastikan penutupnya wujud."""
    content = read(relative_path)
    assert content.startswith("---\n"), f"{relative_path} tiada frontmatter."
    parts = content.split("---", 2)
    assert len(parts) == 3, f"Frontmatter {relative_path} tidak lengkap."
    return parts[1]


def metadata_list(metadata, key):
    """Tukar nilai senarai YAML sebaris kepada set token."""
    match = re.search(rf"^{re.escape(key)}:\s*\[([^]]*)]$", metadata, re.MULTILINE)
    assert match, f"Medan senarai {key!r} tidak ditemui."
    return {item.strip().strip('"\'') for item in match.group(1).split(",")}


def assert_in_order(content, fragments):
    """Pastikan semua fragmen hadir dalam urutan aliran kerja yang ditetapkan."""
    cursor = 0
    for fragment in fragments:
        position = content.find(fragment, cursor)
        assert position >= 0, f"Fragmen tiada atau tersalah urutan: {fragment!r}"
        cursor = position + len(fragment)


@pytest.mark.parametrize(
    "relative_path",
    [WA04_MANUAL, WA05_MANUAL, TOPIC_01, WA04_SKILL, WA05_SKILL],
)
def test_changed_source_documents_exist(relative_path):
    """Semua sumber yang membentuk migrasi Bab 9 mesti kekal tersedia."""
    assert (REPO_ROOT / relative_path).is_file()


def test_wa04_manual_frontmatter_maps_the_new_gnome_scope():
    """Metadata WA04 mesti boleh ditemui melalui istilah baharu migrasi."""
    metadata = frontmatter(WA04_MANUAL)

    assert "type: knowledge-node" in metadata
    assert 'resource: "file:///manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md"' in metadata
    assert {
        "noss-linux",
        "cu01",
        "wa04",
        "gnome",
        "nautilus",
        "applet",
        "workspace",
        "luks2",
    } <= metadata_list(metadata, "topics")


def test_wa04_manual_covers_supported_desktops_and_luks_key_recovery():
    """Pemasangan desktop dan pemulihan LUKS2 ialah hasil pembelajaran WA04."""
    content = read(WA04_MANUAL)

    for expected in (
        'Ubuntu 26.04 LTS "Resolute Raccoon"',
        'AlmaLinux 10 "Purple Lion"',
        "Fedora 43",
        "GNOME 48 pada Ubuntu 26.04 LTS",
        "GNOME 47 pada AlmaLinux 10",
        "cryptsetup luksDump /dev/nvme0n1p3",
        "cryptsetup luksAddKey /dev/nvme0n1p3",
    ):
        assert expected in content


def test_wa04_manual_teaches_complete_nautilus_and_gnome_workflows():
    """Ujian sempadan: satu sebutan GNOME sahaja tidak dianggap liputan lengkap."""
    content = read(WA04_MANUAL)

    for expected in (
        "Workspace Switcher",
        "Super + PageUp/PageDown",
        "Tree View",
        "Local Files Only",
        "drag-and-drop",
        "nautilus ~",
        "nautilus admin:///etc/",
        "gnome-control-center",
        "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'",
        "gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true",
    ):
        assert expected.lower() in content.lower()


def test_wa04_manual_preserves_desktop_security_controls():
    """Kes negatif: panduan desktop tidak boleh menggalakkan sesi grafik root."""
    content = read(WA04_MANUAL)

    assert "selepas 5 minit" in content
    assert "Elakkan daripada menjalankan sesi grafik GNOME terus sebagai pengguna `root`" in content
    assert "gunakan `sudo` bagi tugas pentadbiran" in content
    assert "Log Out" in content and "Power Off" in content


def test_wa05_manual_frontmatter_maps_gui_and_tarball_scope():
    """Metadata WA05 mesti menyenaraikan kedua-dua alat GUI dan tarball."""
    metadata = frontmatter(WA05_MANUAL)

    assert "type: knowledge-node" in metadata
    assert 'resource: "file:///manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"' in metadata
    assert {"synaptic", "gnome-software", "tarball"} <= metadata_list(metadata, "topics")
    assert {"synaptic", "gnome-software", "tarball"} <= metadata_list(metadata, "tags")


def test_wa05_manual_covers_gui_installation_and_launch_commands():
    """Aliran GUI mesti menerangkan fungsi, pemasangan dan pelancaran alat."""
    content = read(WA05_MANUAL)

    for expected in (
        "GNOME Software (`gnome-software`)",
        "PackageKit",
        "gnome-software &",
        "sudo apt install -y synaptic",
        "/etc/apt/sources.list",
        "sudo synaptic &",
    ):
        assert expected in content


def test_wa05_tarball_workflow_verifies_before_extracting_and_building():
    """Regresi keselamatan: arkib mesti disahkan sebelum kodnya dieksekusi."""
    content = read(WA05_MANUAL)

    assert_in_order(
        content,
        (
            "gpg --keyring",
            "sha256sum -c sampel-aplikasi-1.0.tar.gz.sha256 || exit 1",
            "tar -zxvf sampel-aplikasi-1.0.tar.gz",
            "cat README || cat INSTALL",
            "./configure --prefix=/usr/local",
            "make -j$(nproc)",
            "sudo make install",
        ),
    )
    assert "`./configure` hanya terhad untuk projek berasaskan Autotools" in content
    assert "`sudo make install` tidak dijejak oleh pangkalan data pakej sistem" in content


@pytest.mark.parametrize(
    "relative_path,expected_topics,expected_commands",
    [
        (
            WA04_SKILL,
            {"gnome", "nautilus", "applet", "workspace"},
            {
                "cryptsetup luksFormat --type luks2",
                "cryptsetup luksAddKey",
                "nautilus ~ &",
                "gnome-control-center",
                "gsettings set org.gnome.desktop.interface",
            },
        ),
        (
            WA05_SKILL,
            {"synaptic", "gnome-software", "tarball"},
            {
                "apt install -y curl git vlc synaptic gnome-software",
                "rpmkeys --checksig",
                "tar -zxvf sample-app-1.0.tar.gz",
                "./configure --prefix=/usr/local",
                "sudo make install",
            },
        ),
    ],
)
def test_agent_skills_expose_the_migrated_topics_and_commands(
    relative_path, expected_topics, expected_commands
):
    """Kemahiran ejen mesti boleh melaksanakan skop yang diajar oleh manual."""
    metadata = frontmatter(relative_path)
    content = read(relative_path)

    assert expected_topics <= metadata_list(metadata, "topics")
    for command in expected_commands:
        assert command in content


def test_openwiki_maps_gnome_and_package_workflows_to_the_manual_and_skills():
    """Halaman sintesis mesti memautkan pembaca kepada nod dan kemahiran tepat."""
    content = read(TOPIC_01)

    for expected in (
        "GNOME 48 / 47",
        "Workspace Switcher",
        "Pengurus Fail Nautilus (GNOME Files)",
        "GNOME Software",
        "Synaptic Package Manager",
        "PackageKit",
        "./configure`, `make`, `sudo make install",
        WA04_MANUAL,
        WA05_MANUAL,
        WA04_SKILL,
        WA05_SKILL,
    ):
        assert expected in content


@pytest.mark.parametrize(
    "skill_name,expected_topics",
    [
        (
            "cu01-wa04-install-computer-desktop-operating-systems",
            {"gnome", "nautilus", "applet", "workspace"},
        ),
        (
            "cu01-wa05-install-computer-applications-and-device-drivers",
            {"synaptic", "gnome-software", "tarball"},
        ),
    ],
)
def test_skill_registry_indexes_the_new_discovery_terms(skill_name, expected_topics):
    """Istilah carian baharu mesti berada pada baris kemahiran yang betul."""
    registry = read(".agents/skills/index.md")
    row = next(line for line in registry.splitlines() if f"**`{skill_name}`**" in line)

    assert expected_topics <= {cell.strip() for cell in row.split("|")[-2].split(",")}


@pytest.mark.parametrize(
    "relative_path,expected_fragments",
    [
        (
            "html/manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.html",
            ("GNOME 48", "Workspace Switcher", "Nautilus", "gnome-control-center"),
        ),
        (
            "html/manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html",
            ("GNOME Software", "Synaptic Package Manager", "PackageKit", "sha256sum"),
        ),
        (
            "html/openwiki/topic-01-linux-desktop-and-basics.html",
            ("GNOME 48 / 47", "Nautilus", "Synaptic Package Manager", "Tarball"),
        ),
    ],
)
def test_generated_html_contains_the_migrated_content(relative_path, expected_fragments):
    """Tapak prabina tidak boleh ketinggalan daripada sumber Markdown."""
    content = read(relative_path)

    for fragment in expected_fragments:
        assert fragment in content


@pytest.mark.parametrize(
    "location,expected_tags",
    [
        (
            "manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.html",
            {"cu01", "wa04", "gnome", "nautilus", "applet", "workspace", "luks2"},
        ),
        (
            "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html",
            {"cu01", "wa05", "synaptic", "gnome-software", "tarball"},
        ),
    ],
)
def test_search_index_exposes_the_new_manual_tags(location, expected_tags):
    """Kes sempadan penemuan: halaman akar mesti mempunyai semua tag baharu."""
    search_index = json.loads(read("html/search/search_index.json"))
    matching_documents = [doc for doc in search_index["docs"] if doc["location"] == location]

    assert len(matching_documents) == 1
    assert expected_tags <= set(matching_documents[0]["tags"])


def test_llms_catalogues_use_the_new_wa04_titles():
    """Katalog LLM sumber dan HTML mesti menunjuk tajuk migrasi yang sama."""
    manual_entry = (
        "[CU01-WA04: Pemasangan OS Desktop Linux & Persekitaran Meja GNOME]"
        f"({WA04_MANUAL})"
    )
    skill_entry = (
        "[CU01-WA04: Pemasangan Sistem Operasi Linux Desktop & Persekitaran Meja GNOME]"
        f"({WA04_SKILL})"
    )

    for relative_path in ("llms.txt", "html/llms.txt"):
        content = read(relative_path)
        assert manual_entry in content
        assert skill_entry in content
