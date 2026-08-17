# 📐 Pelan Pelaksanaan Google Jules: Migrasi Silibus Bab 5 (Pengurusan Proses, Pemantauan Prestasi & Servis Teras Pelayan ke manual/cu03/ dan manual/cu06/)

## 1. Objektif Utama Sesi Jules
Memindahkan, memodenkan, menyelidik secara mendalam (*Deep Web Research*), dan memetakan kandungan arkib manual lama **Bab 5 (`references/manual/bab_05/`)** ke dalam direktori **`manual/cu03/`** (Konfigurasi Teras Pelayan & Servis Systemd) dan **`manual/cu06/`** (Pemantauan Prestasi Sistem & Diagnostik Proses), serta mengemas kini **`openwiki/topic-03-linux-server-administration.md`** dan **`openwiki/topic-06-troubleshooting-and-logs.md`** berlandaskan piawaian **NOSS Level 3 (CU03 & CU06)**, edaran kanonik Linux 2026 (Ubuntu 26.04 LTS & AlmaLinux 10), 4 kuadran Diátaxis, dan arahan keselamatan **Jabatan Digital Negara (JDN) / MAMPU** serta **ISO/IEC 27001**.

---

## 2. Garis Panduan Transformasi & Pematuhan Perlembagaan AI

### A. Kitaran Mandatori Peraturan 21 (Deep Research & CU/WA Mapping)
1. **Penilaian Silibus:**
   - `CU03-WA04`: Konfigurasi Teras Pelayan (pengurusan unit servis `systemd`, `systemctl`, `journalctl`, konfigurasi masa `timedatectl`/`chrony`, dan profil perkhidmatan teras).
   - `CU06-WA05`: Pengoptimuman Prestasi & Pemantauan Proses Sistem (`ps aux`, `top`, `htop`, `vmstat`, `iostat`, `kill`, `killall`, `nice`, `renice`, cgroups v2, dan isyarat proses SIGTERM/SIGKILL).
   - `CU01`: Halaman dokumentasi `man` (seksyen 1–9), `/usr/share/man`, `mandb`, alatan bantuan CLI moden.
2. **Penyelidikan Mendalam (*Deep Web Research*):**
   - Sintaks arahan moden systemd: `systemctl status/start/stop/enable/disable/restart`, `systemctl daemon-reload`, `journalctl -u <service> -f`, `timedatectl set-ntp true`.
   - Isyarat proses POSIX: `kill -15` (SIGTERM - penutupan anggun), `kill -9` (SIGKILL - henti paksa), `kill -1` (SIGHUP - muat semula konfigurasi).
   - Penalaan keutamaan proses: `nice -n -10`, `renice -n 5 -p <PID>`, `ionice`.
   - Alat pemantauan moden: `vmstat 1 5`, `iostat -xz 1 5`, `free -h`, `uptime`, `pidstat`.
3. **Pengayaan Keselamatan & Prestasi:**
   - Had sumber proses melalui cgroups v2 dan `systemd-run` / unit drop-in overrides (`/etc/systemd/system/<service>.d/override.conf`).
   - Standard audit log sistem selaras dengan ISO/IEC 27001 dan pekeliling JDN/MAMPU.
4. **Penyusunan Output Terstruktur:**
   - Hasilkan nod amali di `manual/cu03/pengurusan-proses-dan-servis-teras-pelayan.md` atau kemas kini nod WA berkaitan di `manual/cu03/` dan `manual/cu06/`.
   - Pautkan ke `openwiki/topic-03-linux-server-administration.md`.

### B. Mandat Porting Pengetahuan ke Kemahiran AI (Knowledge-to-Skill Porting)
- Naik taraf atau cipta modul AI Agent Skill di bawah `.agents/skills/`:
  - `.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md` (format `type: skill`).
  - `.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md` (format `type: skill`).
- Daftarkan ke Master Palace Registry (`uv run scripts/generate_palace_registry.py`).

### C. Suite Ujian Pematuhan Kualiti (Quality Gate & Test Suite)
- Tambah suite ujian unit Python: `tests/test_manual_cu03_cu06_process_server_content.py` bagi mengesahkan nod manual, kemahiran AI, frontmatter OKF, dan pautan openwiki.
- Sahkan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` melepasi 100% Quality Gate.

---

## 3. Langkah Operasi Langkah Demi Langkah untuk Jules

```bash
# 1. Baca arkib mentah Bab 5 (DILARANG padam mengikut Peraturan 17)
# references/manual/bab_05/part_01.md & part_02.md

# 2. Tulis nod amali moden ke manual/cu03/ & manual/cu06/
# manual/cu03/pengurusan-proses-dan-servis-teras-pelayan.md
# Kemas kini manual/cu03/cu03-wa04-*.md & manual/cu06/cu06-wa05-*.md

# 3. Porting ke Kemahiran AI
# .agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md
# .agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md

# 4. Kemas kini Silibus OpenWiki
# openwiki/topic-03-linux-server-administration.md
# openwiki/topic-06-troubleshooting-and-logs.md

# 5. Cipta Ujian Unit
# tests/test_manual_cu03_cu06_process_server_content.py

# 6. Jana semula indeks & bina web
uv run scripts/generate_palace_registry.py
uv run scripts/generate_llms_txt.py
uv run scripts/llms_to_xml.py
uv run scripts/serve_mkdocs.py --build-only

# 7. Sahkan 100% Quality Gate
uv run run_all_tests.py

# 8. Komit dan tolak ke GitHub & GitLab
git add -A
git commit -m "feat(manual): migrate Bab 5 core server services and process management to manual/cu03 and manual/cu06"
git push origin main
git push github main
```
