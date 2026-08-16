---
title: "Node Slide Generator"
description: "DSOM Reference document for Node Slide Generator."
type: "reference"
id: "docs/reference/skills/node-slide-generator.md"
dsom_governance:
  domain: "AI"
  context_tier: "L2-Operational"
tags:
  - "dsom-protocol"
  - "diataxis-quadrant"
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---

# node-slide-generator

Use this skill when the user asks to compile, generate, or format PowerPoint presentation slides using Node.js.

## Instructions
1. Ensure the source markdown outline exists (e.g., `docs/slides_outline.md` or `docs/client_name/client_slides.md`).
2. Run the Node.js compiler script passing the input markdown file and the desired output pptx file.
   Command: `node tools/compile_node_slides.js <input.md> <output.pptx>`
   Example: `node tools/compile_node_slides.js docs/slides_outline.md docs/Node_Migration_Presentation.pptx`
3. Verify the output was created successfully.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
