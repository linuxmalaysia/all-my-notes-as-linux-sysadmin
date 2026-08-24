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
    assert "rpmkeys --checksig" in content
    assert "rpm -Uvh" in content
    assert "rpm -qi" in content
    assert "rpm -V" in content
    assert "--rebuilddb" in content
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
    assert "rpmbuild --rebuild" in content01
    assert "akmod-nvidia" in content01

    content01_html = read("html/openwiki/topic-01-linux-desktop-and-basics.html")
    assert "RPM" in content01_html
    assert "DEB" in content01_html

    content05 = read("openwiki/topic-05-linux-security.md")
    assert "unattended-upgrades" in content05
    assert "dnf-automatic" in content05
    assert re.search(r"\brpm -V\b", content05)


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
