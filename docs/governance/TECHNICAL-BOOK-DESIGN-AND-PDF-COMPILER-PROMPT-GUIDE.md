---
okf_version: "0.2"
type: governance
title: "Terminal & Cloud PDF Compilation Master Prompt & Reference Guide"
timestamp: "2026-09-30T00:00:00Z"
generated: "2026-09-30T00:00:00Z"
verified: "2026-09-30T00:00:00Z"
status: "verified"
stale_after: "2027-09-30T00:00:00Z"
sources:
  - "AGENTS.md"
  - ".agents/AGENTS.md"
topics: ["governance", "pdf-compilation", "weasyprint", "rule-11.16", "dsom"]
tags: ["pdf", "weasyprint", "pandoc", "rule-11.16", "compilation", "ebook"]
description: "Master prompt and reference guide for compiling publication-grade PDFs from Markdown using native Linux WeasyPrint and Pandoc toolchains under DSOM Rule 11.16."
resource: "file:///docs/governance/TECHNICAL-BOOK-DESIGN-AND-PDF-COMPILER-PROMPT-GUIDE.md"
---

# Terminal & Cloud PDF Compilation Master Prompt & Reference Guide

> **Classification:** DSOM Rule 11 & Rule 11.16 — Technical Book Design & Linux-Native PDF Compilation
> **Author:** Harisfazillah Jamel (LinuxMalaysia)
> **Date:** 30 September 2026
> **Purpose:** Self-contained prompt to reproduce publication-grade PDFs from Markdown using the full Linux toolchain

---

## Rule 11.16: Linux-Native PDF Compilation Mandate (WeasyPrint / Typst Engine)

When compiling technical documentation suites, forensic audit reports, or executive handbooks into publication-grade PDFs in Linux and WSL2 environments:

1. **Zero Windows Host Dependency:**
   - The AI and compilation pipelines are strictly prohibited from depending on Windows host browser binaries (`chrome.exe`, `msedge.exe`) or Windows interop subprocesses (`cmd.exe /c start /wait`, `powershell.exe`) from within Linux/WSL2.
   - Eliminates Windows profile lockouts, headless drawing stalls, interop command timeouts (code 124), and cross-filesystem path translation overhead.

2. **Linux-Native Headless PDF Engines (WeasyPrint First):**
   - The preferred, primary PDF compilation engine in Linux is native **WeasyPrint** executed via `uv` (`uv run --with weasyprint weasyprint <input.html> <output.pdf>`) or native headless Linux tools (`typst`, `xelatex`).
   - The script must supply print-optimized CSS enforcing:
     - Pure white background (`#FFFFFF !important`).
     - Crisp, embedded standalone vector SVG diagrams (`<img src="*.svg">`).
     - Continuous multi-page table flow with repeated table headers (`thead { display: table-header-group; }`, `tr { page-break-inside: avoid; }`).
     - Standard A4 margins (`@page { size: A4 portrait; margin: 10mm 10mm 12mm 10mm; }`) and running footers (`Page X of Y`).

3. **Deterministic Output & Disk Verification:**
   - The compiler script must synchronously assert that the output PDF exists on disk and has a non-zero byte size (`size > 10 KB`).
   - If visual inspection is needed, verify pages locally using native Linux tools (`pdftoppm -png -r 150 <output.pdf> build/page`) without touching Windows.

---

## 1. Toolchain Overview

```
                    ┌──────────────────┐
                    │  Source Markdown  │  (OKF v0.2 frontmatter + report content)
                    │  docs/reports/   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Python Compiler  │  Strip frontmatter, strip footers,
                    │  tools/compile_*  │  stage SVG assets, write CSS
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │     Pandoc        │  Markdown → Standalone HTML
                    │  --standalone     │  Syntax highlighting: tango
                    │  --css style.css  │  Table of contents (optional)
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼───────┐  ┌──▼──────────┐  ┌▼──────────────┐
     │  WeasyPrint     │  │ Headless    │  │ Typst /       │
     │  (PREFERRED)    │  │ Chromium    │  │ XeLaTeX       │
     │  uv run --with  │  │ (Linux)     │  │ (Linux Native)│
     │  weasyprint     │  │             │  │               │
     └────────┬────────┘  └──────┬──────┘  └──────┬─────────┘
              │                  │                │
              └──────────────────┴────────────────┘
                             │
                    ┌────────▼─────────┐
                    │   docs/dist/     │
                    │  report.html     │  Standalone HTML (primary)
                    │  report.pdf      │  Publication-grade PDF
                    └──────────────────┘
```

### Required Software (Linux / WSL2)

| Tool | Install Command | Purpose |
|:-----|:----------------|:--------|
| **Pandoc** | `sudo apt install pandoc` | Markdown → Standalone HTML conversion |
| **uv** | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | Python package runner (no virtualenv needed) |
| **WeasyPrint** | `uv run --with weasyprint weasyprint` | HTML → PDF (CSS `@page` support, running headers/footers) |
| **Python 3.10+** | Pre-installed on most Linux | Compiler script execution |
| **Chromium** (optional) | `sudo apt install chromium-browser` | Alternative headless PDF renderer |

---

## 2. The Terminal & Cloud CSS Framework (Pure White Print Mode)

This is the **complete, production-tested CSS** used in all our reports:

```css
/* ═══════════════════════════════════════════════════════════════════
   Terminal & Cloud Design Framework — Print-Optimized Pure White
   DSOM Rule 11 & Rule 11.16 | Zero Ink Waste | A4 Portrait | 10mm Margins
   ═══════════════════════════════════════════════════════════════════ */

/* ──── Page Layout & Running Footer ──── */
@page {
    size: A4 portrait;
    margin: 10mm 10mm 12mm 10mm;
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748B;
    }
    @bottom-left {
        content: "PRIVATE AND CONFIDENTIAL (P&C) | Compile by: Harisfazillah Jamel";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748B;
    }
}

/* ──── Body Typography ──── */
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.8pt;
    line-height: 1.5;
    color: #0F172A;                         /* Dark Slate for maximum legibility */
    background-color: #FFFFFF !important;   /* Pure white — ZERO toner waste */
    margin: 0;
    padding: 0;
}

/* Hide Pandoc's auto-generated title block (we use custom covers) */
#title-block-header {
    display: none !important;
}

/* ──── Heading Hierarchy ──── */
h1 {
    font-size: 17pt;
    font-weight: 800;
    color: #0F172A;
    border-bottom: 2px solid #0284C7;       /* Sky Blue accent */
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h2 {
    font-size: 12pt;
    font-weight: 700;
    color: #1E3A8A;                         /* Linux Blue */
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h3 {
    font-size: 10pt;
    font-weight: 600;
    color: #0F172A;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

/* ──── Paragraphs ──── */
p {
    margin-top: 0;
    margin-bottom: 8px;
}

/* ──── Blockquotes (Blue Info Callout) ──── */
blockquote {
    border-left: 3.5px solid #0284C7;
    background-color: #F8FAFC;
    color: #334155;
    padding: 8px 12px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    font-size: 8.4pt;
}

/* ──── Tables (Multi-Page Flow + Zebra Stripes) ──── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 7.6pt;
    page-break-inside: auto;               /* Allow tables to span pages */
}

thead {
    display: table-header-group;            /* REPEAT headers on every page */
}

tr {
    page-break-inside: avoid;              /* Never split a row across pages */
}

th {
    background-color: #F1F5F9;
    color: #0F172A;
    font-weight: 700;
    text-align: left;
    padding: 5px 7px;
    border: 1px solid #CBD5E1;
}

td {
    padding: 5px 7px;
    border: 1px solid #E2E8F0;
    vertical-align: top;
}

tbody tr:nth-child(even) {
    background-color: #F8FAFC;             /* Light zebra striping */
}

/* ──── Code (Light Terminal Container) ──── */
code {
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 7.8pt;
    background-color: #F1F5F9;
    color: #0F172A;
    padding: 1.5px 3.5px;
    border-radius: 4px;
    border: 1px solid #E2E8F0;
}

pre {
    background-color: #F8FAFC !important;  /* Light gray — NOT dark/black */
    border: 1px solid #CBD5E1;
    border-left: 3.5px solid #1E3A8A;      /* Linux Blue left accent */
    border-radius: 6px;
    padding: 8px 10px;
    margin: 10px 0;
    overflow-x: auto;
    page-break-inside: avoid;
}

pre code {
    background-color: transparent !important;
    border: none;
    padding: 0;
    font-size: 7.4pt;
    color: #0F172A;
    line-height: 1.4;
    white-space: pre-wrap;                 /* Wrap long lines in PDF */
    word-break: break-all;
}

/* ──── Images & SVG Diagrams ──── */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 10px auto;
    page-break-inside: avoid;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    background-color: #FFFFFF;
}

/* ──── Horizontal Rules ──── */
hr {
    border: 0;
    height: 1px;
    background: #E2E8F0;
    margin: 16px 0;
}

/* ──── Callout Boxes (Warning / Note / Tip) ──── */
.callout-warning {
    background-color: #FEF2F2;            /* Light red pastel */
    border-left: 4px solid #EA580C;        /* Orange accent */
    padding: 12px 16px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
}

.callout-note {
    background-color: #F0F9FF;            /* Light blue pastel */
    border-left: 4px solid #0284C7;        /* Blue accent */
    padding: 12px 16px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
}

.callout-tip {
    background-color: #F0FDF4;            /* Light green pastel */
    border-left: 4px solid #16A34A;        /* Green accent */
    padding: 12px 16px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    page-break-inside: avoid;
}

/* ──── Card Accent Left Border Standard ──── */
.card-blue   { border-left: 5px solid #0284C7; background: #F8FAFC; padding: 10px; margin: 8px 0; }
.card-green  { border-left: 5px solid #16A34A; background: #F8FAFC; padding: 10px; margin: 8px 0; }
.card-amber  { border-left: 5px solid #CA8A04; background: #F8FAFC; padding: 10px; margin: 8px 0; }
.card-red    { border-left: 5px solid #DC2626; background: #F8FAFC; padding: 10px; margin: 8px 0; }
.card-purple { border-left: 5px solid #7C3AED; background: #F8FAFC; padding: 10px; margin: 8px 0; }
```

---

## 3. Checklist Before Every Compilation

- [ ] Source Markdown has NO raw `---` frontmatter (stripped by compiler)
- [ ] All SVG diagrams staged to both `build/` and `docs/dist/`
- [ ] CSS uses pure white `#FFFFFF` body background
- [ ] CSS uses light code containers `#F8FAFC` (NOT dark/black)
- [ ] Tables have `page-break-inside: auto` + `thead { display: table-header-group; }`
- [ ] No `<colgroup>` tags in HTML (strip them — they break table column widths)
- [ ] Running footer shows "Page X of Y" and report title
- [ ] Attribution: "Compile by: Harisfazillah Jamel"
- [ ] PDF file size > 10KB (assertion check)
- [ ] Visual inspection: no blank pages, no orphaned headings, no clipped tables

---
*Linux for NOSS Malaysia (Sovereign Governance) | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
