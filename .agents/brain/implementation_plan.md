# 📐 Pelan Pelaksanaan Google Jules: Audit Bab 1 & 2, Penukaran Ilmu ke Agent Skills, dan Migrasi Bab 3

## 1. Objektif Utama Sesi Jules
1. **Audit & Penyelarasan Bab 1 & Bab 2 (`manual/cu01/` & `openwiki/topic-01`):**
   - Memeriksa semula semua nod amali Bab 1 & 2 bagi memastikan pematuhan penuh kepada Peraturan 21 (Deep Research, data 2026, arahan CLI terkini, standard **Jabatan Digital Negara (JDN) / MAMPU**, ISO/IEC 27001, OKF v0.1, dan 3 seksyen penutup).
2. **Penukaran Pengetahuan kepada AI Agent Skills (Knowledge-to-Skill Porting):**
   - Mana-mana modul ilmu amali yang telah lengkap di `manual/` MESTI dijadikan modul **AI Agent Skill** di bawah `.agents/skills/<skill-folder>/SKILL.md` (menggunakan kombinasi frontmatter OKF v0.1 + Antigravity/Jules schema) dan didaftarkan dalam Master Palace Registry (`uv run scripts/generate_palace_registry.py`).
3. **Migrasi Silibus Bab 3 (`references/manual/bab_03/` ➔ `manual/cu02/`):**
   - Melaksanakan transformasi storan, partisi GPT, LVM2, dan sistem fail EXT4/XFS/Btrfs, serta menukarkannya kepada kemahiran AI CU02.

---

## 2. Senarai Tindakan Terperinci untuk Jules

### Fasa A: Audit & Pengukuhan Bab 1 & Bab 2 (CU01)
1. **Semak Kandungan `manual/cu01/`:**
   - Pastikan tiada arahan lapuk (seperti Red Hat 9 / CentOS / MBR).
   - Pastikan panduan Penyulitan LUKS2 merujuk **Jabatan Digital Negara (JDN) / MAMPU** dan ISO/IEC 27001.
   - Pastikan setiap nod mengandungi 3 seksyen penutup (AI Prompts, URL, Syor Buku) dan Sovereign Dual-License Footer.
2. **Pindahkan / Kemas Kini AI Agent Skills (`.agents/skills/`):**
   - `cu01-wa00-memahami-ekosistem-linux/SKILL.md`
   - `cu01-wa04-install-computer-desktop-operating-systems/SKILL.md`
   - Kemas kini `cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md` dengan arahan amali Ubuntu 26.04 (APT, Snap, Flatpak) dan AlmaLinux 10 (DNF, Flatpak).
   - Kemas kini `cu01-wa06-configure-endpoint-network-connectivity/SKILL.md` dengan `nmcli` / `iproute2`.

### Fasa B: Migrasi Silibus Bab 3 (CU02) & Penjanaan Skills
1. **Analisis Arkib Mentah (`references/manual/bab_03/`):**
   - Nilai dan petakan topik kepada `CU02-WA01` hingga `CU02-WA04`.
   - Lakukan *Deep Web Research* untuk sintaks `parted`, `gdisk`, `lsblk`, `pvcreate`, `vgcreate`, `lvcreate`, `mkfs.xfs`, `mkfs.ext4`, `mkfs.btrfs`.
2. **Tulis Nod Amali di `manual/cu02/`:**
   - `manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md`
   - Kemas kini fail `manual/cu02/cu02-wa01-*.md` hingga `cu02-wa04-*.md`.
   - Pautkan ke `openwiki/topic-02-storage-and-virtualisation.md`.
3. **Cipta / Kemas Kini Kemahiran AI CU02:**
   - Kemas kini `.agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md`
   - Kemas kini `.agents/skills/cu02-wa02-install-type-2-hypervisor-platform/SKILL.md`
   - Kemas kini `.agents/skills/cu02-wa03-deploy-guest-virtual-machines-vm/SKILL.md`
   - Kemas kini `.agents/skills/cu02-wa04-prepare-virtualisation-configuration-records/SKILL.md`

### Fasa C: Verifikasi Kualiti & Indeks Palace
```bash
# 1. Jana semula indeks kemahiran AI
uv run scripts/generate_palace_registry.py

# 2. Jana indeks suapan LLM
uv run scripts/generate_llms_txt.py
uv run scripts/llms_to_xml.py

# 3. Bina laman web statik HTML
uv run scripts/serve_mkdocs.py --build-only

# 4. Sahkan 100% Quality Gate
uv run run_all_tests.py

# 5. Komit & Segerakkan dwi-remote
git add -A
git commit -m "feat(manual): audit Bab 1-2, update agent skills, and migrate Bab 3 storage"
git push origin main
git push github main
```
