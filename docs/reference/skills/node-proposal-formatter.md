---
title: "Node Proposal Formatter"
description: "DSOM Reference document for Node Proposal Formatter."
type: "reference"
id: "docs/reference/skills/node-proposal-formatter.md"
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

# node-proposal-formatter

Use this skill when the user asks to compile or generate a DOCX proposal using the Node.js compiler, or when updating a document formatted via Node.

## Instructions
1. Ensure the source markdown file exists (e.g., `docs/proposal.md` or `docs/client_name/client_proposal.md`).
2. Run the Node.js compiler script passing the input markdown file and the desired output docx file.
   Command: `node tools/compile_node_proposal.js <input.md> <output.docx>`
   Example: `node tools/compile_node_proposal.js docs/proposal.md docs/Node_Proposal.docx`
3. Verify the output was created successfully.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
