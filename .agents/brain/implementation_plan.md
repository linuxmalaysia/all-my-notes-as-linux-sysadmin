# 📐 Pelan Pelaksanaan Google Jules: Migrasi Silibus Bab 6 (Pemprosesan Teks, Sandaran & Pemampatan, Pelekapan Storan, dan Automasi ke manual/cu04/ dan manual/cu06/)

## 1. Objektif Utama Sesi Jules
Memindahkan, memodenkan, menyelidik secara mendalam (*Deep Web Research*), dan memetakan kandungan arkib manual lama **Bab 6 (`references/manual/bab_06/`)** ke dalam direktori **`manual/cu04/`** (Sandaran & Pemulihan Data/Sistem) dan **`manual/cu06/`** (Diagnostik Peranti Luaran & Analisis Log), serta mengemas kini **`openwiki/topic-04-automation-and-backup.md`** dan **`openwiki/topic-06-troubleshooting-and-logs.md`** berlandaskan piawaian **NOSS Level 3 (CU04 & CU06)**, edaran kanonik Linux 2026 (Ubuntu 26.04 LTS & AlmaLinux 10), 4 kuadran Diátaxis, dan standard keselamatan **Jabatan Digital Negara (JDN) / MAMPU** serta **ISO/IEC 27001**.

---

## 2. Garis Panduan Transformasi & Pematuhan Perlembagaan AI

### A. Kitaran Mandatori Peraturan 21 (Deep Research & CU/WA Mapping)
1. **Penilaian Silibus:**
   - `CU04-WA02`: Pelaksanaan Operasi Sandaran & Pemampatan Data (arkib `tar`, pemampat moden `gzip`, `xz`, `zstd`, penyegerakan data `rsync -avzP`, penyulitan sandaran, jadual `cron` / `systemd.timer`).
   - `CU04-WA04`: Prosedur Pemulihan Data & Integriti Sistem Fail (pengekstrakan arkib, pengesahan checksum `sha256sum`, pengesahan pemulihan bare-metal).
   - `CU06-WA04`: Pelekapan dan Troubleshooting Media Storan Luaran (`mount`, `umount`, `findmnt`, `lsblk`, pemacu NVMe/SATA/USB, `/etc/fstab` dengan pilihan selamat `nodev,nosuid,noexec`).
   - `CU06-WA07`: Pemprosesan Teks Aluran & Analisis Log Anomali (`grep` / `ripgrep`, `sed`, `awk`, `cut`, `sort`, `uniq`, pengalihan I/O `|`, `>`, `>>`, `2>&1`, `tee`, penyunting CLI `vim` / `nano`).
2. **Penyelidikan Mendalam (*Deep Web Research*):**
   - Sintaks `tar` moden dengan pemampatan pelbagai bebenang (contoh: `tar -I zstd -cvf`), `rsync --delete-after`, automasi `systemd-timer` vs `crontab`.
   - Sintaks selamat pengalihan fail: `set -o pipefail` dalam skrip Bash.
   - Pilihan pelekap keselamatan storan JDN/MAMPU: `noexec,nosuid,nodev` pada partition `/tmp`, `/dev/shm`, dan media luaran.
3. **Pengayaan Keselamatan & Prestasi:**
   - Garis panduan sandaran berperingkat 3-2-1 mengikut piawaian ISO/IEC 27001 dan JDN/MAMPU.
   - Integriti data dengan SHA-256 / GPG signing.
4. **Penyusunan Output Terstruktur:**
   - Kemas kini atau bina nod amali:
     - `manual/cu04/cu04-wa02-pelaksanaan-operasi-sandaran-sistem.md`
     - `manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md`
     - `manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md`
     - `manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md`
   - Pautkan ke `openwiki/topic-04-automation-and-backup.md` dan `openwiki/topic-06-troubleshooting-and-logs.md`.

### B. Mandat Porting Pengetahuan ke Kemahiran AI (Knowledge-to-Skill Porting)
- Naik taraf atau bina modul AI Agent Skill di bawah `.agents/skills/`:
  - `.agents/skills/cu04-wa02-execute-system-backup-operations/SKILL.md` (format `type: skill`).
  - `.agents/skills/cu04-wa04-perform-data-and-filesystem-recovery/SKILL.md` (format `type: skill`).
  - `.agents/skills/cu06-wa04-troubleshoot-external-and-storage-devices/SKILL.md` (format `type: skill`).
  - `.agents/skills/cu06-wa07-analyze-root-cause-and-audit-logs/SKILL.md` (format `type: skill`).
- Daftarkan ke Master Palace Registry (`uv run scripts/generate_palace_registry.py`).

### C. Suite Ujian Pematuhan Kualiti (Quality Gate & Test Suite)
- Tambah suite ujian unit Python: `tests/test_manual_cu04_cu06_backup_troubleshooting_content.py` bagi mengesahkan nod manual, kemahiran AI, frontmatter OKF, dan pautan openwiki.
- Sahkan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` melepasi 100% Quality Gate.

---

## 3. Langkah Operasi Langkah Demi Langkah untuk Jules

```bash
# 1. Baca arkib mentah Bab 6 (DILARANG padam mengikut Peraturan 17)
# references/manual/bab_06/part_01.md & part_02.md

# 2. Tulis & modenkan nod amali ke manual/cu04/ & manual/cu06/
# manual/cu04/cu04-wa02-pelaksanaan-operasi-sandaran-sistem.md
# manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md
# manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md
# manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md

# 3. Porting ke Kemahiran AI
# .agents/skills/cu04-wa02-*/SKILL.md
# .agents/skills/cu04-wa04-*/SKILL.md
# .agents/skills/cu06-wa04-*/SKILL.md
# .agents/skills/cu06-wa07-*/SKILL.md

# 4. Kemas kini Silibus OpenWiki
# openwiki/topic-04-automation-and-backup.md
# openwiki/topic-06-troubleshooting-and-logs.md

# 5. Cipta Ujian Unit
# tests/test_manual_cu04_cu06_backup_troubleshooting_content.py

# 6. Jana semula indeks & bina web
uv run scripts/generate_palace_registry.py
uv run scripts/generate_llms_txt.py
uv run scripts/llms_to_xml.py
uv run scripts/serve_mkdocs.py --build-only

# 7. Sahkan 100% Quality Gate
uv run run_all_tests.py

# 8. Komit dan tolak ke GitHub & GitLab
git add -A
git commit -m "feat(manual): migrate Bab 6 backup, text processing, and storage mounting to manual/cu04 and manual/cu06"
git push origin main
git push github main
```
