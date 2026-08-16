---
okf_version: 0.1
type: guide
title: "Panduan Penggunaan & Pengemaskinian Tapak Web HTML Statik"
timestamp: "2026-08-16T22:54:00Z"
topics: ["html", "mkdocs", "deploy", "nginx", "apache", "github-pages", "offline", "how-to"]
tags: ["how-to", "html", "panduan", "pelayan-web", "offline-viewing", "okf"]
description: "Panduan langkah demi langkah cara menggunakan direktori html/ prabina secara terus selepas git pull serta prosedur mengemas kini dan membina semula laman web statik."
resource: "file:///docs/how-to/deploy-and-serve-html.md"
---

# Panduan Penggunaan & Pengemaskinian Tapak Web HTML Statik

Direktori `html/` di dalam repositori ini disediakan secara **prabina (pre-built)** dan dijejak terus di dalam Git. Ini bermakna sesiapa sahaja yang melakukan `git pull` atau `git clone` boleh terus membaca dan menggunakan laman web HTML yang lengkap serta-merta tanpa perlu memasang sebarang perisian binaan tambahan.

---

## 1. Penggunaan Terus Selepas `git pull` (Tanpa Perlu Build)

Sebaik sahaja anda memuat turun atau mengemas kini repositori ini:

### Kaedah A: Pembacaan Luar Talian (Offline / Local File)
Anda boleh terus membuka fail utama menggunakan pelayar web pilihan anda (Chrome, Firefox, Edge):
- **Windows File Explorer:** Dwi-klik pada fail `html/index.html`.
- **Pelayar Web:** Masukkan alamat `file:///D:/Users/LinuxMalaysia/Projects/skills-noss/html/index.html` (atau laluan folder tempatan anda).
- Semua skrip CSS, JavaScript (*Material for MkDocs*), fon, dan gambar rajah Mermaid akan dimuatkan secara luar talian dengan sokongan mod siang/malam (*light/dark mode*).

### Kaedah B: Pengehosan Pantas Menggunakan Python
Jika anda ingin melayan laman web ini kepada peranti lain dalam rangkaian setempat (LAN):
```bash
# Dari direktori punca projek
cd html
python -m http.server 8080
```
Buka pelayar web di `http://localhost:8080` atau `http://<IP-Komputer>:8080`.

---

## 2. Prosedur Mengemas Kini & Membina Semula HTML (Untuk Penulis/Penyumbang)

Sekiranya anda telah menambah nota kemahiran baharu dalam `palace/`, menyunting `openwiki/`, atau mengubah dokumentasi `docs/`, anda perlu membina semula direktori `html/`:

### A. Membina Semula HTML Statik (Production Build)
Jalankan skrip automasi Python UV:
```bash
uv run scripts/serve_mkdocs.py --build-only
```
* **Apa yang berlaku:** Skrip akan menyegerakkan nod memori, menghubungkan *junctions*, menjana fail HTML terkini ke dalam folder `html/`, dan menyuntik teks penafian rasmi secara automatik.

### B. Menjalankan Pelayan Pembangunan Interaktif (Live Preview)
Untuk melihat perubahan teks secara masa-nyata (*hot-reloading*) semasa menulis dokumen:
```bash
uv run scripts/serve_mkdocs.py
```
Pelayan tempatan akan dibuka secara automatik pada alamat `http://127.0.0.1:8000`.

---

## 3. Panduan Pengehosan Pelayan Pengeluaran (Production Deployment)

### Konfigurasi Nginx
Tambahkan blok pelayan (*server block*) berikut dalam konfigurasi Nginx anda:
```nginx
server {
    listen 80;
    server_name noss-linux.internal;

    root /var/www/skills-noss/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Konfigurasi Apache HTTP Server
Tetapkan `DocumentRoot` ke dalam folder `html/`:
```apache
<VirtualHost *:80>
    ServerName noss-linux.internal
    DocumentRoot "/var/www/skills-noss/html"

    <Directory "/var/www/skills-noss/html">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

---

## 4. Pengesahan Kualiti Sebelum Komit (Quality Gate)

Berasaskan **Peraturan 12 & 19 Perlembagaan AI DSOM**, setelah membina semula fail HTML, sentiasa jalankan suite ujian penuh dan komit perubahan:
```bash
# 1. Jalankan ujian pematuhan 100%
uv run run_all_tests.py

# 2. Rekodkan kemas kini ke dalam Git
git add html/ docs/ openwiki/ palace/
git commit -m "docs(html): rebuild static site distribution files"
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
