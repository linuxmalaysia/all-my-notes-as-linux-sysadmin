---
spec_version: '0.2'
okf_version: '0.2'
type: governance_protocol
title: '🛡️ CRISP² Operational Strategy: The Five Pillars of Persistence'
description: Dokumentasi OKF v0.2 bagi CRISP2-OPERATIONAL-STRATEGY.md.
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
title: "Crisp2 Operational Strategy"
description: "DSOM Concept document for Crisp2 Operational Strategy."
type: "concept"
id: "docs/explanation/governance/CRISP2-OPERATIONAL-STRATEGY.md"
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

# 🛡️ CRISP² Operational Strategy: The Five Pillars of Persistence

**Author:** Harisfazillah Jamel  
**Version:** 1.1.0
**License:** GPLv3  
**Status:** Core Framework Documentation

---

## 1. Introduction

The **CRISP² Matrix** (Context-Record-Iteration-Single-Purpose-Pedagogy) is the operational engine of the DSOM protocol. It provides a structured methodology to prevent **Context Decay**—the phenomenon where an AI gradually loses track of complex architectural logic over a long conversation.

---

## 2. The Five Pillars (Generic Tasks)

### 🧩 I. Context Awareness (The Anchor)

Before any code is written, the AI must "synchronise" with the physical state of the repository.

* **The Action:** Reading `.agents/brain/` artifacts (`palace_registry.md`, `task.md`, `walkthrough.md`).
* **The Goal:** Ensure the AI's internal "Mental Anchor" matches the Human Architect's last saved state.
* **Human Check:** Always ask: *"What is our current Mental Anchor?"*

### 📝 II. Review & Record (The Audit Trail)

Logic must be committed to text before it is committed to code.

* **The Action:** Updating `walkthrough.md` and Palace `closet.md` files with the reasoning behind a change.
* **The Goal:** Create a permanent spatial record of *why* a decision was made, which serves as the "memory" for the next AI session.
* **DBP-Standard:** *Rekod dahulu, kod kemudian.*

### 🔄 III. Iteration (Atomic Git Hygiene)

Large, monolithic changes are the primary cause of architectural drift and bugs.

* **The Action:** Modifying only one file at a time; one commit per sub-task.
* **The Goal:** Maintain **High-Availability (HA)** of the codebase. If an error occurs, we can roll back a single "atomic" step.
* **Commit Format:** `type(scope): descriptive message` (e.g., `feat(entities): add validation logic`).

### 🎯 IV. Single-purpose Prompts (The Focus)

AI models perform best when given a narrow, high-depth task rather than a broad, shallow one.

* **The Action:** Focusing the prompt on one specific **Clean Architecture** layer (e.g., just the Entities).
* **The Goal:** Prevent the AI from hallucinating dependencies between unrelated layers.

### 🧠 V. Pedagogical Logic (The 'Why')

Code without explanation is "technical debt" in a multi-agent environment.

* **The Action:** Explaining the security, performance, or structural logic *before* providing the code block.
* **The Goal:** Ensure the Human Architect and the AI are in total agreement on the underlying theory.
* **Malay:** *Terangkan logik (Kenapa) sebelum kod (Apa).*

---

## 3. Hierarchy Mapping (CRISP-DM Integration)

| Level | Description | CRISP² Application |
| :--- | :--- | :--- |
| **L1** | **Phase** | The current stage of the project (e.g., Phase 2: Cognitive Core). |
| **L2** | **Generic Tasks** | The 5 CRISP Pillars described in this document. |
| **L3** | **Specialised Tasks** | Applying CRISP to specific tools (e.g., `reanimate-claude.sh`). |
| **L4** | **Process Instance** | The actual content of `walkthrough.md` for today's session. |

---

## 4. Troubleshooting Context Decay

If the AI begins to repeat errors or ignore the CRISP Strategy:

1. **STOP** the current dialogue.
2. **SYNC** local files to GitHub.
3. **REANIMATE** using the `REANIMATION-PROMPT-TEMPLATE.md`.

---
*Generated for the DSOM Sovereign Environment. UK English & DBP-standard Malay Enforced.*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
