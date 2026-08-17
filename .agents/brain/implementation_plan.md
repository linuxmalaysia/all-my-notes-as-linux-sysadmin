# 📐 Pelan Pelaksanaan Google Jules: Migrasi Silibus Bab 4 (Pentadbiran Pengguna, Kebenaran Fail, POSIX ACL & Keselamatan Endpoint ke manual/cu05/ dan manual/cu01/)

## 1. Objektif Utama Sesi Jules
Memindahkan, memodenkan, menyelidik secara mendalam (*Deep Web Research*), dan memetakan kandungan arkib manual lama **Bab 4 (`references/manual/bab_04/`)** ke dalam direktori **`manual/cu05/`** (Kawalan Keselamatan Endpoint & Audit Pengguna), **`manual/cu01/`**, serta mengemas kini **`openwiki/topic-05-linux-security.md`** berlandaskan piawaian **NOSS Level 3 (CU05 & CU01)**, edaran Linux kanonik 2026 (Ubuntu 26.04 LTS & AlmaLinux 10), 4 kuadran Diátaxis, dan standard keselamatan **Jabatan Digital Negara (JDN) / MAMPU** serta **ISO/IEC 27001**.

---

## 2. Garis Panduan Transformasi & Pematuhan Perlembagaan AI

### A. Kitaran Mandatori Peraturan 21 (Deep Research & CU/WA Mapping)
1. **Penilaian Silibus:**
   - `CU05-WA01`: Audit akaun pengguna, kumpulan, fail `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, dan kebenaran fail / POSIX ACL.
   - `CU05-WA05`: Pengurusan kawalan keselamatan fizikal, terminal console, timeout sesi shell (`TMOUT`), dan penutupan sistem selamat.
   - `CU01`: Navigasi FHS, alatan pencarian fail moden (`plocate`, `find`), dan halaman panduan manual (`man-db`, `mandb`).
2. **Penyelidikan Mendalam (*Deep Web Research*):**
   - Sintaks moden pengurusan pengguna: `useradd -m -s /bin/bash`, `usermod -aG sudo,wheel`, `visudo`, `faillock` / `pam_faillock`.
   - Pengurusan kebenaran lanjutan: `chmod`, `chown`, SUID/SGID/Sticky bit, `umask 027`, POSIX Access Control Lists (`getfacl`, `setfacl -m u:pengguna:rwx`).
   - Kawalan had akses: `/etc/security/limits.conf`, `/etc/login.defs` (dasar panjang kata laluan & tamat tempoh mengikut JDN/MAMPU).
3. **Pengayaan Keselamatan & Penalaan Prestasi:**
   - Menghapuskan amalan lapuk (seperti log masuk terus akaun `root`).
   - Wajibkan konfigurasi `sudo` dengan audit log, perlindungan brute-force `faillock`, dan prinsip keistimewaan paling minimum (*Principle of Least Privilege*).
4. **Penyusunan Output Terstruktur:**
   - Hasilkan nod amali di `manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md` atau kemas kini nod WA berkaitan di `manual/cu05/`.
   - Pautkan ke `openwiki/topic-05-linux-security.md`.

### B. Mandat Porting Pengetahuan ke Kemahiran AI (Knowledge-to-Skill Porting)
- Naik taraf atau cipta modul AI Agent Skill di bawah `.agents/skills/`:
  - `.agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md` (format `type: skill`).
  - `.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md` (format `type: skill`).
- Daftarkan ke Master Palace Registry (`uv run scripts/generate_palace_registry.py`).

### C. Suite Ujian Pematuhan Kualiti (Quality Gate & Test Suite)
- Tambah suite ujian unit Python: `tests/test_manual_cu05_user_security_content.py` bagi mengesahkan nod manual, kemahiran AI, frontmatter OKF, dan pautan openwiki.
- Sahkan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` melepasi 100% Quality Gate.

---

## 3. Langkah Operasi Langkah Demi Langkah untuk Jules

```bash
# 1. Baca arkib mentah Bab 4 (DILARANG padam mengikut Peraturan 17)
# references/manual/bab_04/part_01.md

# 2. Tulis nod amali moden ke manual/cu05/
# manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md
# Kemas kini manual/cu05/cu05-wa01-*.md & cu05-wa05-*.md

# 3. Porting ke Kemahiran AI
# .agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md
# .agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md

# 4. Kemas kini Silibus OpenWiki
# openwiki/topic-05-linux-security.md

# 5. Cipta Ujian Unit
# tests/test_manual_cu05_user_security_content.py

# 6. Jana semula indeks & bina web
uv run scripts/generate_palace_registry.py
uv run scripts/generate_llms_txt.py
uv run scripts/llms_to_xml.py
uv run scripts/serve_mkdocs.py --build-only

# 7. Sahkan 100% Quality Gate
uv run run_all_tests.py

# 8. Komit dan tolak ke GitHub & GitLab
git add -A
git commit -m "feat(manual): migrate Bab 4 user administration and security to manual/cu05"
git push origin main
git push github main
```
