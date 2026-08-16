"""Module operations for extract_detailed_highlights.py.

This module provides internal functions and automation utilities for the
extract_detailed_highlights.py skill/script, adhering to the DSOM architecture.
"""
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "defusedxml",
# ]
# ///

import json
import sys
import zipfile

import defusedxml.ElementTree as ET

if len(sys.argv) != 3:
    print("Usage: uv run --with defusedxml extract_detailed_highlights.py <input.docx> <output.json>")
    sys.exit(1)

docx_path = sys.argv[1]
output_path = sys.argv[2]

namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
}

highlights_data = []

try:
    with zipfile.ZipFile(docx_path) as docx:
        document_xml = docx.read('word/document.xml')
        doc_root = ET.fromstring(document_xml)
        
        page_number = 1
        paragraph_number = 0
        
        for p in doc_root.findall('.//w:p', namespaces):
            paragraph_number += 1
            
            # Count page breaks
            for el in p.iter():
                if el.tag == f"{{{namespaces['w']}}}lastRenderedPageBreak" or \
                   (el.tag == f"{{{namespaces['w']}}}br" and el.get(f"{{{namespaces['w']}}}type") == 'page'):
                    page_number += 1

            has_highlight = False
            for run in p.findall('.//w:r', namespaces):
                highlight = run.find('.//w:highlight', namespaces)
                if highlight is not None:
                    has_highlight = True
                    break
                    
            if has_highlight:
                runs = p.findall('.//w:r', namespaces)
                run_texts = []
                for run in runs:
                    text_nodes = run.findall('.//w:t', namespaces)
                    text = "".join([t.text for t in text_nodes if t.text])
                    if text:
                        highlight = run.find('.//w:highlight', namespaces)
                        is_highlighted = highlight is not None
                        run_texts.append({'text': text, 'highlighted': is_highlighted})
                
                blocks = []
                for rt in run_texts:
                    if not blocks:
                        blocks.append(rt)
                    else:
                        if blocks[-1]['highlighted'] == rt['highlighted']:
                            blocks[-1]['text'] += rt['text']
                        else:
                            blocks.append(rt)
                
                for i, block in enumerate(blocks):
                    if block['highlighted'] and block['text'].strip():
                        before_context = "".join([b['text'] for b in blocks[:i]])
                        after_context = "".join([b['text'] for b in blocks[i+1:]])
                        
                        highlights_data.append({
                            'page': page_number,
                            'paragraph': paragraph_number,
                            'before': before_context.strip(), 
                            'highlight': block['text'].strip(),
                            'after': after_context.strip()
                        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(highlights_data, f, indent=2)

    print(f"Extraction complete. Found {len(highlights_data)} detailed highlights.")

except Exception as e:
    print(f"Error: {e}")
