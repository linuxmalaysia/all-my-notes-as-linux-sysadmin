---
spec_version: '0.2'
okf_version: '0.2'
type: automation_tool
title: 'HOWTO: setup-dsom-control-node — Linux Environment Hardening'
description: Dokumentasi OKF v0.2 bagi HOWTO-SETUP-DSOM-CONTROL-NODE.md.
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

﻿---
title: "Howto Setup Dsom Control Node"
description: "DSOM Reference document for Howto Setup Dsom Control Node."
type: "reference"
id: "docs/reference/tools/HOWTO-SETUP-DSOM-CONTROL-NODE.md"
dsom_governance:
  domain: "AI"
  context_tier: "L2-Operational"
tags:
  - "dsom-protocol"
  - "diataxis-quadrant"
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---

# HOWTO: setup-dsom-control-node — Linux Environment Hardening

# docs/tools/HOWTO-SETUP-DSOM-CONTROL-NODE.md

> **Standard: DSOM For My AI Protocol v6.1 | OS Hardening**
> **Tools:** `setup-dsom-control-node.sh`
> **Platforms:** Linux / AlmaLinux 10 (WSL2 / Bare Metal)

---

## 1. Purpose

`setup-dsom-control-node` is the **System Configuration Engine** for a fresh DSOM Tier 2 node. It transforms a vanilla Linux installation into a fully hardened, Ansible-ready control node with standardised user identities and performance-tuned WSL interoperability settings.

**Use it to:**
- Provision the standard **`dsom-admin`** service user (UID 2001).
- Install the DSOM toolstack: `ansible`, `git`, `rsync`, and `python3-pip`.
- Configure `wsl.conf` for **systemd** support and optimized disk mounting metadata.
- Generate a project-specific ED25519 SSH keypair.
- Set up the global `~/.ansible.cfg` for high-concurrency pipe-lining.

**Location:** 
- `tools/setup-dsom-control-node.sh`

---

## 2. Prerequisites

| Requirement | Minimum | Notes |
|:---|:---|:---|
| OS | AlmaLinux / RHEL 9+ | Specifically tested on AlmaLinux 10. |
| Access | **Root** | Must run as the root user or via `sudo`. |
| Network | External | Requires access to DNF repositories and PyPI (pip). |

---

## 3. Usage

### 3.1 Targeted WSL Deployment

If you used the `setup-wsl-almalinux10.ps1` orchestrator, this tool is run **automatically** on your behalf. To re-run it manually:

```bash

# Run as root inside the WSL instance

bash tools/setup-dsom-control-node.sh

```

---

## 4. Configuration Changes

The tool performs several persistent system modifications:

### 4.1 Identity Management

- Creates group `dsom-admin` (GID 2001).
- Creates user `dsom-admin` (UID 2001).
- Adds user to the `wheel` group.
- Configures **passwordless sudo** via `/etc/sudoers.d/dsom-admin`.

### 4.2 WSL Interoperability (`/etc/wsl.conf`)

- Sets `default=dsom-admin`.
- Enables `systemd=true`.
- Disables `appendWindowsPath=false` (to prevent PATH pollution).
- Mounts `/mnt/c` with `metadata` options enabled (improves permission handling).

### 4.3 SSH Hardening

- Generates `~/.ssh/id_ed25519` for the `dsom-admin` user.
- Sets strict permission 700/600 on the `.ssh` directory.

---

## 5. Reading the Output & Status Codes

| Label | Meaning | Action Needed |
|:---|:---|:---|
| `[PASS]` | Component configured. | None. |
| `[SKIP]` | Feature already exists. | Useful for idempotency checks. |
| `[ERROR]` | Root access missing. | Rerun using `sudo` or `wsl -u root`. |
| `[INFO]` | Public Key displayed. | **Copy this key** to your target node's `authorized_keys`. |

---

## 6. Security Advisory

> [!WARNING]  
> This script disables `appendWindowsPath` in WSL. This means Windows executables (like `code.exe` or `git.exe` from T1) will no longer be in your Linux PATH. This is intentional to ensure your T2 Ansible operations are purely deterministic and isolated.

---

## 7. Related Documents

| Document | Purpose |
|:---|:---|
| [`HOWTO-SETUP-WSL-ALMALINUX.md`](HOWTO-SETUP-WSL-ALMALINUX.md) | The Windows orchestrator that calls this script. |
| [`docs/HOWTO-SETUP-ANSIBLE-BASELINE.md`](../HOWTO-SETUP-ANSIBLE-BASELINE.md) | Next steps for inventory management. |

---

*Standard: DSOM For My AI Protocol v6.1 | Harisfazillah Jamel | LinuxMalaysia*
*Document Version: v1.0 | Created: 2026-04-08*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
