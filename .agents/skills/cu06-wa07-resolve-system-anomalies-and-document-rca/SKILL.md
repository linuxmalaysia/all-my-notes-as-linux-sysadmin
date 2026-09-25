---
okf_version: 0.1
name: cu06-wa07-resolve-system-anomalies-and-document-rca
description: Melaksanakan Aktiviti Kerja NOSS CU06-WA07 - Menyelesaikan Anomali Sistem dan Mendokumentasikan RCA menggunakan penapis teks (grep, sed, awk, cut, sort, uniq), pengalihan I/O, penyunting terminal (regex Vim %s/asal/ganti/g, Nano), pemboleh ubah persekitaran ($EDITOR/$VISUAL), penyuntingan selamat (sudoedit/visudo), dan pelaporan RCA.
topics: [noss, cu06, wa07, grep, sed, awk, cut, sort, uniq, vim, neovim, nano, sudoedit, visudo, editor, rca]
type: skill
title: "Resolve System Anomalies and Document RCA (CU06-WA07)"
timestamp: "2026-08-17T00:00:00Z"
tags: ["cu06", "wa07", "noss", "grep", "sed", "awk", "vim", "neovim", "nano", "sudoedit", "visudo", "editor", "rca"]
resource: "file:///.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md"
---

# Resolve System Anomalies and Document RCA

*Executes NOSS standard K622-001-3:2026-C06 WA07: Resolve System Anomalies and Document RCA*

## 🎯 Gambaran Keseluruhan Kemahiran

Kemahiran ejen AI ini menyediakan teknik sistematik untuk pemprosesan aluran log menggunakan utiliti penapis teks (`grep`, `sed`, `awk`, `cut`, `sort`, `uniq`), pelaksanaan pengalihan I/O dan saluran paip, pengurusan penyunting terminal (**Vim / Neovim**, **GNU Nano / Pico**, **GNU Emacs**), konfigurasi pemboleh ubah persekitaran (`$EDITOR`/`$VISUAL`), penyuntingan fail sistem secara selamat (`sudoedit`, `visudo`), serta penyediaan laporan Analisis Punca Utama (*Root Cause Analysis - RCA*).

---

## 🛠️ Execution Procedure

### 1. High-Performance Text Processing & Log Filtering

```bash
# Filter failed log-in attempts
grep -in "failed" /var/log/auth.log

# Extract top failed IP addresses
grep "Failed password" /var/log/auth.log | cut -d' ' -f11 | sort | uniq -c | sort -nr

# Stream replacement with sed
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# Column extraction with awk
awk '{print $1, $5}' /var/log/syslog | head -n 10
```

### 2. I/O Redirection & Piping

```bash
# Tee output to both terminal and audit log
sudo systemctl status nginx 2>&1 | tee /tmp/nginx_error_audit.log
```

### 3. Terminal Text Editing & Safe System Modifications

```bash
# 1. Konfigurasi Pemboleh Ubah Persekitaran (~/.bashrc, /etc/environment, atau /etc/profile)
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim

# 2. Operasi Vim / Neovim
# Carian & penggantian regex mod Ex:
# :%s/temp/tmp/g
# Perekaman & pelaksanaan makro:
# Rekod makro ke dalam daftar 'a': qa ... q
# Jalankan semula makro: @a atau 5@a

# 3. Pintasan GNU Nano & Pico
# Nano: Simpan: Ctrl+O | Keluar: Ctrl+X | Cari: Ctrl+W | Ganti: Ctrl+\ | Potong: Ctrl+K | Tampal: Ctrl+U | Fail Konfigurasi: ~/.nanorc
# Pico: Menyokong majoriti pintasan asas Pico (seperti sisip fail Ctrl+R); Nano menambah keupayaan carian ganti Ctrl+\ dan penyerlahan sintaks.

# 4. Mod Terminal GNU Emacs (-nw)
# Buka dalam terminal: emacs -nw fail.txt
# Buka: C-x C-f | Simpan: C-x C-s | Keluar: C-x C-c | Batal: C-g
# Konfigurasi Lisp: ~/.emacs atau ~/.config/emacs/init.el ((setq-default major-mode 'text-mode) dan (add-hook 'text-mode-hook 'auto-fill-mode))

# 5. Penyuntingan fail sistem secara selamat menggunakan sudoedit (sudo -e) & visudo
sudoedit /etc/netplan/01-netcfg.yaml
sudo visudo -c
```

### 4. Root Cause Analysis (RCA) Report Structure

1. **Incident Summary**: Date, time, impacted services.
2. **Chronology**: Timeline extracted from logs (`journalctl`, `syslog`).
3. **Root Cause**: Anomaly source identified via log filtering (`grep`/`awk`).
4. **Remediation**: Corrective actions taken.
5. **Prevention**: System hardening or automation to prevent recurrence.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
