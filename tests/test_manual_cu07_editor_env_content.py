"""Tests for Chapter 7 Migration: Terminal Editors (Vim/Neovim, Nano), Environment Variables ($EDITOR/$VISUAL),
Safe Editing (sudoedit/visudo), and RCA / Anomaly Analysis Content.

Covers:
  - manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md
  - manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
  - manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md
  - openwiki/topic-06-troubleshooting-and-logs.md
  - openwiki/topic-01-linux-desktop-and-basics.md
  - .agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md
"""

  - .agents/skills/index.md (Master Palace Registry row for cu06-wa07)
  - html/manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html
  - html/manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html
  - html/manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html
  - html/openwiki/topic-01-linux-desktop-and-basics.html
  - html/openwiki/topic-06-troubleshooting-and-logs.html
  - html/search/search_index.json
  - llms.txt / llms-full.txt / llms_context.xml (aggregated knowledge base exports)
"""

import json
import re
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def read(relative_path):
    """
    Read a repository file as UTF-8 text.
    
    Parameters:
    	relative_path: Path to the file relative to the repository root.
    
    Returns:
    	str: The file contents.
    """
    path = REPO_ROOT / relative_path
    return path.read_text(encoding="utf-8-sig")

def extract_frontmatter(content):
    """
    Extract the YAML frontmatter content from a document.
    
    Parameters:
    	content (str): Document text beginning with YAML frontmatter delimited by `---` markers.
    
    Returns:
    	str: The text between the opening and closing frontmatter delimiters.
    
    Raises:
    	AssertionError: If the document does not contain frontmatter with the expected delimiters.
    """
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert match, "Expected YAML frontmatter delimited by '---' markers"
    return match.group(1)

def frontmatter_field(content, field):
    """
    Retrieve a named field value from YAML frontmatter.
    
    Parameters:
    	content (str): Text containing the frontmatter.
    	field (str): Name of the frontmatter field to retrieve.
    
    Returns:
    	str: The trimmed value of the specified field.
    
    Raises:
    	AssertionError: If the specified field is not present in the frontmatter.
    """
    fm = extract_frontmatter(content)
    match = re.search(rf'^{field}:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
    assert match, f"Frontmatter field '{field}' not found"
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


# ---------------------------------------------------------------------------
# .agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md
# (Deeper frontmatter / structural checks)
# ---------------------------------------------------------------------------

SKILL_CU06_WA07 = ".agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md"


def test_skill_cu06_wa07_frontmatter_topics_and_tags_expanded():
    fm = extract_frontmatter(read(SKILL_CU06_WA07))
    topics_line = re.search(r"^topics:.*$", fm, re.MULTILINE)
    tags_line = re.search(r"^tags:.*$", fm, re.MULTILINE)
    assert topics_line, "SKILL.md frontmatter is missing a 'topics' field."
    assert tags_line, "SKILL.md frontmatter is missing a 'tags' field."
    for keyword in ["vim", "neovim", "nano", "sudoedit", "visudo", "editor"]:
        assert keyword in topics_line.group(0), f"'{keyword}' should be listed in SKILL.md topics"
        assert keyword in tags_line.group(0), f"'{keyword}' should be listed in SKILL.md tags"


def test_skill_cu06_wa07_frontmatter_description_mentions_new_capabilities():
    content = read(SKILL_CU06_WA07)
    description = frontmatter_field(content, "description")
    assert "Vim regex %s/old/new/g" in description
    assert "$EDITOR/$VISUAL" in description
    assert "sudoedit/visudo" in description


def test_skill_cu06_wa07_resource_matches_file_location():
    content = read(SKILL_CU06_WA07)
    resource = frontmatter_field(content, "resource")
    assert resource == f"file:///{SKILL_CU06_WA07}"


def test_skill_cu06_wa07_has_four_numbered_procedure_sections():
    content = read(SKILL_CU06_WA07)
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"SKILL.md should have numbered procedure section {n}."
        )
    assert not re.search(r"^### 5\. ", content, re.MULTILINE)


def test_skill_cu06_wa07_terminal_editing_section_commands():
    content = read(SKILL_CU06_WA07)
    assert "### 3. Terminal Text Editing & Safe System Modifications" in content
    assert "export VISUAL=/usr/bin/vim" in content
    assert "# 2. Vim Regex Search & Replace (%s/pattern/replace/g)" in content
    assert ":%s/temp/tmp/g" in content
    assert "sudoedit /etc/netplan/01-netcfg.yaml" in content
    assert "sudo visudo -c" in content


def test_skill_cu06_wa07_rca_report_structure_items():
    content = read(SKILL_CU06_WA07)
    assert "### 4. Root Cause Analysis (RCA) Report Structure" in content
    for item in [
        "**Incident Summary**",
        "**Chronology**",
        "**Root Cause**",
        "**Remediation**",
        "**Prevention**",
    ]:
        assert item in content, f"SKILL.md RCA structure should mention {item}."


def test_skill_cu06_wa07_has_sovereign_footer_dated_2026_08_17():
    content = read(SKILL_CU06_WA07).strip()
    assert "Harisfazillah Jamel" in content
    assert "2026-08-17" in content
    assert "Notis Perundangan" in content


# ---------------------------------------------------------------------------
# .agents/skills/index.md (Master Palace Registry row for cu06-wa07)
# ---------------------------------------------------------------------------

SKILLS_INDEX = ".agents/skills/index.md"


def test_skills_index_cu06_wa07_row_has_updated_description():
    content = read(SKILLS_INDEX)
    expected_fragment = (
        "Executes NOSS Work Activity CU06-WA07 - Resolve System Anomalies and "
        "Document RCA using text filters (grep, sed, awk, cut, sort, uniq), "
        "I/O redirection, terminal editors (Vim regex %s/old/new/g, Nano), "
        "environment variables ($EDITOR/$VISUAL), safe editing (sudoedit/visudo), "
        "and RCA reporting."
    )
    assert expected_fragment in content


def test_skills_index_cu06_wa07_row_has_updated_topics():
    content = read(SKILLS_INDEX)
    row_match = re.search(r"\*\*`cu06-wa07-resolve-system-anomalies-and-document-rca[^\n]*\n", content)
    assert row_match, "Expected a registry row referencing 'cu06-wa07-resolve-system-anomalies-and-document-rca'."
    row = row_match.group(0)
    for keyword in ["vim", "neovim", "nano", "sudoedit", "visudo", "editor", "rca"]:
        assert keyword in row, f"Registry row for cu06-wa07 should list topic '{keyword}'."


def test_skills_index_cu06_wa07_row_no_longer_placeholder():
    content = read(SKILLS_INDEX)
    row_match = re.search(r"\*\*`cu06-wa07-resolve-system-anomalies-and-document-rca[^\n]*\n", content)
    assert row_match
    assert "No description provided." not in row_match.group(0)


def test_skills_index_timestamp_updated_and_valid():
    frontmatter = extract_frontmatter(read(SKILLS_INDEX))
    match = re.search(r'timestamp:\s*"([^"]+)"', frontmatter)
    assert match, "Master Palace Registry is missing a timestamp field."
    assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", match.group(1))


# ---------------------------------------------------------------------------
# manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md
# (Deeper structural checks for the new environment-variable section)
# ---------------------------------------------------------------------------

MANUAL_CU01_WA05 = "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"


def test_manual_cu01_wa05_has_four_numbered_sections_after_insertion():
    content = read(MANUAL_CU01_WA05)
    for n in range(1, 5):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu01-wa05 manual node should have numbered section {n}."
        )
    assert not re.search(r"^### 5\. ", content, re.MULTILINE)


def test_manual_cu01_wa05_editor_section_is_section_3_and_drivers_pushed_to_4():
    content = read(MANUAL_CU01_WA05)
    assert "### 3. Konfigurasi Pemboleh Ubah Persekitaran `$EDITOR` & `$VISUAL`" in content
    assert (
        "### 4. Pengesanan & Pemasangan Pemacu Peranti (GPU & Rangkaian Tanpa Wayar)"
        in content
    )


def test_manual_cu01_wa05_bashrc_and_global_profile_subsections():
    content = read(MANUAL_CU01_WA05)
    assert "#### A. Konfigurasi Persekitaran Pengguna Indivdu (`~/.bashrc`)" in content
    assert (
        "#### B. Konfigurasi Persekitaran Sistem Global (`/etc/environment` & `/etc/profile.d/editor.sh`)"
        in content
    )
    assert "sudo tee /etc/profile.d/editor.sh << 'EOF'" in content
    assert "sudo chmod +x /etc/profile.d/editor.sh" in content
    assert "source ~/.bashrc" in content
    assert "echo $EDITOR" in content
    assert "echo $VISUAL" in content


def test_manual_cu01_wa05_learning_objectives_mention_shell_env_vars():
    content = read(MANUAL_CU01_WA05)
    assert (
        "Menguruskan pemboleh ubah persekitaran shell pengguna dan sistem "
        "(`$EDITOR`, `$VISUAL`, `/etc/environment`, `~/.bashrc`)."
    ) in content


def test_manual_cu01_wa05_checklist_and_ai_prompt_mention_editor_vars():
    content = read(MANUAL_CU01_WA05)
    assert (
        "- [ ] Berjaya menetapkan pemboleh ubah persekitaran `$EDITOR` dan "
        "`$VISUAL` dalam `~/.bashrc` dan `/etc/environment`."
    ) in content
    assert (
        '"Apakah perbezaan antara pemboleh ubah persekitaran $EDITOR dan '
        '$VISUAL mengikut standard POSIX dan utiliti Linux?"'
    ) in content


def test_manual_cu01_wa05_apt_and_dnf_install_vim_and_nano():
    content = read(MANUAL_CU01_WA05)
    assert "sudo apt install -y curl git vlc vim nano" in content
    assert "sudo dnf install -y htop wget vim nano" in content


# ---------------------------------------------------------------------------
# manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md
# (Deeper structural checks for the new environment-variable section)
# ---------------------------------------------------------------------------

MANUAL_CU03_WA04 = "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md"


def test_manual_cu03_wa04_has_seven_numbered_sections_after_insertion():
    content = read(MANUAL_CU03_WA04)
    for n in range(1, 8):
        assert re.search(rf"^### {n}\. ", content, re.MULTILINE), (
            f"cu03-wa04 manual node should have numbered section {n}."
        )
    assert not re.search(r"^### 8\. ", content, re.MULTILINE)


def test_manual_cu03_wa04_editor_section_is_section_5_and_time_sync_pushed_to_6_and_7():
    content = read(MANUAL_CU03_WA04)
    assert (
        "### 5. Penyesuaian Pemboleh Ubah Persekitaran Shell Pentadbiran "
        "(`$EDITOR` & `$VISUAL`)"
    ) in content
    assert (
        "### 6. Konfigurasi Zon Masa & Penyegerakan Masa (`timedatectl` & `chrony`)"
        in content
    )
    assert "### 7. Bantuan Dokumentasi & Navigasi Sistem Linux" in content


def test_manual_cu03_wa04_editor_dependent_admin_tools_mentioned():
    content = read(MANUAL_CU03_WA04)
    assert (
        "alatan CLI seperti `systemctl edit`, `visudo`, dan `crontab -e` "
        "bergantung secara automatik kepada pemboleh ubah persekitaran "
        "`$EDITOR` dan `$VISUAL`."
    ) in content
    assert "sudo systemctl edit myapp.service" in content


def test_manual_cu03_wa04_checklist_and_prerequisites_mention_editor_vars():
    content = read(MANUAL_CU03_WA04)
    assert (
        "- [ ] Berjaya mengkonfigurasi pemboleh ubah `$EDITOR` dan `$VISUAL` "
        "bagi perkhidmatan pentadbiran pelayan."
    ) in content
    assert "Pakej perisian terpasang: `systemd`, `chrony`, `man-db`, `plocate`, `vim`, `nano`." in content


def test_manual_cu03_wa04_ai_prompt_mentions_editor_and_systemctl_edit():
    content = read(MANUAL_CU03_WA04)
    assert (
        '"Bagaimanakah pemboleh ubah persekitaran $EDITOR mempengaruhi '
        'tingkah laku arahan systemctl edit dan visudo?"'
    ) in content


# ---------------------------------------------------------------------------
# manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md
# (Deeper structural checks for Nano / Vim / sudoedit / visudo content)
# ---------------------------------------------------------------------------

MANUAL_CU06_WA07 = "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md"


def test_manual_cu06_wa07_section_3_subsections_a_b_c():
    content = read(MANUAL_CU06_WA07)
    assert "### 3. Penyuntingan Fail Konfigurasi Terminal CLI & Amalan Keselamatan" in content
    assert "#### A. GNU Nano (Penyunting Teks Mudah & Pantas)" in content
    assert "#### B. Vim / Neovim (Penyunting Teks Terminal Lanjutan Pentadbir Sistem)" in content
    assert (
        "#### C. Amalan Keselamatan Penyuntingan Fail Konfigurasi Sistem "
        "(`sudoedit` & `visudo`)"
    ) in content


def test_manual_cu06_wa07_nano_keyboard_shortcuts_and_nanorc():
    content = read(MANUAL_CU06_WA07)
    for shortcut in [
        "`Ctrl + O`: Menyimpan fail (*WriteOut*).",
        "`Ctrl + X`: Keluar dari editor.",
        "`Ctrl + W`: Carian teks (*Where Is*).",
        "`Ctrl + \\`: Carian dan penggantian teks (*Replace*).",
        "`Ctrl + K`: Memotong (*cut*) baris semasa.",
        "`Ctrl + U`: Menampal (*uncut*) baris.",
    ]:
        assert shortcut in content, f"Nano section should document shortcut: {shortcut!r}"
    assert "set linenumbers" in content
    assert "set tabstospaces" in content
    assert 'include "/usr/share/nano/*.nanorc"' in content


def test_manual_cu06_wa07_vim_modes_and_navigation():
    content = read(MANUAL_CU06_WA07)
    assert "**4 Mod Operasi Utama Vim**" in content
    assert "**Mod Arahan / Normalkan (Command / Normal Mode)**" in content
    assert "**Mod Sisipan (Insert Mode)**" in content
    assert "**Mod Visual (Visual Mode)**" in content
    assert "**Mod Ex / Terakhir (Ex / Command-line Mode)**" in content
    assert "`dd` (padam/potong satu baris)" in content
    assert "`:wq` atau `:x` (simpan dan keluar)" in content


def test_manual_cu06_wa07_vim_regex_search_and_replace_examples():
    content = read(MANUAL_CU06_WA07)
    assert "`%s/corak_asal/teks_baharu/g`" in content
    assert ":%s/temp/tmp/g" in content
    assert ":%s/Port 22/Port 2222/gc" in content


def test_manual_cu06_wa07_vim_macro_recording_and_playback():
    content = read(MANUAL_CU06_WA07)
    assert "**Perekaman & Pelaksanaan Makro Vim**" in content
    assert "`qa`: Mula merekod makro ke dalam daftar `a`." in content
    assert "`q`: Hentikan rakaman." in content
    assert "`@a`: Jalankan makro dalam daftar `a`." in content
    assert "`5@a`: Jalankan makro sebanyak 5 kali berturut-turut." in content


def test_manual_cu06_wa07_sudoedit_and_visudo_usage_examples():
    content = read(MANUAL_CU06_WA07)
    assert "**Menggunakan `sudoedit` (`sudo -e`)**" in content
    assert "sudoedit /etc/netplan/01-netcfg.yaml" in content
    assert "**Menggunakan `visudo` untuk Pengurusan Sudoers**" in content
    assert "sudo visudo\n" in content
    assert "sudo visudo -c" in content


def test_manual_cu06_wa07_checklist_mentions_editor_modes_and_safe_editing():
    content = read(MANUAL_CU06_WA07)
    assert (
        "- [ ] Berjaya menyunting fail konfigurasi sistem menggunakan "
        "`vim` / `nvim` (mod operasi, regex `%s/old/new/g`, makro) dan "
        "`nano` (`.nanorc`)."
    ) in content
    assert (
        "- [ ] Berjaya mengamalkan penyuntingan selamat sistem menggunakan "
        "`sudoedit` dan `visudo`."
    ) in content


def test_manual_cu06_wa07_ai_prompts_mention_sudoedit_least_privilege():
    content = read(MANUAL_CU06_WA07)
    assert (
        '"Mengapakah penggunaan sudoedit lebih selamat berbanding sudo vim '
        'dari sudut prinsip keselamatan paling kurang keistimewaan '
        '(least privilege)?"'
    ) in content


def test_manual_cu06_wa07_frontmatter_topics_and_tags():
    fm = extract_frontmatter(read(MANUAL_CU06_WA07))
    topics_line = re.search(r"^topics:.*$", fm, re.MULTILINE)
    tags_line = re.search(r"^tags:.*$", fm, re.MULTILINE)
    assert topics_line, "cu06-wa07 manual node frontmatter is missing a 'topics' field."
    assert tags_line, "cu06-wa07 manual node frontmatter is missing a 'tags' field."
    for keyword in ["vim", "neovim", "nano", "sudoedit", "visudo"]:
        assert keyword in topics_line.group(0)
        assert keyword in tags_line.group(0)


# ---------------------------------------------------------------------------
# openwiki/topic-01-linux-desktop-and-basics.md /
# openwiki/topic-06-troubleshooting-and-logs.md (deeper checks)
# ---------------------------------------------------------------------------

OPENWIKI_TOPIC_01_MD = "openwiki/topic-01-linux-desktop-and-basics.md"
OPENWIKI_TOPIC_06_MD = "openwiki/topic-06-troubleshooting-and-logs.md"


def test_openwiki_topic01_section7_covers_shell_env_vars():
    content = read(OPENWIKI_TOPIC_01_MD)
    assert (
        "### 7. Pemasangan Aplikasi, Pemacu Peranti & Persekitaran Shell (CU01-WA05)"
        in content
    )
    assert (
        "Penyesuaian pemboleh ubah persekitaran shell (`$EDITOR`, `$VISUAL`, "
        "`/etc/environment`, `~/.bashrc`)"
    ) in content


def test_openwiki_topic01_overview_paragraph_mentions_editor_vars():
    content = read(OPENWIKI_TOPIC_01_MD)
    assert "penyesuaian pemboleh ubah persekitaran shell ($EDITOR/$VISUAL)" in content


def test_openwiki_topic06_silibus_mentions_editors_and_safe_editing():
    content = read(OPENWIKI_TOPIC_06_MD)
    assert (
        "Pemprosesan Teks Aluran, Penyunting CLI & Amalan Keselamatan "
        "(Text Filters, CLI Editors & Security)"
    ) in content
    assert (
        "Penyunting teks CLI pentadbiran: **Vim / Neovim** (mod "
        "Normal/Insert/Visual/Ex, regex search/replace `%s/old/new/g`, "
        "makro) dan **GNU Nano** (`.nanorc`)."
    ) in content
    assert (
        "Penyuntingan selamat fail konfigurasi sistem: `sudoedit` "
        "(`sudo -e`), `visudo`, dan semakan sintaks `visudo -c`."
    ) in content


def test_openwiki_topic06_ai_prompt_replaced_with_sudoedit_question():
    content = read(OPENWIKI_TOPIC_06_MD)
    assert (
        '"Apakah kelebihan keselamatan menggunakan sudoedit berbanding '
        'sudo vim semasa menyunting fail /etc/environment?"'
    ) in content
    # The old umount troubleshooting prompt should have been replaced.
    assert "'target is busy'" not in content


# ---------------------------------------------------------------------------
# Rebuilt static HTML manual pages: new sections / subsections
# ---------------------------------------------------------------------------

HTML_CU01_WA05 = "html/manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
HTML_CU03_WA04 = "html/manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html"
HTML_CU06_WA07 = "html/manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html"


def test_html_cu01_wa05_meta_description_mentions_editor_vars():
    content = read(HTML_CU01_WA05)
    assert (
        '<meta name="description" content="Panduan amali NOSS CU01-WA05 bagi '
        "pengurusan pakej perisian (APT, DNF, Flatpak, Snap), penyesuaian "
        "pemboleh ubah persekitaran $EDITOR/$VISUAL, dan pemasangan pemacu "
        'peranti GPU/pemacu proprietari di Linux.">'
    ) in content


def test_html_cu01_wa05_editor_section_headings_present():
    content = read(HTML_CU01_WA05)
    assert (
        '<h3 id="3-konfigurasi-pemboleh-ubah-persekitaran-editor-visual">'
        "3. Konfigurasi Pemboleh Ubah Persekitaran <code>$EDITOR</code> "
        "&amp; <code>$VISUAL</code>"
    ) in content
    assert (
        '<h4 id="a-konfigurasi-persekitaran-pengguna-indivdu-bashrc">'
        "A. Konfigurasi Persekitaran Pengguna Indivdu (<code>~/.bashrc</code>)"
    ) in content
    assert (
        '<h4 id="b-konfigurasi-persekitaran-sistem-global-etcenvironment-etcprofilededitorsh">'
        "B. Konfigurasi Persekitaran Sistem Global (<code>/etc/environment</code> "
        "&amp; <code>/etc/profile.d/editor.sh</code>)"
    ) in content


def test_html_cu01_wa05_driver_section_renumbered_to_4():
    content = read(HTML_CU01_WA05)
    assert (
        '<h3 id="4-pengesanan-pemasangan-pemacu-peranti-gpu-rangkaian-tanpa-wayar">'
        "4. Pengesanan &amp; Pemasangan Pemacu Peranti (GPU &amp; Rangkaian "
        "Tanpa Wayar)"
    ) in content
    # The old section-3 numbering for the driver detection heading should be gone.
    assert 'id="3-pengesanan-pemasangan-pemacu-peranti-gpu-rangkaian-tanpa-wayar"' not in content


def test_html_cu03_wa04_meta_description_mentions_editor_vars():
    content = read(HTML_CU03_WA04)
    assert (
        '<meta name="description" content="Panduan amali konfigurasi teras '
        "pelayan Linux, pengurusan unit perkhidmatan systemd, audit log "
        "journalctl, penyegerakan masa timedatectl/chrony, penyesuaian "
        '$EDITOR/$VISUAL, dan sistem dokumentasi man.">'
    ) in content


def test_html_cu03_wa04_editor_section_and_renumbered_sections():
    content = read(HTML_CU03_WA04)
    assert (
        '<h3 id="5-penyesuaian-pemboleh-ubah-persekitaran-shell-pentadbiran-editor-visual">'
        "5. Penyesuaian Pemboleh Ubah Persekitaran Shell Pentadbiran "
        "(<code>$EDITOR</code> &amp; <code>$VISUAL</code>)"
    ) in content
    assert (
        '<h3 id="6-konfigurasi-zon-masa-penyegerakan-masa-timedatectl-chrony">'
        "6. Konfigurasi Zon Masa &amp; Penyegerakan Masa (<code>timedatectl</code> "
        "&amp; <code>chrony</code>)"
    ) in content
    assert (
        '<h3 id="7-bantuan-dokumentasi-navigasi-sistem-linux">'
        "7. Bantuan Dokumentasi &amp; Navigasi Sistem Linux"
    ) in content


def test_html_cu06_wa07_meta_description_mentions_secure_editors():
    content = read(HTML_CU06_WA07)
    assert (
        '<meta name="description" content="Panduan amali pemprosesan teks '
        "aluran menggunakan penapis Linux (grep, sed, awk, cut, sort, "
        "uniq), pengalihan I/O dan piping, penyuntingan fail konfigurasi "
        "selamat menggunakan Vim/Neovim, GNU Nano, sudoedit/visudo, serta "
        'dokumentasi laporan RCA.">'
    ) in content


def test_html_cu06_wa07_editor_subsections_a_b_c_present():
    content = read(HTML_CU06_WA07)
    assert (
        '<h3 id="3-penyuntingan-fail-konfigurasi-terminal-cli-amalan-keselamatan">'
        "3. Penyuntingan Fail Konfigurasi Terminal CLI &amp; Amalan Keselamatan"
    ) in content
    assert (
        '<h4 id="a-gnu-nano-penyunting-teks-mudah-pantas">'
        "A. GNU Nano (Penyunting Teks Mudah &amp; Pantas)"
    ) in content
    assert (
        '<h4 id="b-vim-neovim-penyunting-teks-terminal-lanjutan-pentadbir-sistem">'
        "B. Vim / Neovim (Penyunting Teks Terminal Lanjutan Pentadbir Sistem)"
    ) in content
    assert (
        '<h4 id="c-amalan-keselamatan-penyuntingan-fail-konfigurasi-sistem-sudoedit-visudo">'
        "C. Amalan Keselamatan Penyuntingan Fail Konfigurasi Sistem "
        "(<code>sudoedit</code> &amp; <code>visudo</code>)"
    ) in content


def test_html_cu06_wa07_grep_subsection_heading_capitalised():
    """The old lowercase 'carian Corak' heading was corrected to 'Carian Corak'."""
    content = read(HTML_CU06_WA07)
    assert '<h4 id="a-carian-corak-dengan-grep-ripgrep">A. Carian Corak dengan' in content
    assert "A. carian Corak dengan" not in content


# ---------------------------------------------------------------------------
# Rebuilt static HTML openwiki pages
# ---------------------------------------------------------------------------

HTML_OPENWIKI_TOPIC_01 = "html/openwiki/topic-01-linux-desktop-and-basics.html"
HTML_OPENWIKI_TOPIC_06 = "html/openwiki/topic-06-troubleshooting-and-logs.html"


def test_html_openwiki_topic01_meta_description_mentions_editor_vars():
    content = read(HTML_OPENWIKI_TOPIC_01)
    assert (
        '<meta name="description" content="Silibus komprehensif CU01 '
        "dikemaskini dengan edaran rujukan 2026 (Ubuntu 26.04 LTS, Fedora "
        "43, AlmaLinux 10), penyulitan LUKS2, konfigurasi $EDITOR/$VISUAL, "
        'dan prosedur pemasangan NOSS Level 3.">'
    ) in content


def test_html_openwiki_topic01_section7_heading_mentions_shell_env():
    content = read(HTML_OPENWIKI_TOPIC_01)
    assert (
        '<h3 id="7-pemasangan-aplikasi-pemacu-peranti-persekitaran-shell-cu01-wa05">'
        "7. Pemasangan Aplikasi, Pemacu Peranti &amp; Persekitaran Shell (CU01-WA05)"
    ) in content


def test_html_openwiki_topic06_meta_description_mentions_editors_and_sudoedit():
    content = read(HTML_OPENWIKI_TOPIC_06)
    assert (
        '<meta name="description" content="Silibus penyelesaian masalah '
        "sistem, pelekapan storan mount/fstab, penapis teks grep/sed/awk, "
        "penyunting teks Vim/Neovim/Nano, penyuntingan selamat "
        "sudoedit/visudo, pemantauan prestasi, dan dokumentasi RCA "
        'dipetakan kepada NOSS CU06.">'
    ) in content


def test_html_openwiki_topic06_silibus_lists_secure_editing_bullet():
    content = read(HTML_OPENWIKI_TOPIC_06)
    assert (
        "Penyuntingan selamat fail konfigurasi sistem: <code>sudoedit</code> "
        "(<code>sudo -e</code>), <code>visudo</code>, dan semakan sintaks "
        "<code>visudo -c</code>."
    ) in content


# ---------------------------------------------------------------------------
# html/search/search_index.json
# ---------------------------------------------------------------------------

SEARCH_INDEX_PATH = "html/search/search_index.json"


@pytest.fixture(scope="module")
def search_index():
    with open(REPO_ROOT / SEARCH_INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _locations(search_index):
    return {doc["location"] for doc in search_index["docs"]}


@pytest.mark.parametrize(
    "anchor",
    [
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
        "#3-konfigurasi-pemboleh-ubah-persekitaran-editor-visual",
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
        "#4-pengesanan-pemasangan-pemacu-peranti-gpu-rangkaian-tanpa-wayar",
        "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html"
        "#5-penyesuaian-pemboleh-ubah-persekitaran-shell-pentadbiran-editor-visual",
        "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.html"
        "#7-bantuan-dokumentasi-navigasi-sistem-linux",
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html"
        "#3-penyuntingan-fail-konfigurasi-terminal-cli-amalan-keselamatan",
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html"
        "#b-vim-neovim-penyunting-teks-terminal-lanjutan-pentadbir-sistem",
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html"
        "#c-amalan-keselamatan-penyuntingan-fail-konfigurasi-sistem-sudoedit-visudo",
        "openwiki/topic-01-linux-desktop-and-basics.html"
        "#7-pemasangan-aplikasi-pemacu-peranti-persekitaran-shell-cu01-wa05",
    ],
)
def test_search_index_contains_new_editor_section_anchors(search_index, anchor):
    assert anchor in _locations(search_index), f"Expected search index anchor entry: {anchor!r}"


def test_search_index_no_longer_has_old_cu01_wa05_section3_anchor(search_index):
    stale_anchor = (
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.html"
        "#3-pengesanan-pemasangan-pemacu-peranti-gpu-rangkaian-tanpa-wayar"
    )
    assert stale_anchor not in _locations(search_index)


def test_search_index_cu06_wa07_page_title_updated(search_index):
    matches = [
        doc
        for doc in search_index["docs"]
        if doc["location"] == "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.html"
    ]
    assert matches
    assert matches[0]["title"] == (
        "Pemprosesan Teks Aluran, Saluran Paip, Editor CLI &amp; Analisis Punca Utama (RCA)"
    )


# ---------------------------------------------------------------------------
# llms.txt (aggregated link index) - regression check after list reordering
# ---------------------------------------------------------------------------

LLMS_TXT = "llms.txt"


@pytest.mark.parametrize(
    "expected_link",
    [
        "- [DSOM how-to guides](docs/how-to/index.md)",
        "- [DSOM reference material](docs/reference/index.md)",
        "- [DSOM tutorials](docs/tutorials/index.md)",
        "- [DSOM explanation and architecture](docs/explanation/index.md)",
    ],
)
def test_llms_txt_docs_taxonomy_links_all_present_regardless_of_order(expected_link):
    content = read(LLMS_TXT)
    assert expected_link in content


@pytest.mark.parametrize(
    "expected_link",
    [
        "- [CU01: Persediaan Sistem Komputer & Desktop Linux](manual/cu01/index.md)",
        "- [CU02: Pengurusan Storan & Infrastruktur Pemayaan](manual/cu02/index.md)",
        "- [CU03: Pentadbiran & Perkhidmatan Pelayan Linux](manual/cu03/index.md)",
        "- [CU04: Automasi, Sandaran & Pemulihan Sistem](manual/cu04/index.md)",
        "- [CU05: Kawalan Keselamatan Endpoint & Pengerasan Linux](manual/cu05/index.md)",
        "- [CU06: Sokongan Pengguna, Troubleshooting & Penyelenggaraan](manual/cu06/index.md)",
    ],
)
def test_llms_txt_cu_manual_index_links_all_present_regardless_of_order(expected_link):
    content = read(LLMS_TXT)
    assert expected_link in content


def test_llms_txt_cu06_wa07_manual_link_present():
    content = read(LLMS_TXT)
    assert (
        "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md" in content
    )


# ---------------------------------------------------------------------------
# llms-full.txt / llms_context.xml (full-content aggregated exports)
# ---------------------------------------------------------------------------

LLMS_FULL_TXT = "llms-full.txt"
LLMS_CONTEXT_XML = "llms_context.xml"


def _extract_llms_full_block(content, relpath):
    """Extract the embedded file body between the BEGIN/END FILE markers in llms-full.txt."""
    pattern = re.compile(
        rf"<!-- BEGIN FILE: {re.escape(relpath)} -->(.*?)<!-- END FILE: {re.escape(relpath)} -->",
        re.DOTALL,
    )
    match = pattern.search(content)
    assert match, f"Expected embedded file block for {relpath!r} in llms-full.txt"
    return match.group(1)


def _extract_llms_context_block(content, relpath):
    """Extract the embedded file body inside <file path="..."> in llms_context.xml."""
    pattern = re.compile(
        rf'<file path="{re.escape(relpath)}">(.*?)</file>',
        re.DOTALL,
    )
    match = pattern.search(content)
    assert match, f"Expected embedded <file> block for {relpath!r} in llms_context.xml"
    return match.group(1)


@pytest.mark.parametrize(
    "relpath",
    [
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md",
        "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md",
    ],
)
def test_llms_full_txt_embedded_manual_blocks_mention_editor_env_vars(relpath):
    content = read(LLMS_FULL_TXT)
    block = _extract_llms_full_block(content, relpath)
    assert "$EDITOR" in block or "EDITOR=" in block


@pytest.mark.parametrize(
    "relpath",
    [
        "manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md",
        "manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md",
    ],
)
def test_llms_context_xml_embedded_manual_blocks_mention_editor_env_vars(relpath):
    content = read(LLMS_CONTEXT_XML)
    block = _extract_llms_context_block(content, relpath)
    assert "$EDITOR" in block or "EDITOR=" in block


def test_llms_full_txt_cu06_wa07_block_mentions_sudoedit_and_visudo():
    content = read(LLMS_FULL_TXT)
    block = _extract_llms_full_block(
        content, "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md"
    )
    assert "sudoedit" in block
    assert "visudo" in block


def test_llms_context_xml_cu06_wa07_block_mentions_sudoedit_and_visudo():
    content = read(LLMS_CONTEXT_XML)
    block = _extract_llms_context_block(
        content, "manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md"
    )
    assert "sudoedit" in block
    assert "visudo" in block
