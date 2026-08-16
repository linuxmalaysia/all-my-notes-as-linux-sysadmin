---
okf_version: 0.1
type: memory-closet
title: "Fact Closet: Tooling & Automation"
timestamp: "2026-08-17T00:00:00Z"
topics: ["dsom", "tooling", "automation", "quality-gate"]
tags: ["dsom-core", "tools", "memory-closet"]
description: "Fakta alatan pembangunan, penjanaan laman web statik MkDocs, dan orkestrator ujian 100% pematuhan."
resource: "file:///.agents/brain/wings/wing_dsom_core/hall_facts/room_tooling/closet.md"
---

# Fact Closet: Tooling & Automation

## Absolute Facts
- **Binaan Laman Web Statik:** `uv run scripts/serve_mkdocs.py --build-only` menjana laman web ke direktori `html/` yang dijejak dalam Git.
- **Ujian Pematuhan Penuh:** `uv run run_all_tests.py` merangkumi Pytest (Python, OKF compliance, cross-platform filesystem) dan Jest (JavaScript).
- **Piawaian Penjanaan Symlink/Junction:** Menggunakan `mklink /J` di Windows dan `os.symlink` di POSIX.
