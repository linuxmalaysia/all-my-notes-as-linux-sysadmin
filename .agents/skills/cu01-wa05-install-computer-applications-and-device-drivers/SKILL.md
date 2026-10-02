---
name: cu01-wa05-install-computer-applications-and-device-drivers
description: 'Executes NOSS Work Activity: Install Computer Applications And Device
  Drivers (APT, DNF5, Flatpak, Snap, GPU Drivers)'
topics:
- noss
- cu01
- wa05
- package-management
- synaptic
- gnome-software
- tarball
- device-drivers
tags:
- cu01
- wa05
- apt
- dnf
- synaptic
- gnome-software
- tarball
- flatpak
- snap
- nvidia
- driver
okf_version: '0.2'
type: agent_skill
spec_version: '0.2'
title: cu01-wa05-install-computer-applications-and-device-drivers
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

# Install Computer Applications And Device Drivers

*Executes NOSS standard K622-XXX-3:2026-C01 WA05*

## Overview

This skill provides automated guidance and execution steps for managing Linux application packages CLI & GUI (APT on Ubuntu 26.04 LTS "Resolute Raccoon", DNF5 on AlmaLinux 10 / Fedora 43, Synaptic Package Manager, GNOME Software, Flatpak, Snap, Tarball compilation) and installing proprietary device drivers (NVIDIA GPU, AMD Radeon, and wireless networking) in accordance with NOSS Level 3 standards.

## Procedure

### 1. Native Package Management & GUI Package Tools

- **Ubuntu 26.04 LTS "Resolute Raccoon" (APT & Synaptic / GNOME Software):**

  ```bash
  sudo apt update
  sudo apt upgrade -y
  sudo apt install -y curl git vlc synaptic gnome-software
  ```

- **AlmaLinux 10 / Fedora 43 (DNF5 & PackageKit):**

  ```bash
  sudo dnf check-upgrade || true
  sudo dnf upgrade -y
  sudo dnf install -y htop wget
  ```

- **RPM Package Operations & Source Tarball Compilation:**

  ```bash
  # 1. Verify GPG digital signature before installation
  rpmkeys --checksig nmap-7.95-1.x86_64.rpm

  # 2. Install / Upgrade RPM package with hash progress (#)
  sudo rpm -Uvh nmap-7.95-1.x86_64.rpm
  rpm -qi nmap
  rpm -ql nmap
  rpm -V nmap

  # 3. Install build tools and resolve BuildRequires before SRPM rebuild
  sudo dnf install -y rpm-build rpmdevtools gcc gcc-c++ make dnf-plugins-core
  rpmkeys --checksig openssh-9.8p1-1.src.rpm
  sudo dnf builddep -y openssh-9.8p1-1.src.rpm
  rpmbuild --rebuild openssh-9.8p1-1.src.rpm

  # 4. Manual compilation from tarball (.tar.gz / .tar.zst) - chained execution stopping on failure
  # Set KEYRING according to distro (Debian/Ubuntu: /etc/apt/trusted.gpg.d/vendor.gpg or /etc/apt/keyrings/vendor.gpg; AlmaLinux/Fedora: /etc/pki/rpm-gpg/RPM-GPG-KEY-vendor or /etc/pki/gpg/vendor.gpg)
  GPG_STATUS=$(mktemp) && \
  trap 'rm -f "$GPG_STATUS"' EXIT && \
  KEYRING="/etc/apt/trusted.gpg.d/vendor.gpg" && \
  EXPECTED_FPR="1234567890ABCDEF1234567890ABCDEF12345678" && \
  gpg --no-default-keyring --keyring "$KEYRING" --status-fd 1 --verify sample-app-1.0.tar.gz.sha256.asc sample-app-1.0.tar.gz.sha256 > "$GPG_STATUS" 2>&1 && \
  grep -q -E "^\[GNUPG:\] VALIDSIG $EXPECTED_FPR " "$GPG_STATUS" && \
  [ $(grep -E "  sample-app-1\.0\.tar\.gz$" sample-app-1.0.tar.gz.sha256 | wc -l) -eq 1 ] && \
  grep -E "  sample-app-1\.0\.tar\.gz$" sample-app-1.0.tar.gz.sha256 | sha256sum -c - && \
  tar -zxvf sample-app-1.0.tar.gz && \
  cd sample-app-1.0 && \
  ./configure --prefix=/usr/local && \
  make -j$(nproc) && \
  sudo make install
  ```

### 2. Environment Variables Configuration ($EDITOR & $VISUAL)

- **User Environment (~/.bashrc):**
  ```bash
  # Add exports to ~/.bashrc (Run 'source ~/.bashrc' in active terminal to load):
  export EDITOR=/usr/bin/vim
  export VISUAL=/usr/bin/vim
  ```

- **System-Wide Environment (/etc/environment & /etc/profile.d/editor.sh):**
  ```bash
  # In /etc/environment (NAME=VALUE pairs, read by pam_env):
  EDITOR="/usr/bin/vim"
  VISUAL="/usr/bin/vim"

  # In /etc/profile.d/editor.sh (For interactive login shells):
  export EDITOR=/usr/bin/vim
  export VISUAL=/usr/bin/vim
  ```

### 3. Universal Containerized Packaging

- **Flatpak (Flathub):**

  ```bash
  sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
  flatpak install flathub org.gimp.GIMP -y
  ```

- **Snap (Ubuntu):**

  ```bash
  sudo snap install code --classic
  ```

### 4. GPU & Device Driver Installation

- **Detect Hardware (GPU & Wireless):**

  ```bash
  lspci -nnk | grep -A3 -i vga
  lspci -nnk | grep -A3 -i network
  ```

- **Ubuntu NVIDIA Drivers:**

  ```bash
  sudo ubuntu-drivers install
  nvidia-smi
  ```

- **Fedora 43 NVIDIA Drivers (RPM Fusion):**

  ```bash
  sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
  sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
  sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
  ```

- **AlmaLinux 10 NVIDIA Drivers (RPM Fusion):**

  ```bash
  sudo dnf install -y https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-10.noarch.rpm
  sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-10.noarch.rpm
  sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
  ```

## Security & Governance

- For APT third-party repositories, use repository-scoped keyrings under `/etc/apt/keyrings/` with `signed-by=` in `/etc/apt/sources.list.d/`.
- Retain `gpgcheck=1` for DNF repositories.
- Adhere to JDN/MAMPU guidelines and ISO/IEC 27001 audit logging (`/var/log/dpkg.log` or `/var/log/dnf.log`).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
