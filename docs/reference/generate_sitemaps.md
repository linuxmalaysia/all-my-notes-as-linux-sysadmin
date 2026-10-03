---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: generate_sitemaps.py reference
description: Dokumentasi OKF v0.2 bagi generate_sitemaps.md.
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
title: "Generate_Sitemaps"
description: "DSOM Reference document for Generate_Sitemaps."
type: "reference"
id: "docs/reference/generate_sitemaps.md"
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

# generate_sitemaps.py reference

Dynamic, unified sitemap and search engine optimiser (SEO) asset generator.

## Description

The `generate_sitemaps.py` utility builds the MkDocs static site. It compiles URLs across **GitHub Pages**, **Read the Docs**, and **GitBook** and outputs sitemaps and robots rules.

## Script path

`tools/generate_sitemaps.py`

## CLI signature

```bash
uv run python tools/generate_sitemaps.py

```

## Inputs

- **site/sitemap.xml:** Compiled sitemap parsed to discover fresh GitHub Pages web paths.
- **SUMMARY.md:** GitBook navigation parsed to identify all valid internal markdown resources.

## Outputs

Unified assets exported to three targets: root directory `./`, `docs/`, and built `site/`:
- **sitemap.txt:** Plaintext listing of all consolidated indexing URLs.
- **sitemap.xml:** Standard XML sitemap with synchronised `<lastmod>` tags.
- **robots.txt:** Robot guidelines mapping rules pointing directly to the sitemaps.

## Dependencies

- **Python:** 3.12+ (managed through standard `uv` environment).
- **mkdocs-material:** Static site generator package.
- **pyyaml:** Standard YAML parser.

## Internal Python API

### `find_repo_root()`

Locates the repository root by detecting the nearest `.git` ancestor.
- **Returns:** `pathlib.Path` pointing to root.
- **Raises:** `RuntimeError` if `.git` cannot be resolved.

### `build_mkdocs()`

Triggers compilation of static HTML site files.
- **Command executed:** `uv run --with mkdocs-material mkdocs build`.

### `parse_github_pages_urls()`

Parses the generated `site/sitemap.xml` XML structure.
- **Returns:** Sorted list of GitHub Pages string URLs.

### `to_gitbook_slug(path_str)`

Converts raw Markdown file paths to URL-safe lower-case slugs.
- **Arguments:** `path_str` (string relative markdown file path).
- **Returns:** String normalised GitBook URL slug.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
