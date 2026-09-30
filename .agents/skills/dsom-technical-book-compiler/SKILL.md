---
okf_version: 0.1
name: dsom-technical-book-compiler
description: "Compiles technical books, executive reports, and handbooks into publication-grade PDFs and standalone HTML using Pandoc and native WeasyPrint under DSOM Rule 11 and Rule 11.16."
topics: ["pdf", "compilation", "weasyprint", "pandoc", "rule-11.16", "dsom"]
tags: ["pdf", "compilation", "weasyprint", "pandoc", "ebook", "rule-11.16"]
type: skill
---

# 📚 DSOM Technical Book & PDF Compiler

## Overview
This skill governs the compilation of publication-grade PDF ebooks, technical books, executive handbooks, and forensic audit reports directly within Linux and WSL2 environments using Pandoc and WeasyPrint, adhering to DSOM Rule 11 and Rule 11.16.

## Rule 11.16 Execution Directives
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

## Procedure & Usage

### 1. Markdown → Standalone HTML Conversion
```bash
cp build/style.css docs/dist/style.css
pandoc build/report_clean.md \
  -o docs/dist/report.html \
  --standalone \
  --css=style.css \
  --highlight-style=tango \
  --metadata title="Report Title"
```

### 2. Standalone HTML → Publication PDF Conversion via WeasyPrint
```bash
uv run --with weasyprint weasyprint \
  docs/dist/report.html \
  docs/dist/report.pdf
```

### 3. Automated Python Compiler Script
Use `tools/compile_pdf.py` or similar Python scripts invoking `pandoc` and `weasyprint` via `subprocess.run([sys.executable, "-m", "weasyprint", ...])` or direct `uv` invocation.

## Security & Governance
- Ensures zero Windows host binary calls from Linux environments.
- Enforces pure white print background (`#FFFFFF !important`) for zero ink waste.
- Embeds verified SVG vector assets cleanly without black fills or distorted paths.

---
*Linux for NOSS Malaysia (Sovereign AI Protocol) | Harisfazillah Jamel (LinuxMalaysia) | 2026-09-30*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
