# NOSS Linguistic Audit Examples

## How to use this file

An AI agent reads these examples to understand what PASS and FAIL looks like
for each quality gate before auditing real content.

---

## Example A — FULL PASS (CU03-WA01)

This is a correctly written Work Activity. All 4 gates pass.

```
WA Title : Prepare server installation requirements.
WA Code  : IT-020-3:2026-CU03-WA01
Platform : Linux
```

### Work Steps ✅

| # | Step | Gate G1 check |
|:--|:-----|:-------------|
| 1.1 | Identify server installation specifications. | ✅ "Identify" — action verb |
| 1.2 | Identify server hardware requirements. | ✅ "Identify" — action verb |
| 1.3 | Identify server software requirements. | ✅ "Identify" — action verb |
| 1.4 | Map server network configuration settings. | ✅ "Map" — action verb |
| 1.5 | Prepare server installation tools and safety equipment. | ✅ "Prepare" — action verb |

### Performance Criteria ✅

| # | Criterion | Gate G2 check |
|:--|:----------|:-------------|
| 1.1 | Server installation specifications and deployment requirements **analyzed** in accordance with the enterprise server installation checklist. | ✅ "analyzed" in whitelist |
| 1.2 | Server physical form factor and hardware module specs **determined** in accordance with the hardware inventory record procedure. | ✅ "determined" in whitelist |
| 1.3 | Server operating systems and configuration profiles **determined** in accordance with software technical specifications. | ✅ "determined" in whitelist |
| 1.4 | Pre-installation server configuration details (hostnames, static IPs, DNS) **mapped** in accordance with network addressing scheme. | ✅ "mapped" in whitelist |
| 1.5 | Server installation tools and safety gear **prepared** in accordance with server environment handling guidelines. | ✅ "prepared" in whitelist |

### Audit Result

```
✅ PASS — IT-020-3:2026-CU03-WA01
Steps: 5 | Criteria: 5 | 1-to-1: ✓ | Active Voice: ✓ | Passive Voice: ✓ | Language: ✓
```

---

## Example B — MULTIPLE FAILURES (CU03-WA02)

This Work Activity has intentional errors across all 4 gates.

```
WA Title : Carry out server hardware installation.
WA Code  : IT-020-3:2026-CU03-WA02
Platform : Linux
```

### Work Steps ❌ (with errors)

| # | Step (with errors) | Problem |
|:--|:-------------------|:--------|
| 2.1 | Server chassis was unpacked and inspected for damage. | ❌ G1: "was unpacked" = passive voice |
| 2.2 | Assembled server processors, cooling modules, memory. | ❌ G1: "Assembled" = past tense |
| 2.3 | Mount server chassis on rack rails and secure it. | ✅ "Mount" = OK |
| 2.4 | Make sure the cables are all plugged in properly. | ❌ G4a: "Make sure" is vague; "properly" is vague |
| 2.5 | Use ipconfig to check server IP after boot. | ❌ G4b: `ipconfig` is a Windows command in Linux content |

**Step count: 5**

### Performance Criteria ❌ (with errors)

| # | Criterion (with errors) | Problem |
|:--|:------------------------|:--------|
| 2.1 | Server chassis unpacked and modules inspected for damage in accordance with server safety guidelines. | ✅ OK |
| 2.2 | The technician assembles server hardware and checks it is working. | ❌ G2: Active voice, starts with "The technician" |
| 2.3 | Server chassis mounted in accordance with datacenter mounting specs. | ✅ OK |
| 2.4 | All cables plugged in. | ❌ G2: No passive verb from whitelist, no "in accordance with" |

**Criteria count: 4**

### Audit Report

```
❌ FAIL — IT-020-3:2026-CU03-WA02

[G3] 1-to-1 MAPPING MISMATCH
  Issue: Steps count (5) does not match Criteria count (4).
  Fix: Add missing criterion 2.5 to match step 2.5.

[G1] ACTIVE VOICE VIOLATION — Step 2.1
  Current: "Server chassis was unpacked and inspected for damage."
  Fix:     "Unpack server chassis and inspect modules for damage."

[G1] ACTIVE VOICE VIOLATION — Step 2.2
  Current: "Assembled server processors, cooling modules, memory."
  Fix:     "Assemble server processors, cooling modules, and memory channels."

[G4a] VAGUE LANGUAGE — Step 2.4
  Current: "Make sure the cables are all plugged in properly."
  Fix:     "Connect server interface cables firmly to the designated ports."

[G4b] OS BOUNDARY VIOLATION — Step 2.5
  Current: "Use ipconfig to check server IP after boot."
  Fix:     "Verify server IP address assignment using the ip addr show command."
           (ipconfig is a Windows command — forbidden in Linux content)

[G2] PASSIVE VOICE VIOLATION — Criterion 2.2
  Current: "The technician assembles server hardware and checks it is working."
  Fix:     "Server hardware components assembled in accordance with server hardware installation manuals."

[G2] PASSIVE VOICE VIOLATION — Criterion 2.4
  Current: "All cables plugged in."
  Fix:     "Server physical interface connections connected firmly in accordance with cabling protocols."
```

---

## Example C — CORRECTED VERSION of Example B

After applying all fixes from the audit report:

### Work Steps ✅ (corrected)

| # | Step | Gate G1 |
|:--|:-----|:--------|
| 2.1 | Unpack server chassis and inspect modules for damage. | ✅ "Unpack" |
| 2.2 | Assemble server processors, cooling modules, and memory channels. | ✅ "Assemble" |
| 2.3 | Mount server chassis on rack rails and secure within the enclosure. | ✅ "Mount" |
| 2.4 | Connect server interface cables firmly to the designated ports. | ✅ "Connect" |
| 2.5 | Boot up the server and verify the POST status output. | ✅ "Boot" |

### Performance Criteria ✅ (corrected)

| # | Criterion | Gate G2 |
|:--|:----------|:--------|
| 2.1 | Server chassis **unpacked** and internal modules **inspected** for damage in accordance with server safety guidelines. | ✅ |
| 2.2 | Server processors, cooling modules, and memory channels **assembled** in accordance with server hardware installation manuals. | ✅ |
| 2.3 | Server chassis **mounted** on rack rails and **secured** within the server rack enclosure in accordance with datacenter mounting specifications. | ✅ |
| 2.4 | Server physical interface connections **connected** firmly in accordance with cabling protocols. | ✅ |
| 2.5 | Server Power-On Self-Test (POST) status **verified** without errors in accordance with controller BIOS specifications. | ✅ |

### Audit Result

```
✅ PASS — IT-020-3:2026-CU03-WA02 (corrected)
Steps: 5 | Criteria: 5 | 1-to-1: ✓ | Active Voice: ✓ | Passive Voice: ✓ | Language: ✓
```

---

## Example D — G4c Complex Command Violation

A step that uses a multi-pipe command forbidden at Level 3.

### ❌ FAIL

```
Step 3.2: Extract failed SSH login attempts from the auth log using the command:
  awk '/Failed password/ {print $11}' /var/log/auth.log | sort | uniq -c | sort -rn | head -10
```

**Audit finding:**
```
[G4c] COMPLEX PIPELINE VIOLATION — Step 3.2
  Issue: 4-pipe awk command detected. awk is a forbidden complex utility at Level 3.
  Fix:   Run the audit-ssh-failures.sh script to extract failed login events.
         (The complex pipeline is abstracted into /scripts/audit-ssh-failures.sh)
```

### ✅ PASS (after fix)

```
Step 3.2: Run the audit-ssh-failures.sh script to extract failed SSH login events.
```

---

## Passive Verb Whitelist — Quick Lookup Table

Use this table when checking if a criterion contains an approved passive verb.

| A–C | D–L | M–R | S–Z |
|:----|:----|:----|:----|
| accessed | defined | maintained | saved |
| activated | deployed | managed | scheduled |
| added | determined | mapped | secured |
| allocated | diagnosed | matched | selected |
| analysed | disabled | monitored | set |
| applied | displayed | mounted | simulated |
| archived | documented | notified | started |
| assembled | established | operated | stopped |
| assigned | evaluated | parsed | structured |
| audited | executed | performed | submitted |
| booted | exported | prepared | supported |
| captured | extracted | provided | synchronized |
| checked | filtered | pulled | tested |
| cleared | formatted | queried | toggled |
| cloned | generated | recorded | traced |
| collected | handled | registered | tracked |
| compiled | identified | removed | triaged |
| completed | implemented | resolved | triggered |
| confirmed | inspected | restored | updated |
| configured | installed | restricted | uploaded |
| connected | investigated | retrieved | validated |
| converted | isolated | reviewed | verified |
| copied | launched | reverted | visualised |
| created | loaded | | written |
| | locked | | |
| | logged | | |


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
