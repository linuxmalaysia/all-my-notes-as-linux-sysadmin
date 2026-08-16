# 🤝 Taklimat Penyerahan Sesi: Google Jules (GitHub)

> **Kepada:** Google Jules (AI Autonomous Coding Agent)  
> **Daripada:** Antigravity (Pair-Programming Lead Agent)  
> **Projek:** Linux for NOSS Malaysia (Sovereign Markdown Palace & DSOM v0.1)  
> **Repositori GitHub:** `https://github.com/linuxmalaysia/all-my-notes-as-linux-sysadmin`  
> **Status:** Fasa 1 Selesai (100% Quality Gate). Sedia untuk Fasa 2 (Migrasi Kandungan Silibus).

---

## 🧭 Protokol Operasi Jules
1. **Baca Perlembagaan AI:** Sila baca [`.agents/AGENTS.md`](../AGENTS.md) terlebih dahulu sebelum memulakan sebarang tugas.
2. **Ketahui Struktur Projek:** Rujuk [`README.md`](../../README.md), [`START-HERE.md`](../../START-HERE.md), dan [`llms.txt`](../../llms.txt).
3. **Penyelarasan Tugas:** Semak [`.agents/brain/task.md`](task.md) dan [`.agents/brain/implementation_plan.md`](implementation_plan.md).

---

## 🎯 Tugasan Utama Anda (Fasa 2):
1. **Migrasi Bab 2 (`references/manual/bab_02/`):**
   - Rujuk manual arkib lama (kekalkan fail mentah - Rule 17).
   - Bentuk nod memori modular dalam `palace/cu01/` berlandaskan edaran moden 2026: **Ubuntu 26.04 LTS**, **Fedora 43**, dan **AlmaLinux 10** (Rule 15).
   - Sertakan panduan **Penyulitan Penuh Cakera LUKS2 Pejabat** (Rule 15).
   - Kemas kini indeks silibus di `openwiki/topic-01-linux-desktop-and-basics.md`.
   - Lengkapkan seksyen penutup silibus (AI Prompts, URL Rujukan, Syor Buku) (Rule 16).
2. **Bina Semula HTML Prabina:** Jalankan `uv run scripts/serve_mkdocs.py --build-only` (Rule 18).
3. **Ujian Kualiti 100%:** Jalankan `uv run run_all_tests.py` sebelum komit (Rule 12).
4. **GitOps Dual-Remote:** Rekodkan komit bermakna dan pastikan perubahan disegerakkan ke remote (Rule 19).
