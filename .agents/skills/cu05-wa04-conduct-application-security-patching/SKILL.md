---
name: cu05-wa04-conduct-application-security-patching
description: "Melaksanakan Aktiviti Kerja NOSS: Pelaksanaan Tampalan Keselamatan Aplikasi (unattended-upgrades, dnf-automatic, rpm -V, dpkg --verify)"
topics: [noss, cu05, wa04, security-patching, unattended-upgrades, dnf-automatic]
tags: [cu05, wa04, security, patching, unattended-upgrades, dnf-automatic, rpm]
okf_version: 0.1
type: skill
title: "Pelaksanaan Tampalan Keselamatan Aplikasi"
timestamp: "2026-08-17T00:00:00Z"
resource: "file:///.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md"
---

# Pelaksanaan Tampalan Keselamatan Aplikasi

*Melaksanakan standard NOSS K622-001-3:2026-C05 WA04 (Sementara: Kod Sementara Standard NOSS)*

## Gambaran Keseluruhan (Overview)

Kemahiran ini menyediakan prosedur operasi bagi mengautomasikan pemasangan tampalan keselamatan (`unattended-upgrades` pada Debian/Ubuntu 26.04 LTS, `dnf-automatic` pada Red Hat/AlmaLinux 10 / Fedora 43), mengesahkan integriti fail pakej terpasang (`rpm -V`, `dpkg --verify`), dan mengaudit kelemahan CVE mengikut piawaian NOSS Tahap 3 serta standard keselamatan ISO/IEC 27001.

## Prosedur (Procedure)

### 1. Automasi Tampalan Keselamatan

- **Debian / Ubuntu 26.04 LTS (`unattended-upgrades`):**

  ```bash
  sudo apt update
  sudo apt install -y unattended-upgrades
  sudo dpkg-reconfigure --priority=low unattended-upgrades
  sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log
  ```

- **Red Hat / AlmaLinux 10 / Fedora 43 (`dnf-automatic`):**

  ```bash
  sudo dnf install -y dnf-automatic
  sudo sed -i 's/^upgrade_type =.*/upgrade_type = security/' /etc/dnf/automatic.conf
  sudo sed -i 's/^apply_updates =.*/apply_updates = yes/' /etc/dnf/automatic.conf
  grep -E '^(upgrade_type|apply_updates)' /etc/dnf/automatic.conf
  sudo systemctl enable --now dnf-automatic.timer
  sudo systemctl status dnf-automatic.timer
  ```

### 2. Integriti Pakej & Audit CVE

- **Integriti Pakej Red Hat / AlmaLinux / Fedora:**

  ```bash
  sudo rpm -Va
  sudo rpm -V openssh-server
  sudo dnf updateinfo list security
  sudo dnf updateinfo info security
  ```

- **Integriti Pakej & Audit CVE Debian / Ubuntu:**

  ```bash
  sudo dpkg --verify
  sudo apt install -y debsecan
  debsecan --suite $(lsb_release -cs)
  ```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
