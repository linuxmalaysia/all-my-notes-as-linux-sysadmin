import os
import re
from datetime import datetime

skills_dir = os.path.join(".agents", "skills")
output_file = os.path.join(skills_dir, "index.md")

timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
date_str = datetime.utcnow().strftime("%Y-%m-%d")

footer = f"""
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | {date_str}*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
"""

header = f"""---
okf_version: 0.1
type: documentation
title: "Master Palace Registry"
timestamp: "{timestamp}"
topics: ["registry", "dsom", "noss"]
tags: ["index", "skills", "map"]
description: "Master directory mapping all active Sovereign AI Skills within the repository."
resource: "file:///.agents/skills/index.md"
---

# 🏛️ Master Palace Registry (Skills Index)

This registry dynamically maps all functional AI skills available in the Sovereign Markdown Palace. 

**Total Modules Indexed:** `[TOTAL_COUNT]`

| Skill Name / Folder | Description | Topics / Scope |
|---|---|---|
"""

def extract_yaml_frontmatter(content):
    parts = content.split("---", 2)
    if len(parts) >= 3 and content.startswith("---"):
        return parts[1]
    return ""

def parse_metadata(frontmatter):
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
