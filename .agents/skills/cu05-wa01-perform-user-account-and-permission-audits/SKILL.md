---
name: cu05-wa01-perform-user-account-and-permission-audits
okf_version: '0.2'
type: agent_skill
title: Perform User Account and Permission Audits (CU05-WA01)
timestamp: '2026-08-17T00:00:00Z'
topics:
- noss
- cu05
- wa01
- user-audit
- permissions
- visudo
- faillock
tags:
- noss
- cu05
- wa01
- security
- linux
- permissions
- acl
description: 'Executes NOSS Work Activity CU05-WA01: Audit user accounts, group memberships,
  authentication files (/etc/passwd, /etc/shadow), sudoers configuration, file permissions,
  POSIX ACLs, and faillock.'
resource: file:///.agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md
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

# 🛡️ Perform User Account and Permission Audits (CU05-WA01)

## 📌 Executive Overview

This skill executes **NOSS Level 3 Unit CU05 WA01** (*Perform User Account and Permission Audits*). It empowers AI agents to inspect, audit, and remediate user accounts, privileged access (`sudoers`), file permissions, special bits (SUID/SGID/Sticky), POSIX ACLs, and PAM lockouts on **Ubuntu 26.04 LTS "Resolute Raccoon"** and **AlmaLinux 10**.

---

## ⚙️ Prerequisites & Security Governance

- **Distribution Standard:** Ubuntu 26.04 LTS "Resolute Raccoon" & AlmaLinux 10 "Purple Lion".
- **Privilege Mandate:** Must be executed with `sudo` privileges or as a security auditor account.
- **Compliance Baseline:** ISO/IEC 27001 & Pekeliling Jabatan Digital Negara (JDN) / MAMPU.

---

## 🛠️ Step-by-Step Execution Workflows

### 1. User & Group Identity Verification (`/etc/passwd` & `/etc/shadow`)

- **Check for Unauthorized Superusers (UID 0 except root):**
  ```bash
  awk -F: '($3 == "0" && $1 != "root") { print $1 }' /etc/passwd
  ```
- **Audit Passwordless or Locked Suspicious Accounts (empty or starting with !):**
  ```bash
  sudo awk -F: '($2 == "" || $2 ~ /^!/) { print $1 }' /etc/shadow
  ```
- **Integrity Validation:**
  ```bash
  sudo pwck -r
  sudo grpck -r
  ```

### 2. Privileged Access (`sudoers`) Audit via `visudo`

- **Verify Syntax & Structural Integrity of `/etc/sudoers`:**
  ```bash
  sudo visudo -c
  ```
- **Audit Specific User Privileges:**
  ```bash
  sudo -l -U <username>
  ```

### 3. File Permissions, Special Bits & POSIX ACL Audit

- **Identify Files with SUID Executable Bit Set:**
  ```bash
  find / -perm -4000 -type f -ls 2>/dev/null
  ```
- **Inspect POSIX ACLs on Sensitive Target Directories:**
  ```bash
  getfacl /srv/projek_sec/
  ```
- **Grant Controlled Access via POSIX ACL:**
  ```bash
  sudo setfacl -m u:zarith:rw- /srv/projek_sec/dokumen.pdf
  ```

### 4. Account Lockout Audit & Remediation (`faillock`)

- **Check Failure Logs for Locked Accounts:**
  ```bash
  sudo faillock --user <username>
  ```
- **Reset Lockout Status:**
  ```bash
  sudo faillock --user <username> --reset
  ```

---

## 📋 Audit Verification Checklist

- [ ] Confirmed zero unauthorized UID 0 accounts (excluding root).
- [ ] Confirmed `/etc/sudoers` passes `visudo -c` validation.
- [ ] Verified SUID/SGID audit outputs match expected baseline binaries.
- [ ] Verified `faillock` successfully unlocks valid user accounts.

---
*Linux for NOSS Malaysia (Sovereign AI Skill) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
