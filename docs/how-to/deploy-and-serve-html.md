---
okf_version: 0.1
type: guide
title: "Panduan Penggunaan & Pengemaskinian Tapak Web HTML Statik"
timestamp: "2026-08-16T22:54:00Z"
topics: ["html", "mkdocs", "deploy", "docker", "podman", "nginx", "apache", "github-pages", "offline", "how-to"]
tags: ["how-to", "html", "panduan", "docker-compose", "podman", "pelayan-web", "offline-viewing", "okf"]
description: "Panduan langkah demi langkah cara menggunakan direktori html/ prabina, melancarkan pelayan pengeluaran Nginx dan Apache menggunakan Docker Compose dan Podman Pod, serta prosedur binaan semula."
resource: "file:///docs/how-to/deploy-and-serve-html.md"
---

# Panduan Penggunaan, Kontena & Pengehosan Tapak Web HTML Statik

Direktori `html/` di dalam repositori ini disediakan secara **prabina (pre-built)** dan dijejak terus di dalam Git. Ini bermakna sesiapa sahaja yang melakukan `git pull` atau `git clone` boleh terus membaca dan menggunakan laman web HTML yang lengkap serta-merta tanpa perlu memasang perisian pembina dokumentasi.

Bagi persekitaran pengeluaran (*production*), repositori ini turut menyediakan fail konfigurasi siap guna untuk **Docker Compose** dan **Podman Pod (Kube / Quadlet)** bagi kedua-dua pelayan **Nginx** dan **Apache HTTP Server**.

---

## 1. Penggunaan Terus Selepas `git pull` (Tanpa Perlu Build)

### Kaedah A: Pembacaan Luar Talian (Offline / Local File)
Anda boleh terus membuka fail utama menggunakan pelayar web (Chrome, Firefox, Edge):
- **Windows File Explorer / Linux GUI:** Dwi-klik pada fail `html/index.html`.
- **Pelayar Web:** Buka alamat `file:///laluan/ke/skills-noss/html/index.html`.
- Semua CSS, JavaScript (*Material for MkDocs*), fon, dan gambar rajah Mermaid akan dimuatkan secara luar talian dengan sokongan mod siang/malam (*light/dark mode*).

### Kaedah B: Pengehosan Pantas Menggunakan Python
Jika anda ingin melayan laman web ini kepada peranti lain dalam rangkaian setempat (LAN):
```bash
cd html
python3 -m http.server 8080
```
Buka pelayar web di `http://localhost:8080`.

---

## 2. Pengehosan Kontena: Docker Compose (Nginx & Apache)

Fail konfigurasi [`docker-compose.yml`](../../docker-compose.yml) disediakan di direktori punca dengan konfigurasi pengeluaran bagi Nginx dan Apache:

### A. Jalankan Nginx (Lalai pada port 8080)
```bash
docker compose up -d nginx
```
* **Akses Laman Web:** `http://localhost:8080`
* **Ciri-ciri Nginx:** Pemampatan Gzip aktif, penimbalan aset statik (1 tahun), pengepala keselamatan (*Security Headers*), dan pengalihan 404.

### B. Jalankan Apache HTTP Server (pada port 8081)
```bash
docker compose up -d apache
```
* **Akses Laman Web:** `http://localhost:8081`
* **Ciri-ciri Apache:** Dikonfigurasikan dengan `mod_deflate`, `mod_expires`, dan `mod_headers`.

### C. Jalankan Kedua-dua Pelayan Serentak
```bash
docker compose up -d
```

### D. Menghentikan Kontena
```bash
docker compose down
```

---

## 3. Pengehosan Kontena: Podman Pod (Rootless / Enterprise Linux)

Untuk persekitaran Linux perusahaan seperti **AlmaLinux 10**, **Fedora 43**, atau **RHEL 9**, Podman disokong melalui format spesifikasi Kubernetes YAML dan Systemd Quadlet:

### Kaedah 1: Menggunakan `podman play kube` (Pod Tunggal)
Fail definisi Pod Kubernetes terletak di [`deploy/podman/pod-noss-linux.yml`](../../deploy/podman/pod-noss-linux.yml):

```bash
# 1. Melancarkan Podman Pod (Nginx pada port 8080, Apache pada port 8081)
podman play kube deploy/podman/pod-noss-linux.yml

# 2. Semak status Pod dan kontena yang berjalan
podman pod ps
podman ps

# 3. Menghentikan dan membuang Pod
podman play kube --down deploy/podman/pod-noss-linux.yml
```

### Kaedah 2: Menggunakan Podman Systemd Quadlet (Rootless Auto-Start)
Salin fail-fail Quadlet di `deploy/podman/quadlet/` ke direktori perkhidmatan pengguna systemd:

```bash
# Salin konfigurasi Quadlet ke direktori pengguna
mkdir -p ~/.config/containers/systemd/
cp deploy/podman/quadlet/* ~/.config/containers/systemd/

# Muat semula daemon systemd pengguna
systemctl --user daemon-reload

# Mulakan perkhidmatan Pod NOSS Linux
systemctl --user start noss-linux-pod.service

# Dayakan auto-start semasa boot
systemctl --user enable noss-linux-pod.service
loginctl enable-linger $USER
```

---

## 4. Konfigurasi Pelayan Hos Asli (Bare-Metal Nginx & Apache)

Jika anda memasang Nginx atau Apache terus pada sistem operasi hos (tanpa kontena):

### Konfigurasi Nginx (`/etc/nginx/conf.d/noss-linux.conf`)
Rujuk fail lengkap di [`deploy/nginx/nginx.conf`](../../deploy/nginx/nginx.conf):
```nginx
server {
    listen 80;
    server_name noss-linux.internal;

    root /var/www/skills-noss/html;
    index index.html;

    gzip on;
    gzip_types text/plain text/css application/json application/javascript image/svg+xml;

    location / {
        try_files $uri $uri/ $uri.html =404;
    }
}
```

### Konfigurasi Apache (`/etc/httpd/conf.d/noss-linux.conf`)
Rujuk fail lengkap di [`deploy/apache/httpd.conf`](../../deploy/apache/httpd.conf):
```apache
<VirtualHost *:80>
    ServerName noss-linux.internal
    DocumentRoot "/var/www/skills-noss/html"

    <Directory "/var/www/skills-noss/html">
        Options -Indexes +FollowSymLinks
        AllowOverride None
        Require all granted
        DirectoryIndex index.html
    </Directory>
</VirtualHost>
```

---

## 5. Automasi Penyebaran Menggunakan Ansible Playbook

Fail playbook Ansible rasmi disediakan di [`deploy/ansible/`](../../deploy/ansible/) bagi mengautomasikan penyebaran ke pelbagai pelayan Linux secara serentak (**Ubuntu 26.04/24.04 LTS**, **AlmaLinux 10**, **Fedora 43**, atau **Rocky Linux 9**):

### Struktur Direktori Ansible
```text
deploy/ansible/
├── ansible.cfg                    # Konfigurasi lalai Ansible
├── inventory/
│   └── hosts.ini                  # Senarai inventori pelayan sasaran
├── site.yml                       # Titik masuk induk (Master Playbook)
└── deploy-noss-linux.yml          # Tugasan penyebaran berbilang mod
```

### Arahan Pelaksanaan Mengikut Mod (Tags):

```bash
# A. Pasang Nginx Asli (Bare-Metal) pada pelayan sasaran:
ansible-playbook -i deploy/ansible/inventory/hosts.ini deploy/ansible/deploy-noss-linux.yml --tags nginx

# B. Pasang Apache Asli (Bare-Metal) pada pelayan sasaran:
ansible-playbook -i deploy/ansible/inventory/hosts.ini deploy/ansible/deploy-noss-linux.yml --tags apache

# C. Sebarkan menggunakan Docker Compose:
ansible-playbook -i deploy/ansible/inventory/hosts.ini deploy/ansible/deploy-noss-linux.yml --tags docker

# D. Sebarkan menggunakan Podman Pod:
ansible-playbook -i deploy/ansible/inventory/hosts.ini deploy/ansible/deploy-noss-linux.yml --tags podman
```

Playbook ini menguruskan secara automatik penyalinan dokumen `html/`, pemasangan pakej sistem, konfigurasi fail pelayan web, serta pembukaan port *firewall* (`ufw` atau `firewalld`).

---

## 6. Prosedur Mengemas Kini & Membina Semula HTML (Untuk Penulis/Penyumbang)

Sekiranya anda telah menambah modul kemahiran baharu dalam `manual/`, menyunting `openwiki/`, atau mengubah dokumentasi `docs/`, bina semula folder `html/`:

### A. Membina Semula HTML Statik
```bash
uv run scripts/serve_mkdocs.py --build-only
```

### B. Menjalankan Pelayan Pembangunan Interaktif (Live Preview)
```bash
uv run scripts/serve_mkdocs.py
```
Pelayan tempatan akan dibuka secara automatik pada alamat `http://127.0.0.1:8000`.

---

## 7. Pengesahan Kualiti Sebelum Komit (Quality Gate)

Berasaskan **Peraturan 12 & 19 Perlembagaan AI DSOM**, setelah membina semula fail HTML, sentiasa jalankan suite ujian penuh dan komit perubahan:
```bash
# 1. Jalankan ujian pematuhan 100%
uv run run_all_tests.py

# 2. Rekodkan kemas kini ke dalam Git
git add -A
git commit -m "docs(deploy): add Ansible playbooks and update deployment docs"
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
