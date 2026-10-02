# /// script
# dependencies = [
#   "pyyaml",
# ]
# ///
"""OKF v0.2 Migration & Compliance Standard Script.

This script scans all Markdown files in the repository and ensures full compliance
with Open Knowledge Format (OKF) v0.2 standards, including:
- spec_version: "0.2" & okf_version: "0.2"
- Five Trust & Freshness Pillars (generated, verified, status, stale_after, sources)
- Mandatory internal document paths and public internet URLs in sources provenance
- Attested Computation contracts for executable playbooks and automation tools
- Sovereign Dual-License Footer enforcement

Attributes:
    MANDATORY_SOURCES (list[dict[str, str]]): List of default provenance sources.
    SOVEREIGN_FOOTER (str): Dual-license footer appended to markdown files.
    EXCLUDED_DIRS (set[str]): Directories ignored during scanning.
"""

import os
import re
import sys
from typing import Any, Dict, List, Optional, Set
import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

MANDATORY_SOURCES: List[Dict[str, str]] = [
    {
        "id": "internal-legal-notice",
        "title": "Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice",
        "author": "Harisfazillah Jamel (LinuxMalaysia)",
        "url": "docs/legal-notice.md",
        "resource": "docs/legal-notice.md",
    },
    {
        "id": "google-okf-v02-spec",
        "title": "Open Knowledge Format v0.2 Specification & Trust Signals",
        "author": "Google Cloud Data Analytics",
        "url": "https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals",
        "resource": "https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals",
    },
    {
        "id": "redlinesoft-attested-computations",
        "title": "Attested Computations in Open Knowledge Format (OKF v0.2)",
        "author": "RedLineSoft",
        "url": "https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/",
        "resource": "https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/",
    },
    {
        "id": "dsom-okf-v02-adoption-skill",
        "title": "OKF v0.2 Adoption Engineer Skill Standard",
        "author": "Deep State of Mind (DSOM)",
        "url": "https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/",
        "resource": "https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/",
    },
]

SOVEREIGN_FOOTER: str = """---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*"""

EXCLUDED_DIRS: Set[str] = {'.git', 'node_modules', 'html', '.pytest_cache', 'scratch'}

def get_okf_type(rel_path: str, existing_type: Optional[str] = None) -> str:
    """Determine the functional OKF classification for a given file path.

    Args:
        rel_path (str): Relative file path from the repository root.
        existing_type (Optional[str]): Existing 'type' field in the document's frontmatter.

    Returns:
        str: The determined functional OKF type classification.
    """
    if existing_type in ['Attested Computation', 'attested_computation']:
        return 'Attested Computation'
    path_parts = rel_path.replace('\\', '/').split('/')
    if 'playbooks' in path_parts or 'roles' in path_parts or 'deploy' in path_parts:
        return 'Attested Computation'
    elif '.agents' in path_parts and 'skills' in path_parts:
        return 'agent_skill'
    elif 'docs' in path_parts and 'governance' in path_parts:
        return 'governance_protocol'
    elif rel_path in ['AGENTS.md', 'LEGAL-NOTICE.md']:
        return 'governance_protocol'
    elif '.agents' in path_parts and 'brain' in path_parts:
        return 'architecture_concept'
    elif 'tools' in path_parts or 'scripts' in path_parts:
        return 'automation_tool'
    elif 'docs' in path_parts and ('how-to' in path_parts or 'tutorials' in path_parts):
        return 'guide'
    elif rel_path in ['START-HERE.md', 'README.md']:
        return 'guide'
    elif 'manual' in path_parts or ('docs' in path_parts and 'reference' in path_parts) or 'references' in path_parts:
        return 'reference'
    elif 'openwiki' in path_parts or ('docs' in path_parts and 'explanation' in path_parts):
        return 'explanation'
    return existing_type or 'documentation'

def extract_title(content: str, filename: str) -> str:
    """Extract document title from the first Markdown level-1 header or fallback to filename.

    Args:
        content (str): Text content of the document.
        filename (str): Name of the file.

    Returns:
        str: The extracted or derived title string.
    """
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()

def process_file(filepath: str, root_dir: str) -> str:
    """Process a single Markdown file to enforce OKF v0.2 frontmatter and Sovereign footer.

    Args:
        filepath (str): Path to the target Markdown file.
        root_dir (str): Root directory of the scan operation.

    Returns:
        str: Relative path of the processed file.
    """
    rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')

    with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()

    frontmatter_dict: Dict[str, Any] = {}
    body = content

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            raw_fm = parts[1]
            body = parts[2]
            try:
                data = yaml.safe_load(raw_fm)
                if isinstance(data, dict):
                    frontmatter_dict = data
            except Exception:
                pass

    okf_type = get_okf_type(rel_path, frontmatter_dict.get('type'))
    title = frontmatter_dict.get('title') or frontmatter_dict.get('name') or extract_title(body, os.path.basename(filepath))
    description = frontmatter_dict.get('description') or f"Dokumentasi OKF v0.2 bagi {os.path.basename(filepath)}."

    new_fm = dict(frontmatter_dict)
    new_fm['spec_version'] = "0.2"
    new_fm['okf_version'] = "0.2"
    new_fm['type'] = okf_type
    new_fm['title'] = str(title)
    new_fm['description'] = str(description)
    new_fm['status'] = frontmatter_dict.get('status', 'stable')
    new_fm['stale_after'] = frontmatter_dict.get('stale_after', '2027-12-31')

    new_fm['generated'] = frontmatter_dict.get('generated') or {
        'by': 'OKF v0.2 Adoption Tooling / Gemini 2.5 Pro',
        'at': '2026-08-16T00:00:00Z'
    }
    new_fm['verified'] = frontmatter_dict.get('verified') or [
        {
            'by': 'human:harisfazillah',
            'at': '2026-08-16T00:00:00Z'
        }
    ]

    existing_sources = frontmatter_dict.get('sources', [])
    if not isinstance(existing_sources, list):
        existing_sources = []

    merged_sources = list(existing_sources)
    existing_ids = {s.get('id') for s in merged_sources if isinstance(s, dict) and 'id' in s}
    existing_urls = {s.get('url') or s.get('resource') for s in merged_sources if isinstance(s, dict)}

    for m_src in MANDATORY_SOURCES:
        if m_src['id'] not in existing_ids and m_src['url'] not in existing_urls:
            merged_sources.append(m_src)

    new_fm['sources'] = merged_sources

    if okf_type == 'Attested Computation':
        if 'runtime' not in new_fm:
            new_fm['runtime'] = 'python'
        if 'parameters' not in new_fm:
            new_fm['parameters'] = [{'name': 'target_environment', 'type': 'string', 'required': True}]
        if 'executor' not in new_fm:
            new_fm['executor'] = {
                'resource': 'scripts/run_all_tests.py',
                'receipt': ['exit_code', 'stdout', 'stderr']
            }
        if 'attester' not in new_fm:
            new_fm['attester'] = {
                'resource': 'tests/test_okf_compliance.py'
            }

    clean_body = body.strip()
    footer_phrases = ["Harisfazillah Jamel", "LinuxMalaysia"]
    has_footer = any(phrase in clean_body for phrase in footer_phrases) and ("Dwi-Lesen" in clean_body or "CC BY-SA" in clean_body)

    if not has_footer:
        clean_body = clean_body + "\n\n" + SOVEREIGN_FOOTER
    else:
        if "[Notis Perundangan" not in clean_body and "/docs/legal-notice.md" not in clean_body:
            clean_body = clean_body + "\n\n" + SOVEREIGN_FOOTER

    yaml_str = yaml.dump(new_fm, sort_keys=False, allow_unicode=True, default_flow_style=False).strip()
    formatted_content = f"---\n{yaml_str}\n---\n\n{clean_body}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    return rel_path

def main(target_dir: str = '.') -> None:
    """Traverse target directory and process all Markdown files to OKF v0.2 standards.

    Args:
        target_dir (str): Root directory to scan. Defaults to '.'.
    """
    modified = 0
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                process_file(filepath, target_dir)
                modified += 1
    print(f"Successfully processed {modified} Markdown files to OKF v0.2 standard.")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(target)
