---
title: "Howto Setup Ansible Baseline"
description: "DSOM Reference document for Howto Setup Ansible Baseline."
type: "reference"
id: "docs/explanation/reference-architectures/HOWTO-SETUP-ANSIBLE-BASELINE.md"
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

# 🛠️ HOWTO: Set Up the Ansible Baseline for a DSOM Project (Example Elastic SOC)

**Title:** HOWTO: Set Up the Ansible Baseline for Example Elastic SOC
**Author:** Harisfazillah Jamel (LinuxMalaysia)
**Version:** 1.0
**Date:** 2026-06-11
**License:** GPLv3
**Standard:** Linux Documentation Project (LDP) | UK English

---

## 1. Introduction

### 1.1 Scope

This guide describes how the **Ansible baseline** is established for the **Example Elastic SOC** project built on the DSOM skeleton. Currently, you have:

- A standard Ansible directory structure (`playbooks/`, `roles/`, `inventory/`, `vault/`)
- A configured `ansible.cfg`
- A template `inventory/hosts.yml` (featuring Elastic nodes, Logstash nodes, and Kibana nodes)

### 1.2 Target Audience

- Lead Architects and DevOps Engineers deploying the Example Elastic SOC
- AI Agents (Cognitive Digital Twins) bootstrapping context for the Elastic SOC

### 1.3 Related Documents

- [`docs/AI-MASTER-PROTOCOL.md`](../governance/AI-MASTER-PROTOCOL.md) — Governance laws

---

## 2. Prerequisites

Before running any playbooks, verify the following are available on your **Tier 2 Dev Bridge** (or Tier 1 Command Centre for Windows):

| Requirement | Minimum Version | Verification Command |
|:---|:---|:---|
| Python | 3.9+ | `python3 --version` |
| pip | 23+ | `pip3 --version` |
| Ansible | 2.15+ | `ansible --version` |
| SSH Client | Any | `ssh -V` |
| Git | 2.30+ | `git --version` |

---

## 3. Procedure

### Step 1: Directory Structure Verification

The DSOM Ansible directory skeleton should already exist at your project root:
- `inventory/`
- `playbooks/`
- `roles/`
- `vault/`
- `.logs/`

Secrets are protected via `.gitignore`.

### Step 2: Ansible Configuration (`ansible.cfg`)

The `ansible.cfg` at the root defines DSOM-standard settings.
**Important:** `host_key_checking = False` is set for dynamic inventories, but ensure your network is secured at the perimeter level.

### Step 3: Modifying `inventory/hosts.yml`

Update the placeholder `hosts.yml` with the actual IP addresses of your Elastic Stack nodes.
Remember: This file must NOT contain plaintext passwords or secrets.

### Step 4: Group Variables

Place variables applied to ALL hosts in `inventory/group_vars/all.yml` (create this file if needed).

### Step 5: Ansible Vault (Secrets Management)

Encrypt secrets required for Elastic Stack (like `elastic_password`, certificates passphrases) using `ansible-vault`.

```bash
ansible-vault encrypt /path/to/secrets_draft.yml --output vault/production_secrets.yml

```

Vault encryption ensures secrets can never be accidentally committed to Git. The vault password itself is stored out-of-band.

---

## 4. Troubleshooting

### Problem: `UNREACHABLE! Failed to connect`

- **Cause**: SSH key not distributed to target node, or wrong `ansible_host` IP.
- **Fix**: Run `ssh-copy-id [USER]@[HOST]` from your Tier 2 Dev Bridge, then retry the ping.

### Problem: `MODULE FAILURE: No Python interpreter found`

- **Cause**: Python 3 not installed on target node.
- **Fix**: Install Python: `sudo apt install -y python3` (Debian/Ubuntu) or `sudo dnf install -y python3` (RHEL/Rocky).

### Problem: Playbook is not idempotent (changes on re-run)

- **Cause**: Task uses `command:` or `shell:` module without `changed_when: false` or `creates:` condition.
- **Fix**: Replace with idempotent modules. Use `changed_when: false` for read-only commands.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
