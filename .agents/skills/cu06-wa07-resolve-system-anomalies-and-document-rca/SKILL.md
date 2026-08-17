---
okf_version: 0.1
name: cu06-wa07-resolve-system-anomalies-and-document-rca
description: Executes NOSS Work Activity CU06-WA07 - Resolve System Anomalies and Document RCA using text filters (grep, sed, awk, cut, sort, uniq), I/O redirection, vim/nano, and RCA reporting.
topics: [noss, cu06, wa07, grep, sed, awk, cut, sort, uniq, vim, nano, rca]
type: skill
title: "Resolve System Anomalies and Document RCA (CU06-WA07)"
timestamp: "2026-08-17T00:00:00Z"
tags: ["cu06", "wa07", "noss", "grep", "sed", "awk", "vim", "nano", "rca"]
resource: "file:///.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md"
---

# Resolve System Anomalies and Document RCA
*Executes NOSS standard K622-001-3:2026-C06 WA07: Resolve System Anomalies and Document RCA*

## 🎯 Skill Overview
This AI agent skill provides systematic techniques for processing log streams using text processing utilities (`grep`, `sed`, `awk`, `cut`, `sort`, `uniq`), executing I/O redirection and piping, modifying system configs safely, and drafting Root Cause Analysis (RCA) reports.

---

## 🛠️ Execution Procedure

### 1. High-Performance Text Processing & Log Filtering
```bash
# Filter failed log-in attempts
grep -in "failed" /var/log/auth.log

# Extract failed IP addresses using token-aware parsing (field after "from")
grep "Failed password" /var/log/auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr

# Safe SSH port reconfiguration procedure:
# 1. Keep active SSH session open.
# 2. Backup configuration.
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
# 3. Update port and validate syntax with sshd -t before reloading.
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
sudo sshd -t && sudo systemctl reload sshd
```

### 2. I/O Redirection & Piping
```bash
# Tee output to both terminal and audit log
sudo systemctl status nginx 2>&1 | tee /tmp/nginx_error_audit.log
```

### 3. Root Cause Analysis (RCA) Report Structure
1. **Incident Summary**: Date, time, impacted services.
2. **Chronology**: Timeline extracted from logs (`journalctl`, `syslog`).
3. **Root Cause**: Anomaly source identified via log filtering (`grep`/`awk`).
4. **Remediation**: Corrective actions taken.
5. **Prevention**: System hardening or automation to prevent recurrence.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
