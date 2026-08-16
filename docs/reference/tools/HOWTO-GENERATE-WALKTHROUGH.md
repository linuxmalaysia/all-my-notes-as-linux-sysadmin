---
title: "Howto Generate Walkthrough"
description: "DSOM Reference document for Howto Generate Walkthrough."
type: "reference"
id: "docs/reference/tools/HOWTO-GENERATE-WALKTHROUGH.md"
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

# HOWTO: generate-walkthrough — Session Scribe

# docs/tools/HOWTO-GENERATE-WALKTHROUGH.md

> **Standard: DSOM For My AI Protocol v6.1 | Cognitive Automation**
> **Tools:** `generate-walkthrough.ps1`, `generate-walkthrough.sh`
> **Platforms:** Windows Native (T1), Linux/WSL2 (T2)

---

## 1. Purpose

`generate-walkthrough` is the **Session Summarizer** of the DSOM ecosystem. It automates the extraction of "Accomplishments" from your Git history and your `task.md` file, formatting them into a standardised "Session Anchor" block ready to be pasted into `walkthrough.md`.

**Use it to:**
- Automatically harvest all commit messages from "Today".
- Identify all tasks marked as `(SELESAI)` in your `task.md`.
- Ensure consistent formatting for your daily mental anchors.
- Reduce the manual overhead of the End-of-Day consolidation ritual.

**Location:** 
- `tools/generate-walkthrough.ps1` (Windows)
- `tools/generate-walkthrough.sh` (Linux/WSL2)

---

## 2. Prerequisites

| Requirement | Minimum | Notes |
|:---|:---|:---|
| Protocol | DSOM 5.0+ | Expects `[x]` and `(SELESAI)` markers in tasks. |
| Git | Yes | Used to harvest today's commit logs. |
| Brain Dir | `.agents/brain/` | Must contain the `task.md` file. |

---

## 3. Usage

### 3.1 Standard Generation

```powershell

# Windows (T1)

.\tools\generate-walkthrough.ps1

```

```bash

# WSL2 / Linux (T2)

bash tools/generate-walkthrough.sh

```

---

## 4. Operation Workflow (Harvesting Logic)

1. **Git Harvest:** Scans `git log` since `today`. It automatically filters out internal `chore(hibernation)` commits to keep the output high-density.
2. **Task Harvest:** Greps for lines containing `[x]` and the tag **`(SELESAI)`** (Malay for Complete) to identify finished work.
3. **Block Generation:** Prints a Markdown snippet to the console.

---

## 5. Reading the Output

The tool prints a block like this:

```markdown

## 🏁 Session Anchor: 2026-04-08 (Auto-Generated)

- **Accomplished:**
    - [x] Initialise project (SELESAI)
    - feat(ui): add modern glassmorphism
- **Current State:** [UPDATE ME]
- **Mental Anchor:** [UPDATE ME]

```

**Instruction:** Copy this entire block and paste it at the TOP of your **`.agents/brain/walkthrough.md`** file during your End-of-Day ritual. Fill in the `[UPDATE ME]` fields manually to provide the AI with logical context for the next session.

---

## 6. Related Documents

| Document | Purpose |
|:---|:---|
| [`.agents/brain/walkthrough.md`](https://gitlab.com/linuxmalaysia/skills-noss-malaysia-for-linux.git/blob/main/.agents/brain/walkthrough.md) | The target file for the generated output. |
| [`docs/EOD-RITUAL.md`](../EOD-RITUAL.md) | Where this tool fits in the session close-out. |

---

*Standard: DSOM For My AI Protocol v6.1 | Harisfazillah Jamel | LinuxMalaysia*
*Document Version: v1.0 | Created: 2026-04-08*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
