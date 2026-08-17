"""Ujian pengesahan bagi Migrasi Bab 7: Penyunting Teks Terminal (Vim/Neovim, Nano),
Pemboleh Ubah Persekitaran ($EDITOR/$VISUAL), Penyuntingan Selamat (sudoedit/visudo),
serta Kandungan Analisis Anomali & RCA.

Merangkumi:
  - manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md
  - manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
  - manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md
  - openwiki/topic-06-troubleshooting-and-logs.md
  - openwiki/topic-01-linux-desktop-and-basics.md
  - .agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def extract_frontmatter(content):
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert match, "Jangkaan blok YAML frontmatter dibatasi oleh tanda '---'"
    return match.group(1)

def frontmatter_field(content, field):
    fm = extract_frontmatter(content)
    match = re.search(rf'^{field}:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    assert match, f"Medan frontmatter '{field}' tidak dijumpai"
    return match.group(1).strip()


def test_manual_cu06_wa07_editor_and_safe_editing_concepts():
    content = read("manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md")
    assert "Vim" in content or "vim" in content
    assert "Neovim" in content or "nvim" in content
    assert "Nano" in content or "nano" in content
    assert "%s/" in content  # Regex search & replace
    assert ".nanorc" in content
    assert "sudoedit" in content
    assert "visudo" in content
    assert "visudo -c" in content


def test_manual_cu01_wa05_editor_env_vars():
    content = read("manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md")
    assert "export EDITOR=/usr/bin/vim" in content
    assert "export VISUAL=/usr/bin/vim" in content
    assert "/etc/environment" in content
    assert "~/.bashrc" in content


def test_manual_cu03_wa04_editor_env_vars():
    content = read("manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md")
    assert "export EDITOR=/usr/bin/vim" in content
    assert "export VISUAL=/usr/bin/vim" in content
    assert "/etc/profile.d/editor.sh" in content


def test_openwiki_topics_editor_mentions():
    content01 = read("openwiki/topic-01-linux-desktop-and-basics.md")
    assert "$EDITOR" in content01
    assert "$VISUAL" in content01

    content06 = read("openwiki/topic-06-troubleshooting-and-logs.md")
    assert "Vim" in content06
    assert "Nano" in content06
    assert "sudoedit" in content06
    assert "visudo" in content06


def test_skill_cu06_wa07_editor_enhancements():
    content = read(".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md")
    assert "type: skill" in content
    assert "export EDITOR=/usr/bin/vim" in content
    assert "sudoedit" in content
    assert "visudo -c" in content
    assert "%s/" in content
