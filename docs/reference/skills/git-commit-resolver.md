---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🔍 Git Commit Resolver Skill
description: Dokumentasi OKF v0.2 bagi git-commit-resolver.md.
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
title: "Git Commit Resolver"
description: "DSOM Reference document for Git Commit Resolver."
type: "reference"
id: "docs/reference/skills/git-commit-resolver.md"
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

# 🔍 Git Commit Resolver Skill

## Purpose
The DSOM repository has undergone Git history rewrites (e.g., using `git-filter-repo` for security sanitization). This process permanently alters cryptographic commit IDs (SHA-1 hashes) while leaving commit messages, dates, and authors intact.
As a result, some commit IDs stored in the `.agents/brain/` memory (e.g., in `palace_registry.md` or `HISTORY.md`) may become **invalid or orphaned**. 

## When to use this skill
Trigger this skill whenever you attempt to reference, checkout, or view a Git commit ID (e.g., `git show <hash>`) and Git returns an error indicating the commit does not exist or is invalid.

## Execution Steps

### 1. Identify the Context
If a commit hash is invalid, do not assume the work was lost. Find the context of the commit by reading the surrounding text in the brain artifact or ledger to determine the **Commit Subject/Message** or **Date**.

### 2. Search Git Log by Message
Use the `git log` command with the `--grep` flag to search for the original commit message.

```bash
git log --grep="<part of the commit message>" --oneline
```
*Example:* If the old hash `abc1234` was for "docs: update gitbook architecture", run:
`git log --grep="update gitbook architecture" --oneline`

### 3. Extract the New Hash
The command will return the *new* valid commit hash associated with that exact same work. Use this new hash for your operations.

### 4. Self-Healing (Optional but Recommended)
If you are actively editing a brain artifact or ledger when you discover a broken hash, proactively update the document to replace the old broken hash with the newly resolved valid hash to heal the Sovereign Memory.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
