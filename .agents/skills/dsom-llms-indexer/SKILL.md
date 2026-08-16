---
okf_version: 0.1
name: dsom-llms-indexer
description: Skrip automasi untuk menjana dan mengemas kini indeks llms.txt, llms-full.txt, dan llms_context.xml berasaskan spesifikasi llmstxt.org.
topics: [llms, ai-context, automation, indexing, markdown]
tags: [llms, xml, scripts, generate, context, dsom]
type: operational_skill
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
