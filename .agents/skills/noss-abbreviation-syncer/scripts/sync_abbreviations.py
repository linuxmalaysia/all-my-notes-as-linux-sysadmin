import re
import os
import json
import datetime

# Define paths relative to the workspace root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
EXTRACTED_NOSS_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "references", "extracted_noss.md")
V2_ABBREV_PATH = os.path.join(BASE_DIR, "noss-rebuild-v2", "addon-knowledge", "abbreviations.md")
V3_ABBREV_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "addon-knowledge", "abbreviations.md")
JSON_DUMP_PATH = os.path.join(BASE_DIR, "noss-l3-latest", "scripts", "abbreviations_data.json")

def run_sync():
    merged = {}

    # 1. Read v2 Legacy Master
    if os.path.exists(V2_ABBREV_PATH):
        with open(V2_ABBREV_PATH, 'r', encoding='utf-8') as f:
            v2_content = f.read()
        for m in re.findall(r"\|\s*\d+\s*\|\s*\*\*([A-Za-z0-9\/]+)\*\*\s*\|\s*([^|]+)\|", v2_content):
            merged[m[0].strip()] = m[1].strip()

    # 2. Extract fresh acronyms from extracted_noss.md
    if os.path.exists(EXTRACTED_NOSS_PATH):
        with open(EXTRACTED_NOSS_PATH, 'r', encoding='utf-8') as f:
            noss_content = f.read()
        
        matches = re.findall(r"([A-Za-z\s\-]+)\s+\(([A-Z0-9a-z]{2,8})\)", noss_content)
        for m in matches:
            full = m[0].strip()
            acronym = m[1].strip()
            if len(full.split()) <= 6 and acronym.isupper():
                if acronym not in merged:
                    merged[acronym] = full
    else:
        print("Warning: extracted_noss.md not found.")
        noss_content = ""

    # 3. Filter out bad acronyms
    clean_merged = {k: v for k, v in merged.items() if len(k) > 1 and k.upper() == k}

    # 4. Strict Inclusion Audit (Zero-Count Purge)
    # We only keep acronyms that literally appear in the NOSS text.
    verified_merged = {}
    for acro, desc in clean_merged.items():
        safe_acronym = re.escape(acro)
        pattern = re.compile(rf"\b{safe_acronym}\b")
        if pattern.search(noss_content):
            verified_merged[acro] = desc

    # Sort alphabetically by key
    sorted_keys = sorted(verified_merged.keys(), key=lambda x: x.lower())
    
    # Dump JSON for Node.js DOCX compiler
    json_data = []
    for i, key in enumerate(sorted_keys, 1):
        json_data.append({"no": str(i), "acronym": key, "definition": verified_merged[key]})
        
    os.makedirs(os.path.dirname(JSON_DUMP_PATH), exist_ok=True)
    with open(JSON_DUMP_PATH, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Build the new OKF compliant Markdown
    markdown_output = f"""---
okf_version: 0.1
type: documentation
title: "ICT Abbreviations & Standard Definitions"
description: "Standard ICT acronyms and definitions to support NOSS framework learning."
timestamp: {timestamp}
topics: [abbreviations, definitions, ict, noss]
---

# Unified Abbreviations Reference Matrix

This document contains the consolidated glossary of all institutional, standard, and technical abbreviations utilized across the TVET NOSS Level 3 curriculum.

| No. | Abbreviation | Complete Technical / Institutional Definition |
| :--- | :--- | :--- |
"""

    for i, key in enumerate(sorted_keys, 1):
        definition = verified_merged[key]
        markdown_output += f"| {i} | **{key}** | {definition} |\n"

    with open(V3_ABBREV_PATH, 'w', encoding='utf-8') as f:
        f.write(markdown_output)

    print(f"✅ Extracted, verified, and purged 0-count acronyms.")
    print(f"✅ Successfully synced {len(sorted_keys)} abbreviations to {V3_ABBREV_PATH}.")
    print(f"✅ JSON dump ready for DOCX compiler.")

if __name__ == "__main__":
    run_sync()
