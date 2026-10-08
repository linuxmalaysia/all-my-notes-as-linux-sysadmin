#!/usr/bin/env python3
# /// script
# dependencies = [
#   "weasyprint",
#   "markdown",
# ]
# ///
"""Enterprise HA Database Solution PDF Compiler Script (DSOM Rule 11 & Rule 11.16).

This module compiles the Enterprise High Availability Database Solution document into
publication-grade PDF and standalone HTML using Pandoc (or Python Markdown fallback) and native WeasyPrint.

Outputs:
    - docs/dist/solusi-pangkalan-data-kebolehseediaan-tinggi.html (standalone HTML)
    - docs/dist/solusi-pangkalan-data-kebolehseediaan-tinggi.pdf  (print-optimized PDF)
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def clean_markdown(src_path: Path, build_dir: Path) -> Path:
    """Strips OKF YAML frontmatter and DSOM footers from source Markdown.

    Args:
        src_path (Path): Path to the source Markdown document.
        build_dir (Path): Path to the intermediate build directory.

    Returns:
        Path: Path to the cleaned intermediate Markdown file.
    """
    content = src_path.read_text(encoding="utf-8")

    # Strip OKF YAML frontmatter only when both opening and closing delimiters exist
    if content.startswith("---"):
        parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            content = parts[2].lstrip()

    # Strip DSOM signature footer only when anchored at the end of the document
    content = re.sub(
        r"---\s*\n\*Linux for NOSS Malaysia[^\n]*(?:\n\*[^\n]*)*\s*\Z",
        "",
        content,
        flags=re.MULTILINE,
    ).strip()

    intermediate_md = build_dir / "ha_db_clean.md"
    intermediate_md.write_text(content, encoding="utf-8")
    return intermediate_md


def write_css(build_dir: Path) -> Path:
    """Writes print-optimized pure white CSS style for WeasyPrint rendering.

    Args:
        build_dir (Path): Path to the build directory.

    Returns:
        Path: Path to the generated CSS file.
    """
    css_content = """/* ═══════════════════════════════════════════════════════════════════
   Enterprise High Availability Database Blueprint — Print-Optimized Pure White
   DSOM Rule 11 & Rule 11.16 | Zero Ink Waste | A4 Portrait | 10mm Margins
   ═══════════════════════════════════════════════════════════════════ */

@page {
    size: A4 portrait;
    margin: 10mm 10mm 12mm 10mm;
    @bottom-right {
        content: "Muka Surat " counter(page) " dari " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #64748B;
    }
    @bottom-left {
        content: "DOKUMEN REKA BENTUK TEKNIKAL HA DB | Harisfazillah Jamel (LinuxMalaysia)";
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
    font-size: 16pt;
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
    css_file = build_dir / "style.css"
    css_file.write_text(css_content, encoding="utf-8")
    return css_file


def compile_html(
    md_path: Path, css_file: Path, build_dir: Path, dist_html: Path
) -> Path:
    """Converts cleaned Markdown to standalone HTML using Pandoc or Python markdown fallback.

    Args:
        md_path (Path): Path to intermediate cleaned Markdown file.
        css_file (Path): Path to CSS file.
        build_dir (Path): Path to build directory.
        dist_html (Path): Path to destination HTML file.

    Returns:
        Path: Path to the generated standalone HTML file.
    """
    pandoc_path = shutil.which("pandoc")
    if pandoc_path:
        pandoc_cmd = [
            pandoc_path,
            str(md_path),
            "-o",
            str(build_dir / "report.html"),
            "--standalone",
            "--css",
            "style.css",
            "--highlight-style=tango",
            "--metadata",
            "title=Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise",
        ]
        print("Running Pandoc...")
        subprocess.run(pandoc_cmd, check=True, cwd=build_dir)
    else:
        print("Pandoc not found. Using Python Markdown fallback...")
        import markdown

        md_text = md_path.read_text(encoding="utf-8")
        body_html = markdown.markdown(
            md_text,
            extensions=[
                "tables",
                "fenced_code",
                "codehilite",
                "toc",
                "attr_list",
                "def_list",
            ],
        )
        full_html = f"""<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="utf-8">
    <title>Solusi Pangkalan Data Kebolehseediaan Tinggi Enterprise</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{body_html}
</body>
</html>
"""
        (build_dir / "report.html").write_text(full_html, encoding="utf-8")

    html_content = (build_dir / "report.html").read_text(encoding="utf-8")
    html_content = re.sub(r"<colgroup>.*?</colgroup>", "", html_content, flags=re.DOTALL)
    (build_dir / "report.html").write_text(html_content, encoding="utf-8")

    shutil.copy(css_file, dist_html.parent / "style.css")
    shutil.copy(build_dir / "report.html", dist_html)
    print(f"HTML generated: {dist_html} ({dist_html.stat().st_size:,} bytes)")
    return dist_html


def compile_pdf(dist_html: Path, dist_pdf: Path) -> Path:
    """Converts standalone HTML into a publication-grade PDF using WeasyPrint.

    Args:
        dist_html (Path): Path to input standalone HTML file.
        dist_pdf (Path): Path to output PDF file.

    Returns:
        Path: Path to the generated PDF file.

    Raises:
        RuntimeError: If PDF generation fails or output file size is <= 10 KB.
    """
    wp_cmd = [
        sys.executable,
        "-m",
        "weasyprint",
        str(dist_html),
        str(dist_pdf),
    ]
    print("Running WeasyPrint...")
    subprocess.run(wp_cmd, check=True, timeout=120)

    if not dist_pdf.exists():
        raise RuntimeError("Output PDF file does not exist.")

    pdf_size = dist_pdf.stat().st_size
    if pdf_size <= 10240:
        raise RuntimeError(f"Output PDF size ({pdf_size:,} bytes) is at or below the 10KB limit.")

    print(f"PDF successfully generated: {dist_pdf} ({pdf_size:,} bytes)")
    return dist_pdf


def main() -> None:
    """Orchestrates the PDF compiler pipeline."""
    project_root = Path(__file__).resolve().parent.parent
    doc_src = (
        project_root
        / "manual"
        / "cu03"
        / "cu03-wa05-solusi-pangkalan-data-kebolehseediaan-tinggi.md"
    )
    build_dir = project_root / "build" / "ha_db_pdf"
    dist_dir = project_root / "docs" / "dist"

    dist_html = dist_dir / "solusi-pangkalan-data-kebolehseediaan-tinggi.html"
    dist_pdf = dist_dir / "solusi-pangkalan-data-kebolehseediaan-tinggi.pdf"

    build_dir.mkdir(parents=True, exist_ok=True)
    dist_dir.mkdir(parents=True, exist_ok=True)

    cleaned_md = clean_markdown(doc_src, build_dir)
    css_file = write_css(build_dir)
    compiled_html = compile_html(cleaned_md, css_file, build_dir, dist_html)
    compile_pdf(compiled_html, dist_pdf)


if __name__ == "__main__":
    main()
