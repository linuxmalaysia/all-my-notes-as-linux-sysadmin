---
okf_version: 0.1
type: documentation
title: "topic-04-automation-and-backup"
timestamp: "2026-08-16T08:43:42Z"
topics: ["bash-scripting", "backup", "cu04"]
tags: ["linux", "backup", "scripting", "cu04"]
description: "Silibus automasi skrip dan sandaran Linux (Cron, Bash, Rsync) dipetakan kepada NOSS CU04."
resource: "file:///openwiki/topic-04-automation-and-backup.md"
---

# Topik 4: Automasi & Sandaran (CU04)

## Overview (Gambaran Keseluruhan)
Sistem Linux terkenal dengan keupayaan automasinya. Topik ini menyentuh asas penulisan skrip (shell scripting) dan penggunaan utiliti sandaran data (backup). Dipetakan daripada **CU04 (Backup & Recovery Tools)**.

## Silibus Utama
1. **Arkib & Pemampatan (Archiving & Compression)**:
   - Penggunaan `tar`, `gzip`, `zip`.
2. **Bash Scripting Basics**:
   - Pembolehubah (Variables).
   - Struktur kawalan (If-else, For loops).
   - Kebenaran pelaksanaan (`chmod +x script.sh`).
3. **Penyelarasan Masa (Job Scheduling)**:
   - Menggunakan `cron` dan penyuntingan jadual menerusi `crontab -e`.
4. **Alatan Sandaran Berpusat Rangkaian (Network Backup)**:
   - Penggunaan `rsync` untuk menyegerak fail antara pelayan berbeza (`rsync -avz /source/ user@server:/destination/`).

## Pemetaan NOSS (NOSS Mapping)
Silibus ini memandu kemahiran Ejen AI berikut:
- `cu04-wa02-perform-local-backup-operations`
- `cu04-wa03-perform-network-based-backup`

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
