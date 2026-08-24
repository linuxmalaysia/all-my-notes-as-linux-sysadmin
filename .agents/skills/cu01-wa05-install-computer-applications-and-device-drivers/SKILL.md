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

This skill provides automated guidance and execution steps for managing Linux application packages (APT on Ubuntu 26.04 LTS "Resolute Raccoon", DNF5 on AlmaLinux 10 / Fedora 43, Flatpak, Snap) and installing proprietary device drivers (NVIDIA GPU, AMD Radeon, and wireless networking) in accordance with NOSS Level 3 standards.

## Procedure

### 1. Native Package Management

- **Ubuntu 26.04 LTS "Resolute Raccoon" (APT):**

  ```bash
  sudo apt update
  sudo apt upgrade -y
  sudo apt install -y curl git vlc
  ```

- **AlmaLinux 10 / Fedora 43 (DNF5):**

  ```bash
  sudo dnf check-upgrade || true
  sudo dnf upgrade -y
  sudo dnf install -y htop wget
  ```

- **RPM Package Operations & Source Compilation:**

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

  # 4. Manual compilation from tarball (verify checksums first, inspect README/INSTALL)
  sha256sum -c sample-app-1.0.tar.gz.sha256
  tar -xvf sample-app-1.0.tar.gz
  cd sample-app-1.0
  cat README || cat INSTALL
  # For Autotools-based projects:
  ./configure --prefix=/usr/local
  make -j$(nproc)
  sudo make install
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

### 3. GPU & Device Driver Installation

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
