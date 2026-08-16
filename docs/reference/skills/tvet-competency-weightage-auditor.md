---
title: "Tvet Competency Weightage Auditor"
description: "DSOM Reference document for Tvet Competency Weightage Auditor."
type: "reference"
id: "docs/reference/skills/tvet-competency-weightage-auditor.md"
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

# TVET Competency Weightage Auditor Skill

## 1. Purpose

This skill teaches an AI agent to **audit, validate, and structure** JPK-compliant **Competency Weightage (Peratusan Pemberat Kompetensi)** matrices for NOSS curricula.

The agent applies **four strict validation gates** to check mathematical integrity, elective bounds, and educational prioritization before generating or publishing weightage sheets.

---

## 2. Validation Gates

### Gate G1 — Core CU Sum Constraint (100% Core Total)
* **Rule:** The sum of parent `Competency Unit Weightage` percentages across all Core Competency Units must equal exactly **100%**.
* **Audit Action:** Sum the parent percentages of all Core CUs. If the total is not 100%, flag a failure.

### Gate G2 — Work Activity Sum Constraint (100% per CU)
* **Rule:** Within any single Competency Unit, the sum of all child `Work Activities Weightage` percentages must equal exactly **100%**.
* **Audit Action:** For each CU, sum the child WA percentages. If any CU's activities do not sum to exactly 100%, flag a failure for that CU.

### Gate G3 — Elective CU Capacity Cap (Max 30%)
* **Rule:** If elective Competency Units are included in the curriculum, their combined weightage must not exceed **30%** of the total core competency unit weightage.
* **Audit Action:** Check if the sum of all elective CUs is \(\le 30\%\).

### Gate G4 — Complexity and Priority Check (Pedagogical Check)
* **Rule:** Module weightages must align with task complexity, safety risks, and training contact hours:
  - High-complexity modules (e.g., system administration, troubleshooting, security hardening) should generally have higher weightage.
  - Basic or introductory modules (e.g., computer setup) should have lower or moderate weightage.

---

## 3. Reference Table Structure

All generated Competency Weightage tables must be structured as follows:

| CU CODE | COMPETENCY UNIT TITLE | COMPETENCY UNIT WEIGHTAGE | WORK ACTIVITIES | WORK ACTIVITIES WEIGHTAGE |
| :--- | :--- | :--- | :--- | :--- |
| **[CU-CODE-1]** | [CU Title 1] | [CU-1 Weight]% | 1. [WA 1 Title]<br>2. [WA 2 Title]<br>3. [WA 3 Title] | [WA-1 Weight]%<br>[WA-2 Weight]%<br>[WA-3 Weight]% |
| **[CU-CODE-2]** | [CU Title 2] | [CU-2 Weight]% | 1. [WA 1 Title]<br>2. [WA 2 Title] | [WA-1 Weight]%<br>[WA-2 Weight]% |
| **TOTAL** | **CORE COMPETENCY** | **100%** | | |

---

## 4. Audit Execution Runbook

When requested to review a weightage sheet, execute this checklist:
1. **List all Core CUs** and calculate the sum of the `Competency Unit Weightage` column. Verify it is exactly `100%`.
2. **For each CU**, verify that the child `Work Activities Weightage` values sum up to exactly `100%`.
3. **If electives exist**, sum their parent weights and ensure the total is \(\le 30\%\).
4. **Identify anomalies:** Flag any CUs or WAs with \(0\%\) weightage, non-integer values, or missing titles.
5. **Output a clear pass/fail report** indicating the status of Gates G1 to G4.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
