---
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

Introduced by Google Cloud on June 12, 2026, the **Open Knowledge Format (OKF)** is a vendor-neutral, open specification designed to solve the "context decay" problem in AI-driven development. 

Historically, AI agents struggle because organizational knowledge is scattered or formatted poorly. OKF creates a standardised "common language" by structuring knowledge so that it is equally readable by human engineers and autonomous AI agents. By enforcing YAML frontmatter and strict architectural placement, OKF allows AI to map out knowledge domains without reading entire files blindly.

---

## OKF in Linux for NOSS Malaysia

In the **Linux for NOSS Malaysia** project, our goal is to build an open-source, AI-ready repository mapping Linux skills to the Malaysian National Occupational Skills Standard (NOSS). 

To ensure AI agents can navigate our massive syllabus, we have strictly adopted OKF v0.2 across our **Sovereign Markdown Palace** architecture.

### 1. The Public Knowledge Base (`openwiki/`)

Our primary syllabus content lives in the `openwiki/` directory. Each NOSS Competency Unit (CU) is distilled into a single markdown node. To be OKF-compliant, every node must begin with a structured YAML frontmatter block.

**Example implementation in `openwiki/topic-01-linux-desktop-and-basics.md`:**
```yaml
---
okf_version: 0.2
type: documentation
title: "topic-01-linux-desktop-and-basics"
timestamp: "2026-08-16T08:00:00Z"
topics: ["linux-desktop", "cu01"]
tags: ["linux", "desktop", "cu01"]
description: "Silibus asas Sistem Operasi Linux (Desktop, FHS, APT/YUM) dipetakan kepada NOSS CU01."
resource: "file:///openwiki/topic-01-linux-desktop-and-basics.md"
---
```

### 2. AI Agent Skills (`.agents/skills/`)

Repositori ini turut menyimpan kemahiran AI berfungsi yang dipetakan kepada modul NOSS Tahap 3. Arahan yang mengawal cara AI melaksanakan tugasan (fail `SKILL.md`) juga mematuhi standard OKF v0.2 secara ketat.

We maintain the exact same schema for our skills to ensure the AI knows it is reading an executable skill rather than static documentation:

```yaml
---
okf_version: 0.2
type: skill
title: "cu03-wa04-perform-core-server-configurations"
timestamp: "2026-08-16T08:00:00Z"
topics: ["linux-server", "cu03"]
tags: ["linux", "server", "cu03"]
description: "Skill to perform core Linux server configuration."
resource: "file:///.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md"
---
```

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

By adopting OKF v0.1 alongside our strict Dual-License footers, the **Linux for NOSS Malaysia** repository is more than just a collection of Markdown files. It is a highly optimized, machine-readable knowledge graph that allows external AI agents to digest, update, and contribute to the national skills syllabus with extreme accuracy and minimal context loss.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
