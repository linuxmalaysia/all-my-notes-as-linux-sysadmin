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
This AI agent skill provides operational procedures for identifying storage device nodes (`/dev/nvmeXn1`, `/dev/sdX`, `/dev/sr0`), executing manual mount/umount operations, and configuring `/etc/fstab` for both required internal storage and optional removable media with appropriate flags (`nofail`, `x-systemd.device-timeout=5s`, `nodev,nosuid,noexec`).

---

## 🛠️ Execution Procedure

### 1. Storage Identification
```bash
# List block devices with UUID and filesystem type
lsblk -f

# Obtain specific partition UUID
sudo blkid /dev/sdb1
```

### 2. Manual Mount and Safe Removal
```bash
# Mount filesystem without forcing type
sudo mkdir -p /mnt/external_usb
sudo mount /dev/sdb1 /mnt/external_usb

# Inspect mount hierarchy
findmnt /mnt/external_usb

# Safe unmount and removal for whole-disk USB
sudo umount /mnt/external_usb
sudo udisksctl power-off -b /dev/sdb

# Eject CD/DVD optical media
eject /dev/sr0
```

### 3. Persistent Automated Mounting in `/etc/fstab`

#### A. Required Storage (Internal Drives / Boot Partitions)
```ini
UUID=550e8400-e29b-41d4-a716-446655440000 /mnt/required_storage ext4 defaults 0 2
```

#### B. Optional / Removable Storage Media
```ini
UUID=a1b2c3d4-e5f6-7890-abcd-1234567890ab /mnt/removable_usb ext4 defaults,nofail,x-systemd.device-timeout=5s,nodev,nosuid,noexec 0 2
```

Test configuration without rebooting:
```bash
sudo mount -a
findmnt /mnt/removable_usb
```

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
