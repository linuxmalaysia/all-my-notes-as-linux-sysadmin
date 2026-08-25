"""Builds the Diátaxis-compliant documentation structure.

This module automates the reorganization of the docs/ directory into the
four Diátaxis quadrants (tutorials, how-to, reference, explanation), applies
Google OKF v0.1 YAML frontmatter, and generates required index files like
llms.txt and SUMMARY.md.
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
    """Initializes the four Diátaxis quadrants.

    Creates the required directories (tutorials, how-to, reference, explanation)
    and migrates non-conforming directories like 'governance' and 'tools' into
    their appropriate quadrants.
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
    """Generates an OKF v0.1 compliant YAML frontmatter string.

    Args:
        title (str): The document title.
        description (str): A brief description of the document.
        doc_type (str): The Diátaxis quadrant type (concept, guide, reference, tutorial).
        file_id (str): The unique file path identifier.
        domain (str, optional): The operational domain. Defaults to "AI".
        tier (str, optional): The context tier. Defaults to "L2-Operational".
        tags (list, optional): List of tags. Defaults to ["dsom-protocol", "diataxis-quadrant"].

    Returns:
        str: A fully formatted YAML frontmatter string.
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
    """Strips existing YAML frontmatter from a markdown string.

    Args:
        content (str): The raw markdown content.

    Returns:
        str: The markdown content without its leading YAML block.
    """
    parts = content.split("---")
    if len(parts) >= 3 and content.startswith("---"):
        return "---".join(parts[2:]).lstrip()
    return content

def get_doc_type(filepath):
    """Determines the Diátaxis document type based on the file path.

    Args:
        filepath (str): The path to the markdown file.

    Returns:
        str: The inferred document type ('tutorial', 'guide', 'reference', or 'concept').
    """
    path_str = filepath.lower()
    if "tutorial" in path_str: return "tutorial"
    if "how-to" in path_str: return "guide"
    if "reference" in path_str: return "reference"
    if "explanation" in path_str or "governance" in path_str: return "concept"
    return "guide"

def process_existing_docs():
    """Processes all existing markdown documents in the docs directory.

    Replaces old frontmatter with the new strict OKF schema while preserving
    the document body.
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
    """Generates reference documents for all AI skills and scripts.

    Iterates through the .agents/skills/ and scripts/ directories to create
    individual markdown reference files in docs/reference/ for zero-context
    LLM understanding.
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
    """Generates the GitBook / mkdocs SUMMARY.md navigation file.

    Builds a static Markdown link tree that complies with the Diátaxis
    quadrant structure.
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
    """Generates the llms.txt index file.

    Creates an optimized markdown index at the project root intended for
    autonomous agent ingestion and navigation.
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
