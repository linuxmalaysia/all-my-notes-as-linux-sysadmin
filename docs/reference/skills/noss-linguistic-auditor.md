---
title: "Noss Linguistic Auditor"
description: "DSOM Reference document for Noss Linguistic Auditor."
type: "reference"
id: "docs/reference/skills/noss-linguistic-auditor.md"
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

# NOSS Linguistic Auditor Skill

## 1. Purpose

This skill teaches an AI agent to **read and audit** NOSS Level 3 Competency
Profile content for linguistic compliance.

The agent applies **four quality gates** by reading the content and comparing
it against the rules and examples in this document:

| Gate | Name | What it checks |
| :--- | :--- | :------------- |
| G1 | **Active Voice** | Work Steps begin with an action verb |
| G2 | **Passive Voice** | Performance Criteria contain a passive-voice indicator |
| G3 | **1-to-1 Mapping** | Step count exactly equals Criteria count per WA |
| G4 | **Language Cleanliness** | No vague phrases, no forbidden OS commands |
| G5 | **UK English Spelling** | All content uses British English spelling conventions |
| G6 | **ASE Domain Separation**| Strict separation of physical Safety vs IT Security, plus grammar rules |

---

## 2. The Four Quality Gates

---

### Gate G1 — Active Voice (Work Steps)

**Rule:** Every Work Step must begin with a present-tense **action verb**.

A step describes what **the person does**. It must not begin with:
- A past-tense verb ending in `-ed` (e.g. `Installed`, `Configured`, `Verified`)
- A noun (e.g. `The system`, `Server`, `Network`)
- A passive construction (e.g. `Is installed`, `Was configured`)

#### ✅ PASS Examples (Active Voice)

```
Install the server operating system using the bootable USB drive.
Configure the hostname and static IP address in the network settings file.
Verify the network adapter link status using the ping command.
Open the firewall management console on the local system.
Check the system log directory for critical error entries.
```

#### ❌ FAIL Examples (Passive Voice in Steps)

```
Installed the server OS using the bootable USB.       ← past-tense, sounds passive
The hostname was configured in the settings file.     ← "was configured" = passive
Network adapter is verified using ping.               ← "is verified" = passive
System log directory is opened to check errors.       ← "is opened" = passive
```

#### 🔧 How to Fix

| ❌ FAIL | ✅ PASS |
| :------ | :------ |
| `Installed the server OS` | `Install the server OS` |
| `The hostname was configured` | `Configure the hostname` |
| `Network adapter is verified` | `Verify the network adapter` |

**Pattern:** Strip past tense / passive wrapper → start with bare infinitive verb.

---

### Gate G2 — Passive Voice (Performance Criteria)

**Rule:** Every Performance Criterion must contain a **passive-voice indicator**
verb and end with `in accordance with [reference/standard/policy]`.

A criterion describes what **was achieved**. It must:
1. Start with the **object** (not the person)
2. Contain a past-participle passive verb (see whitelist below)
3. End with `in accordance with [document/policy/procedure]`

#### Approved Passive Verb Whitelist

The criterion must contain **at least one** of these words:

> **Note:** All words use **UK English spelling**. US spellings (e.g. `analyzed`, `synchronized`) are not accepted.

```
accessed        activated       added           addressed       allocated
analysed        applied         archived        assembled       assigned
audited         booted          captured        categorised     checked
cleared         cloned          closed          collected       compiled
completed       confirmed       configured      connected       conducted
converted       copied          created         defined         deployed
determined      diagnosed       disabled        displayed       documented
established     evaluated       executed        exported        extracted
filtered        formatted       generated       handled         identified
implemented     installed       inspected       investigated    isolated
launched        loaded          locked          logged          maintained
managed         mapped          matched         monitored       mounted
notified        operated        organised       parsed          performed
prepared        provided        pulled          purged          queried
recognised      recorded        reclaimed       registered      removed
resolved        restored        restricted      retrieved       reviewed
reverted        saved           scheduled       secured         selected
set             simulated       started         stopped         structured
submitted       supported       synchronised    tested          toggled
traced          tracked         triaged         triggered       updated
uploaded        validated       verified        visualised      written
```

#### ✅ PASS Examples (Passive Voice Criteria)

```
Server operating system installed and license credentials configured in
accordance with license compliance guides.

Network adapter link status and gateway connectivity verified using ping
tools in accordance with connection guidelines.

System log directory accessed and critical error files identified in
accordance with diagnostic checklist.

Firewall inbound rules configured to block unauthorized packets in
accordance with host network defense policies.
```

#### ❌ FAIL Examples (Active / No Passive Indicator)

```
The technician installs the OS and sets up the credentials.
← Active voice, starts with "the technician"

User opens the firewall console and blocks the ports.
← Active voice, no passive verb from whitelist

Network settings should be correct for the system to work.
← Vague, no passive indicator, no "in accordance with"

Check that the ping works.
← Active command, not a criterion
```

#### 🔧 How to Fix

| ❌ FAIL | ✅ PASS |
| :------ | :------ |
| `The technician installs the OS` | `OS installed and credentials configured in accordance with license compliance guides.` |
| `User opens the firewall` | `Firewall configuration interface accessed in accordance with security policy.` |
| `Check that the ping works` | `Network connectivity verified using ping tools in accordance with connection guidelines.` |

**Pattern:** Object first → passive verb → `in accordance with [reference]`.

---

### Gate G3 — 1-to-1 Mapping

**Rule:** The number of Work Steps in a WA must **exactly equal** the number
of Performance Criteria in that same WA.

Each step N.M must have a matching criterion N.M.

#### ✅ PASS Example (5 steps = 5 criteria)

```
WORK STEPS                                    PERFORMANCE CRITERIA
1.1 Identify server installation specs.       1.1 Server specs identified in accordance with checklist.
1.2 Identify server hardware requirements.    1.2 Hardware requirements identified in accordance with procedure.
1.3 Identify server software requirements.    1.3 Software requirements identified in accordance with specs.
1.4 Map server network configuration.         1.4 Network config mapped in accordance with addressing scheme.
1.5 Prepare installation tools.               1.5 Tools prepared in accordance with handling guidelines.
```

#### ❌ FAIL Example (5 steps ≠ 4 criteria)

```
WORK STEPS                                    PERFORMANCE CRITERIA
1.1 Identify server installation specs.       1.1 Server specs identified in accordance with checklist.
1.2 Identify server hardware requirements.    1.2 Hardware requirements identified in accordance with procedure.
1.3 Identify server software requirements.    1.3 Software requirements identified in accordance with specs.
1.4 Map server network configuration.         1.4 Network config mapped in accordance with addressing scheme.
1.5 Prepare installation tools.               ← MISSING criterion 1.5
```

**Fix:** Add the missing criterion, or remove the extra step. Always balance.

---

### Gate G4 — Language Cleanliness

This gate has **three sub-checks**:

#### G4a — No Vague or "Guess and Check" Language

These phrases are **forbidden** anywhere in Work Steps or Performance Criteria:

| Forbidden Phrase | Why forbidden |
| :--------------- | :------------ |
| `guess` | No guessing in a structured operation |
| `trial and error` | Trainees need deterministic steps |
| `play around` | Unprofessional and unstructured |
| `try running` | Implies uncertainty — use `Run` instead |
| `check the screen error` | Too vague — specify what to check |
| `should work` | Not a verifiable outcome |
| `might be` | Ambiguous |
| `somehow` | Vague |

#### ✅ PASS (Precise language)

```
Run the system disk cleanup utility using the built-in tool.
Verify the backup status in the task scheduler log.
Identify the error code from the system event viewer.
```

#### ❌ FAIL (Vague language)

```
Try running the cleanup tool and see if it works.
Play around with the settings until the backup works.
Somehow get the error message from somewhere in the log.
```

---

#### G4b — No Forbidden OS Commands (OS Boundary Check)

Linux content must not reference Windows commands.
Windows content must not reference Linux commands.

**Forbidden in Linux content:**

```
ipconfig       powershell      cmd.exe
cls            dir /           dir \
```

**Forbidden in Windows content:**

```
apt update     apt install     clamscan
lynis          systemctl restart    sudo systemctl
```

#### ✅ PASS

```
[Linux step]  Check network interface settings using the ip addr command.
[Windows step] Check network adapter settings using the ipconfig command.
```

#### ❌ FAIL

```
[Linux step]  Use ipconfig to check network settings.     ← Windows command in Linux content
[Windows step] Run apt install to install the package.    ← Linux command in Windows content
```

---

#### G4c — No Overly Complex Commands in Trainee Steps

Commands in Work Steps must be simple, single-purpose, and Level 3 appropriate.

**Forbidden patterns:**

| Pattern | Why forbidden |
| :------ | :------------ |
| `awk` pipelines | Too complex for L3 trainees |
| `sed` inline substitution | Abstracted to `/scripts/` |
| `grep -E` or `grep -P` | Regex too advanced |
| More than 1 pipe `\|` in one command | Complex pipeline — abstract it |
| `perl -e` | Not a basic utility |

#### ✅ PASS (Simple commands)

```
cat /var/log/syslog
systemctl status nginx
ip addr show
ping -c 4 8.8.8.8
ls -lh /var/backups/
```

#### ❌ FAIL (Too complex for Level 3)

```
awk '{print $1}' /var/log/auth.log | sort | uniq -c | sort -rn | head -10
grep -E "Failed|Invalid" /var/log/auth.log | awk '{print $NF}' | sort
sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
```

**Fix:** Move complex commands to `/scripts/` bash files. Reference the script name in the step:
```
Run the audit-ssh-failures.sh script to extract failed login events.
```

---

## 3. How to Apply This Skill (Step-by-Step)

### Step 1 — Read the content

Read the Work Activity content to be audited. Identify:
- The WA title and code
- All Work Steps (numbered N.M)
- All Performance Criteria (numbered N.M)

### Step 2 — Run Gate G3 first (count check)

Count the steps and count the criteria.
If they do not match → flag immediately and stop. Fix the count before checking voice.

### Step 3 — Run Gate G1 (Active Voice on Steps)

For each step:
- Read the first word
- Is it a present-tense action verb? → PASS
- Does it end in `-ed`? → FAIL
- Does it start with `The`, `A`, `An`? → FAIL
- Does it contain `is/was/were + verb`? → FAIL

### Step 4 — Run Gate G2 (Passive Voice on Criteria)

For each criterion:
- Does it contain at least one word from the Passive Verb Whitelist? → PASS
- Does it end with `in accordance with [something]`? → Required
- Does it start with an object (not "The technician" or "The person")? → Required

### Step 5 — Run Gate G4 & G5

Scan every line for:
- Forbidden vague phrases (G4a)
- Wrong OS commands for the platform (G4b)
- Complex multi-pipe commands or awk/sed (G4c)
- UK English spelling enforcement (G5)

### Step 6 — Run Gate G6 (ASE Domain Separation)

Scan Attitude/Safety/Environment columns:
- Does SAFETY contain IT security rules? (e.g., password, firewall, SHA-256) → FAIL
- Do ATTITUDE sentences start with a descriptive adjective? → Required
- Do ENVIRONMENT sentences start with a sustainability verb? → Required
- Do SAFETY sentences start with a physical care imperative verb? → Required

### Step 7 — Report findings

For each error found, report in this format:

```
[GATE] [WA Code] [Step/Criterion Number]
Issue: [description of the problem]
Current text: "[the failing text]"
Suggested fix: "[the corrected text]"
```

### Step 8 — Confirm PASS

If no errors are found across all 4 gates:
```
✅ PASS — [WA Code]: All linguistic quality gates satisfied.
Steps: N | Criteria: N | Active Voice: ✓ | Passive Voice: ✓ | Language: ✓
```

---

## 4. Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│               NOSS L3 LINGUISTIC QUALITY GATES                  │
├──────┬──────────────────────────────────────────────────────────┤
│  G1  │ WORK STEPS → Active Voice                                │
│      │ ✓ Start with action verb: Install / Configure / Verify   │
│      │ ✗ No past tense: Installed / Configured / Was verified   │
├──────┼──────────────────────────────────────────────────────────┤
│  G2  │ PERFORMANCE CRITERIA → Passive Voice                     │
│      │ ✓ Object first + passive verb + "in accordance with"     │
│      │ ✗ No active construction, no missing reference           │
├──────┼──────────────────────────────────────────────────────────┤
│  G3  │ 1-to-1 MAPPING                                           │
│      │ ✓ Step count = Criteria count (exact match)              │
│      │ ✗ Any mismatch = immediate FAIL                          │
├──────┼──────────────────────────────────────────────────────────┤
│  G4  │ LANGUAGE CLEANLINESS                                     │
│      │ ✓ Precise, deterministic language                        │
│      │ ✗ No: "try", "guess", "play around", "should work"       │
│      │ ✗ No: wrong OS commands for the platform                 │
│      │ ✗ No: awk / sed / grep -E / multi-pipe commands          │
├──────┼──────────────────────────────────────────────────────────┤
│  G5  │ UK ENGLISH SPELLING                                      │
│      │ ✓ Use -ise, -our, -re (e.g. Virtualisation, Colour)      │
│      │ ✗ No US spelling (e.g. Virtualization, Color)            │
├──────┼──────────────────────────────────────────────────────────┤
│  G6  │ ASE DOMAIN SEPARATION                                    │
│      │ ✓ SAFETY is strictly physical (ESD, lifting)             │
│      │ ✗ SAFETY must NOT contain IT Security (passwords, crypto)│
└──────┴──────────────────────────────────────────────────────────┘
```

---

## 5. Gate G5 — UK English Spelling

**Rule:** All content must use **British English** spelling. Malaysia follows the
Commonwealth standard and JPK documents use British English conventions.

### Mandatory UK Spellings

| ❌ US Spelling (REJECT) | ✅ UK Spelling (ACCEPT) |
| :---------------------- | :--------------------- |
| `analyzed` | `analysed` |
| `Analyze` | `Analyse` |
| `organized` | `organised` |
| `recognized` | `recognised` |
| `synchronized` | `synchronised` |
| `categorized` | `categorised` |
| `prioritized` | `prioritised` |
| `optimized` | `optimised` |
| `utilization` | `utilisation` |
| `virtualization` | `virtualisation` |
| `organization` | `organisation` |
| `authorization` | `authorisation` |
| `initialization` | `initialisation` |
| `visualization` | `visualisation` |
| `color` | `colour` |
| `behavior` | `behaviour` |
| `neighbor` | `neighbour` |
| `license` (noun) | `licence` (noun) |
| `practice` (verb) | `practise` (verb) |
| `program` (non-IT) | `programme` |

> **Note:** In computing contexts, `program` (software) is acceptable in both variants.
> `licence` as a noun (e.g. `license key`) — use `licence`. As a verb `to license` both are accepted but prefer UK.

### ✅ PASS Examples

```
Server operating systems and virtualisation platforms determined...
Diagnostic findings analysed in accordance with troubleshooting guidelines.
Resource utilisation metrics verified in accordance with monitoring policy.
Organised in accordance with inventory organisation standards.
```

### ❌ FAIL Examples

```
Diagnostic findings analyzed in accordance with troubleshooting guidelines.
← "analyzed" is US spelling → fix to "analysed"

Virtualization platforms installed in accordance with...
← "Virtualization" is US spelling → fix to "Virtualisation"

Resource utilization metrics verified...
← "utilization" is US spelling → fix to "utilisation"
```

---

## 6. Gate G6 — ASE Domain Separation

**Rule:** The `ATTITUDE / SAFETY / ENVIRONMENT` section must strictly separate physical human safety from IT security, and enforce specific grammatical constraints for each domain.

### G6a — Safety vs. Security
*   **SAFETY** is strictly about the physical safety of the human performing the task. (e.g., ergonomics, ESD straps, handling sharp tools). IT Security (passwords, firewalls, credentials, cryptographic hashes) must **NEVER** be placed under SAFETY.

### G6b — Grammar Enforcements
*   **ATTITUDE:** Must begin with a descriptive adjective (e.g., *Systematic in...*, *Careful in...*).
*   **ENVIRONMENT:** Must begin with a sustainability action verb (e.g., *Practice [3R]*, *Minimize...*).
*   **SAFETY:** Must begin with a physical care action verb (e.g., *Wear*, *Practice*, *Isolate*).
*   **SECURITY:** Must begin with a defense/governance action verb (e.g., *Comply*, *Protect*, *Validate*).

#### ✅ PASS Examples
```
ATTITUDE Systematic in recording support information.
ENVIRONMENT Practice 3R concept for electronic parts.
SAFETY Wear ESD wrist strap when handling electronics.
SECURITY Protect database folders containing licensing keys.
```

#### ❌ FAIL Examples
```
SAFETY Protect administrator credentials.
← FAIL (G6a): IT Security must not be listed as Safety.

ENVIRONMENT Always turn off the lights.
← FAIL (G6b): Missing sustainability action verb (e.g. "Minimize").
```

---

## 7. Scope Boundary

> **⚠️ LEVEL 3 CONSTRAINT**
>
> This skill audits content intended for **SPM-entry vocational trainees**.
> All corrections must maintain Level 3 simplicity.
> Do not introduce advanced terminology, complex commands, or Level 4+ concepts
> when suggesting fixes.

---

## 8. Related Skills

- **`noss-cp-docx-formatter`** — use after linguistic audit to regenerate CP documents
- **`noss-cpc-docx-formatter`** — use after audit to regenerate CPC documents
- **`template-noss-l3-skill`** — reference template for correct SKILL.md structure
