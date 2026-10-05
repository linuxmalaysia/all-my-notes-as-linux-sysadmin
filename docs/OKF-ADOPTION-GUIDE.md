---
spec_version: '0.2'
okf_version: '0.2'
type: documentation
title: Open Knowledge Format (OKF) Adoption Guide
description: Dokumentasi OKF v0.2 bagi OKF-ADOPTION-GUIDE.md.
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
title: "Okf Adoption Guide"
description: "DSOM Guide document for Okf Adoption Guide."
type: "guide"
id: "docs/OKF-ADOPTION-GUIDE.md"
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

# Open Knowledge Format (OKF) Adoption Guide

## What is the Open Knowledge Format (OKF)?

Introduced by Google Cloud Platform, the **Open Knowledge Format (OKF v0.2)** is an open, vendor-neutral specification designed for representing *knowledge*: the metadata, context, trust signals, and curated insight surrounding data and systems.

OKF v0.2 addresses the key challenges of agent-maintained knowledge corpora:
1. **Provenance:** What was this created from, and how was it verified? (`sources`)
2. **Trust:** How much should I trust it? (`generated`, `verified`, trust tiers)
3. **Freshness:** Is it still true? (`stale_after`)
4. **Lifecycle:** Is it current? (`status`)
5. **Attestation:** Was this value/computation produced the sanctioned way? (`Attested Computation`)

---

## OKF v0.2 Core Frontmatter Specification

Every non-reserved OKF v0.2 concept document consists of YAML frontmatter delimited by `---` and a free-form Markdown body. Note that reserved files `index.md` and `log.md` contain no frontmatter, with one exception: a bundle-root `index.md` MAY carry an `okf_version: "0.2"` key in frontmatter.

### Required & Recommended Fields

```yaml
---
spec_version: "0.2"
okf_version: "0.2"
type: explanation                  # REQUIRED: Concept type (e.g. guide, reference, explanation, agent_skill, Attested Computation)
title: "Topik 01: Desktop Linux"   # Display name
description: "Silibus asas Sistem Operasi Linux dipetakan kepada NOSS CU01."
resource: "openwiki/topic-01-linux-desktop-and-basics.md"  # URI or bundle-relative path
tags: [linux, desktop, cu01]
status: stable                     # draft | stable | deprecated
stale_after: "2027-12-31T00:00:00Z"
generated:
  by: okf_tooling/v0.2
  at: "2026-10-02T08:43:43Z"
verified:
  - by: "human:harisfazillah"
    at: "2026-10-02T09:00:00Z"
sources:
  - id: internal-legal-notice
    title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
    author: "human:harisfazillah"
    resource: docs/legal-notice.md
  - id: google-okf-v02-spec
    title: Open Knowledge Format v0.2 Specification
    author: "team:google-cloud-data-analytics"
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
---
```

### Actor Identification Convention (§7)

Identity strings in `generated.by` and `verified[].by` follow standard prefixes:
- `<producer>/<version>` for agents/tools (e.g., `okf_tooling/v0.2`, `jules_agent/v1.0`).
- `human:<id>` for people (e.g., `human:harisfazillah`).
- `process:<id>` for automated CI/CD processes (e.g., `process:nightly-audit`).

### Attested Computation Concepts (§10)

For executable playbooks, automation tools, or calculations, use `type: Attested Computation`:

```yaml
---
spec_version: "0.2"
okf_version: "0.2"
type: Attested Computation
title: "Pemasangan Pakej Linux Automated"
description: "Skrip automasi bagi pemasangan pakej Linux NOSS."
status: stable
runtime: python                    # e.g., python, ansible, bigquery, bash
parameters:
  - { name: target_environment, type: string, required: true }
executor:
  resource: references/skills/install_packages.py
  receipt: [exit_code, stdout, stderr]
attester:
  resource: tests/test_okf_compliance.py
generated:
  by: okf_tooling/v0.2
  at: "2026-10-02T08:43:43Z"
sources:
  - id: internal-legal-notice
    resource: docs/legal-notice.md
---

# Computation

```python
import sys
import subprocess

target_env = sys.argv[1] if len(sys.argv) > 1 else "production"
subprocess.run(["echo", f"Installing NOSS Linux packages into {target_env}"], check=True)
subprocess.run(["apt-get", "install", "-y", "curl"], check=True)
```

---

## OKF in Linux for NOSS Malaysia

In the **Linux for NOSS Malaysia** project, our goal is to build an open-source, AI-ready repository mapping Linux skills to the Malaysian National Occupational Skills Standard (NOSS).

To ensure AI agents can navigate our massive syllabus, we have strictly adopted OKF v0.2 across our **Sovereign Markdown Palace** architecture.

### 1. The Public Knowledge Base (`openwiki/`)

Our primary syllabus content lives in the `openwiki/` directory. Each NOSS Competency Unit (CU) is distilled into a single markdown node. To be OKF-compliant, every node must begin with a structured YAML frontmatter block.

### 2. AI Agent Skills (`.agents/skills/`)

Repositori ini turut menyimpan kemahiran AI berfungsi yang dipetakan kepada modul NOSS Tahap 3. Arahan yang mengawal cara AI melaksanakan tugasan (fail `SKILL.md`) juga mematuhi standard OKF v0.2 secara ketat (`type: agent_skill`).

---

## The Sovereign Dual-License Footer

As established in the AI Constitution (Rule 7), this project operates strictly under a **Dual-License model** (CC BY-SA 4.0 for content, MIT for code) to ensure public benefit (Fair Use).

To maintain legal compliance and verify that an AI generated the content correctly, **every OKF document must conclude with the official Sovereign Markdown Palace Footer**.

**Mandatory Footer Format:**
```markdown
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | [DATE]*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
```

## Conclusion

By adopting OKF v0.2 alongside our strict Dual-License footers, the **Linux for NOSS Malaysia** repository is a highly optimized, machine-readable knowledge graph that allows external AI agents to digest, update, and contribute to the national skills syllabus with extreme accuracy, proven trust signals, and minimal context loss.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
