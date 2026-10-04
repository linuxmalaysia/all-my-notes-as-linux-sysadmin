"""Generates the OpenWiki Master Graph mapping Topics to CUs.

This module reads all markdown topic files in the openwiki directory,
extracts their metadata and mapped Competency Units (CUs), and outputs
a Mermaid.js diagram and detailed table to openwiki/index.md.
"""

import os
import re
from datetime import datetime, timezone

OPENWIKI_DIR = "openwiki"
OUTPUT_FILE = os.path.join(OPENWIKI_DIR, "index.md")

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

footer = f"""
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | {date_str}*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
"""

header = f"""---
spec_version: '0.2'
okf_version: '0.2'
type: explanation
title: OpenWiki Master Graph
timestamp: '{timestamp}'
description: Peta grafik keseluruhan (Master Graph) silibus Linux NOSS di dalam OpenWiki.
status: stable
stale_after: '2027-12-31'
generated:
  by: generate_openwiki_graph.py / OKF v0.2
  at: '{timestamp}'
resource: file:///openwiki/index.md
topics:
- openwiki
- noss-linux
- graph
tags:
- index
- mermaid
- map
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

# 🧠 OpenWiki Master Graph (Linux NOSS Syllabus)

Dokumen ini memaparkan gambaran visual dan hierarki bagi kesemua topik NOSS (Level 3) Linux yang sedia ada di dalam pangkalan data `openwiki/`. 
Graf ini dijana secara automatik menggunakan teknologi *Mermaid.js*.

## Peta Topik dan Pemetaan CU

```mermaid
graph TD
    Root(("Silibus Pusat\\nLinux NOSS (L3)"))
"""

def extract_metadata(filepath):
    """Extracts title, description, and Competency Unit (CU) from a topic file.

    Args:
        filepath (str): The absolute or relative path to the markdown file.

    Returns:
        dict: A dictionary containing 'title', 'desc', and 'cu' extracted from
              the file's YAML frontmatter and body.
    """
    meta = {"title": "", "desc": "", "cu": ""}
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    parts = content.split("---", 2)
    if len(parts) >= 3:
        for line in parts[1].split('\n'):
            if line.startswith('title:'):
                meta['title'] = line.replace('title:', '').strip().strip('"').strip("'")
            elif line.startswith('description:'):
                meta['desc'] = line.replace('description:', '').strip().strip('"').strip("'")
                
    # Search body for CU references
    body = parts[2] if len(parts) >= 3 else content
    cu_matches = set(re.findall(r'(CU0[1-6])', body, re.IGNORECASE))
    
    if cu_matches:
        meta['cu'] = next(iter(cu_matches)).upper()
    else:
        # fallback from filename
        filename = os.path.basename(filepath)
        num_match = re.search(r'topic-(0[1-6])', filename)
        if num_match:
            meta['cu'] = f"CU{num_match.group(1)}"
            
    return meta

def generate_graph():
    """Compiles the extracted topic data into a Mermaid graph and index table.

    Iterates over all topic-*.md files in the openwiki directory, formats
    the Mermaid graph nodes and relationships, builds a markdown table,
    and writes the final assembled output to openwiki/index.md.
    """
    topics = []
    
    for f in sorted(os.listdir(OPENWIKI_DIR)):
        if f.endswith('.md') and f.startswith('topic-'):
            filepath = os.path.join(OPENWIKI_DIR, f)
            meta = extract_metadata(filepath)
            topics.append({
                "file": f,
                "title": meta['title'],
                "desc": meta['desc'],
                "cu": meta['cu']
            })
            
    mermaid_nodes = []
    mermaid_links = []
    table_rows = []
    
    for i, t in enumerate(topics):
        node_id = f"T{i+1}"
        # Node definition
        safe_title = t['title'].replace('"', "'")
        mermaid_nodes.append(f"    {node_id}[\"{safe_title} <br> <i>({t['cu']})</i>\"]")
        # Link from root
        mermaid_links.append(f"    Root --> {node_id}")
        
        # Add to table
        table_rows.append(f"| [{t['title']}]({t['file']}) | {t['cu']} | {t['desc']} |")
        
    graph_content = header + "\n" + "\n".join(mermaid_nodes) + "\n" + "\n".join(mermaid_links) + "\n```\n\n## Perincian Modul\n\n| Topik | Kod CU | Penerangan |\n|---|---|---|\n" + "\n".join(table_rows) + "\n" + footer
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(graph_content)
        
    print(f"OpenWiki graph successfully generated at {OUTPUT_FILE}.")

if __name__ == "__main__":
    generate_graph()
