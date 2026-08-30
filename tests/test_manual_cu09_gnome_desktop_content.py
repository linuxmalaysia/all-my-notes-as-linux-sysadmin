"""Ujian pengesahan bagi Migrasi Bab 9: Persekitaran Meja GNOME (GNOME 48/47), Pengurus Fail Nautilus,
Pengurusan Perisian GUI (Synaptic, GNOME Software), Pengompilan Tarball (.tar.gz),
serta Komponen Panel & Ruang Kerja (Workspace Switcher).

Merangkumi:
  - manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md
  - manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
  - openwiki/topic-01-linux-desktop-and-basics.md
  - .agents/skills/cu01-wa04-install-computer-desktop-operating-systems/SKILL.md
  - .agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """Baca fail relatif daripada punca repositori menjadi rentetan.

    Args:
        relative_path (str): Laluan relatif daripada punca repositori.

    Returns:
        str: Kandungan rentetan fail UTF-8.
    """
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")


def test_manual_cu01_wa04_gnome_desktop_concepts():
    content = read("manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md")
    assert "GNOME" in content
    assert "Nautilus" in content
    assert "Workspace Switcher" in content or "ruang kerja" in content
    assert "nautilus" in content
    assert "gnome-control-center" in content
    assert "Log Out" in content
    assert "Power Off" in content
    assert "LUKS2" in content
    assert "cryptsetup luksDump" in content
    assert "cryptsetup luksAddKey" in content
    assert "Screen Lock" in content or "kunci skrin" in content.lower()
    assert "Unprivileged User" in content or "pengguna biasa" in content.lower()


def test_manual_cu01_wa05_gui_package_tools_and_tarball():
    content = read("manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md")
    assert "GNOME Software" in content
    assert "Synaptic" in content or "synaptic" in content
    assert ".tar.gz" in content
    assert "./configure" in content
    assert "make -j" in content
    assert "make install" in content


def test_openwiki_topic01_gnome_mentions():
    content = read("openwiki/topic-01-linux-desktop-and-basics.md")
    assert "GNOME" in content
    assert "Nautilus" in content
    assert "Synaptic" in content
    assert "GNOME Software" in content
    assert "Tarball" in content


def test_skill_cu01_wa04_gnome_enhancements():
    content = read(".agents/skills/cu01-wa04-install-computer-desktop-operating-systems/SKILL.md")
    assert "GNOME" in content
    assert "nautilus" in content
    assert "gnome-control-center" in content or "gsettings" in content


def test_skill_cu01_wa05_tarball_and_gui_enhancements():
    content = read(".agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md")
    assert "Synaptic" in content or "synaptic" in content
    assert "GNOME Software" in content or "gnome-software" in content
    assert "./configure" in content
    assert "make install" in content
