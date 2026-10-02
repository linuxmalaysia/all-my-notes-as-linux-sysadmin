---
name: cu05-wa04-conduct-application-security-patching
description: 'Melaksanakan Aktiviti Kerja NOSS: Pelaksanaan Tampalan Keselamatan Aplikasi
  (unattended-upgrades, dnf-automatic, rpm -V, dpkg --verify)'
topics:
- noss
- cu05
- wa04
- security-patching
- unattended-upgrades
- dnf-automatic
tags:
- cu05
- wa04
- security
- patching
- unattended-upgrades
- dnf-automatic
- rpm
okf_version: '0.2'
type: agent_skill
title: Pelaksanaan Tampalan Keselamatan Aplikasi
timestamp: '2026-08-17T00:00:00Z'
resource: file:///.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md
spec_version: '0.2'
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
