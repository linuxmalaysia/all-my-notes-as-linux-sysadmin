---
okf_version: 0.1
name: cu04-wa04-restore-endpoint-data
description: Executes NOSS Work Activity CU04-WA04 - Restore Endpoint Data and Filesystem Recovery including sha256sum checksum validation and selective archive extraction.
topics: [noss, cu04, wa04, restore, sha256sum, bare-metal, tar]
type: skill
title: "Restore Endpoint Data (CU04-WA04)"
timestamp: "2026-08-17T00:00:00Z"
tags: ["cu04", "wa04", "noss", "restore", "sha256sum", "bare-metal"]
resource: "file:///.agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md"
---

# Restore Endpoint Data
*Executes NOSS standard K622-001-3:2026-C04 WA04: Perform Data and Filesystem Recovery*

## 🎯 Skill Overview
This AI agent skill guides the execution of data integrity verification using `sha256sum`, selective file extraction from `tar.zst` archives, permission preservation, and bare-metal disaster recovery procedures.

---

## 🛠️ Execution Procedure

### 1. Integrity Verification (`sha256sum`)
```bash
# Verify checksum before attempting restoration
cd /mnt/backup/
sha256sum -c system_config_20260817.tar.zst.sha256
```

### 2. Selective File Extraction
```bash
# Extract single configuration file to staging folder
mkdir -p /tmp/recovery_staging
sudo tar -I zstd -xvf /mnt/backup/system_config_20260817.tar.zst \
  -C /tmp/recovery_staging \
  etc/netplan/01-netcfg.yaml
```

### 3. Decrypting & Restoring Encrypted Backup
```bash
# Decrypt GPG encrypted tar stream
gpg --decrypt /mnt/backup/backup_encrypted.tar.zst.gpg | sudo tar -I zstd -xvf - -C /tmp/recovery_staging/
```

### 4. Bare-Metal System Recovery Overview
1. Boot from Ubuntu 26.04 / AlmaLinux 10 Live ISO.
2. Mount root and boot partitions to `/mnt`.
3. Extract bare-metal archive: `sudo tar -I zstd -xvf /mnt/backup/full_system.tar.zst -C /mnt`.
4. Reinstall GRUB bootloader via chroot.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
