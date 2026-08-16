---
# Markdown Format Reference — CP-Level-3

## Purpose

This document shows the exact Markdown syntax used in `CP-Level-3-Generated.md`.
AI agents must produce output that exactly matches this pattern.

---

## Document Preamble

```markdown
# 1. Competency Profile (CP)

| SECTION | (J) Information and Communication | | |
| :---- | :---- | :---- | :---- |
| GROUP | (620) Computer Programming, Consultancy and Related Activities | | |
| AREA | Computer System Administration | | |
| NOSS TITLE | Sovereign IT Infrastructure Operations | | |
| NOSS LEVEL | LEVEL 3 | NOSS CODE | IT-020-3:2026 |
```

Note: The header table has 4 columns. The empty `| |` cells create the colspan
effect in standard Markdown viewers.

---

## Per-CU Header Block

```markdown
| CU TITLE & CU CODE | Perform Basic Computer System Installation and Configuration (IT-020-3:2026-CU01) |
| :---- | :---- |
| CU DESCRIPTOR | Paragraph 1 text.<br><br>Paragraph 2 text.<br><br>Paragraph 3 text. |
```

**Rules:**
- `CU TITLE & CU CODE` — literal label (left column)
- Right column: `<Title> (<NOSS Code>)` — title + code in parentheses
- `CU DESCRIPTOR` — literal label (left column)
- Right column: three paragraphs joined with `<br><br>` (double break)
- Blank line after the 2-row table

---

## WA Matrix Block

```markdown
| WORK ACTIVITIES | WORK STEPS | PERFORMANCE CRITERIA |
| ----- | ----- | ----- |
| Prepare server installation requirements..<br>(IT-020-3:2026-CU03-WA01) | 1.1 Identify server installation specifications.<br>1.2 Identify server hardware requirements.<br>1.3 Identify server software requirements.<br>1.4 Map server network configuration settings.<br>1.5 Prepare server installation tools and safety equipment. | 1.1 Server installation specifications and deployment requirements analyzed in accordance with the enterprise server installation checklist.<br>1.2 Server physical form factor (tower, rack, or blade unit) and hardware module specs determined in accordance with the hardware inventory record procedure.<br>1.3 Server operating systems, virtualization platforms, and system configuration profiles determined in accordance with software technical specifications.<br>1.4 Pre-installation server configuration details (hostnames, static IPs, subnet masks, DNS settings) mapped in accordance with network addressing scheme.<br>1.5 Server installation tools and hardware handling safety gear prepared in accordance with server environment handling guidelines. |
```

**Rules for WA column (Col 1):**
- `<WA Name>..` — WA name followed by `..` (two dots, intentional)
- `<br>` — line break
- `(<WA Code>)` — WA code in parentheses

**Rules for Steps column (Col 2):**
- `N.M <Step text>` — numbered with WA number + step number
- Steps separated by `<br>` (single break)
- No trailing `<br>`

**Rules for PC column (Col 3):**
- `N.M <PC text>` — same numbering scheme as Steps
- PCs separated by `<br>` (single break)
- Each PC ends with `in accordance with [reference].`

---

## Complete Example (CU03 WA01)

```markdown
| CU TITLE & CU CODE | Server Installation & Maintenance (IT-020-3:2026-CU03) |
| :---- | :---- |
| CU DESCRIPTOR | Server Installation & Maintenance describes mounting servers in cabinets, deploying server OS, configuring Netplan IPs, checking server room environments, and managing server registries. This activity typically takes place in server environments and is performed to ensure hardware and OS baseline readiness. <br><br>The person who is competent in this CU should be able to prepare server installation requirements, carry out server hardware installation, carry out server software and OS installation, perform server functionality testing and maintenance, and prepare server installation and maintenance records. <br><br>The outcome of this CU is a successfully rack-mounted server with a configured base OS and registered inventory details. |

| WORK ACTIVITIES | WORK STEPS | PERFORMANCE CRITERIA |
| ----- | ----- | ----- |
| Prepare server installation requirements..<br>(IT-020-3:2026-CU03-WA01) | 1.1 Identify server installation specifications.<br>1.2 Identify server hardware requirements.<br>1.3 Identify server software requirements.<br>1.4 Map server network configuration settings.<br>1.5 Prepare server installation tools and safety equipment. | 1.1 Server installation specifications and deployment requirements analyzed in accordance with the enterprise server installation checklist.<br>1.2 Server physical form factor determined in accordance with the hardware inventory record procedure.<br>1.3 Server operating systems and configuration profiles determined in accordance with software technical specifications.<br>1.4 Pre-installation server configuration details mapped in accordance with network addressing scheme.<br>1.5 Server installation tools and safety gear prepared in accordance with server environment handling guidelines. |
```

---

## Blank Line Rules

```
[Header table block]
[blank line]
[CU01 CU TITLE table]
[blank line]
[CU01 WA Matrix table]
[blank line]
[CU02 CU TITLE table]
...
[Final blank line at EOF]
```


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
