---
okf_version: '0.2'
name: cu06-wa04-configure-and-troubleshoot-peripheral-connections
description: Executes NOSS Work Activity CU06-WA04 - Configure and Troubleshoot Peripheral
  Connections including storage mounting, umount, findmnt, and /etc/fstab security
  hardening.
topics:
- noss
- cu06
- wa04
- mount
- umount
- findmnt
- fstab
- storage
type: agent_skill
title: Configure and Troubleshoot Peripheral Connections (CU06-WA04)
timestamp: '2026-08-17T00:00:00Z'
tags:
- cu06
- wa04
- noss
- mount
- fstab
- peripherals
resource: file:///.agents/skills/cu06-wa04-configure-and-troubleshoot-peripheral-connections/SKILL.md
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:45Z'
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
