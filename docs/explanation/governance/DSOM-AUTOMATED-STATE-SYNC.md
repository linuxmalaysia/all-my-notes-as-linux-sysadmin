---
spec_version: '0.2'
okf_version: '0.2'
type: governance_protocol
title: DSOM Automated State Sync
description: Dokumentasi OKF v0.2 bagi DSOM-AUTOMATED-STATE-SYNC.md.
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
title: "Dsom Automated State Sync"
description: "DSOM Concept document for Dsom Automated State Sync."
type: "concept"
id: "docs/explanation/governance/DSOM-AUTOMATED-STATE-SYNC.md"
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

# DSOM Automated State Sync

## 1. Vectorized Memory Tiering

Instead of pushing an entire project history into every prompt, DSOM categorizes information into distinct operational layers:
*   **Active Layer**: Houses only the immediate, high-priority variables for the current task.
*   **Compressed Layer**: Stores foundational rules and past decisions as dense, key-value indices (`.agents/brain/current_state.dsom`).
*   **Archival Layer**: Offloads long-term data to the Git history and Sovereign Markdown Palace.

## 2. Semantic Compaction (Token Distillation)

DSOM applies a "distillation loop" using an automated GitHub Action. 
When a Pull Request is merged, `.github/workflows/dsom-pr-sync.yml` triggers `.github/scripts/action_update_dsom.py`.
This script calls an LLM (e.g. OpenAI) to review the PR diff and update `.agents/brain/current_state.dsom` strictly in OKF v0.1 format, eliminating redundant conversational fluff and appending only critical architectural decisions.

## 3. Configuration

- Ensure the `OPENAI_API_KEY` secret is available to the GitHub Action.
- The state is persisted in `.agents/brain/current_state.dsom`.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
