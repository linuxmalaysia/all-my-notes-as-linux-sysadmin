# 🚶 Ringkasan Pencapaian Projek (Session Walkthrough)

## 📌 Status Terkini
- **Ejen Pengendali:** Antigravity ➔ Handover ke Google Jules (GitHub).
- **Tarikh:** 2026-08-16
- **Status Ujian:** 644/644 lulus (100% Pematuhan Quality Gate).
- **Status Remote Git:**
  - `origin` (GitLab): `https://gitlab.com/linuxmalaysia/skills-noss-malaysia-for-linux.git`
  - `github` (GitHub): `https://github.com/linuxmalaysia/all-my-notes-as-linux-sysadmin.git`

---

## 🛠️ Ringkasan Artifak & Kejayaan Utama:

1. **Seni Bina Diátaxis & Format Dwicapaian (Rule 18):**
   - Laman web dokumentasi disusun mengikut 4 kuadran Diátaxis di `docs/tutorials/`, `docs/how-to/`, `docs/explanation/`, `docs/reference/`.
   - Mod pautan berkait `use_directory_urls: false` diaktifkan untuk menyokong pembacaan luar talian (`file:///`) serta pengehosan statik multi-platform (GitHub/GitLab Pages, Read the Docs, GitBook, Nginx, Apache).

2. **Khazanah Sejarah Sumber Terbuka Malaysia:**
   - `docs/explanation/sejarah-dokumen-asal-linux-kpm.md` (Modul ISL9 KPM 2004).
   - `docs/explanation/sejarah-oscc-mampu-malaysia.md` (OSCC MAMPU 2004–2020 & 3 Fasa Pelan Induk OSS Sektor Awam).
   - `docs/explanation/sejarah-mosc-malaysia.md` (Malaysia Open Source Conference / MOSCMY 2009–2019).

3. **Pengedaran HTML Prabina (`html/` di dalam Git):**
   - Direktori `html/` dijejak penuh di dalam Git supaya pengguna yang `git pull` mendapat tapak web statik siap guna serta-merta tanpa perlu kompilasi.

4. **Matriks Penyebaran Pelayan Pengeluaran (Rule 20):**
   - Konfigurasi pengeluaran Nginx (`deploy/nginx/nginx.conf`) & Apache (`deploy/apache/httpd.conf`).
   - `docker-compose.yml` (Nginx port 8080 & Apache port 8081).
   - Podman Pod (`deploy/podman/pod-noss-linux.yml`) & Systemd Quadlet.
   - Ansible Playbook (`deploy/ansible/deploy-noss-linux.yml` & `site.yml`) menyokong keluarga Debian & RedHat secara *idempotent*.

5. **Invarian Atribusi Hak Cipta Sahih (Rule 7):**
   - **Deep State of Mind (DSOM):** Harisfazillah Jamel (LinuxMalaysia).
   - **MemPalace Framework:** Milla Jovovich & Ben Sigman (Spatial Memory / Method of Loci concept).
