---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: 💉 OKF Frontmatter Injector
description: Dokumentasi OKF v0.2 bagi SKILL.md.
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
okf_version: 0.1
type: agent_skill
title: okf-frontmatter-injector
description: Scans a target directory and automatically injects OKF v0.2 YAML frontmatter into Markdown files.
topics: [okf, frontmatter, yaml, compliance, markdown]
timestamp: 2026-07-04T10:00:00Z
---

# 💉 OKF Frontmatter Injector

## When to use this skill
Use this skill when the user asks to ensure documentation is OKF (Open Knowledge Format v0.2) compliant, or when importing new markdown files that lack standard YAML frontmatter headers.

## Instructions
1. This skill utilises a Python script embedded in `scripts/apply_okf_v02.py`.
2. Ask the user for the target directory to scan (default is the project root `.`).
3. Execute the script using `uv`:
   ```bash
   uv run --with pyyaml python scripts/apply_okf_v02.py <TARGET_DIRECTORY>
   ```
4. The script will automatically skip files that already possess frontmatter. It categorizes files dynamically based on their folder structure (e.g. `agent_skill`, `governance_protocol`, etc.).
5. Inform the user of the total number of files modified based on the script's output.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
