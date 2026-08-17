# 🤝 Taklimat Penyerahan Memori Ejen: Google Antigravity ➔ Google Jules

**Tarikh / Masa:** 2026-08-17  
**Status Sesi Terkini:** PR #4 (Bab 1-2 Audit, Porting Kemahiran CU01/CU02, dan Migrasi Bab 3 Storan) telah **SELESAI & DIGABUNGKAN (MERGED)** dengan 100% Quality Gate (902 pytest tests, 38 jest tests).

---

## 📌 Ringkasan Status & Perubahan Terkini
1. **Fasa 1, 2, dan 3 Selesai Sepenuhnya:**
   - Direktori `manual/cu01/` dan `manual/cu02/` lengkap dengan amali moden (Ubuntu 26.04 LTS & AlmaLinux 10, LUKS2 FDE, LVM2, GPT).
   - Kemahiran AI `cu01-wa00`, `cu01-wa04`, `cu01-wa05`, `cu01-wa06`, dan `cu02-wa01` aktif di `.agents/skills/`.
2. **Ketetapan Perlembagaan AI yang Perlu Dipatuhi:**
   - **Peraturan 14:** Non-Interactive CI Execution (`npm test` / `jest --ci`).
   - **Peraturan 15:** Piawaian Ubuntu 26.04 LTS, AlmaLinux 10, Fedora 43, Penyulitan LUKS2 mengikut Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU & ISO/IEC 27001.
   - **Peraturan 17:** DILARANG memadam arkib `references/manual/bab_04/`.
   - **Peraturan 18:** Pematuhan 4 Kuadran Diátaxis & multi-artifact output.
   - **Peraturan 21:** Kitaran 3 Peringkat (Penilaian CU/WA, Deep Web Research 2026, Pengayaan Keselamatan JDN/MAMPU & Prestasi, dan Output Terstruktur).
   - **Knowledge-to-Skill Porting Mandate:** Wajib menukarkan amali teknikal `manual/` ke dalam `.agents/skills/<skill-folder>/SKILL.md` (format `type: skill`).

---

## 🎯 Tugasan Utama untuk Google Jules: Fasa 4 (Migrasi Silibus Bab 4)

### 1. Ekstrak & Transformasi Bab 4 (`references/manual/bab_04/`) ke `manual/cu05/` & `manual/cu01/`:
- **Pentadbiran Pengguna & Kumpulan:** `useradd`, `usermod`, `userdel`, `groupadd`, `/etc/passwd`, `/etc/shadow`, `/etc/sudoers` (`visudo`), dasar kata laluan dan penguncian akaun `faillock`.
- **Kebenaran Fail & POSIX ACL:** `chmod`, `chown`, `chgrp`, bit SUID/SGID/Sticky, `umask 027`, POSIX Access Control Lists (`getfacl`, `setfacl`).
- **Navigasi FHS & Pencarian Fail:** Struktur direktori FHS moden, `plocate`, `find`, dan dokumentasi `man-db`.
- **Kawalan Keselamatan Endpoint & Sesi:** Konfigurasi had keselamatan `/etc/security/limits.conf`, `TMOUT`, kawalan konsol maya, dan penutupan selamat `systemctl poweroff`/`shutdown`.

### 2. Porting Kemahiran AI CU05 (`.agents/skills/`):
- Naik taraf `.agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md` ke format `type: skill` lengkap dengan contoh CLI sebenar dan seksyen Security & Governance.
- Naik taraf `.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md` ke format `type: skill`.

### 3. Kemas Kini Silibus OpenWiki:
- Kemas kini `openwiki/topic-05-linux-security.md` dengan menghubungkan nod amali baharu di `manual/cu05/` dan kemahiran AI CU05.

### 4. Ujian Unit & Jaminan Kualiti (100% Quality Gate):
- Tambah suite ujian unit: `tests/test_manual_cu05_user_security_content.py`.
- Jalankan `uv run scripts/generate_palace_registry.py`, `uv run scripts/serve_mkdocs.py --build-only`, dan `uv run run_all_tests.py` sehingga 100% lulus.
- Komit dan tolak ke GitHub dan GitLab.

---

## 💬 Prompt Salin & Tampal untuk Memulakan Sesi Google Jules

```text
Hai Jules! Sila bertindak sebagai Pakar Linux NOSS Malaysia dan Harisfazillah Jamel (LinuxMalaysia), di bawah kerangka Deep State of Mind (DSOM v0.1). 

Sila baca dan teliti fail-fail berikut dalam memori projek sebelum memulakan tugasan:
1. .agents/brain/handover_to_jules.md
2. .agents/brain/implementation_plan.md
3. .agents/brain/task.md
4. .agents/AGENTS.md (khususnya Peraturan 2, 14, 15, 17, 18, 21, dan Knowledge-to-Skill Porting Mandate)
5. .agents/skills/noss-content-transformation-pipeline/SKILL.md

TUGASAN UTAMA ANDA SEKARANG (FASA 4: TRANSFORMASI SILIBUS BAB 4):
1. TRANSFORMASI AMALI BAB 4: Laksanakan migrasi amali Bab 4 (Pentadbiran Pengguna & Kumpulan, /etc/shadow, visudo, Kebenaran Fail chmod/chown, SUID/SGID/Sticky bit, POSIX ACL getfacl/setfacl, Dasar Kata Laluan & faillock, Navigasi FHS, dan Penutupan Sistem Selamat) daripada arkib `references/manual/bab_04/` ke dalam `manual/cu05/` (dan `manual/cu01/` jika berkaitan) serta kemas kini `openwiki/topic-05-linux-security.md`.
2. PORTING KEMAHIRAN AI: Naik taraf kemahiran AI `.agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md` dan `.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md` ke format `type: skill` penuh mengikut standard 2026.
3. KUALITI, UJIAN & INDEKS: Tambahkan suite ujian `tests/test_manual_cu05_user_security_content.py`, jalankan `uv run scripts/generate_palace_registry.py`, bina semula web dengan `uv run scripts/serve_mkdocs.py --build-only`, dan sahkan 100% Quality Gate dengan `uv run run_all_tests.py` sebelum membuat PR/komit dan tolak ke GitHub dan GitLab.
```
