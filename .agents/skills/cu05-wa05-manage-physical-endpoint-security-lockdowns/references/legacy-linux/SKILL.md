---
okf_version: 0.1
type: legacy_reference_skill
name: "[LEGACY] linux-l3-c05-w05"
title: linux-l3-c05-w05
version: 1.0.0
description: "[LEGACY REFERENCE FOR HUMAN CONSULTATION ONLY] MANAGE SECURITY LOGS AND INCIDENT REPORT."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: IT-020-3:2026-CU05-WA05
target_level: 3
weightage: "20%"
---
# Work Activity Summary
This skill governs the execution of MANAGE SECURITY LOGS AND INCIDENT REPORT. to produce functional operational outputs according to enterprise quality standards.

## Required Utilities & Prerequisites
*   **System Commands:** standard linux utilities
*   **Hardware / Equipment:** Laptops (1:1), Desktops (1:1), Network firewall (1:1), Network router & switch (1:5), Wireless access point (1:5), Server machine / virtualisation host (1:5), Network equipment rack (1:5), KVM switch (1:5), UPS (1:5), NAS / network backup storage (1:2)
*   **Tools:** Screwdrivers (Philips & Flathead), Crimping tools, Punch down tools, Pliers and pry tools, Anti-static wrist straps, ESD mats, Multimeters, Cable testers
*   **Materials:** RJ45 connectors, Cat5e/Cat6 cables, Cable ties, Labels, Thermal paste
*   **Documentation:** organizational SOPs, vendor manuals

## Core Execution Steps (Work Steps)
*   **Step 5.1:** Access event viewers.
*   **Step 5.2:** Filter authentication logs.
*   **Step 5.3:** Export security logs.
*   **Step 5.4:** Archive log files.
*   **Step 5.5:** Report security anomalies.

## Performance Criteria (Quality Gates)
> Note: For full compliance checklists, refer to the Compliance archive.

*   System event viewers or log directories accessed.
*   Event logs filtered to identify failed authentication and login attempts.
*   Filtered security logs exported to external storage formats.
*   Security log files archived to restricted system folders.
*   Security anomalies and audit findings reported to the support supervisor.


## 📂 References (Progressive Disclosure)
To maintain context efficiency and save token budget, detailed 
operational commands and troubleshooting matrices are stored in modular reference files:

*   [**Standard Operating Procedure (SOP)**](references/SOP.md)
*   [**Troubleshooting Guide**](references/TROUBLESHOOTING.md)
*   [**NOSS Compliance Matrix**](references/COMPLIANCE.md)
*   [**Poka-Yoke Execution Scripts**](../../../../../scripts/)


## 🎯 Pedagogical Scope
**Target Level:** NOSS Level 3 (System Administration)
**Constraint:** Execution must be restricted to Level 3 boundaries. Do not introduce advanced orchestration (e.g., Kubernetes), High-Availability clusters, or Level 4/5 architectural complexities.


## Level 4 Progression Pathway (Path of Knowledge)
**Target Competency:** L4-CU05 (L4-C05-W03-firewall-siem-integration)
**Context Bridge:** Bridges host-based security hardening to centralised security information and event management (SIEM) log analytics.
