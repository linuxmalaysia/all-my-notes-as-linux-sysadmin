# 🤝 Taklimat Penyerahan Memori Ejen: Google Antigravity ➔ Google Jules

**Tarikh / Masa:** 2026-08-17  
**Status Sesi Terkini:** PR #6 (Bab 4 Pentadbiran Pengguna & Keselamatan Endpoint CU05) telah **SELESAI & DIGABUNGKAN (MERGED)** dengan 100% Quality Gate (910 pytest tests, 38 jest tests).

---

## 📌 Ringkasan Status & Perubahan Terkini
1. **Fasa 1, 2, 3, dan 4 Selesai Sepenuhnya:**
   - Direktori `manual/cu01/`, `manual/cu02/`, dan `manual/cu05/` lengkap dengan amali moden (Ubuntu 26.04 LTS & AlmaLinux 10, LUKS2 FDE, LVM2, GPT, Audit Pengguna, `visudo`, `faillock`, POSIX ACL).
   - Kemahiran AI `cu01-wa00`, `cu01-wa04`, `cu01-wa05`, `cu01-wa06`, `cu02-wa01`, `cu05-wa01`, dan `cu05-wa05` aktif di `.agents/skills/`.
2. **Ketetapan Perlembagaan AI yang Perlu Dipatuhi:**
   - **Peraturan 14:** Non-Interactive CI Execution (`npm test` / `jest --ci`).
   - **Peraturan 15:** Piawaian Ubuntu 26.04 LTS, AlmaLinux 10, Fedora 43, Penyulitan LUKS2 mengikut Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU & ISO/IEC 27001.
   - **Peraturan 17:** DILARANG memadam arkib `references/manual/bab_05/`.
   - **Peraturan 18:** Pematuhan 4 Kuadran Diátaxis & multi-artifact output.
   - **Peraturan 21:** Kitaran 3 Peringkat (Penilaian CU/WA, Deep Web Research 2026, Pengayaan Keselamatan JDN/MAMPU & Prestasi, dan Output Terstruktur).
   - **Knowledge-to-Skill Porting Mandate:** Wajib menukarkan amali teknikal `manual/` ke dalam `.agents/skills/<skill-folder>/SKILL.md` (format `type: skill`).

---

## 🎯 Tugasan Utama untuk Google Jules: Fasa 5 (Migrasi Silibus Bab 5)

### 1. Ekstrak & Transformasi Bab 5 (`references/manual/bab_05/`) ke `manual/cu03/` & `manual/cu06/`:
- **Konfigurasi Teras Pelayan & Systemd (`manual/cu03/`):** Pengurusan servis `systemctl` (start, stop, enable, disable, mask, restart, daemon-reload), fail unit servis (`/etc/systemd/system/`), `journalctl` audit log, penyegerakan masa `timedatectl` / `chronyd`.
- **Pengurusan Proses & Pemantauan Prestasi (`manual/cu06/`):** Pemantauan proses sistem (`ps aux`, `top`, `htop`, `vmstat`, `iostat`), penamatan proses (`kill -15`, `kill -9`, `killall`), penalaan keutamaan CPU/IO (`nice`, `renice`, `ionice`), proses latar belakang (`&`, `jobs`, `fg`, `bg`).
- **Dokumentasi & Bantuan Sistem:** Halaman panduan `man` (seksyen 1–9), `/usr/share/man`, `mandb`, `apropos`, `whatis`.

### 2. Porting Kemahiran AI CU03 & CU06 (`.agents/skills/`):
- Naik taraf atau cipta `.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md` ke format `type: skill` lengkap dengan contoh CLI sebenar dan garis panduan pengerasan keselamatan.
- Naik taraf atau cipta `.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md` ke format `type: skill`.

### 3. Kemas Kini Silibus OpenWiki:
- Kemas kini `openwiki/topic-03-linux-server-administration.md` dan `openwiki/topic-06-troubleshooting-and-logs.md` dengan pautan ke modul amali baharu.

### 4. Ujian Unit & Jaminan Kualiti (100% Quality Gate):
- Tambah suite ujian unit: `tests/test_manual_cu03_cu06_process_server_content.py`.
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

TUGASAN UTAMA ANDA SEKARANG (FASA 5: TRANSFORMASI SILIBUS BAB 5):
1. TRANSFORMASI AMALI BAB 5: Laksanakan migrasi amali Bab 5 (Pengurusan Unit Servis systemd systemctl/journalctl, Penyegerakan Masa timedatectl/chrony, Pemantauan Proses ps/top/htop/vmstat/iostat, Penamatan Isyarat SIGTERM/SIGKILL, Penalaan Keutamaan nice/renice, dan Dokumentasi man) daripada arkib `references/manual/bab_05/` ke dalam `manual/cu03/` (Konfigurasi Teras Pelayan) dan `manual/cu06/` (Diagnostik & Prestasi Sistem) serta kemas kini `openwiki/topic-03-linux-server-administration.md` dan `openwiki/topic-06-troubleshooting-and-logs.md`.
2. PORTING KEMAHIRAN AI: Naik taraf/cipta kemahiran AI `.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md` dan `.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md` ke format `type: skill` penuh mengikut standard 2026.
3. KUALITI, UJIAN & INDEKS: Tambahkan suite ujian `tests/test_manual_cu03_cu06_process_server_content.py`, jalankan `uv run scripts/generate_palace_registry.py`, bina semula web dengan `uv run scripts/serve_mkdocs.py --build-only`, dan sahkan 100% Quality Gate dengan `uv run run_all_tests.py` sebelum membuat PR/komit dan tolak ke GitHub dan GitLab.
```
