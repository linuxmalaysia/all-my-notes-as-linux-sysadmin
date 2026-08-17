---
okf_version: 0.1
type: documentation
title: "Topik 6: Penyelesaian Masalah, Pemantauan Prestasi & Analisis Log (CU06)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["troubleshooting", "logs", "performance", "cu06", "openwiki", "noss"]
tags: ["linux", "troubleshooting", "logs", "cu06", "prestasi", "openwiki"]
description: "Silibus penyelesaian masalah sistem, pemantauan prestasi & proses, analisis log journalctl, dan sokongan pengguna dipetakan kepada NOSS CU06."
resource: "file:///openwiki/topic-06-troubleshooting-and-logs.md"
---

# Topik 6: Penyelesaian Masalah, Pemantauan Prestasi & Analisis Log (CU06)

## 📌 Overview (Gambaran Keseluruhan)
Topik ini memfokuskan kepada teknik merungkaikan masalah sistem (*troubleshooting*), memeriksa kesihatan & prestasi sistem, penalaan proses, dan pengurusan perkhidmatan sokongan pengguna. Dipetakan secara terus daripada **NOSS CU06 (End-User Support & System Maintenance)**.

---

## 📚 Silibus Utama
1. **Pemantauan Proses & Sumber Sistem (Resource & Process Monitoring)**:
   - Arahan pemerhatian statik dan interaktif masa nyata: `ps aux`, `top`, `htop`, `pidstat`.
   - Analisis beban purata (*load average*), penggunaan memori fizikal & swap: `uptime`, `free -h`.
   - Menganalisis memori maya dan I/O cakera: `vmstat 1 5`, `iostat -xz 1 5`.
2. **Kitaran Hayat Proses & Penalaan Keutamaan (Process Lifecycle & Tuning)**:
   - Penghantaran isyarat POSIX (`kill -15` SIGTERM, `kill -9` SIGKILL, `kill -1` SIGHUP, `killall`, `pkill`).
   - Penalaan keutamaan penjadualan CPU (*nice value* -20 hingga 19): `nice`, `renice`.
   - Penalaan keutamaan I/O cakera: `ionice`.
   - Penghadan sumber sistem melalui `cgroups v2` dan `systemd-run`.
3. **Penyelesaian Masalah Rangkaian & Sambungan (Network Troubleshooting)**:
   - Pemeriksaan IP & Antaramuka: `ip a`, `ip route`.
   - Menguji capaian & laluan: `ping`, `traceroute`, `tracepath`, `curl`, `dig`.
   - Pemerhatian port & soket aktif: `ss -tulpn`.
4. **Pembacaan & Analisis Log Sistem (Log Analysis & Auditing)**:
   - Audit log sistem terpusat menggunakan `journalctl` (parameter `-u`, `-f`, `--since`, `-p err`).
   - Menyelidik fail log sistem tradisional di `/var/log/` (`syslog`, `auth.log`, `messages`, `secure`).
   - Penyiasatan punca kegagalan sistem (*Root Cause Analysis - RCA*).

---

## 🗺️ Pemetaan Modul Amali & Kemahiran AI (NOSS Mapping)
Silibus ini memandu modul amali di `manual/cu06/` dan kemahiran AI di `.agents/skills/`:
- `manual/cu06/cu06-wa01-keperluan-perkhidmatan-sokongan-pengguna.md` ➔ `.agents/skills/cu06-wa01-prepare-end-user-support-service-requirements/`
- `manual/cu06/cu06-wa02-pengendalian-aduan-dan-insiden-pengguna.md` ➔ `.agents/skills/cu06-wa02-handle-end-user-requests-and-incidents/`
- `manual/cu06/cu06-wa03-diagnostik-dan-troubleshooting-perkakasan.md` ➔ `.agents/skills/cu06-wa03-support-hardware-troubleshooting/`
- `manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md` ➔ `.agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/`
- `manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md` ➔ `.agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/`
- `manual/cu06/cu06-wa06-pengurusan-tiket-sokongan-dan-sla.md` ➔ `.agents/skills/cu06-wa06-manage-support-tickets-and-slas/`
- `manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md` ➔ `.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/`

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Bagaimanakah cara menganalisis punca kemerosotan prestasi I/O pelayan apabila vmstat menunjukkan nilai swap-out (so) yang tinggi secara berterusan?"*
2. *"Tunjukkan skrip Python untuk mengautomasikan pemantauan log journalctl dan menghantar amaran ke saluran Telegram/Slack apabila ralat kritikal (Priority ERR) dikesan."*
3. *"Apakah langkah-langkah penyediaan laporan RCA (Root Cause Analysis) yang mematuhi format ISO/IEC 27001 bagi insiden perkhidmatan terhenti disebabkan OOM Killer?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Brendan Gregg's Linux Performance & Tuning Guide](https://www.brendangregg.com/linuxperf.html)
- [Ubuntu Server Administration & Diagnostics Guide](https://ubuntu.com/server/docs)
- [AlmaLinux 10 Performance Optimization Wiki](https://wiki.almalinux.org/)
- [Systemd Journalctl User Guide](https://www.freedesktop.org/software/systemd/man/journalctl.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Systems Performance: Enterprise and the Cloud (2nd Edition)** oleh Brendan Gregg.
- **Linux Troubleshooting Bible** oleh Christopher Negus & Thomas Weeks.
- **Pengoptimuman & Diagnostik Prestasi Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
