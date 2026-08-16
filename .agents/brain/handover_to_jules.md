# 🤝 Taklimat Penyerahan Memori Ejen: Google Antigravity ➔ Google Jules

**Tarikh / Masa:** 2026-08-17  
**Status Sesi Terkini:** Penstrukturan Semula Seni Bina DSOM, `manual/`, Hab Diátaxis, dan Pengukuhan Peraturan 21 Selesai (100% Quality Gate).

---

## 📌 Ringkasan Status & Perubahan Seni Bina Terkini
1. **Pemisahan `manual/` & `.agents/brain/wings/`:**
   - **`manual/`:** Menempatkan kesemua fail modul amali teknikal NOSS Linux (CU01 hingga CU06).
   - **`.agents/brain/wings/`:** Memori Ruang Ejen AI (*Method of Loci / Spatial Memory Palace*) untuk mengekalkan fakta mutlak dan lejar status projek.
   - **`openwiki/`:** Indeks naratif silibus untuk rujukan cepat.
2. **Hab Rujukan Setempat 4 Kuadran Diátaxis:**
   - Pintu masuk utama di `manual/index.md` dan `openwiki/index.md`.
   - Navigasi web di `mkdocs.yml` tersusun mengikut: `1. Pembelajaran (Tutorials)`, `2. Panduan Operasi (How-To Guides)`, `3. Manual Amali NOSS (Reference)`, dan `4. Kefahaman & Silibus (Explanation)`.
3. **Kemahiran Transformasi Kandungan & Peraturan 21:**
   - Kemahiran `.agents/skills/noss-content-transformation-pipeline/` sedia digunakan untuk memproses bahan secara automatik mengikut model IPO (Penilaian CU/WA ➔ Deep Web Research ➔ Pengayaan Keselamatan JDN/MAMPU & Prestasi ➔ Output Terstruktur).
4. **Mandat Porting Kemahiran (Knowledge-to-Skill Mandate):**
   - Setiap modul amali teknikal yang telah disiapkan di `manual/` MESTI dijadikan modul **AI Agent Skill** di bawah `.agents/skills/<skill-folder>/SKILL.md` supaya mana-mana ejen AI lain boleh menggunakannya secara langsung.

---

## 🎯 Tugasan Utama untuk Google Jules (Actionable Next Steps)

### 1. Audit Semula Bab 1 & Bab 2 (manual/cu01/)
- Pastikan semua nod mematuhi Peraturan 21: Deep Research fakta 2026, standard keselamatan **Jabatan Digital Negara (JDN) / MAMPU** (LUKS2/FDE), ISO/IEC 27001, skema OKF v0.1, dan 3 seksyen penutup (AI Prompts, URL, Syor Buku).
- **Porting Kemahiran:** Lengkapkan modul AI Agent Skill bagi CU01 yang belum selesai di `.agents/skills/` (contohnya `cu01-wa05-install-computer-applications-and-device-drivers` dan `cu01-wa06-configure-endpoint-network-connectivity`).

### 2. Migrasi Silibus Bab 3 (Pengurusan Storan, Partisi & Sistem Fail)
- Ekstrak arkib mentah `references/manual/bab_03/` (DILARANG padam mengikut Peraturan 17).
- Lakukan *Deep Web Research* untuk arahan GPT (`gdisk`/`parted`), LVM2, EXT4, XFS, dan Btrfs.
- Tulis modul ke `manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md` dan pautkan ke `openwiki/topic-02-storage-and-virtualisation.md`.
- Tukar hasil amali Bab 3 kepada kemahiran AI CU02 (`cu02-wa01` hingga `cu02-wa04`).

### 3. Jaminan Kualiti & Indeks Palace
- Jalankan `uv run scripts/generate_palace_registry.py` untuk mengemas kini indeks kemahiran AI.
- Jalankan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` (100% Quality Gate).
- Komit dan tolak ke GitLab (`origin`) dan GitHub (`github`).

---

## 💬 Prompt Salin & Tampal untuk Memulakan Sesi Google Jules

```text
Hai Jules! Sila bertindak sebagai Pakar Linux NOSS Malaysia di bawah kerangka Deep State of Mind (DSOM v0.1). 

Sila baca dan fahami fail-fail berikut dalam memori projek:
1. .agents/brain/handover_to_jules.md
2. .agents/brain/implementation_plan.md
3. .agents/brain/task.md
4. .agents/AGENTS.md (Peraturan 2, 15, 17, 18, dan 21)
5. .agents/skills/noss-content-transformation-pipeline/SKILL.md

TUGASAN ANDA SEKARANG:
1. AUDIT & PORTING BAB 1 & 2: Periksa semula kandungan Bab 1 & Bab 2 dalam `manual/cu01/` dan `openwiki/topic-01-linux-desktop-and-basics.md` agar 100% mematuhi Peraturan 21 (Deep Research, standard 2026, arahan keselamatan Jabatan Digital Negara (JDN) / MAMPU & ISO 27001, OKF v0.1, dan 3 seksyen penutup). Tukarkan mana-mana amali teknikal yang telah siap ke dalam modul AI Agent Skills di bawah `.agents/skills/` (khususnya cu01-wa05 dan cu01-wa06).
2. TRANSFORMASI BAB 3: Laksanakan migrasi amali Bab 3 (Storan, Partisi GPT, LVM2, EXT4/XFS/Btrfs) dari `references/manual/bab_03/` ke dalam `manual/cu02/` dan `openwiki/topic-02-storage-and-virtualisation.md`, serta jana kemahiran AI CU02 berkaitan.
3. KUALITI & INDEKS: Jalankan `uv run scripts/generate_palace_registry.py`, bina semula web dengan `uv run scripts/serve_mkdocs.py --build-only`, dan sahkan 100% Quality Gate dengan `uv run run_all_tests.py` sebelum membuat komit dan tolak (push) ke GitLab dan GitHub.
```
