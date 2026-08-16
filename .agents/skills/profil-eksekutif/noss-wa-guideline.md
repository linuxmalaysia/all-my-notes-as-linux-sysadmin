---
name: noss-wa-development-guideline
description: >
  Operational standards, imperative syntax, level taxonomy, and quality perimeters
  for constructing Work Activities (WA) and Competency Units (CU) compliant with
  the NOSS Development Guideline 2020 Edition (JPK) and MSIC-2008.
metadata:
  version: 1.2.1
  source_provenance: "NOSS DEVELOPMENT GUIDELINE 2020 EDITION (Department of Skills Development)"
  compliance_framework: MSIC-2008 / DESCUM / Agent Skills Open Standard
  classification: Unclassified - Public Technical Manual
---

# Master Manual for Work Activities (WA) Development

This document establishes the engineering standard for national skills curriculum knowledge management. It serves as a strict guideline for decomposing occupational profiles from macro functions (**Competency Unit - CU**) into deterministic, measurable, and executable micro sub-competencies (**Work Activities - WA**).

---

## 🏛️ 1. WA Syntax & Structural Formula

The syntax for writing a Work Activity (WA) is an imperative command. Each statement line must be locked using the following linguistic mathematical formula:

$$\text{Work Activity (WA)} = \text{Verb (Active Transitive)} + \text{Object} + \left[ \text{Qualifier (Context)} \right]$$

### 🔎 Breakdown of the Standard Syntax Components

1. **Verb (Active Verb):** 
* Must begin with an **Active Transitive Verb** that carries a physical or cognitive action that is visibly *observable*.
* **Strict Prohibition:** It is strictly prohibited to use abstract words that cannot be objectively measured (e.g., *Understand*, *Know*, *Familiarise*, *Learn*).
* **Single Action Verb:** Each WA statement is only permitted to contain **one (1) main verb** to maintain atomic assessment integrity.

2. **Object:**
* The direct receiver of the verb's action. It must be a tangible physical entity, data, system, or legitimate artefact.

3. **Qualifier (Context):**
* An additional phrase that defines the boundaries, criteria, industry standards, or operational limits of the action. It is *optional* but highly critical if misinterpretation could occur without its presence.

### 🗺️ NOSS & CoCU Linguistic Transformation Matrix

There is a strict morphological difference between the standard profile documents (NOSS) and the curriculum learning module titles (Curriculum of Competency Unit - CoCU). Failure to adhere to this transformation will result in a document audit failure.

| Document Type | Structural Component | Morphological Standard (English) | Application Example |
| --- | --- | --- | --- |
| **NOSS (Standard)** | Competency Unit (CU) | Noun Phrase / Gerund | **Deployment** of endpoint devices configuration. |
| **NOSS (Standard)** | Work Activity (WA) | Active Imperative Verb | **Configure** the Fleet logging agent cluster. |
| **CoCU (Curriculum)**| Module Title | **Noun Phrase** / Gerund | **Manufacturing** of Traditional Wood Carving / **Management** of L1 Ingest Operations. |

---

## ⚙️ 2. Mandatory Functional Viability Criteria

Every sub-work function nominated as a WA must pass the **12-Point Assessment Filter** before being included in the *Competency Profile Chart* (CPC):

1. **Observable & Measurable:** The work output must be visually observable or proven via concrete logs/artefacts.
2. **Functional Focus:** Explains *what is done*, rather than describing the work situation or environment.
3. **Standalone Independence:** Can be executed in isolation as a discrete task without mandatory dependency drag from another WA.
4. **Complete Work Cycle:** Has a clear trigger point and a distinct definition of done.
5. **Meaningful Outcome:** Produces a product, service, or decision that holds economic value.
6. **Economic/Assignable Value:** A unit of work that can be assigned to an individual, for which they are entitled to receive remuneration.
7. **Official Certifiable:** Meets the syllabus requirements allowing an assessment panel to verify competency.
8. **Structural Compliance:** Fully adheres to the $\text{Verb} + \text{Object} + \text{Qualifier}$ formula.
9. **Single Action Verb:** No use of bivalent conjunctions (such as "and", "or") that combine two separate work phases.
10. **Step Count Baseline:** Must contain **more than two (>2) work steps** (execution procedures). If a task is completed in 1 or 2 steps, it is classified as a *Task* or *Step*, not a *Work Activity*.
11. **Time-Bound Execution:** Can be completed within a reasonable working shift timeframe, not an endless continuous project.
12. **Explicit Performance Language:** Written with concrete vocabulary that directly references industry performance standards without layered interpretations.

---

## 🧠 3. NOSS Level Matrix Mapping (Levels 1–5 Contextual Alignment)

The selection of Active Verbs must be aligned with the level of responsibility and work autonomy according to the **National Occupational Skills Standard** framework:

| NOSS Level | Competency Nature & Responsibility Boundaries | Suitable Verbs (JPK Taxonomy) |
| --- | --- | --- |
| **Level 1** | Execution of routine, simple, repetitive, and highly predictable tasks under strict supervision. | *Prepare, Wash, Lift, Clean, Move* |
| **Level 2** | Tasks involving various operational contexts with limited autonomous application. | *Handle, Install, Replace, Repair, Maintain* |
| **Level 3** | Complex, non-routine tasks, full autonomy in execution, and bearing the responsibility to guide and control others (*Supervisory Context*). | *Configure, Coordinate, Control, Investigate, Test* |
| **Level 4** | Technical management, system design, resource planning, systemic troubleshooting, and accountability for team output. | *Manage, Plan, Design, Evaluate, Validate* |
| **Level 5** | Strategic, fundamental analysis, macro architectural design, policy rollout, technological innovation, and cross-organisational governance. | *Approve, Formulate, Audit, Mentor, Spearhead* |

### 🔬 Structural Enclosure: Level 3 Specific Focus (Supervisor / Officer Track)

When developing a profile for **NOSS Level 3** (e.g., Malaysian Skills Certificate Level 3 / MQF Level 3), the WA profile must exhibit operational leadership characteristics:

* **Operational Context:** The agent or individual operates systems in highly variable and non-routine environments.
* **Autonomy Level:** Possesses absolute ownership over their own work outputs without requiring micro-management validation at every step.
* **Supervisory Role (*Operational Control*):** Must include at least one Core CU or sub-WA addressing the aspects of **Controlling Others** (monitoring crew SOP compliance) and **Providing Guidance** (training and transferring technical skills to Level 1 & 2 workers).

---

## 🛡️ 4. OpSec & Quality Error Filtration (Anti-Pattern Filters)

During curriculum analysis sessions using the **DESCUM** method, ensure the following error filters (*Anti-Patterns*) are aggressively enforced:

```text
❌ STRUCTURAL ERROR: "Development of logstash logging system" 
   (Reason: Using an Abstract Noun "Development" at the beginning of the WA structure)
✅ STANDARD COMPLIANCE: "Develop Logstash logging pipeline configurations" 
   (Reason: Using an Active Transitive Verb "Develop")

❌ STRUCTURAL ERROR: "Install and configure firewall devices" 
   (Reason: Using Compound Verbs / Two verbs that can be split into 2 separate WAs)
✅ STANDARD COMPLIANCE: WA 1: "Install firewall devices on the server rack"
                      WA 2: "Configure firewall security perimeter rules"

❌ STRUCTURAL ERROR: "Prepare the action plan using Microsoft Excel with full diligence"
   (Reason: Including internal worker attributes "full diligence" and specific tool constraints)
✅ STANDARD COMPLIANCE: "Prepare the infrastructure crisis management action plan"
```

### 📦 Cluster Structure Design Constraints

* **Core CU Payload Limit:** The number of Competency Units (CU) for a single NOSS qualification level must not be left to expand uncontrollably. The standard limits the range to a maximum of **5 to 10 core CUs** per level to prevent token inflation, excessive training costs, and dilution of certification focus.
* **Title Fragility Prevention:** The *Job Title* must possess a clear degree of semantic separation from the *Job Area*. Literal repetition errors (Example: Job Title: *Security Officer* inhabiting Job Area: *Security Officer*) are prohibited. Correct structure: Job Title: *Sovereign Infrastructure Supervisor* inhabiting Job Area: *Guard and Security Technology Services*.

---

## 🗂️ 5. Competency Unit Coding Structure Scheme (MSIC 2008 Standard)

Every unit and activity successfully framed must be assigned a uniquely structured alphanumeric identifier index based on the **MSIC 2008** (Malaysia Standard Industrial Classification) industry classification reference:

```text
[SECTOR CODE] - [SUB-SECTOR CODE] - [LEVEL] : [APPROVAL YEAR] - CU [SEQUENCE NUMBER] - WA [ACTIVITY NUMBER]
```

> **Complex Code Marking Example:**
> * `F43-001-3:2026-CU02-WA04`
> * `F43-001-3:2026` represents the NOSS Code for the Level 3 AIOps Logistics Architecture field approved in the year 2026.
> * `CU02` means the second Competency Unit under that structure.
> * `WA04` refers to the fourth Work Activity arranged in logical work sequence from left to right within the skills profile matrix.

---

## 🛠️ 6. Local WA Syntax Validation Automation Script (`scripts/wa-linter.py`)

To ensure this document does not merely remain passive text, install the WA writing error eradication Python utility script within the `scripts/` folder, to be executed automatically before initiating a Git-Native commit.
