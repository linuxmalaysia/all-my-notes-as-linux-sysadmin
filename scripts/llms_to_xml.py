# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///

import argparse
import re
from pathlib import Path


def parse_llms_txt(llms_txt_path: Path) -> list[str]:
    """Extracts valid file paths from an llms.txt markdown file."""
    paths = []
    # Regex to capture standard markdown links: [Title](path/to/file.md)
    link_pattern = re.compile(r'\[.*?\]\((.*?\.md)\)')
    
    with open(llms_txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = link_pattern.search(line)
            if match:
                path = match.group(1).strip()
                paths.append(path)
    return paths

def generate_xml_context(root_dir: Path, file_paths: list[str], output_path: Path):
    """Reads all referenced markdown files and generates an XML context file."""
    # We use simple string concatenation here to avoid XXE vulnerabilities (Rule #13)
    # when processing user data, though here we are just generating XML.
    
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        out.write('<context>\n')
        
        for rel_path in file_paths:
            full_path = root_dir / rel_path
            if full_path.exists() and full_path.is_file():
                try:
                    with open(full_path, 'r', encoding='utf-8') as src:
                        content = src.read()
                        
                    # Escape basic XML special characters
                    content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    
                    out.write(f'  <file path="{rel_path}">\n')
                    out.write('    <content>\n')
                    out.write(content)
                    out.write('\n    </content>\n')
                    out.write('  </file>\n')
                except Exception as e:
                    print(f"Warning: Could not read {rel_path}: {e}")
            else:
                print(f"Warning: File not found {rel_path}")
                
        out.write('</context>\n')

def main():
    parser = argparse.ArgumentParser(description="Parse llms.txt and generate an XML context file.")
    parser.add_argument("--input", "-i", type=str, default="llms.txt", help="Path to llms.txt")
    parser.add_argument("--output", "-o", type=str, default="llms_context.xml", help="Output XML file path")
    args = parser.parse_args()

    root_dir = Path.cwd()
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        return
        
    print(f"Parsing {input_path.name}...")
    file_paths = parse_llms_txt(input_path)
    print(f"Found {len(file_paths)} file references.")
    
    print(f"Generating XML context to {output_path.name}...")
    generate_xml_context(root_dir, file_paths, output_path)
    print("Done.")

if __name__ == '__main__':
    main()
