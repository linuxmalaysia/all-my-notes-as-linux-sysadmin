---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🏗️ DSOM Project Cloner Skill
description: Dokumentasi OKF v0.2 bagi dsom-project-cloner.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:43Z'
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
title: "Dsom Project Cloner"
description: "DSOM Reference document for Dsom Project Cloner."
type: "reference"
id: "docs/reference/skills/dsom-project-cloner.md"
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

# 🏗️ DSOM Project Cloner Skill

## When to use this skill
Use this skill when the user asks to create, clone, scaffold, or bootstrap a **new** DSOM project based on the current baseline repository (e.g., "Create a new project at D:\Projects\my-new-app").

## Prerequisites
- The user must provide the **absolute path** to the new target repository. Ask for it if not provided.

## Instructions

1. **Verify Target Path:** Ensure you have the absolute path for the new target repository from the user.
2. **Establish Directories:** Use your terminal execution tools (`run_command`) to create the mandatory folder structures in the target path:
   - `<target_path>/.agents/brain/wings`
   - `<target_path>/.agents/skills`
   - `<target_path>/docs/agent-configs`
   - `<target_path>/docs/governance`
   - `<target_path>/tools`
3. **Copy the Four Pillars:** Use your terminal execution tools (`run_command`) to copy the assets from the CURRENT repository (baseline) to the TARGET repository:
   - **Pillar A (The Engine):** Copy `.agents/AGENTS.md` to `<target_path>/.agents/`
   - **Pillar B (The Intelligence Payload):** Recursively copy all contents of `.agents/skills/` to `<target_path>/.agents/skills/`
   - **Pillar C (Governance & Configuration):**
     - Recursively copy `docs/agent-configs/` to `<target_path>/docs/agent-configs/`
     - Recursively copy `docs/governance/` to `<target_path>/docs/governance/`
     - Copy `docs/AI-AGENT-SKILLS-GUIDE.md` to `<target_path>/docs/`
     - Copy all `docs/HOWTO-*.md` files to `<target_path>/docs/`
   - **Pillar D (Ritual Scripts):** Recursively copy `tools/` to `<target_path>/tools/`
4. **Persona Injection Check:** Ask the user if they wish to automatically inject their persona using the `persona-injector` skill for the new project.
5. **Finalization:** Output a success message to the user, providing them with the initialization commands for their new workspace:
   - `bash tools/reanimate.sh` or `.\tools\reanimate.ps1`
   - `git add .`
   - `git commit -m "chore(dsom): scaffold genesis dsom architecture and AI skills"`


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
