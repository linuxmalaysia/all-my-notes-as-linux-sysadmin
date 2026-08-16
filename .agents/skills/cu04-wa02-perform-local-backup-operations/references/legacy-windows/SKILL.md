---
okf_version: 0.1
type: legacy_reference_skill
name: "[LEGACY] windows-l3-c04-w02"
title: windows-l3-c04-w02
version: 1.0.0
description: "[LEGACY REFERENCE FOR HUMAN CONSULTATION ONLY] PERFORM LOCAL ENDPOINT FILE BACKUP."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: IT-020-3:2026-CU04-WA02
target_level: 3
weightage: "20%"
---
# Work Activity Summary
This skill governs the execution of PERFORM LOCAL ENDPOINT FILE BACKUP. to produce functional operational outputs according to enterprise quality standards.

## Required Utilities & Prerequisites
*   **System Commands:** standard windows utilities
*   **Hardware / Equipment:** Laptops (1:1), Desktops (1:1), Network firewall (1:1), Network router & switch (1:5), Wireless access point (1:5), Server machine / virtualisation host (1:5), Network equipment rack (1:5), KVM switch (1:5), UPS (1:5), NAS / network backup storage (1:2)
*   **Tools:** Screwdrivers (Philips & Flathead), Crimping tools, Punch down tools, Pliers and pry tools, Anti-static wrist straps, ESD mats, Multimeters, Cable testers
*   **Materials:** RJ45 connectors, Cat5e/Cat6 cables, Cable ties, Labels, Thermal paste
*   **Documentation:** organizational SOPs, vendor manuals

## Core Execution Steps (Work Steps)
*   **Step 2.1:** Connect backup storage.
*   **Step 2.2:** Access backup utility.
*   **Step 2.3:** Configure backup scope.
*   **Step 2.4:** Execute local backup.
*   **Step 2.5:** Verify backup result.

## Performance Criteria (Quality Gates)
> Note: For full compliance checklists, refer to the Compliance archive.

*   Local backup storage connected.
*   Endpoint backup utility accessed.
*   Backup scope configured.
*   Local file backup executed.
*   Backup result verified.


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
**Target Competency:** L4-CU04 (L4-C04-W03-restic-automated-snapshots)
**Context Bridge:** Bridges manual file backups to encrypted, automated offsite snapshot policies using restic.
