import sys
import json

if len(sys.argv) != 3:
    print("Usage: uv run generate_detailed_md.py <input.json> <output.md>")
    sys.exit(1)

input_path = sys.argv[1]
output_md = sys.argv[2]

def get_advice(highlight_text):
    text = highlight_text.lower()
    if any(k in text for k in ["protect", "encryption", "hash", "privileges", "credentials", "security", "access"]):
        return "Critical NOSS Violation: This is an IT Security rule that has been illegally placed into an ASE (Affective, Safety, Environment) column. DSOM rules strictly dictate IT Security must be moved to Performance Criteria or Related Skills."
    elif any(k in text for k in ["bash", "python", "powershell", "script"]):
        return "Server Scripting Environment Invariant: Ensure cross-platform scripting parity is maintained (Windows/Linux/Cross-Platform) in CU03 as explicitly mandated by DSOM."
    elif any(k in text for k in ["3r", "patience", "wear", "isolate"]):
        return "ASE Domain Formatting Check: This is a valid ASE domain behavior, but verify that the grammar strictly follows the required format (e.g., ATTITUDE begins with a descriptive adjective, SAFETY/ENVIRONMENT begin with specific physical care/sustainability verbs)."
    elif "kena tambah knowledge" in text:
        return "Auditor Action Item: The reviewer is explicitly requesting that additional 'Related Knowledge' items be expanded for this Work Activity."
    elif any(k in text for k in ["backup", "log"]):
        return "Data Recovery Standard: Ensure backup, retention, and verification criteria align with the required server recovery specifications in CU04/CU05."
    elif any(k in text for k in ["hardware", "chassis", "cable", "post"]):
        return "Active Voice Compliance: Ensure these physical assembly instructions use standard active verbs in the related skills column (CU01)."
    else:
        return "General Review Highlight: The Subject Matter Expert likely wants this specific item verified, added, or explicitly stated in the curriculum."

try:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# Detailed NOSS Document Review Notes\n\n")
        f.write("This document tracks every highlighted segment found in the original source document, preserving its exact location, surrounding text, and an automated DSOM rule-based analysis on why it was flagged.\n\n")
        
        for i, item in enumerate(data, 1):
            ref_id = f"HL-{i:03d}"
            f.write(f"## [{ref_id}] Highlight at Page {item['page']}, Paragraph {item['paragraph']}\n\n")
            
            f.write("| Attribute | Content |\n")
            f.write("| :--- | :--- |\n")
            f.write(f"| **Reference ID** | **{ref_id}** |\n")
            f.write(f"| **Context Before** | _{item['before']}_ |\n")
            f.write(f"| **Highlighted Text** | **`{item['highlight']}`** |\n")
            f.write(f"| **Context After** | _{item['after']}_ |\n")
            
            advice = get_advice(item['highlight'])
            f.write(f"| **Analysis / Advice** | ⚠️ {advice} |\n\n")

    print("Detailed markdown generated successfully.")

except Exception as e:
    print(f"Error: {e}")
