"""Bina struktur dokumentasi yang mematuhi kerangka Diátaxis.

Modul ini mengautomasikan penyusunan semula direktori docs/ kepada empat
kuadran Diátaxis (tutorials, how-to, reference, explanation), mengaplikasikan
YAML frontmatter Google OKF v0.2, serta menjana fail indeks seperti
llms.txt dan SUMMARY.md.
"""

import os
import shutil

DOCS_DIR = "docs"
SKILLS_DIR = os.path.join(".agents", "skills")
SCRIPTS_DIR = "scripts"

QUADRANTS = {
    "tutorials": "tutorial",
    "how-to": "guide",
    "reference": "reference",
    "explanation": "concept"
}

def init_quadrants():
    """Basuh dan sediakan empat kuadran Diátaxis.

    Mencipta direktori yang diperlukan (tutorials, how-to, reference, explanation)
    dan memindahkan direktori yang tidak mengikut struktur seperti 'governance' dan 'tools'
    ke kuadran yang sesuai.
    """
    for quad in QUADRANTS:
        os.makedirs(os.path.join(DOCS_DIR, quad), exist_ok=True)
    
    # Move governance and reference-architectures to explanation if they exist
    for f in ["governance", "reference-architectures"]:
        src = os.path.join(DOCS_DIR, f)
        dst = os.path.join(DOCS_DIR, "explanation", f)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)
            
    # Move tools to reference
    for f in ["tools", "tools-and-automation"]:
        src = os.path.join(DOCS_DIR, f)
        dst = os.path.join(DOCS_DIR, "reference", f)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.move(src, dst)

def get_yaml_template(title, description, doc_type, file_id, domain="AI", tier="L2-Operational", tags=None):
    """Jana rentetan YAML frontmatter yang mematuhi standard OKF v0.2.

    Args:
        title (str): Tajuk dokumen.
        description (str): Penerangan ringkas mengenai dokumen.
        doc_type (str): Jenis kuadran Diátaxis (concept, guide, reference, tutorial).
        file_id (str): Pengecam unik laluan fail.
        domain (str, optional): Domain operasi. Lalai kepada "AI".
        tier (str, optional): Tetingkat konteks. Lalai kepada "L2-Operational".
        tags (list, optional): Senarai tag. Lalai kepada ["dsom-protocol", "diataxis-quadrant"].

    Returns:
        str: Rentetan YAML frontmatter yang berformat lengkap.
    """
    tags_str = "\n".join([f'  - "{t}"' for t in (tags or ["dsom-protocol", "diataxis-quadrant"])])
    return f"""---
okf_version: 0.2
title: "{title}"
description: "{description}"
type: "{doc_type}"
id: "{file_id.replace('\\\\', '/')}"
dsom_governance:
  domain: "{domain}"
  context_tier: "{tier}"
tags:
{tags_str}
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---
"""

def strip_old_frontmatter(content):
    """Saring YAML frontmatter sedia ada daripada rentetan Markdown.

    Args:
        content (str): Kandungan mentah Markdown.

    Returns:
        str: Kandungan Markdown tanpa blok YAML di bahagian awal.
    """
    parts = content.split("---")
    if len(parts) >= 3 and content.startswith("---"):
        return "---".join(parts[2:]).lstrip()
    return content

def get_doc_type(filepath):
    """Tentukan jenis dokumen Diátaxis berdasarkan laluan fail.

    Args:
        filepath (str): Laluan ke fail Markdown.

    Returns:
        str: Jenis dokumen yang disimpulkan ('tutorial', 'guide', 'reference', atau 'concept').
    """
    path_str = filepath.lower()
    if "tutorial" in path_str: return "tutorial"
    if "how-to" in path_str: return "guide"
    if "reference" in path_str: return "reference"
    if "explanation" in path_str or "governance" in path_str: return "concept"
    return "guide"

def process_existing_docs():
    """Proses kesemua dokumen Markdown sedia ada di dalam direktori docs.

    Gantikan frontmatter lama dengan skema OKF baharu sambil mengekalkan
    badan utama dokumen.
    """
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                file_id = filepath.replace("\\", "/")
                doc_type = get_doc_type(filepath)
                title = file.replace(".md", "").replace("-", " ").title()
                desc = f"DSOM {doc_type.title()} document for {title}."
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                body = strip_old_frontmatter(content)
                new_frontmatter = get_yaml_template(title, desc, doc_type, file_id)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_frontmatter + "\n" + body)

def generate_tool_references():
    """Jana dokumen rujukan untuk kesemua kemahiran AI dan skrip.

    Ulang lelar direktori .agents/skills/ dan scripts/ untuk mencipta
    fail rujukan Markdown individu di docs/reference/ untuk kefahaman LLM.
    """
    ref_dir = os.path.join(DOCS_DIR, "reference", "skills")
    os.makedirs(ref_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            skill_name = os.path.basename(root)
            ref_path = os.path.join(ref_dir, f"{skill_name}.md")
            file_id = ref_path.replace("\\", "/")
            
            with open(os.path.join(root, "SKILL.md"), 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            body = strip_old_frontmatter(content)
            title = f"Skill: {skill_name}"
            desc = f"Reference material for AI skill {skill_name}."
            new_frontmatter = get_yaml_template(title, desc, "reference", file_id, tags=["dsom-protocol", skill_name, "diataxis-reference"])
            
            with open(ref_path, 'w', encoding='utf-8') as f:
                f.write(new_frontmatter + "\n" + body)
                
    script_dir = os.path.join(DOCS_DIR, "reference", "scripts")
    os.makedirs(script_dir, exist_ok=True)
    if os.path.exists(SCRIPTS_DIR):
        for script in os.listdir(SCRIPTS_DIR):
            if script.endswith((".py", ".sh", ".js")):
                ref_path = os.path.join(script_dir, f"{script}.md")
                file_id = ref_path.replace("\\", "/")
                title = f"Script: {script}"
                desc = f"Execution reference for {script}."
                new_frontmatter = get_yaml_template(title, desc, "reference", file_id, tags=["dsom-protocol", script, "diataxis-reference"])
                body = f"# {title}\\n\\nThis is a system script located at `{SCRIPTS_DIR}/{script}`. Execute via `uv run` if python."
                
                with open(ref_path, 'w', encoding='utf-8') as f:
                    f.write(new_frontmatter + "\n" + body)

def generate_summary():
    """Jana fail navigasi SUMMARY.md untuk GitBook / MkDocs.

    Bina pokok pautan Markdown statik yang mematuhi struktur kuadran Diátaxis.
    """
    summary_path = os.path.join(DOCS_DIR, "SUMMARY.md")
    content = """# Summary

* [System Overview](README.md)

## Explanation & Architecture
* [DSOM Governance Framework](explanation/governance/DIGITAL-SOVEREIGNTY-MODEL.md)
* [Diátaxis Architecture](explanation/diataxis.md)
* [System Architecture](explanation/openwiki-mcp-architecture.md)

## Tutorials
* [Quickstart: Onboarding Guide](tutorials/getting-started.md)

## How-To Guides
* [Operational Recipes Index](how-to/index.md)

## Reference Material
* [Component & Tool Index](reference/index.md)
"""
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_llmstxt():
    """Jana fail indeks llms.txt.

    Cipta indeks Markdown yang dioptimumkan di punca projek bagi kegunaan
    penerimaan dan navigasi ejen AI.
    """
    llmstxt_path = "llms.txt"
    content = """# Project Name - DSOM AI Knowledge Base

> DSOM-governed, OKF v0.1 compliant documentation index for AI Agents and LLMs.

## Core Governance & Architecture
- [DSOM Governance](docs/explanation/governance/DIGITAL-SOVEREIGNTY-MODEL.md): Metacognitive context management and protocol standards.
- [Diátaxis Framework](docs/explanation/diataxis.md): Quadrant layout and documentation structure.
- [System Architecture](docs/explanation/openwiki-mcp-architecture.md): Subsystem topologies and integration points.

## Tools & Component References
- [Tool Index](docs/reference/index.md): Exhaustive list of scripts, modules, and API signatures.

## Practical Operational Guides
- [Getting Started Onboarding](docs/tutorials/getting-started.md): Beginner step-by-step onboarding walkthrough.
- [Operational Recipes](docs/how-to/index.md): Task-oriented execution recipes.
"""
    with open(llmstxt_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    init_quadrants()
    generate_tool_references()
    process_existing_docs()
    generate_summary()
    generate_llmstxt()
    print("Diátaxis & OKF Pipeline Execution Completed.")
