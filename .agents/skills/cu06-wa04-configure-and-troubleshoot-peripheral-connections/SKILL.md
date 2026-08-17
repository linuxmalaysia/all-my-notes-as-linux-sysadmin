---
okf_version: 0.1
name: cu06-wa04-configure-and-troubleshoot-peripheral-connections
description: Executes NOSS Work Activity CU06-WA04 - Configure and Troubleshoot Peripheral Connections including storage mounting, umount, findmnt, and /etc/fstab security hardening.
topics: [noss, cu06, wa04, mount, umount, findmnt, fstab, storage]
type: skill
title: "Configure and Troubleshoot Peripheral Connections (CU06-WA04)"
timestamp: "2026-08-17T00:00:00Z"
tags: ["cu06", "wa04", "noss", "mount", "fstab", "peripherals"]
resource: "file:///.agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md"
---

# Configure and Troubleshoot Peripheral Connections
*Executes NOSS standard K622-001-3:2026-C06 WA04: Configure and Troubleshoot Peripheral Connections*

## 🎯 Skill Overview
This AI agent skill provides operational procedures for identifying storage device nodes (`/dev/nvmeXn1`, `/dev/sdX`, `/dev/sr0`), executing manual mount/umount operations, and configuring `/etc/fstab` with security hardening options (`nodev,nosuid,noexec`).

---

## 🛠️ Execution Procedure

### 1. Storage Identification
```bash
# List block devices with UUID and filesystem type
lsblk -f

# Obtain specific partition UUID
sudo blkid /dev/sdb1
```

### 2. Manual Mount and Unmount
```bash
# Mount filesystem
sudo mkdir -p /mnt/external_usb
sudo mount -t ext4 /dev/sdb1 /mnt/external_usb

# Inspect mount hierarchy
findmnt /mnt/external_usb

# Safe unmount and eject
sudo umount /mnt/external_usb
eject /dev/sr0
```

### 3. Persistent Automated Mounting in `/etc/fstab` with Security Hardening
Add partition entry to `/etc/fstab`:
```ini
UUID=550e8400-e29b-41d4-a716-446655440000 /mnt/sec_storage ext4 defaults,nodev,nosuid,noexec 0 2
```

Test configuration without rebooting:
```bash
sudo mount -a
findmnt /mnt/sec_storage
```

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
