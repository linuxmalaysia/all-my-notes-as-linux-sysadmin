---
okf_version: 0.1
type: documentation
title: "topic-06-troubleshooting-and-logs"
timestamp: "2026-08-16T08:43:42Z"
topics: ["troubleshooting", "logs", "cu06"]
tags: ["linux", "troubleshooting", "logs", "cu06"]
description: "Silibus penyelesaian masalah, rangkaian, dan semakan log Linux dipetakan kepada NOSS CU06."
resource: "file:///openwiki/topic-06-troubleshooting-and-logs.md"
---

# Topik 6: Penyelesaian Masalah & Log (CU06)

## Overview (Gambaran Keseluruhan)
Topik terakhir ini memfokuskan kepada teknik merungkaikan masalah sistem (troubleshooting), memeriksa kesihatan sistem, dan menguruskan perkhidmatan sokongan pengguna. Dipetakan terus daripada **CU06 (End-User Support)**.

## Silibus Utama
1. **Pengurusan Perkhidmatan (Service Management)**:
   - Penggunaan `systemctl` (start, stop, enable, status, restart).
   - Memahami Systemd dan init.
2. **Pemantauan Sumber (Resource Monitoring)**:
   - Arahan pemerhatian masa nyata: `top`, `htop`, `free -m`, `uptime`.
3. **Penyelesaian Masalah Rangkaian (Network Troubleshooting)**:
   - Pemeriksaan IP: `ip a`, `ifconfig`.
   - Menguji capaian: `ping`, `traceroute`, `curl`.
   - Pemerhatian port dan soket: `ss -tulpn`, `netstat`.
4. **Pembacaan Log (Log Reading)**:
   - Penggunaan `journalctl`.
   - Menyelidik fail log sistem seperti `/var/log/syslog`, `/var/log/auth.log`, `/var/log/messages`.

## Pemetaan NOSS (NOSS Mapping)
Silibus ini memandu kemahiran Ejen AI berikut:
- `cu06-wa02-handle-end-user-requests-and-incidents`
- `cu06-wa07-resolve-system-anomalies-and-document-rca`

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
