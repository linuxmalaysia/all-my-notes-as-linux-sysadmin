---
okf_version: '0.2'
name: cu01-wa04-install-computer-desktop-operating-systems
description: Kemahiran amali pemasangan sistem operasi Linux desktop & persekitaran
  Meja GNOME (Nautilus, applet, workspace switcher) — dikemaskini dengan prosedur
  terkini 2026 menggunakan Ubuntu 26.04 LTS, Fedora 43, dan AlmaLinux 10.
topics:
- noss
- cu01
- wa04
- linux-install
- gnome
- nautilus
- applet
- workspace
- ubuntu
- fedora
- almalinux
tags:
- linux
- pemasangan
- desktop
- gnome
- nautilus
- applet
- workspace
- ubuntu
- almalinux
- fedora
- cu01
- wa04
type: agent_skill
spec_version: '0.2'
title: cu01-wa04-install-computer-desktop-operating-systems
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

# CU01-WA04: Pemasangan Sistem Operasi Linux Desktop & Persekitaran Meja GNOME

## Tujuan Kemahiran
Kemahiran ini melengkapkan pelajar dengan prosedur pemasangan sistem operasi Linux desktop secara lengkap — daripada menyediakan media pemasangan, penyulitan LUKS2, hinggalah pengoperasian Persekitaran Meja GNOME (Pengurus Fail Nautilus, aplet panel, penukar ruang kerja, dan penyesuaian desktop).

---

## Prasyarat
- Sudah memahami ekosistem Linux (CU01-WA00)
- Pemacu kilat USB (minimum 8GB)
- Sambungan internet untuk muat turun fail ISO
- Komputer sasaran dengan ruang storan minimum 25GB

---

## Prosedur Pemasangan & Pentadbiran GNOME Desktop

### 1. Penyediaan Media Pemasangan & Boot
- **Ubuntu 26.04 LTS "Resolute Raccoon"** (GNOME 48, Kernel 6.14 LTS)
- **AlmaLinux 10 "Purple Lion"** (GNOME 47, Kernel 6.12 LTS, RHEL 10 Compatible)
- **Fedora Workstation 43** (Bleeding-edge GNOME)

```bash
# Tulis ISO ke USB (CLI):
sudo dd if=ubuntu-26.04-desktop-amd64.iso of=/dev/sdX bs=4M status=progress sync
```

### 2. Penyulitan Full Disk Encryption (LUKS2) Manual
```bash
# Aktifkan LUKS2 pada partition sasaran
sudo cryptsetup luksFormat --type luks2 /dev/nvme0n1p3
sudo cryptsetup luksOpen /dev/nvme0n1p3 pejabat-disk

# Penambahan slot kunci pemulihan pentadbir IT
sudo cryptsetup luksAddKey /dev/nvme0n1p3
```

### 3. Pengendalian Persekitaran Meja GNOME & Nautilus File Manager
- **Aplet Panel & Workspace Switcher**: Navigasi tetingkap berbilang meja kerja maya (`Ctrl+Alt+[Up/Down]`).
- **Pengurus Fail Nautilus (`nautilus`)**:
  - Pelancaran dari CLI: `nautilus ~ &`
  - Mod paparan pepohon (*tree view*), kawalan prestasi gambaran kecil (*thumbnails*), dan operasi heret-dan-lepas (*drag-and-drop*).
- **Pusat Kawalan Tetapan GNOME**:
  ```bash
  gnome-control-center
  gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
  ```

---

## Pengesahan Kejayaan

```bash
echo "=== Versi Sistem & Kernel ===" && hostnamectl && uname -r
echo "=== Status LUKS ===" && lsblk -o NAME,FSTYPE | grep -i crypt
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
