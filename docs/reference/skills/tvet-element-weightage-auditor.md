---
title: "Tvet Element Weightage Auditor"
description: "DSOM Reference document for Tvet Element Weightage Auditor."
type: "reference"
id: "docs/reference/skills/tvet-element-weightage-auditor.md"
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

# TVET Element Content Weightage Auditor Skill

## 1. Purpose

This skill teaches an AI agent to **audit, calculate, and construct** JPK-compliant **Element Content Weightage** tables for NOSS curricula.

This matrix differs fundamentally from the standard "Competency Weightage" table. The critical distinction is that weightages are distributed **vertically across all Competency Units** rather than horizontally per unit.

---

## 2. Validation Gates

### Gate G1 — The Vertical Sum Mandate (100% per Column)
* **Rule:** Each individual domain column (OSH, SD, M&A, IT) must sum to exactly **100% vertically** across all Competency Units. 
* **Audit Action:** Sum the percentages down each column. If any column (OSH, SD, M&A, IT) does not equal exactly 100%, the matrix fails validation and must be recalculated.

### Gate G2 — The Justification Requirement
* **Rule:** The `NOTES` row at the bottom of the table must explicitly state which Competency Unit(s) received the *Highest* and *Lowest* percentage for each domain, along with a pedagogical justification.
* **Audit Action:** Ensure the NOTES row contains 4 distinct blocks (OSH, SD, M&A, IT) explaining the reasoning for the highest and lowest values.

---

## 3. Domain Definitions & Pedagogical Anchors

When calculating or distributing weightages, agents must anchor percentages to these specific domain realities:

1. **OSH (Occupational Safety and Health):**
   * *High Weightage:* Tasks involving physical hardware lifting, rack mounting, server room environmental hazards, and under-desk electrical cabling (e.g., Hardware Installation, End-User Support).
   * *Low Weightage:* Pure software, logical, or remotely configured domains (e.g., Virtualisation, Cybersecurity).

2. **SD (Sustainable Development):**
   * *High Weightage:* Domains that heavily reduce physical footprints, power consumption, and e-waste (e.g., Virtualisation / Server Consolidation).
   * *Low Weightage:* Domains focused strictly on logical data protection (e.g., Cybersecurity).

3. **M&A (Management and Administration):**
   * *High Weightage:* Domains with heavy reliance on policy documentation, SLAs, compliance audits, or ticketing systems (e.g., Cybersecurity Audits, DR Policies, Helpdesk Operations).
   * *Low Weightage:* Basic physical procedural tasks with minimal paperwork (e.g., unboxing and installing hardware).

4. **IT (Industry Technological Advances):**
   * *High Weightage:* The deepest technical engineering cores of the curriculum (e.g., Server Administration, Hypervisor Clustering).
   * *Low Weightage:* Tasks that are highly procedural or heavily balanced by soft skills (e.g., End-User Support).

---

## 4. Reference Table Structure

All generated Element Content Weightage tables must be structured via Markdown or DOCX using this exact layout:

| CU CODE | CU TITLE | OSH | SD | M&A | IT |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **[CU-1]** | [Title 1] | X% | X% | X% | X% |
| **[CU-2]** | [Title 2] | X% | X% | X% | X% |
| **TOTAL ELEMENT CONTENT WEIGHTAGE** | | **100/100%** | **100/100%** | **100/100%** | **100/100%** |
| **NOTES** | | [Highest/Lowest OSH justifications] | [Highest/Lowest SD justifications] | [Highest/Lowest M&A justifications] | [Highest/Lowest IT justifications] |

---

## 5. Audit Execution Runbook

When requested to review or generate an Element Content Weightage sheet:
1. **List all Competency Units**.
2. **Assign logical percentages** based on the Pedagogical Anchors.
3. **Verify Gate G1:** Sum each column (OSH, SD, M&A, IT). Adjust values until every column strictly equals 100%.
4. **Construct the NOTES block** validating Gate G2 with specific justifications.
5. **Output the matrix** in the requested formats.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
