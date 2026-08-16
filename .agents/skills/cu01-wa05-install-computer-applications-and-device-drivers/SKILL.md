---
name: cu01-wa05-install-computer-applications-and-device-drivers
description: "Executes NOSS Work Activity: Install Computer Applications And Device Drivers (APT, DNF5, Flatpak, Snap, GPU Drivers)"
topics: [noss, cu01, wa05, package-management, device-drivers]
tags: [cu01, wa05, apt, dnf, flatpak, snap, nvidia, driver]
okf_version: 0.1
type: skill
---

# Install Computer Applications And Device Drivers
*Executes NOSS standard K622-XXX-3:2026-C01 WA05*

## Overview
This skill provides automated guidance and execution steps for managing Linux application packages (APT on Ubuntu 26.04 LTS, DNF5 on AlmaLinux 10 / Fedora 43, Flatpak, Snap) and installing proprietary device drivers (such as NVIDIA GPU drivers) in accordance with NOSS Level 3 standards.

## Procedure

### 1. Native Package Management
- **Ubuntu 26.04 LTS (APT):**
  ```bash
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y curl git vlc
  ```
- **AlmaLinux 10 / Fedora 43 (DNF5):**
  ```bash
  sudo dnf check-update && sudo dnf upgrade -y
  sudo dnf install -y epel-release htop wget
  ```

### 2. Universal Containerized Packaging
- **Flatpak (Flathub):**
  ```bash
  sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
  flatpak install flathub org.gimp.GIMP -y
  ```
- **Snap (Ubuntu):**
  ```bash
  sudo snap install code --classic
  ```

### 3. GPU Device Driver Installation
- **Detect Graphics Hardware:**
  ```bash
  lspci -nnk | grep -A3 -i vga
  ```
- **Ubuntu NVIDIA Drivers:**
  ```bash
  sudo ubuntu-drivers install
  nvidia-smi
  ```
- **AlmaLinux / Fedora NVIDIA Drivers (RPM Fusion):**
  ```bash
  sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
  ```

## Security & Governance
- Verify GPG signatures for all external repositories (`gpgcheck=1`).
- Adhere to JDN/MAMPU guidelines and ISO/IEC 27001 audit logging (`/var/log/dpkg.log` or `/var/log/dnf.log`).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
