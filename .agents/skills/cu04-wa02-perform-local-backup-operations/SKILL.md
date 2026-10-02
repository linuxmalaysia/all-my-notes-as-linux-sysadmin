---
okf_version: '0.2'
name: cu04-wa02-perform-local-backup-operations
description: Executes NOSS Work Activity CU04-WA02 - Perform Local Backup Operations
  including tar archive with zstd compression, rsync incremental sync, and systemd.timer
  automation.
topics:
- noss
- cu04
- wa02
- backup
- tar
- zstd
- rsync
- cron
- systemd-timer
type: agent_skill
title: Perform Local Backup Operations (CU04-WA02)
timestamp: '2026-08-17T00:00:00Z'
tags:
- cu04
- wa02
- noss
- backup
- zstd
- rsync
- systemd
resource: file:///.agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:44Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

# Perform Local Backup Operations
*Executes NOSS standard K622-001-3:2026-C04 WA02: Perform Local Backup Operations*

## 🎯 Skill Overview
This AI agent skill provides systematic procedures for performing local backup operations, multi-threaded tar-zstd compression, incremental directory mirroring with `rsync`, and automated backup scheduling via `cron` or `systemd.timer` according to ISO/IEC 27001 and Malaysian JDN/MAMPU guidelines.

---

## 🛠️ Execution Procedure

### 1. Multi-Threaded Compressed Backup (`tar` + `zstd`)
```bash
# Create a zstd compressed archive (-T0 uses all available CPU threads)
sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/system_config_$(date +%Y%m%d).tar.zst /etc /var/log

# Verify archive listing without extraction
tar -tvf /mnt/backup/system_config_*.tar.zst
```

### 2. Incremental Directory Synchronization (`rsync`)
```bash
# Perform incremental backup with delete-after synchronization
sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/
```

### 3. Automated Backup Scheduling via `systemd.timer`
1. Create service at `/etc/systemd/system/local-backup.service`:
   ```ini
   [Unit]
   Description=NOSS CU04 Local Backup Service

   [Service]
   Type=oneshot
   ExecStart=/usr/local/bin/system_backup.sh
   ```

2. Create timer at `/etc/systemd/system/local-backup.timer`:
   ```ini
   [Unit]
   Description=NOSS CU04 Daily Backup Timer

   [Timer]
   OnCalendar=*-*-* 02:00:00
   Persistent=true

   [Install]
   WantedBy=timers.target
   ```

3. Enable and start timer:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now local-backup.timer
   ```

---

## 🔒 Security & Compliance Safeguards
- Enforce the 3-2-1 backup strategy (3 copies, 2 media types, 1 offsite).
- Encrypt sensitive backups with AES-256 (`gpg --symmetric`).

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
