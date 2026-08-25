---
okf_version: 0.2
type: documentation
title: "Topik 6: Penyelesaian Masalah, Pelekapan Storan, Penapis Teks & Analisis Log (CU06)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["troubleshooting", "logs", "mount", "grep", "sed", "awk", "vim", "neovim", "nano", "sudoedit", "visudo", "cu06", "openwiki", "noss"]
tags: ["linux", "troubleshooting", "logs", "mount", "fstab", "grep", "sed", "awk", "vim", "neovim", "nano", "sudoedit", "visudo", "rca", "cu06"]
description: "Silibus penyelesaian masalah sistem, pelekapan storan mount/fstab, penapis teks grep/sed/awk, penyunting teks Vim/Neovim/Nano, penyuntingan selamat sudoedit/visudo, pemantauan prestasi, dan dokumentasi RCA dipetakan kepada NOSS CU06."
resource: "file:///openwiki/topic-06-troubleshooting-and-logs.md"
---

# Topik 6: Penyelesaian Masalah, Pelekapan Storan, Penapis Teks & Analisis Log (CU06)

## 📌 Overview (Gambaran Keseluruhan)

Topik ini memfokuskan kepada teknik merungkaikan masalah sistem (*troubleshooting*), pemeriksaan pelekapan storan & peranti luaran, pemprosesan teks aluran log, penalaan proses, dan penyediaan laporan Analisis Punca Utama (*Root Cause Analysis - RCA*). Dipetakan secara terus daripada **NOSS CU06 (End-User Support & System Maintenance)**.

---

## 📚 Silibus Utama

1. **Pemantauan Proses & Sumber Sistem (Resource & Process Monitoring)**:
    - Arahan pemerhatian statik dan masa nyata: `ps aux`, `top`, `htop`, `pidstat`.
    - Analisis beban purata (*load average*), memori fizikal, swap, dan I/O: `uptime`, `free -h`, `vmstat`, `iostat`.
    - Isyarat POSIX (`kill`, `pkill`, `killall`), keutamaan `nice`/`renice`, dan `cgroups v2`.
2. **Pelekapan Storan & Peranti Luaran (Storage Mounting & Peripherals)**:
    - Nod peranti moden (`/dev/nvmeXn1`, `/dev/sdX`, `/dev/sr0`, USB) berpandukan FHS.
    - Pelekapan manual dan penangguhan: `mount`, `umount`, `findmnt`, `lsblk`, `eject`.
    - Entri pelekapan kekal dalam `/etc/fstab` dengan pilihan keselamatan JDN/MAMPU (`nodev,nosuid,noexec`).
3. **Pemprosesan Teks Aluran, Penyunting CLI & Amalan Keselamatan (Text Filters, CLI Editors & Security)**:
    - Penapis teks: `grep` / `ripgrep`, `sed` (stream editor), `awk` (pattern scanning), `cut`, `sort`, `uniq`, `wc`, `tr`.
    - Operator pengalihan I/O (`>`, `>>`, `<`, `2>&1`, `|` piping, `tee`).
    - Penyunting teks CLI pentadbiran: **Vim / Neovim** (mod Normal/Insert/Visual/Ex, regex search/replace `%s/old/new/g`, makro) dan **GNU Nano** (`.nanorc`).
    - Penyuntingan selamat fail konfigurasi sistem: `sudoedit` (`sudo -e`), `visudo`, dan semakan sintaks `visudo -c`.
4. **Pembacaan Log Sistem & Laporan RCA (Log Analysis & Root Cause Analysis)**:
    - Audit log sistem terpusat menggunakan `journalctl` dan fail `/var/log/`.
    - Penyediaan laporan Analisis Punca Utama (*Root Cause Analysis - RCA*) mengikut standard ISO/IEC 27001 dan JDN/MAMPU.

---

## 🗺️ Pemetaan Modul Amali & Kemahiran AI (NOSS Mapping)

Silibus ini memandu modul amali di `manual/cu06/` dan kemahiran AI di `.agents/skills/`:

- `manual/cu06/cu06-wa01-keperluan-perkhidmatan-sokongan-pengguna.md` ➔ `.agents/skills/cu06-wa01-prepare-end-user-support-service-requirements/`
- `manual/cu06/cu06-wa02-pengendalian-aduan-dan-insiden-pengguna.md` ➔ `.agents/skills/cu06-wa02-handle-end-user-requests-and-incidents/`
- `manual/cu06/cu06-wa03-diagnostik-dan-troubleshooting-perkakasan.md` ➔ `.agents/skills/cu06-wa03-support-hardware-troubleshooting/`
- `manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md` ➔ `.agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/`
- `manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md` ➔ `.agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/` & `.agents/skills/cu06-wa05-optimize-system-performance-and-storage/`
- `manual/cu06/cu06-wa06-pengurusan-tiket-sokongan-dan-sla.md` ➔ `.agents/skills/cu06-wa06-manage-support-tickets-and-slas/`
- `manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md` ➔ `.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/`

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bagaimanakah cara menggunakan awk dan sort untuk mengekstrak alamat IP terbanyak yang membuat percubaan akses SSH gagal daripada log auth.log?"*
2. *"Apakah kelebihan keselamatan menggunakan sudoedit berbanding sudo vim semasa menyunting fail /etc/environment?"*
3. *"Tunjukkan contoh persediaan laporan RCA (Root Cause Analysis) yang lengkap bagi insiden kegagalan perkhidmatan pelayan."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Brendan Gregg's Linux Performance & Tuning Guide](https://www.brendangregg.com/linuxperf.html)
- [Ubuntu Server Storage & Diagnostics Guide](https://ubuntu.com/server/docs)
- [GNU Sed and Awk User Manuals](https://www.gnu.org/software/sed/manual/sed.html)
- [Systemd Journalctl User Guide](https://www.freedesktop.org/software/systemd/man/journalctl.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Systems Performance: Enterprise and the Cloud** oleh Brendan Gregg.
- **Sed & Awk (2nd Edition)** oleh Dale Dougherty & Arnold Robbins.
- **Pengoptimuman & Diagnostik Prestasi Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
