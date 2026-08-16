---
title: "Tvet Tem Auditor"
description: "DSOM Reference document for Tvet Tem Auditor."
type: "reference"
id: "docs/reference/skills/tvet-tem-auditor.md"
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

# TVET Tools, Equipment, and Materials (TEM) Auditor Skill

## 1. Purpose

This skill teaches an AI agent to **audit, validate, and structure** JPK-compliant **Tools, Equipment, and Materials (TEM)** lists for NOSS curricula.

The agent applies **four validation gates** to verify equipment ratios, brand neutrality, classification categories, and resource mappings.

---

## 2. Validation Gates

### Gate G1 — Brand Neutrality (Generic Descriptions)
* **Rule:** All items must be listed by their generic technical specification. Specific commercial brand names must not be used as direct item names. Brands can only be referenced as examples using `(e.g., [Brand/Software] or equivalent)`.
* **Audit Action:** Scan the item column. Flag any absolute brand names that do not include the "or equivalent" qualifier.

### Gate G2 — Cohort Ratio Verification (Base 25 Trainees)
* **Rule:** Quantities and ratios must be optimized for a maximum training cohort of **25 trainees** at one time. Valid ratios include:
  - **1:1:** For individual hand tools, software interfaces, or workstations.
  - **1:5:** For shared testing equipment, multimeters, or lab test stations.
  - **1:10:** For racks, ladders, routers, and switches.
  - **1:25:** For collective reference gear, fiber splicing machines, OTDRs, or master network sources.
  - **AR (As Required):** For software features, digital templates, and reference materials.
* **Audit Action:** Flag any arbitrary ratios (e.g., 1:3, 1:7) that do not fit standard TVET cohort distributions.

### Gate G3 — Infrastructure and General Facilities Exclusion
* **Rule:** General institutional furniture, office equipment, or facilities (e.g., chairs, desks, whiteboards, air conditioning, internet access, AV aids) must be excluded from TEM as they are governed under separate licensing criteria.
* **Audit Action:** Flag and reject any general facility items found in the TEM list.

### Gate G4 — Grouping and Classification Integrity
* **Rule:** Every item must be correctly categorized under one of the three JPK groups:
  - **A. Tools:** Hand tools, software toolkits, simulators, and diagnostic programs.
  - **B. Equipment:** Heavy hardware, physical computers, servers, switches, routers, and test devices.
  - **C. Materials:** UTP/fiber cables, connectors, document templates, operational manuals, and threat/configuration logs.
* **Audit Action:** Verify that items are in their correct section. (e.g., a "cabling template document" should be under Materials, not Tools).

---

## 3. Reference Matrix Layout

All TEM tables must match this standard format:

| NO. | ITEM* | RATIO (TEM : Trainees or AR = As Required) |
| :--- | :--- | :--- |
| | | **C01** \| **C02** \| **C03** \| **C04** \| **C05** \| **C06** |
| **A. Tools** | | |
| 1 | Pliers set | 1:1 \| 1:1 \| 1:1 \| \| 1:1 \| |
| 2 | Terminal emulation software (e.g., PuTTY or equivalent) | \| \| 1:1 \| 1:1 \| 1:1 \| 1:1 |
| **B. Equipment** | | |
| 1 | Workstations/Laptops | 1:1 \| 1:1 \| 1:1 \| 1:1 \| 1:1 \| 1:1 |
| 2 | Network switch (e.g., Cisco or equivalent) | \| \| 1:10 \| 1:10 \| 1:10 \| 1:10 |
| **C. Materials** | | |
| 1 | UTP patch cord | \| AR \| AR \| AR \| \| |
| 2 | Sample of network configuration template | \| \| 1:1 \| 1:1 \| 1:1 \| |

---

## 4. Audit Runbook

When requested to review a TEM list, perform these steps:
1. Confirm the list is grouped into **A. Tools**, **B. Equipment**, and **C. Materials**.
2. Run the **Brand Neutrality Check** on all items to verify "or equivalent" wording.
3. Verify that all numerical ratios conform to the standard set of values (**1:1**, **1:5**, **1:10**, **1:25**, or **AR**).
4. Verify that general classroom fittings are excluded.
5. Output a status report indicating if the list passes all four gates.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
