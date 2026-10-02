---
okf_version: '0.2'
name: cu04-wa04-restore-endpoint-data
description: Executes NOSS Work Activity CU04-WA04 - Restore Endpoint Data and Filesystem
  Recovery including sha256sum checksum validation and selective archive extraction.
topics:
- noss
- cu04
- wa04
- restore
- sha256sum
- bare-metal
- tar
type: agent_skill
title: Restore Endpoint Data (CU04-WA04)
timestamp: '2026-08-17T00:00:00Z'
tags:
- cu04
- wa04
- noss
- restore
- sha256sum
- bare-metal
resource: file:///.agents/skills/cu04-wa04-restore-endpoint-data/SKILL.md
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
