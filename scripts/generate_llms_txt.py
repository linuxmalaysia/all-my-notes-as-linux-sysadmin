# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///

from pathlib import Path


def get_markdown_title(filepath: Path) -> str:
    """Extracts the first H1 heading from a markdown file to use as the title."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    return line[2:].strip()
    except Exception:
        pass
    return filepath.name

def main():
    root_dir = Path(__file__).parent.parent.resolve()
    target_dirs = ['docs', 'openwiki', 'manual', '.agents/skills', '.agents/brain/wings']
    root_files = ['README.md', 'START-HERE.md', 'AGENTS.md', 'CHANGELOG.md', 'NOTICE.md', 'LEGAL-NOTICE.md']
    
    llms_txt_path = root_dir / 'llms.txt'
    llms_full_txt_path = root_dir / 'llms-full.txt'
    
    sections = {
        'Root Documents': [],
        'Documentation (docs)': [],
        'OpenWiki': [],
        'Sovereign Manual NOSS (manual)': [],
        'Agent Skills': [],
        'DSOM Spatial Memory Palace': []
    }
    
    all_files = []
    
    # Gather root files
    for rf in root_files:
        fpath = root_dir / rf
        if fpath.exists():
            sections['Root Documents'].append(fpath)
            all_files.append(fpath)
            
    # Gather directory files
    dir_mapping = {
        'docs': 'Documentation (docs)',
        'openwiki': 'OpenWiki',
        'manual': 'Sovereign Manual NOSS (manual)',
        '.agents/skills': 'Agent Skills',
        '.agents/brain/wings': 'DSOM Spatial Memory Palace'
    }
    
    for d in target_dirs:
        dir_path = root_dir / d
        if dir_path.exists():
            # Exclude node_modules or venv just in case, though they shouldn't be here
            for md_file in dir_path.rglob('*.md'):
                if 'node_modules' in md_file.parts or '.venv' in md_file.parts:
                    continue
                sections[dir_mapping[d]].append(md_file)
                all_files.append(md_file)
                
    # Generate llms.txt
    print("Generating llms.txt...")
    with open(llms_txt_path, 'w', encoding='utf-8') as f:
        f.write("# DSOM AI Knowledge Base\n\n")
        f.write("> DSOM-governed, OKF v0.1 compliant documentation index for AI Agents and LLMs. This file lists all relevant markdown documentation in the repository.\n\n")
        
        for section_name, files in sections.items():
            if not files:
                continue
            f.write(f"## {section_name}\n")
            # Sort files alphabetically
            sorted_files = sorted(files, key=lambda x: x.name)
            for fpath in sorted_files:
                # Get relative path from root using forward slashes
                rel_path = fpath.relative_to(root_dir).as_posix()
                title = get_markdown_title(fpath)
                f.write(f"- [{title}]({rel_path})\n")
            f.write("\n")
            
    # Generate llms-full.txt
    print("Generating llms-full.txt...")
    with open(llms_full_txt_path, 'w', encoding='utf-8') as f:
        f.write("# DSOM AI Knowledge Base (Full Content)\n\n")
        f.write("This file contains the full concatenated contents of all markdown documents in the repository.\n\n")
        
        for section_name, files in sections.items():
            if not files:
                continue
            sorted_files = sorted(files, key=lambda x: x.name)
            for fpath in sorted_files:
                rel_path = fpath.relative_to(root_dir).as_posix()
                f.write(f"<!-- BEGIN FILE: {rel_path} -->\n")
                f.write(f"## File: {rel_path}\n\n")
                try:
                    with open(fpath, 'r', encoding='utf-8') as src:
                        f.write(src.read())
                except Exception as e:
                    f.write(f"[Error reading file: {e}]\n")
                f.write(f"\n<!-- END FILE: {rel_path} -->\n\n")

    print(f"Successfully generated {llms_txt_path.name} and {llms_full_txt_path.name}")

if __name__ == '__main__':
    main()
