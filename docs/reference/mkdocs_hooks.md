---
title: "Mkdocs_Hooks"
description: "DSOM Reference document for Mkdocs_Hooks."
type: "reference"
id: "docs/reference/mkdocs_hooks.md"
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

# mkdocs_hooks.py reference

Custom MkDocs page compilation hook for relative Markdown URL rewriting.

## Description

The `mkdocs_hooks.py` script intercepts static pages during compilation. It strips unnecessary `docs/` prefixes and normalises repository-root relative paths (`../../` to `../`), ensuring links work seamlessly on both GitHub.com and built HTML servers.

## Script path

`tools/mkdocs_hooks.py`

## CLI integration

Automated by the static site compiler. Registered inside `mkdocs.yml`:

```yaml
hooks:
  - tools/mkdocs_hooks.py

```

## Functions

### `on_page_markdown(markdown, page, config, files)`

Interceptors registered by the MkDocs lifecycle.
- **Arguments:** `markdown` content (string), `page` metadata, `config` context, `files` collection.
- **Returns:** Modified Markdown string with rewritten relative URLs.

## Rewriting rules

- **External links:** Keeps `http://`, `https://`, `mailto:`, `ftp:`, and `#` anchor links unchanged.
- **`docs/` prefix:** Strips `docs/` from relative paths (e.g. `docs/governance/PROTOCOL.md` becomes `governance/PROTOCOL.md`).
- **`../../` prefix:** Normalises double-parent directories (e.g. `../../AGENTS.md` becomes `../AGENTS.md`).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
