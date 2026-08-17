---
okf_version: 0.1
name: cu04-wa02-perform-local-backup-operations
description: Executes NOSS Work Activity CU04-WA02 - Perform Local Backup Operations including tar archive with zstd compression, rsync incremental sync, and systemd.timer automation.
topics: [noss, cu04, wa02, backup, tar, zstd, rsync, cron, systemd-timer]
type: skill
title: "Perform Local Backup Operations (CU04-WA02)"
timestamp: "2026-08-17T00:00:00Z"
tags: ["cu04", "wa02", "noss", "backup", "zstd", "rsync", "systemd"]
resource: "file:///.agents/skills/cu04-wa02-perform-local-backup-operations/SKILL.md"
---

# Perform Local Backup Operations
*Executes NOSS standard K622-001-3:2026-C04 WA02: Perform Local Backup Operations*

## 🎯 Skill Overview
This AI agent skill provides systematic procedures for performing local backup operations, multi-threaded tar-zstd compression, incremental directory mirroring with `rsync`, and automated backup scheduling via `cron` or `systemd.timer` according to ISO/IEC 27001 and Malaysian JDN/MAMPU guidelines.

---

## 🛠️ Execution Procedure

### 1. Multi-Threaded Compressed Backup & Manifest Generation (`tar` + `zstd`)
```bash
# Create a zstd compressed archive (-T0 uses all available CPU threads)
sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/system_config_20260817.tar.zst /etc /var/log

# Generate matching SHA-256 integrity manifest
cd /mnt/backup && sha256sum system_config_20260817.tar.zst > system_config_20260817.tar.zst.sha256

# Verify archive listing without extraction
tar -tvf /mnt/backup/system_config_20260817.tar.zst
```

### 2. Incremental Directory Synchronization (`rsync`)
> ⚠️ **Destructive Mirror Warning:** Using `rsync --delete-after` will purge destination files that do not exist in the source directory. Before executing, ensure a versioned or snapshot-based retention backup exists.

```bash
# Perform incremental mirror with delete-after synchronization
sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/
```

### 3. Automated Backup Scheduling via `systemd.timer`
1. Create service at `/etc/systemd/system/local-backup.service`:
   ```ini
   [Unit]
   Description=NOSS CU04 Local Backup Service
   RequiresMountsFor=/mnt/backup
   ConditionPathIsMountPoint=/mnt/backup

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
