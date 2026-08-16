---
okf_version: 0.1
type: legacy_reference_skill
name: "[LEGACY] linux-l3-c03-w02"
title: linux-l3-c03-w02
version: 1.0.0
description: "[LEGACY REFERENCE FOR HUMAN CONSULTATION ONLY] CARRY OUT SERVER HARDWARE INSTALLATION."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: IT-020-3:2026-CU03-WA02
target_level: 3
weightage: "20%"
---
# Work Activity Summary
This skill governs the execution of CARRY OUT SERVER HARDWARE INSTALLATION. to produce functional operational outputs according to enterprise quality standards.

## Required Utilities & Prerequisites
*   **System Commands:** standard linux utilities
*   **Hardware / Equipment:** Laptops (1:1), Desktops (1:1), Network firewall (1:1), Network router & switch (1:5), Wireless access point (1:5), Server machine / virtualisation host (1:5), Network equipment rack (1:5), KVM switch (1:5), UPS (1:5), NAS / network backup storage (1:2)
*   **Tools:** Screwdrivers (Philips & Flathead), Crimping tools, Punch down tools, Pliers and pry tools, Anti-static wrist straps, ESD mats, Multimeters, Cable testers
*   **Materials:** RJ45 connectors, Cat5e/Cat6 cables, Cable ties, Labels, Thermal paste
*   **Documentation:** organizational SOPs, vendor manuals

## Core Execution Steps (Work Steps)
*   **Step 2.1:** Inspect server hardware.
*   **Step 2.2:** Assemble hardware components.
*   **Step 2.3:** Mount server chassis.
*   **Step 2.4:** Connect server cables.
*   **Step 2.5:** Configure storage layout.
*   **Step 2.6:** Verify POST status.
*   **Step 2.7:** Configure remote management.

## Performance Criteria (Quality Gates)
> Note: For full compliance checklists, refer to the Compliance archive.

*   Unpacked server chassis, accessories, and internal hardware modules inspected for transit damage.
*   Processors, memory modules, and internal hardware components assembled.
*   Rack mounting rails and server chassis mounted within designated rack positions.
*   Power distribution lines, network interfaces, and management cables connected.
*   Local storage devices, hardware RAID volumes and disk controllers configured.
*   Server power-on sequences, BIOS/UEFI POST indicators, and hardware fault alerts verified.
*   Dedicated management ports connected, IP addresses assigned and remote KVM console accessibility verified.


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
**Target Competency:** L4-CU03 (L4-C03-W02-nginx-reverse-proxy-hardening)
**Context Bridge:** Bridges local server software installation to hardened multi-site reverse proxy gateway setups.
