# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "markdown",
#     "jinja2",
#     "pyyaml"
# ]
# ///
"""Penjana Tapak Web HTML Statik.

Modul ini mengurai fail indeks llms.txt dan menukar semua nod Markdown kepada
halaman HTML statik berserta gaya CSS dan templat Jinja2.
"""

import re
import shutil
from pathlib import Path

import markdown
import yaml
from jinja2 import Template

# Basic CSS for the static site
CSS_CONTENT = """
:root {
    --primary-color: #2563eb;
    --text-color: #333;
    --bg-color: #f9fafb;
    --card-bg: #ffffff;
    --border-color: #e5e7eb;
}
body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    margin: 0;
    padding: 0;
}
header {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem 2rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
header a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.2rem;
}
.container {
    max-width: 1000px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: var(--card-bg);
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border-radius: 8px;
}
a { color: var(--primary-color); text-decoration: none; }
a:hover { text-decoration: underline; }
pre { background: #1e1e1e; color: #d4d4d4; padding: 1rem; border-radius: 6px; overflow-x: auto; }
code { font-family: 'Fira Code', monospace; font-size: 0.9em; background: #f1f5f9; padding: 0.2rem 0.4rem; border-radius: 4px; color: #e11d48; }
pre code { background: transparent; color: inherit; padding: 0; }
table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; }
th, td { border: 1px solid var(--border-color); padding: 0.75rem; text-align: left; }
th { background-color: #f8fafc; font-weight: 600; }
blockquote { border-left: 4px solid var(--primary-color); margin: 1.5rem 0; padding: 0.5rem 1rem; background: #eff6ff; color: #1e3a8a; }
.footer { margin-top: 3rem; text-align: center; color: #64748b; font-size: 0.9rem; padding-top: 1rem; border-top: 1px solid var(--border-color); }
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - NOSS Linux Malaysia</title>
    <link rel="stylesheet" href="{{ root_prefix }}assets/style.css">
</head>
<body>
{% if frontmatter %}
    <!--
    OKF Metadata:
{{ frontmatter }}
    -->
{% endif %}
    <header>
        <a href="{{ root_prefix }}index.html">Sovereign Markdown Palace (Web)</a>
    </header>
    <div class="container">
        {{ content }}
        <div class="footer">
            <p>Janaan Automatik DSOM AI | Laman Web Statik Tidak Rasmi</p>
        </div>
    </div>
</body>
</html>
"""

def parse_llms_txt(llms_txt_path: Path) -> list[str]:
    """Urai fail indeks llms.txt dan ekstrak laluan fail Markdown relatif.

    Args:
        llms_txt_path (Path): Laluan ke fail indeks llms.txt.

    Returns:
        list[str]: Senarai laluan fail relatif yang diekstrak daripada pautan Markdown.
    """
    paths = []
    link_pattern = re.compile(r'\[.*?\]\((.*?\.md)\)')
    if not llms_txt_path.exists():
        return paths
    with open(llms_txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = link_pattern.search(line)
            if match:
                paths.append(match.group(1).strip())
    return paths

def fix_internal_links(markdown_text: str) -> str:
    """Gantikan penamat pautan dalaman Markdown (.md) kepada penamat HTML (.html).

    Args:
        markdown_text (str): Teks Markdown mentah atau yang telah dibersihkan.

    Returns:
        str: Teks Markdown yang dikemas kini dengan sasaran pautan .html untuk navigasi web.
    """
    pattern = re.compile(r'(\[[^\]]+\]\([^)]+?)\.md([#)])')
    return pattern.sub(r'\1.html\2', markdown_text)

def strip_frontmatter_and_get_title(markdown_text: str, filename: str) -> tuple[str, str, str]:
    """Saring YAML frontmatter daripada teks mentah Markdown dan tentukan tajuk dokumen.

    Args:
        markdown_text (str): Kandungan rentetan mentah fail Markdown.
        filename (str): Nama fail lalai sebagai sandaran untuk tajuk.

    Returns:
        tuple[str, str, str]: Tigaan bagi (tajuk, markdown_bersih, yaml_frontmatter).
    """
    title = filename
    frontmatter_text = ""
    stripped_text = markdown_text.lstrip()
    if stripped_text.startswith('---'):
        parts = stripped_text.split('---', 2)
        if len(parts) == 3:
            frontmatter_text = parts[1].strip()
            try:
                fm = yaml.safe_load(parts[1])
                if fm and 'title' in fm:
                    title = fm['title']
                elif fm and 'name' in fm:
                    title = fm['name']
            except yaml.YAMLError:
                pass
            markdown_text = parts[2].strip()
            
    # Try to extract first H1 if no title in frontmatter
    if title == filename:
        for line in markdown_text.splitlines():
            if line.startswith('# '):
                title = line[2:].strip()
                break
    return title, markdown_text, frontmatter_text

def main():
    """Laksanakan fungsi utama untuk membina tapak web dokumentasi HTML statik."""
    root_dir = Path.cwd()
    html_dir = root_dir / 'html'
    llms_txt = root_dir / 'llms.txt'
    
    # 1. Bersihkan direktori html/ jika wujud (reset)
    if html_dir.exists():
        shutil.rmtree(html_dir)
    html_dir.mkdir(parents=True)
    
    # 2. Cipta assets/style.css
    assets_dir = html_dir / 'assets'
    assets_dir.mkdir()
    with open(assets_dir / 'style.css', 'w', encoding='utf-8') as f:
        f.write(CSS_CONTENT)
        
    md_paths = parse_llms_txt(llms_txt)
    if not md_paths:
        print("Tiada fail markdown ditemui dalam llms.txt")
        # Fallback to searching
        md_paths = [p.relative_to(root_dir).as_posix() for p in root_dir.rglob('*.md') if 'node_modules' not in p.parts and '.venv' not in p.parts and 'html' not in p.parts]
        
    template = Template(HTML_TEMPLATE)
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'nl2br'])
    
    index_links = []

    # 3. Proses semua fail Markdown
    for rel_path in md_paths:
        src_file = root_dir / rel_path
        if not src_file.exists():
            continue
            
        out_rel_path = str(rel_path)
        if out_rel_path.endswith('.md'):
            out_rel_path = out_rel_path[:-3] + '.html'
            
        # Kira kedalaman (depth) untuk root_prefix (cth: ../../)
        depth = out_rel_path.count('/')
        root_prefix = '../' * depth
            
        out_file = html_dir / out_rel_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(src_file, 'r', encoding='utf-8-sig') as f:
            raw_md = f.read()
            
        title, clean_md, fm_text = strip_frontmatter_and_get_title(raw_md, src_file.name)
        clean_md = fix_internal_links(clean_md)
        html_body = md.convert(clean_md)
        
        final_html = template.render(title=title, content=html_body, root_prefix=root_prefix, frontmatter=fm_text)
        
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        index_links.append((title, out_rel_path))
        print(f"Jana HTML: {out_rel_path}")

    # 4. Bina index.html utama untuk web server
    print("Menjana index.html utama...")
    index_content = "<h1>Kandungan NOSS Linux (Web Statik)</h1><ul>"
    for title, out_path in sorted(index_links, key=lambda x: x[1]):
        index_content += f'<li><a href="{out_path}">{title}</a> ({out_path})</li>'
    index_content += "</ul>"
    
    final_index = template.render(title="Indeks Utama", content=index_content, root_prefix="")
    with open(html_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(final_index)
        
    print("Berjaya! Anda boleh halakan pelayan web anda (root directory) kepada: ./html/")

if __name__ == '__main__':
    main()
