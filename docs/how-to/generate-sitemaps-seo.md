---
title: "Generate Sitemaps Seo"
description: "DSOM Guide document for Generate Sitemaps Seo."
type: "guide"
id: "docs/how-to/generate-sitemaps-seo.md"
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

# Generate SEO assets and sitemaps

This guide explains how to compile search engine optimisation (SEO) assets, text listings, standard XML structures, and crawlers rules.

## Prerequisites

- **Python 3.12+** and **`uv`** installed.
- Valid `SUMMARY.md` file registered at the repository root.

## Step 1: Run sitemap compilation

Run the sitemap script from the repository root. This command builds the static site, crawls local files, translates GitBook paths, and saves outputs:

```bash
uv run --with mkdocs-material python tools/generate_sitemaps.py

```

## Step 2: Confirm generated assets

Verify that sitemap files have been populated under three distinct paths: root directory `./`, `docs/`, and `site/`.

### Check plaintext URL indices

```bash
head -n 5 sitemap.txt

```

### Check XML structure

```bash
head -n 10 sitemap.xml

```

## Step 3: Run regression validation

Execute standard unit test suites to confirm correctness of derived Read the Docs links and GitBook canonical formats:

```bash
uv run --with pyyaml --with pytest pytest tests/test_seo_sitemaps.py tests/test_sitemap_seo_generator_skill.py

```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
