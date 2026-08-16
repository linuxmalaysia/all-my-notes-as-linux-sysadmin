# CPC Markdown Format Reference

## Purpose

Documents the exact Markdown syntax used in `CPC-Level-3.md` (the source)
and the expected output for the CPC in Markdown format.

---

## Complete Format Example

```markdown
# Competency Profile Chart (CPC)

| SECTION | (J) Information and Communication |
| :--- | :--- |
| **GROUP** | (620) Computer Programming, Consultancy and Related Activities |
| **AREA** | Computer System Administration |
| **NOSS TITLE** | Sovereign IT Infrastructure Operations |
| **NOSS LEVEL** | LEVEL 3 |
| **NOSS CODE** | IT-020-3:2026 |


## 🟢 CORE COMPETENCIES

| COMPETENCY UNIT (CU) | WORK ACTIVITIES (WA) |
| :--- | :--- |
| **PERFORM BASIC COMPUTER SYSTEM INSTALLATION AND CONFIGURATION**<br>`[CODE: CU01]` | **1.** Prepare computer system set-up components `[CU01-WA01]`<br><br>**2.** Carry out computer system hardware installation `[CU01-WA02]`<br><br>**3.** Carry out computer Operating System (OS) software installation `[CU01-WA03]`<br><br>**4.** Carry out computer application and device driver installation `[CU01-WA04]`<br><br>**5.** Configure static IP and wireless network parameters `[CU01-WA05]`<br><br>**6.** Prepare computer system installation record `[CU01-WA06]` |
| **OPERATE VIRTUALIZATION ENVIRONMENT**<br>`[CODE: CU02]` | **1.** Determine virtual host and guest VM sizing requirements based on SOP `[CU02-WA01]`<br><br>**2.** Install Type 2 hypervisors and configure local virtual network adapters `[CU02-WA02]`<br><br>**3.** Deploy and configure guest virtual machines `[CU02-WA03]`<br><br>**4.** Manage guest VM operations and server-level network connectivity on a Type 1 hypervisor `[CU02-WA04]`<br><br>**5.** Perform routine troubleshooting for virtualised environments `[CU02-WA05]` |

---
*Note: This Markdown CPC maps identically to the backend .agents/skills registry.*
```

---

## Syntax Rules

### Header Table
- 2-column table (no colspan in Markdown)
- Row 1: plain `SECTION` | plain value (no bold/italics)
- Rows 2–6: `**BOLD LABEL**` | plain value
- NOSS LEVEL and NOSS CODE are separate rows (unlike DOCX which puts them in one row)
- Blank line before and after the table

### CORE COMPETENCIES Table

**CU column (left)**:
```
**CU TITLE IN UPPERCASE BOLD**<br>`[CODE: CUxx]`
```
- `<br>` separates title from code
- Code in backtick monospace: `` `[CODE: CU01]` ``
- Title in `**double asterisk bold**`

**WA column (right)**:
```
**1.** WA Title One `[CUxx-WA01]`<br><br>**2.** WA Title Two `[CUxx-WA02]`
```
- Each WA on a new logical line (separated by `<br><br>`)
- WA number in `**bold**` with a period: `**1.**`
- WA title in plain text (no bold)
- WA code in backtick monospace: `` `[CU01-WA01]` ``
- Code uses short form: `[CUxx-WAyy]` (not full NOSS code)
- NO trailing `<br><br>` after the last WA

### Footer Note
```markdown
---
*Note: This Markdown CPC elegantly replaces the legacy DOCX block layout. It maps identically to the backend `.agents/skills` registry.*
```

---

## Differences: Markdown vs DOCX Representation

| Feature | DOCX Grid | Markdown Table |
| :------ | :-------- | :------------- |
| WA display | Grid cells (max 4 per row) | All WAs in one cell, separated by `<br><br>` |
| CU title | ALL CAPS in yellow cell | `**TITLE CAPS**` in bold |
| CU code | `CODE CUxx` in green cell | `` `[CODE: CUxx]` `` in backtick |
| WA code | `CODE CUxx-WAyy` in blue cell | `` `[CUxx-WAyy]` `` in backtick |
| Section codes | K62, 622 | (J), (620) — human-readable form |
| Colours | Full colour fills | Not represented |
| vMerge | Orange column rowspan | Not applicable |


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
