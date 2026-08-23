---
name: cu05-wa04-conduct-application-security-patching
description: "Executes NOSS Work Activity: Conduct Application Security Patching (unattended-upgrades, dnf-automatic, rpm -V, dpkg --verify)"
topics: [noss, cu05, wa04, security-patching, unattended-upgrades, dnf-automatic]
tags: [cu05, wa04, security, patching, unattended-upgrades, dnf-automatic, rpm]
okf_version: 0.1
type: skill
title: "Conduct Application Security Patching"
timestamp: "2026-08-17T00:00:00Z"
resource: "file:///.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md"
---

# Conduct Application Security Patching
*Executes NOSS standard K622-XXX-3:2026-C05 WA04*

## Overview

This skill provides operational procedures for automating security patch installation (`unattended-upgrades` on Debian/Ubuntu 26.04 LTS, `dnf-automatic` on Red Hat/AlmaLinux 10 / Fedora 43), verifying package integrity (`rpm -V`, `dpkg --verify`), and auditing CVE vulnerabilities in compliance with NOSS Level 3 and ISO/IEC 27001 security standards.

## Procedure

### 1. Automated Security Patching

- **Debian / Ubuntu 26.04 LTS (`unattended-upgrades`):**

  ```bash
  sudo apt update
  sudo apt install -y unattended-upgrades apt-config-auto-update
  sudo dpkg-reconfigure --priority=low unattended-upgrades
  sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log
  ```

- **Red Hat / AlmaLinux 10 / Fedora 43 (`dnf-automatic`):**

  ```bash
  sudo dnf install -y dnf-automatic
  sudo sed -i 's/upgrade_type = default/upgrade_type = security/' /etc/dnf/automatic.conf
  sudo sed -i 's/apply_updates = no/apply_updates = yes/' /etc/dnf/automatic.conf
  sudo systemctl enable --now dnf-automatic.timer
  sudo systemctl status dnf-automatic.timer
  ```

### 2. Package Integrity & Security Auditing

- **Red Hat / AlmaLinux / Fedora Package Integrity:**

  ```bash
  sudo rpm -Va
  sudo rpm -V openssh-server
  sudo dnf updateinfo list security
  ```

- **Debian / Ubuntu Package Integrity:**

  ```bash
  sudo dpkg --verify
  ```


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
