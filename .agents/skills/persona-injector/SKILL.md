---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: 🎭 Persona Injector
description: Dokumentasi OKF v0.2 bagi SKILL.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:45Z'
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
title: persona-injector
description: Guides a user to define their Sovereign Persona and safely injects it into the agent's core AGENTS.md rulebook.
topics: [persona, profile, identity, dsom, agent]
timestamp: 2026-07-04T10:00:00Z
---

# 🎭 Persona Injector

## When to use this skill
Use this skill when a user says "I want to inject my persona", "make the AI act like me", or "setup my identity matrix".

## Instructions
1. **Fetch Template:** Read the `docs/agent-configs/SOVEREIGN-PERSONA-TEMPLATE.md` file using your file reading tools.
2. **Interview User:** Present the categories from the template to the user (e.g., Identity, Core Profile, Writing Style, Architectural Principles). Ask them to provide their specifics either all at once or step-by-step.
3. **Format Matrix:** Once the user has provided their details, format the data exactly as defined in the `<RULE[PERSONA.md]>` OKF block from the template.
4. **Inject Rule:** Use your file editing tools to append this formatted block to the bottom of `.agents/AGENTS.md`.
5. **Verify:** Confirm to the user that the AI operating in this workspace has now permanently inherited their identity, constraints, and linguistic DNA.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
