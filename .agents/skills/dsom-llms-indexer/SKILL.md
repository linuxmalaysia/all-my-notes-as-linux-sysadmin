---
okf_version: '0.2'
name: dsom-llms-indexer
description: Skrip automasi untuk menjana dan mengemas kini indeks llms.txt, llms-full.txt,
  dan llms_context.xml berasaskan spesifikasi llmstxt.org.
topics:
- llms
- ai-context
- automation
- indexing
- markdown
tags:
- llms
- xml
- scripts
- generate
- context
- dsom
type: agent_skill
spec_version: '0.2'
title: dsom-llms-indexer
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:45Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

# 🤖 Pengindeksan Repositori LLM (DSOM LLM Indexer)

## Bilakah kemahiran ini patut digunakan?
Gunakan kemahiran ini selepas anda mencipta, mengubah, atau memadam sebarang dokumen Markdown dalam repositori (khususnya selepas operasi pengekstrakan ilmu berskala besar seperti penghasilan Bab silibus). Ini bagi memastikan agen AI lain mempunyai peta navigasi fail yang terkini.

## Keperluan Utama
- Rujukan Format: Spesifikasi rasmi dari [llmstxt.org](https://llmstxt.org/intro.html).
- Skrip ini menggunakan pelaksana `uv` selaras dengan Peraturan 9 (DSOM).

## Langkah-Langkah Pelaksanaan

### 1. Menjana Fail Teks LLM
Jalankan arahan berikut di terminal dari direktori akar (root) projek:
```powershell
uv run scripts/generate_llms_txt.py
```
**Apa yang berlaku:**
- Skrip akan mengimbas (scan) semua fail `.md` dalam direktori penting (seperti `docs/`, `openwiki/`, `palace/`, dan `.agents/skills/`).
- `llms.txt` akan dijana sebagai fail rujukan peta dengan pautan markdown.
- `llms-full.txt` akan dijana sebagai kompilasi gabungan semua teks dokumen untuk *mass ingestion*.

### 2. Menjana Konteks XML Selamat
Selepas `llms.txt` sedia, tukarkannya ke dalam bentuk XML konteks menggunakan:
```powershell
uv run scripts/llms_to_xml.py
```
**Apa yang berlaku:**
- Skrip akan menguraikan (parse) `llms.txt`.
- Ia akan membina satu `llms_context.xml` yang membalut setiap fail dengan sintaks `<file path="..."><content>...</content></file>`.
- Pemprosesan ini adalah selamat daripada kerentanan XXE.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
