"""Module operations for sync_glossary.py.

This module provides internal functions and automation utilities for the
sync_glossary.py skill/script, adhering to the DSOM architecture.
"""
import datetime
import json
import os
import re

# Define paths relative to the workspace root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
EXTRACTED_NOSS_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "references", "extracted_noss.md")
GLOSSARY_MD_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "addon-knowledge", "glossary.md")
JSON_DUMP_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "scripts", "glossary_data.json")

def run_sync():
    # 1. Extract from extracted_noss.md
    if not os.path.exists(EXTRACTED_NOSS_PATH):
        print("Error: extracted_noss.md not found.")
        return
        
    with open(EXTRACTED_NOSS_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    start_idx = 0
    end_idx = 0
    for i, line in enumerate(lines):
        if "**Glossary**" in line:
            start_idx = i
        if "**List of Figure**" in line:
            end_idx = i
            break
            
    glossary_lines = lines[start_idx:end_idx]
    
    entries = []
    current_entry = None
    
    for line in glossary_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
            
        m_new = re.match(r'^\|\s*(\d+)\.\s+(.*?)\s*\|\s*(.*?)\s*\|$', line)
        if m_new:
            if current_entry:
                entries.append(current_entry)
            current_entry = {
                "no": m_new.group(1).strip(),
                "term": m_new.group(2).strip(),
                "definition": m_new.group(3).strip()
            }
        else:
            m_cont = re.match(r'^\|\s*(.*?)\s*\|\s*(.*?)\s*\|$', line)
            if m_cont and current_entry:
                term_part = m_cont.group(1).strip()
                def_part = m_cont.group(2).strip()
                if term_part:
                    current_entry["term"] += " " + term_part
                if def_part:
                    current_entry["definition"] += " " + def_part
                    
    if current_entry:
        entries.append(current_entry)
        
    for e in entries:
        e["term"] = re.sub(r'\s+', ' ', e["term"])
        e["definition"] = re.sub(r'\s+', ' ', e["definition"])
        
    # 2. Strict Inclusion Audit (Zero-Count Purge)
    verified_entries = []
    for e in entries:
        term = e["term"]
        safe_term = re.escape(term)
        pattern = re.compile(rf"\b{safe_term}\b", re.IGNORECASE)
        
        found = False
        for i, line in enumerate(lines):
            # Skip the glossary section itself
            if start_idx <= i <= end_idx:
                continue
            if pattern.search(line):
                found = True
                break
                
        if found:
            verified_entries.append(e)

    # Re-number
    for i, e in enumerate(verified_entries, 1):
        e["no"] = str(i)

    # Dump JSON
    os.makedirs(os.path.dirname(JSON_DUMP_PATH), exist_ok=True)
    with open(JSON_DUMP_PATH, 'w', encoding='utf-8') as f:
        json.dump(verified_entries, f, indent=2)
        
    # Build MD
    timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    md_content = f"""---
okf_version: 0.1
type: documentation
title: "NOSS Glossary of Terms"
description: "Standard definitions for technical and operational terms used in the NOSS Level 3 curriculum."
timestamp: {timestamp}
topics: [glossary, definitions, ict, noss]
---

# NOSS Glossary of Terms

This document provides standardized definitions for the core operational and technical terminology utilized across the NOSS curriculum.

| No. | Term | Definition |
| :--- | :--- | :--- |
"""

    for e in verified_entries:
        md_content += f"| {e['no']} | **{e['term']}** | {e['definition']} |\n"
        
    with open(GLOSSARY_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"Extracted {len(entries)} raw terms.")
    print(f"Purged zero-count terms. Final active glossary: {len(verified_entries)} terms.")
    print("JSON dump ready for DOCX compiler.")

if __name__ == "__main__":
    run_sync()
