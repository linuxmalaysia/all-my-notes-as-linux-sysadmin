# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///
"""Generates the Master Palace Registry from SKILL.md files.

This module scans the .agents/skills directory for SKILL.md files, extracts
their OKF v0.2 YAML frontmatter, and generates a comprehensive Markdown table
(index.md) mapping all active Sovereign AI Skills.
"""

import os
from datetime import datetime, timezone

import yaml

skills_dir = os.path.join(".agents", "skills")
output_file = os.path.join(skills_dir, "index.md")

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
type: agent_skill
title: Master Palace Registry
description: Master directory mapping all active Sovereign AI Skills within the repository.
status: stable
stale_after: '2027-12-31'
generated:
  by: generate_palace_registry.py / OKF v0.2
  at: '{timestamp}'
resource: file:///.agents/skills/index.md
topics:
- registry
- dsom
- noss
tags:
- index
- skills
- map
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: "human:harisfazillah"
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: "team:google-cloud-data-analytics"
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
---

# 🏛️ Master Palace Registry (Skills Index)

This registry dynamically maps all functional AI skills available in the Sovereign Markdown Palace. 

**Total Modules Indexed:** `[TOTAL_COUNT]`

| Skill Name / Folder | Description | Topics / Scope |
|---|---|---|
"""

def extract_yaml_frontmatter(content):
    """Extracts YAML frontmatter from a Markdown file.

    Args:
        content (str): The raw string content of a Markdown file.

    Returns:
        str: The extracted YAML frontmatter string without the '---' delimiters.
             Returns an empty string if no valid frontmatter is found.
    """
    parts = content.split("---", 2)
    if len(parts) >= 3 and content.startswith("---"):
        return parts[1]
    return ""

def parse_metadata(frontmatter):
    """Parses extracted YAML frontmatter into a dictionary.

    Args:
        frontmatter (str): The raw YAML string to parse.

    Returns:
        dict: A dictionary containing 'title', 'description', and 'topics'.
    """
    try:
        parsed = yaml.safe_load(frontmatter)
        if isinstance(parsed, dict):
            title = parsed.get('title') or parsed.get('name') or ""
            desc = parsed.get('description') or ""
            raw_topics = parsed.get('topics') or ""
            if isinstance(raw_topics, list):
                topics_str = ", ".join(str(t) for t in raw_topics)
            else:
                topics_str = str(raw_topics)
            return {"title": str(title), "description": str(desc), "topics": topics_str}
    except yaml.YAMLError:
        pass

    metadata = {"title": "", "description": "", "topics": ""}
    for line in frontmatter.split('\n'):
        if line.startswith('title:'):
            metadata['title'] = line.replace('title:', '').strip().strip('"').strip("'")
        elif line.startswith('name:') and not metadata['title']:
            metadata['title'] = line.replace('name:', '').strip().strip('"').strip("'")
            
        elif line.startswith('description:'):
            metadata['description'] = line.replace('description:', '').strip().strip('"').strip("'")
            
        elif line.startswith('topics:'):
            metadata['topics'] = line.replace('topics:', '').strip().strip('"').strip("'").replace('[', '').replace(']', '')
            
    return metadata

def generate_registry():
    """Generates the Master Palace Registry Markdown index.

    Walks through the skills directory, parses SKILL.md files, generates
    a formatted Markdown table, and writes the output to index.md.
    """
    rows = []
    
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            skill_folder = os.path.basename(root)
            skill_path = os.path.join(root, "SKILL.md")
            
            with open(skill_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            fm = extract_yaml_frontmatter(content)
            meta = parse_metadata(fm)
            
            title = meta.get('title') or skill_folder
            desc = meta.get('description') or "No description provided."
            topics = meta.get('topics') or "N/A"
            
            # Escape pipes for markdown table
            desc = desc.replace('|', '-')
            
            row = f"| **`{skill_folder}`** <br> *{title}* | {desc} | {topics} |"
            rows.append(row)
            
    # Sort alphabetically by folder name
    rows.sort()
    
    final_output = header.replace("[TOTAL_COUNT]", str(len(rows)))
    final_output += "\n".join(rows)
    final_output += "\n" + footer
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_output)
        
    print(f"Palace Registry successfully generated at {output_file} with {len(rows)} skills.")

if __name__ == "__main__":
    generate_registry()
