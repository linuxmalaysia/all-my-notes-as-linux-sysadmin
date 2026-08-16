import os
import shutil
import sys
from datetime import datetime

def migrate_docs(src_dir, dst_dir):
    skip_files = ["PERSONALIZATION.md", "OKF-ADOPTION-GUIDE.md", "SKILL-FORMAT.md"]

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = datetime.utcnow().strftime("%Y-%m-%d")

    footer = f"""
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | {date_str}*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
"""

    old_urls = [
        ("https://github.com/linuxmalaysia/deep-state-of-mind-for-my-ai", "https://gitlab.com/linuxmalaysia/skills-noss-malaysia-for-linux.git"),
        ("github.com/linuxmalaysia/deep-state-of-mind-for-my-ai", "gitlab.com/linuxmalaysia/skills-noss-malaysia-for-linux")
    ]

    def strip_old_footer(content):
        parts = content.split("---")
        if len(parts) >= 2:
            last_part = parts[-1]
            if "GNU General Public License v3.0" in last_part or "Deep State of Mind (DSOM) For My AI Protocol |" in last_part:
                return "---".join(parts[:-1]).rstrip()
        return content

    def process_markdown(src_path, dst_path, rel_path):
        with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        for old_url, new_url in old_urls:
            content = content.replace(old_url, new_url)

        content = strip_old_footer(content)

        parts = content.split("---", 2)
        has_frontmatter = False
        body = content
        description = ""
        
        if len(parts) >= 3 and content.startswith("---"):
            has_frontmatter = True
            fm_text = parts[1]
            body = parts[2]
            
            for line in fm_text.split('\n'):
                if line.startswith('description:'):
                    description = line.replace('description:', '').strip().strip('"').strip("'")
                    break

        if not description:
            description = f"OKF-compliant documentation for {os.path.basename(src_path)}."

        title = os.path.basename(src_path).replace('.md', '')
        
        new_frontmatter = f"""---
okf_version: 0.1
type: documentation
title: "{title}"
timestamp: "{timestamp}"
topics: ["dsom", "noss-linux"]
tags: ["documentation", "noss"]
description: "{description}"
resource: "file:///docs/{rel_path.replace('\\\\', '/')}"
---"""

        final_content = new_frontmatter + body
        
        if "Sovereign Markdown Palace" not in final_content:
            final_content = final_content.rstrip() + "\n" + footer

        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

    for root, dirs, files in os.walk(src_dir):
        rel_root = os.path.relpath(root, src_dir)
        target_root = os.path.join(dst_dir, rel_root) if rel_root != '.' else dst_dir
        
        if not os.path.exists(target_root):
            os.makedirs(target_root)
            
        for file in files:
            if file in skip_files:
                continue
                
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_root, file)
            rel_file = os.path.relpath(src_file, src_dir)
            
            if file.endswith('.md'):
                process_markdown(src_file, dst_file, rel_file)
            else:
                shutil.copy2(src_file, dst_file)
                
    print("OKF mass migration completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python migrate.py <source_dir> <dest_dir>")
        sys.exit(1)
        
    source = sys.argv[1]
    destination = sys.argv[2]
    migrate_docs(source, destination)
