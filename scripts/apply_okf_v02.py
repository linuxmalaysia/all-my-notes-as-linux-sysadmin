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
from datetime import datetime, timezone
from typing import Any

import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

MANDATORY_SOURCES: list[dict[str, str]] = [
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

EXCLUDED_DIRS: set[str] = {'.git', 'node_modules', 'html', '.pytest_cache', 'scratch'}

def get_okf_type(rel_path: str, existing_type: str | None = None) -> str:
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
    elif 'docs' in path_parts and 'governance' in path_parts or rel_path in ['AGENTS.md', 'LEGAL-NOTICE.md']:
        return 'governance_protocol'
    elif '.agents' in path_parts and 'brain' in path_parts:
        return 'architecture_concept'
    elif 'tools' in path_parts or 'scripts' in path_parts:
        return 'automation_tool'
    elif 'docs' in path_parts and ('how-to' in path_parts or 'tutorials' in path_parts) or rel_path in ['START-HERE.md', 'README.md']:
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

def process_file(
    filepath: str,
    root_dir: str,
    generator_id: str = 'OKF v0.2 Adoption Tooling / Gemini 2.5 Pro'
) -> tuple[bool, bool]:
    """Process a single Markdown file to enforce OKF v0.2 frontmatter and Sovereign footer.

    Args:
        filepath (str): Path to the target Markdown file.
        root_dir (str): Root directory of the scan operation.
        generator_id (str): Identifier for the generator actor.

    Returns:
        Tuple[bool, bool]: (success_flag, changed_flag)
    """
    rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"[SKIP] Non-UTF-8 encoding in file: {rel_path}", file=sys.stderr)
        return False, False
    except OSError as err:
        print(f"[ERROR] Cannot read file {rel_path}: {err}", file=sys.stderr)
        return False, False

    frontmatter_dict: dict[str, Any] = {}
    body = content

    # Line-anchored frontmatter parsing
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", content, re.DOTALL)
    if fm_match:
        raw_fm = fm_match.group(1)
        body = fm_match.group(2)
        try:
            parsed = yaml.safe_load(raw_fm)
            if isinstance(parsed, dict):
                frontmatter_dict = parsed
        except yaml.YAMLError:
            pass

    filename = os.path.basename(filepath)
    if filename in ['index.md', 'log.md'] and rel_path != 'index.md' and not frontmatter_dict:
        # Reserved subdirectory index.md / log.md without existing frontmatter: keep without frontmatter
        clean_body = body.strip()
        footer_phrases = ["Harisfazillah Jamel", "LinuxMalaysia"]
        has_footer = any(phrase in clean_body for phrase in footer_phrases) and ("Dwi-Lesen" in clean_body or "CC BY-SA" in clean_body)

        if not has_footer:
            clean_body = clean_body + "\n\n" + SOVEREIGN_FOOTER
        else:
            if "[Notis Perundangan" not in clean_body and "/docs/legal-notice.md" not in clean_body:
                clean_body = clean_body + "\n\n" + SOVEREIGN_FOOTER

        formatted_content = f"{clean_body}\n"
        if formatted_content == content:
            return True, False

        try:
            with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                f.write(formatted_content)
        except OSError as err:
            print(f"[ERROR] Cannot write reserved file {rel_path}: {err}", file=sys.stderr)
            return False, False

        return True, True

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

    now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    existing_gen = frontmatter_dict.get('generated')
    if isinstance(existing_gen, dict) and 'by' in existing_gen and 'at' in existing_gen:
        new_fm['generated'] = existing_gen
    else:
        new_fm['generated'] = {
            'by': 'okf_tooling/v0.2',
            'at': now_iso
        }

    # Normalize verified if explicitly present in existing metadata
    if 'verified' in frontmatter_dict:
        v_data = frontmatter_dict['verified']
        normalized_verified = []
        if isinstance(v_data, dict):
            v_list = [v_data]
        elif isinstance(v_data, list):
            v_list = v_data
        else:
            v_list = []

        for item in v_list:
            if isinstance(item, dict) and 'by' in item and 'at' in item:
                normalized_verified.append(item)

        if normalized_verified:
            new_fm['verified'] = normalized_verified
        else:
            new_fm.pop('verified', None)

    existing_sources = frontmatter_dict.get('sources', [])
    if not isinstance(existing_sources, list):
        existing_sources = []

    merged_sources = []
    for s in existing_sources:
        if isinstance(s, str):
            merged_sources.append({'resource': s})
        elif isinstance(s, dict):
            s_copy = dict(s)
            if 'url' in s_copy and 'resource' not in s_copy:
                s_copy['resource'] = s_copy['url']
            merged_sources.append(s_copy)

    existing_ids = set()
    existing_resources = set()
    for s in merged_sources:
        if isinstance(s, dict):
            s_id = s.get('id')
            if isinstance(s_id, (str, int)):
                existing_ids.add(str(s_id))
            res = s.get('resource') or s.get('url')
            if isinstance(res, (str, int)):
                existing_resources.add(str(res))

    for m_src in MANDATORY_SOURCES:
        if m_src['id'] not in existing_ids and m_src['resource'] not in existing_resources:
            merged_sources.append(m_src)

    new_fm['sources'] = merged_sources

    if okf_type == 'Attested Computation':
        if 'runtime' not in new_fm:
            new_fm['runtime'] = 'python'
        if 'parameters' not in new_fm:
            new_fm['parameters'] = [{'name': 'target_environment', 'type': 'string', 'required': True}]
        if 'executor' not in new_fm:
            new_fm['executor'] = {
                'resource': 'run_all_tests.py',
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

    if formatted_content == content:
        return True, False

    try:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(formatted_content)
    except OSError as err:
        print(f"[ERROR] Cannot write file {rel_path}: {err}", file=sys.stderr)
        return False, False

    return True, True

def main(target_dir: str = '.') -> int:
    """Traverse target directory and process all Markdown files to OKF v0.2 standards.

    Args:
        target_dir (str): Root directory to scan. Defaults to '.'.

    Returns:
        int: Exit status code (0 for success, non-zero for failures).
    """
    modified = 0
    errors = 0
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                success, changed = process_file(filepath, target_dir)
                if not success:
                    errors += 1
                elif changed:
                    modified += 1
    print(f"Successfully processed Markdown files. Modified: {modified}, Errors: {errors}.")
    return 1 if errors > 0 else 0

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    sys.exit(main(target))
