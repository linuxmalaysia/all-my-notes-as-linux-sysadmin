---
name: "cu05-wa05-manage-physical-endpoint-security-lockdowns"
okf_version: 0.1
type: skill
title: "Manage Physical Endpoint Security Lockdowns (CU05-WA05)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss", "cu05", "wa05", "physical-security", "lockdown", "grub", "tmout", "systemd"]
tags: ["noss", "cu05", "wa05", "security", "linux", "physical-security", "tmout", "limits"]
description: "Executes NOSS Work Activity CU05-WA05: Manage physical endpoint lockdowns, bootloader GRUB2 password protection, session timeout (TMOUT), virtual terminal limits, and safe shutdown procedures."
resource: "file:///.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md"
---

# 🔒 Manage Physical Endpoint Security Lockdowns (CU05-WA05)

## 📌 Executive Overview
This skill executes **NOSS Level 3 Unit CU05 WA05** (*Manage Physical Endpoint Security Lockdowns*). It guides AI agents in hardening Linux endpoints against physical tampering, unauthorized bootloader parameter modifications, abandoned active shell sessions, and uncontrolled system shutdowns on **Ubuntu 26.04 LTS** and **AlmaLinux 10**.

---

## ⚙️ Prerequisites & Security Governance
- **Distribution Standard:** Ubuntu 26.04 LTS "Quetzal" & AlmaLinux 10 "Purple Lion".
- **Privilege Mandate:** Requires full `sudo` privileges.
- **Compliance Baseline:** CIS Benchmarks, ISO/IEC 27001 & Pekeliling Jabatan Digital Negara (JDN) / MAMPU.

---

## 🛠️ Step-by-Step Execution Workflows

### 1. Bootloader GRUB2 Password Protection
- **Protect Boot Menu Parameters from Unauthorized Single-User Mode Edits:**
  ```bash
  # On AlmaLinux 10 / Fedora 43:
  sudo grub2-setpassword
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg

  # On Ubuntu 26.04 LTS:
  # Generate PBKDF2 hash using grub-mkpasswd-pbkdf2 and add user superusers to /etc/grub.d/40_custom
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
- **Restrict Core Dumps & Maximum Simultaneous Logins (`/etc/security/limits.conf`):**
  ```bash
  cat << 'EOF' | sudo tee -a /etc/security/limits.conf
  *          hard    core            0
  *          hard    maxlogins       3
  EOF
  ```

### 4. Safe Graceful System Shutdown Procedures
- **Schedule Broadcast Message and System Power Off:**
  ```bash
  sudo shutdown -h +2 "System undergoing physical maintenance in 2 minutes."
  sudo systemctl poweroff
  ```

---

## 📋 Audit Verification Checklist
- [ ] Confirmed GRUB2 configuration mandates credentials for boot parameter modifications.
- [ ] Verified `TMOUT` environment variable is set and read-only in active sessions.
- [ ] Verified `/etc/security/limits.conf` prevents core dumps and limits logins.
- [ ] Verified graceful shutdown and reboot commands execute via `systemctl`.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
