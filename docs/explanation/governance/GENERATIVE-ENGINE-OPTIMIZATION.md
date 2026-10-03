---
spec_version: '0.2'
okf_version: '0.2'
type: governance_protocol
title: Generative Engine Optimization (GEO)
description: Dokumentasi OKF v0.2 bagi GENERATIVE-ENGINE-OPTIMIZATION.md.
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
title: "Generative Engine Optimization"
description: "DSOM Concept document for Generative Engine Optimization."
type: "concept"
id: "docs/explanation/governance/GENERATIVE-ENGINE-OPTIMIZATION.md"
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

# Generative Engine Optimization (GEO)

This governance document establishes the standard for architecting all documentation within the DSOM framework to be natively "AI-ready." The digital landscape has shifted from traditional deterministic search (SEO) to probabilistic information synthesis (GEO/AEO).

## 1. The GEO Paradigm

Answer engines (e.g., ChatGPT, Perplexity, Claude, Google AI Overviews) synthesize contextualized answers directly. To ensure our documentation is extracted, cited, and summarized accurately, we must optimize for **machine readability, source attribution, and direct answerability**.

## 2. Empirically Validated GEO Strategies

All human contributors and AI agents must actively employ the following content strategies when drafting documentation:
- **Quotation Addition (+41% lift):** Provide discrete, attributable human expertise.
- **Statistics Addition (+31-38% lift):** Replace vague qualitative prose with specific, verifiable data points.
- **Cite Sources (+35% lift):** Inject inline references to credible third parties.
- **Fluency Optimization (+26% lift):** Improve stylistic clarity to make text mechanically easier for the LLM to parse.
- **Authoritative Tone (+21% lift):** Remove hedging and uncertain phrasing, which models interpret as low-confidence data.

*Note: Keyword stuffing actively harms visibility by triggering AI trust-layer penalties (-8% to -12% drop).*

## 3. Content Creation & Hierarchy for AI Ingestion

- **Atomic Intent:** Documentation must consist of atomic pages with a singular, clear intent.
- **Context Window Chunking:** Keep sections concise (max 200–400 words) to prevent the model from truncating vital information.
- **Semantic Hierarchy:** Formulate H2 subheadings directly as common user questions (e.g., "How to rotate an API key").
- **Colocation of Concepts:** Place examples (code snippets, inputs/outputs) in immediate proximity to the theoretical explanation to reduce cognitive load.

## 4. Machine Readability & The llms.txt Standard

LLMs consume raw text. Parsing HTML and complex DOM structures wastes computational resources. DSOM strictly enforces **Markdown** as the native language of knowledge representation.
To guide AI crawlers, the repository must maintain an llms.txt specification at the root directory. This plain-text file acts as an XML sitemap for machine intelligence, providing a curated, high-signal map of our content.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
