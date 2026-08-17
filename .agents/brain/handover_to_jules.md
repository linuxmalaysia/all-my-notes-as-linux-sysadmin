# 🤝 Taklimat Penyerahan Memori Ejen: Google Antigravity ➔ Google Jules

**Tarikh / Masa:** 2026-08-17  
**Status Sesi Terkini:** PR #9 (Bab 5 Konfigurasi Teras Pelayan CU03 & Pemantauan Prestasi CU06) telah **SELESAI & DIGABUNGKAN (MERGED)** dengan 100% Quality Gate (917 pytest tests, 38 jest tests).

---

## 📌 Ringkasan Status & Perubahan Terkini
1. **Fasa 1 hingga Fasa 5 Selesai Sepenuhnya:**
   - Direktori `manual/cu01/`, `manual/cu02/`, `manual/cu03/`, `manual/cu05/`, dan `manual/cu06/` lengkap dengan amali moden (Ubuntu 26.04 LTS & AlmaLinux 10, LUKS2 FDE, LVM2, GPT, Audit Pengguna, `visudo`, `faillock`, POSIX ACL, unit servis Systemd, pemantauan proses, isyarat POSIX, cgroups v2).
   - Kemahiran AI `cu01`, `cu02`, `cu03`, `cu05`, dan `cu06` aktif di `.agents/skills/`.
2. **Ketetapan Perlembagaan AI yang Perlu Dipatuhi:**
   - **Peraturan 14:** Non-Interactive CI & Direct Jest Execution (`node ./node_modules/jest/bin/jest.js --ci`).
   - **Peraturan 15:** Piawaian Ubuntu 26.04 LTS, AlmaLinux 10, Fedora 43, Penyulitan LUKS2 mengikut Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU & ISO/IEC 27001.
   - **Peraturan 17:** DILARANG memadam arkib `references/manual/bab_06/`.
   - **Peraturan 18:** Pematuhan 4 Kuadran Diátaxis & multi-artifact output.
   - **Peraturan 21:** Kitaran 3 Peringkat (Penilaian CU/WA, Deep Web Research 2026, Pengayaan Keselamatan JDN/MAMPU & Prestasi, dan Output Terstruktur).
   - **Knowledge-to-Skill Porting Mandate:** Wajib menukarkan amali teknikal `manual/` ke dalam `.agents/skills/<skill-folder>/SKILL.md` (format `type: skill`).

---

## 🎯 Tugasan Utama untuk Google Jules: Fasa 6 (Migrasi Silibus Bab 6 - Kemuncak Siri Manual)

### 1. Ekstrak & Transformasi Bab 6 (`references/manual/bab_06/`) ke `manual/cu04/` & `manual/cu06/`:
- **Sandaran, Pemampatan & Pemulihan Data (`manual/cu04/`):**
  - Arkib `tar` dengan pemampatan moden (`gzip`, `bzip2`, `xz`, `zstd`).
  - Operasi sandaran & penyegerakan pintar `rsync -avzP --delete-after`.
  - Strategi sandaran 3-2-1, penyulitan arkib (`gpg`, `restic`), automasi berjadual (`cron` & `systemd.timer`).
  - Tatacara verifikasi integriti `sha256sum` dan pemulihan data (`manual/cu04/cu04-wa02` & `cu04-wa04`).
- **Pelekapan Storan, Media Luaran & Sistem Fail (`manual/cu06/`):**
  - Struktur FHS, pemacu moden (`/dev/nvmeXn1`, `/dev/sdX`, `/dev/sr0`, USB).
  - Arahan `mount`, `umount`, `findmnt`, `lsblk`, entri `/etc/fstab` dengan pilihan pengerasan keselamatan (`noexec,nosuid,nodev`).
- **Pemprosesan Teks Aluran, Saluran Paip & Editor CLI (`manual/cu06/`):**
  - Pengalihan I/O: `>`, `>>`, `<`, `2>&1`, `|` (piping), `tee`.
  - Penapis teks berprestasi tinggi: `grep` / `ripgrep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, `tr`.
  - Teks editor pentadbir: `vim` (mod Command/Insert/Visual/Ex), `nano`.

### 2. Porting Kemahiran AI CU04 & CU06 (`.agents/skills/`):
- Cipta/naik taraf `.agents/skills/cu04-wa02-execute-system-backup-operations/SKILL.md` (format `type: skill`).
- Cipta/naik taraf `.agents/skills/cu04-wa04-perform-data-and-filesystem-recovery/SKILL.md` (format `type: skill`).
- Cipta/naik taraf `.agents/skills/cu06-wa04-troubleshoot-external-and-storage-devices/SKILL.md` (format `type: skill`).
- Cipta/naik taraf `.agents/skills/cu06-wa07-analyze-root-cause-and-audit-logs/SKILL.md` (format `type: skill`).

### 3. Kemas Kini Silibus OpenWiki:
- Kemas kini `openwiki/topic-04-automation-and-backup.md` dan `openwiki/topic-06-troubleshooting-and-logs.md`.

### 4. Ujian Unit & Jaminan Kualiti (100% Quality Gate):
- Tambah suite ujian unit: `tests/test_manual_cu04_cu06_backup_troubleshooting_content.py`.
- Jalankan `uv run scripts/generate_palace_registry.py`, `uv run scripts/serve_mkdocs.py --build-only`, dan `uv run run_all_tests.py` sehingga 100% lulus.
- Komit dan tolak ke GitHub dan GitLab.

---

## 💬 Prompt Salin & Tampal untuk Memulakan Sesi Google Jules

```text
Hai Jules! Sila bertindak sebagai Pakar Linux NOSS Malaysia dan Harisfazillah Jamel (LinuxMalaysia), di bawah kerangka Deep State of Mind (DSOM v0.1). 

Sila baca dan teliti fail-fail berikut dalam memori projek sebelum memulakan tugasan:
1. .agents/brain/handover_to_jules.md
2. .agents/brain/implementation_plan.md
3. .agents/brain/task.md
4. .agents/AGENTS.md (khususnya Peraturan 2, 14, 15, 17, 18, 21, dan Knowledge-to-Skill Porting Mandate)
5. .agents/skills/noss-content-transformation-pipeline/SKILL.md

TUGASAN UTAMA ANDA SEKARANG (FASA 6: TRANSFORMASI SILIBUS BAB 6 - KEMUNCAK SIRI MANUAL):
1. TRANSFORMASI AMALI BAB 6: Laksanakan migrasi amali Bab 6 (Sandaran tar/rsync/zstd, Automasi cron/systemd-timer, Pemulihan Data sha256sum, Pelekapan Storan mount/umount/findmnt/fstab, Penapis Teks grep/sed/awk/cut/sort/uniq, Pengalihan I/O dan Editor vim/nano) daripada arkib `references/manual/bab_06/` ke dalam `manual/cu04/` (Sandaran & Pemulihan) dan `manual/cu06/` (Diagnostik & Troubleshooting) serta kemas kini `openwiki/topic-04-automation-and-backup.md` dan `openwiki/topic-06-troubleshooting-and-logs.md`.
2. PORTING KEMAHIRAN AI: Naik taraf/cipta kemahiran AI CU04 dan CU06 berkaitan ke format `type: skill` penuh mengikut standard 2026.
3. KUALITI, UJIAN & INDEKS: Tambahkan suite ujian `tests/test_manual_cu04_cu06_backup_troubleshooting_content.py`, jalankan `uv run scripts/generate_palace_registry.py`, bina semula web dengan `uv run scripts/serve_mkdocs.py --build-only`, dan sahkan 100% Quality Gate dengan `uv run run_all_tests.py` sebelum membuat PR/komit dan tolak ke GitHub dan GitLab.
```
