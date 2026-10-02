---
name: cu05-wa05-manage-physical-endpoint-security-lockdowns
okf_version: '0.2'
type: agent_skill
title: Manage Physical Endpoint Security Lockdowns (CU05-WA05)
timestamp: '2026-08-17T00:00:00Z'
topics:
- noss
- cu05
- wa05
- physical-security
- lockdown
- grub
- tmout
- systemd
tags:
- noss
- cu05
- wa05
- security
- linux
- physical-security
- tmout
- limits
description: 'Executes NOSS Work Activity CU05-WA05: Manage physical endpoint lockdowns,
  bootloader GRUB2 password protection, session timeout (TMOUT), virtual terminal
  limits, and safe shutdown procedures.'
resource: file:///.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md
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

# 🔒 Manage Physical Endpoint Security Lockdowns (CU05-WA05)

## 📌 Executive Overview

This skill executes **NOSS Level 3 Unit CU05 WA05** (*Manage Physical Endpoint Security Lockdowns*). It guides AI agents in hardening Linux endpoints against physical tampering, unauthorized bootloader parameter modifications, abandoned active shell sessions, and uncontrolled system shutdowns on **Ubuntu 26.04 LTS "Resolute Raccoon"** and **AlmaLinux 10**.

---

## ⚙️ Prerequisites & Security Governance

- **Distribution Standard:** Ubuntu 26.04 LTS "Resolute Raccoon" & AlmaLinux 10 "Purple Lion".
- **Privilege Mandate:** Requires full `sudo` privileges.
- **Compliance Baseline:** CIS Benchmarks, ISO/IEC 27001 & Pekeliling Jabatan Digital Negara (JDN) / MAMPU.

---

## 🛠️ Step-by-Step Execution Workflows

### 1. Bootloader GRUB2 Password Protection

- **Protect Boot Menu Parameters from Unauthorized Single-User Mode Edits:**
  - **On AlmaLinux 10 / Fedora 43:**
    ```bash
    sudo grub2-setpassword
    sudo grub2-mkconfig -o /boot/grub2/grub.cfg
    ```
  - **On Ubuntu 26.04 LTS "Resolute Raccoon":**
    ```bash
    # Generate PBKDF2 hash using grub-mkpasswd-pbkdf2
    grub-mkpasswd-pbkdf2

    # Add superusers configuration to /etc/grub.d/40_custom
    # set superusers="admin"
    # password_pbkdf2 admin grub.pbkdf2.sha512...

    # Regenerate GRUB2 configuration using update-grub
    sudo update-grub
    ```

### 2. Mandatory Session Idle Timeout Configuration (`TMOUT`)

- **Enforce Automatic Shell Termination After 15 Minutes Inactivity:**
  ```bash
  cat << 'EOF' | sudo tee /etc/profile.d/timeout.sh
  readonly TMOUT=900
  export TMOUT
  EOF
  sudo chmod +x /etc/profile.d/timeout.sh
  ```

### 3. Resource Limits & Console Hardening

- **Disable Unused Virtual Terminals (getty) & Set Limits:**
  ```bash
  sudo systemctl disable --now getty@tty3.service
  sudo systemctl mask getty@tty3.service

  cat << 'EOF' | sudo tee -a /etc/security/limits.conf
  *          hard    core            0
  *          hard    maxlogins       3
  EOF
  ```

### 4. Safe Graceful System Shutdown Procedures

- **Scheduled Broadcast Shutdown vs Immediate Poweroff (Alternatives):**
  - *Option A (Scheduled grace period):*
    ```bash
    sudo shutdown -h +2 "System undergoing physical maintenance in 2 minutes."
    ```
  - *Option B (Immediate systemd poweroff):*
    ```bash
    sudo systemctl poweroff
    ```

---

## 📋 Audit Verification Checklist

- [ ] Confirmed GRUB2 configuration mandates credentials for boot parameter modifications.
- [ ] Verified `TMOUT` environment variable is set and read-only in active sessions.
- [ ] Verified `/etc/security/limits.conf` prevents core dumps and limits logins.
- [ ] Verified graceful shutdown commands execute via `shutdown` or `systemctl poweroff`.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
