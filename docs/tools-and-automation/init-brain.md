---
okf_version: 0.1
type: documentation
title: "init-brain"
timestamp: "2026-08-16T08:54:28Z"
topics: ["dsom", "noss-linux"]
tags: ["documentation", "noss"]
description: "OKF-compliant documentation for init-brain.md."
resource: "file:///docs/tools-and-automation\init-brain.md"
---

# 🧠 Brain Initializer (init-brain.sh)

> **"A clean home for a clear mind."** - Initializing the Cognitive State.

## 1. 🏛️ Purpose

**Version:** v4.1 (Root Aware)
**Description:** Safely initializes the `.agents/brain` directory and default artifacts (`task.md`, `walkthrough.md`) to ensure cognitive continuity for AI agents.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Idempotency** | ✅ Enforced | Checks `if [ ! -d ]` before creating. Skips existing files. |
| **Exit-on-Error** | ✅ Active | `set -e` injected for safety. |
| **Root Check** | ✅ Active | Fails if not a git repository. |

## 3. ⚙️ Usage

```bash
./tools/init-brain.sh

```

## 4. 🧠 Logic Flow

1. **Repo Check:** Confirms execution within a valid Git repository.
2. **Directory Creation:** Creates `.agents/brain/` if missing.
3. **Artifact Generation:** Populates `task.md`, `walkthrough.md`, `implementation_plan.md`, and `DSOM_TEMPLATE.md` with default boilerplate content *only if they don't exist*.

## 5. 📝 Extracted Comments

>
> "Safely initializes the Deep State of Mind (DSOM) directory and artifacts at the repository root to ensure cognitive continuity for AI agents."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
