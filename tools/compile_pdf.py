#!/usr/bin/env python3
# /// script
# dependencies = [
#   "weasyprint",
# ]
# ///
"""
Compile Terminal & Cloud PDF Compilation Master Prompt & Reference Guide into publication-grade PDF.
DSOM Rule 11 & Rule 11.16 (Terminal & Cloud Design, Pure White Print, 8mm Margins, WeasyPrint Native).

Outputs:
  - docs/dist/terminal-cloud-pdf-compilation-guide.html (standalone HTML)
  - docs/dist/terminal-cloud-pdf-compilation-guide.pdf  (print-optimized PDF)
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOC_SRC = PROJECT_ROOT / "docs" / "governance" / "TECHNICAL-BOOK-DESIGN-AND-PDF-COMPILER-PROMPT-GUIDE.md"
BUILD_DIR = PROJECT_ROOT / "build" / "pdf_compilation_guide"
DIST_DIR = PROJECT_ROOT / "docs" / "dist"

DIST_HTML = DIST_DIR / "terminal-cloud-pdf-compilation-guide.html"
DIST_PDF = DIST_DIR / "terminal-cloud-pdf-compilation-guide.pdf"

BUILD_DIR.mkdir(parents=True, exist_ok=True)
DIST_DIR.mkdir(parents=True, exist_ok=True)

# Step 1: Read and clean source Markdown
content = DOC_SRC.read_text(encoding="utf-8")

# Strip OKF YAML frontmatter
if content.startswith("---"):
    parts = content.split("---", 2)
    if len(parts) >= 3:
        content = parts[2].strip()

# Strip DSOM signature footers
content = re.sub(
    r'---\s*\n\*Linux for NOSS Malaysia[^\n]*\n(?:\*[^\n]*\n?)*',
    '', content
).strip()

intermediate_md = BUILD_DIR / "guide_clean.md"
intermediate_md.write_text(content, encoding="utf-8")

# Step 2: Write CSS file
css_content = """/* ═══════════════════════════════════════════════════════════════════
   Terminal & Cloud Design Framework — Print-Optimized Pure White
   DSOM Rule 11 & Rule 11.16 | Zero Ink Waste | A4 Portrait | 10mm Margins
   ═══════════════════════════════════════════════════════════════════ */

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

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.8pt;
    line-height: 1.5;
    color: #0F172A;
    background-color: #FFFFFF !important;
    margin: 0;
    padding: 0;
}

#title-block-header {
    display: none !important;
}

h1 {
    font-size: 17pt;
    font-weight: 800;
    color: #0F172A;
    border-bottom: 2px solid #0284C7;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h2 {
    font-size: 12pt;
    font-weight: 700;
    color: #1E3A8A;
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

p {
    margin-top: 0;
    margin-bottom: 8px;
}

blockquote {
    border-left: 3.5px solid #0284C7;
    background-color: #F8FAFC;
    color: #334155;
    padding: 8px 12px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    font-size: 8.4pt;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 7.6pt;
    page-break-inside: auto;
}

thead {
    display: table-header-group;
}

tr {
    page-break-inside: avoid;
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
    background-color: #F8FAFC;
}

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
    background-color: #F8FAFC !important;
    border: 1px solid #CBD5E1;
    border-left: 3.5px solid #1E3A8A;
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
    white-space: pre-wrap;
    word-break: break-all;
}

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

hr {
    border: 0;
    height: 1px;
    background: #E2E8F0;
    margin: 16px 0;
}
"""

css_file = BUILD_DIR / "style.css"
css_file.write_text(css_content, encoding="utf-8")

# Step 3: Pandoc — Markdown → Standalone HTML
pandoc_cmd = [
    "pandoc",
    str(intermediate_md),
    "-o", str(BUILD_DIR / "report.html"),
    "--standalone",
    "--css", "style.css",
    "--highlight-style=tango",
    "--metadata", "title=Terminal & Cloud PDF Compilation Master Prompt & Reference Guide"
]
print("Running Pandoc...")
subprocess.run(pandoc_cmd, check=True, cwd=BUILD_DIR)

html_content = (BUILD_DIR / "report.html").read_text(encoding="utf-8")
html_content = re.sub(r'<colgroup>.*?</colgroup>', '', html_content, flags=re.DOTALL)
(BUILD_DIR / "report.html").write_text(html_content, encoding="utf-8")

shutil.copy(css_file, DIST_DIR / "style.css")
shutil.copy(BUILD_DIR / "report.html", DIST_HTML)
print(f"HTML generated: {DIST_HTML} ({DIST_HTML.stat().st_size:,} bytes)")

# Step 4: WeasyPrint — HTML → PDF
try:
    wp_cmd = [
        sys.executable, "-m", "weasyprint",
        str(DIST_HTML),
        str(DIST_PDF)
    ]
    print("Running WeasyPrint...")
    subprocess.run(wp_cmd, check=True, timeout=120)

    if DIST_PDF.exists() and DIST_PDF.stat().st_size > 10240:
        print(f"PDF successfully generated: {DIST_PDF} ({DIST_PDF.stat().st_size:,} bytes)")
    else:
        raise RuntimeError("Output PDF does not exist or is under 10KB assertion limit.")
except Exception as e:
    print(f"PDF Compilation Error: {e}")
    sys.exit(1)
