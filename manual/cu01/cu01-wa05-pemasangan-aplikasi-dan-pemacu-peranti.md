---
okf_version: 0.1
type: knowledge-node
title: "CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu01", "wa05", "pengurusan-pakej", "pemacu-peranti", "editor", "bashrc", "synaptic", "gnome-software", "tarball"]
tags: ["cu01", "wa05", "apt", "dnf", "flatpak", "snap", "nvidia", "driver", "editor", "bashrc", "synaptic", "gnome-software", "tarball"]
description: "Panduan amali NOSS CU01-WA05 bagi pengurusan pakej perisian CLI (APT, DNF5, RPM, Tarball compilation) dan GUI (GNOME Software, Synaptic, PackageKit), penyesuaian pemboleh ubah persekitaran $EDITOR/$VISUAL, dan pemasangan pemacu peranti GPU/pemacu proprietari di Linux."
resource: "file:///manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"
---

# CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux

## 🎯 Objektif Pembelajaran

Menguasai prosedur amali pengurusan aplikasi, pakej perisian CLI & GUI, penyesuaian persekitaran shell, serta pemasangan dan konfigurasi pemacu peranti (*device drivers*) pada sistem operasi Linux desktop mengikut piawaian **NOSS Tahap 3 (CU01-WA05)**.

Setelah menyempurnakan modul ini, pelajar akan dapat:

1. Menguruskan repositori dan pakej perisian menggunakan pengurus pakej asli (**APT** pada Ubuntu 26.04 LTS, **DNF5** pada AlmaLinux 10 dan Fedora 43).
2. Memasang dan menguruskan perisian melalui antara muka grafik GUI (**GNOME Software**, **Synaptic Package Manager**, **PackageKit**).
3. Memasang dan menguruskan aplikasi berasaskan kontena universal (**Flatpak** dan **Snap**).
4. Melaksanakan pengompilan manual perisian daripada arkib kod sumber Tarball (`.tar.gz` / `.tar.zst` via `./configure`, `make`, `sudo make install`).
5. Menguruskan pemboleh ubah persekitaran shell pengguna dan sistem (`$EDITOR`, `$VISUAL`, `/etc/environment`, `~/.bashrc`).
6. Mengesan, memasang, dan mengesahkan pemacu peranti proprietari dan terbuka (GPU NVIDIA, AMD Radeon, serta kad peranti rangkaian tanpa wayar).
7. Mematuhi garis panduan keselamatan Jabatan Digital Negara (JDN) / MAMPU dan ISO/IEC 27001 mengenai integriti perisian dan tandatangan digital (*GPG key verification*).

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Pengurusan Pakej Asli & Antara Muka GUI (APT, DNF5, Synaptic, GNOME Software)

#### A. Debian/Ubuntu (APT - Advanced Package Tool)

Pada **Ubuntu 26.04 LTS "Resolute Raccoon"**, pengurusan pakej CLI dilakukan menggunakan arahan `apt`:

```bash
# 1. Kemas kini indeks repositori dan senaraikan pakej yang boleh dinaik taraf
sudo apt update

# 2. Naik taraf kesemua pakej sistem ke versi terkini secara selamat
sudo apt upgrade -y

# 3. Cari dan pasang aplikasi (contoh: cURL, Git, VLC, Vim, Nano)
sudo apt search vlc
sudo apt install -y curl git vlc vim nano

# 4. Buang pakej yang tidak diperlukan beserta fail konfigurasi sisa
sudo apt purge -y vlc
sudo apt autoremove -y
```

#### B. Pengurusan Pakej Grafik GUI (GNOME Software & Synaptic Package Manager)

Bagi pengguna desktop pejabat dan TVET, pengurusan pakej grafik menyediakan kaedah carian dan pemasangan perisian secara visual:

1. **GNOME Software (`gnome-software`)**:
   - Pusat perisian bersepadu yang menyokong pakej APT/RPM, Flatpak, dan Snap.
   - Pelancaran CLI: `gnome-software &`
2. **Synaptic Package Manager (`synaptic`)**:
   - Pengurus pakej GUI aras tinggi berasaskan APT. Synaptic membolehkan penapisan pakej mengikut status, kategori, atau repositori, pengurusan punca pangkalan data (`/etc/apt/sources.list`), serta semakan kebergantungan pakej secara visual.
   - Pemasangan Synaptic melalui APT:
     ```bash
     sudo apt update && sudo apt install -y synaptic
     ```
   - Pelancaran Synaptic: Menu Utama ➔ System Settings ➔ Synaptic Package Manager, atau melalui terminal:
     ```bash
     sudo synaptic &
     ```

#### C. Red Hat/AlmaLinux/Fedora (DNF5 / DNF & PackageKit)

Pada **AlmaLinux 10 "Purple Lion"** dan **Fedora 43**, pengurus pakej generasi baharu **DNF5** digunakan bersama alatan GUI berasaskan **PackageKit** / GNOME Software:

```bash
# 1. Semak kemas kini pakej dan naik taraf sistem
sudo dnf check-upgrade || true
sudo dnf upgrade -y

# 2. Pasang aplikasi dan kumpulan perisian (Package Groups)
sudo dnf install -y htop wget vim nano
sudo dnf groupinstall -y "Development Tools"

# 3. Pengurusan repositori EPEL pada AlmaLinux 10
sudo dnf install -y epel-release
sudo dnf config-manager --enable epel
```

#### D. Pengurusan Pakej RPM & Kompilasi Kod Sumber Tarball (`.tar.gz` / `.tar.zst`)

Selain pengurus pakej peringkat tinggi (`dnf5`/`apt`), pentadbir sistem perlu menguasai utiliti asas `rpm` dan kaedah pengompilan perisian daripada kod sumber:

1. **Pengesahan Tandatangan Pakej & Operasi Asas Arahan `rpm`:**
   - Dapatkan kunci awam GPG vendor daripada saluran rasmi, bandingkan cap jarinya (*fingerprint*), dan import menggunakan `sudo rpm --import <gpg-key-file>`.
   - Sahkan tandatangan digital GPG pada pakej RPM luar menggunakan `rpmkeys --checksig` atau `rpm -K`. Pemasangan **MESTI DIHENTIKAN** sekiranya hasil semakan mengandungi status `NOKEY` atau pengesahan gagal.
   - Disyorkan memasang pakej RPM melalui pengurus pakej (`sudo dnf install ./nmap-7.95-1.x86_64.rpm`) kerana `dnf` menyelesaikan kebergantungan secara automatik. Arahan `rpm -Uvh` mengekalkan kaedah operasi aras rendah (*low-level*).
   - Sintaks asas: `rpm [operasi] [opsyen] [pakej-fail / nama-pakej]`
   - `-i` (Install): Memasang pakej RPM baharu.
   - `-U` (Upgrade): Memasang pakej baharu atau menaik taraf pakej sedia ada (pilihan paling disyorkan).
   - `-F` (Freshen): Menaik taraf pakej HANYA jika versi terdahulu telah sedia terpasang.
   - `-q` (Query): Menyoal status pakej (`rpm -qa` untuk semua pakej, `rpm -qi <pakej>` untuk maklumat, `rpm -ql <pakej>` memaparkan senarai fail).
   - `-V` (Verify): Mengesan perbezaan fail terpasang berbanding pangkalan data RPM tempatan (nota: ini menyemak integriti metadata tempatan, bukan menjamin sistem bebas pencerobohan luar).
   - `-e` (Erase): Membuang/nyahpasang pakej daripada sistem.
   - `--rebuilddb`: Membina semula pangkalan data RPM sekiranya berlaku kerosakan pangkalan data indeks.

   ```bash
   # 1. Import kunci awam GPG rasmi vendor mengikut edaran (contoh: AlmaLinux/Fedora) dan sahkan tandatangan digital pakej RPM
   sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-AlmaLinux
   rpmkeys --checksig nmap-7.95-1.x86_64.rpm || { echo "Pengesahan GPG gagal atau NOKEY!"; exit 1; }

   # 2. KAEDAH A (Disyorkan): Pemasangan melalui DNF (DNF menyelesaikan kebergantungan automatik)
   sudo dnf install -y ./nmap-7.95-1.x86_64.rpm

   # ATAU KAEDAH B (Alternatif Aras Rendah): Pemasangan terus menggunakan arahan RPM (PILIH SATU KAEDAH SAHAJA)
   # sudo rpm -Uvh nmap-7.95-1.x86_64.rpm

   # 3. Semak maklumat dan fail yang dimiliki oleh sesuatu pakej
   rpm -qi nmap
   rpm -ql nmap

   # 4. Cari pakej RPM yang memiliki fail spesifik di dalam sistem
   rpm -qf /usr/bin/nmap

   # 5. Pengesahan integriti fail terpasang berbanding pangkalan data RPM tempatan
   rpm -V nmap
   rpm -Va
   ```

2. **Pengompilan Kod Sumber daripada Pakej Sumber RPM (`.src.rpm`):**
   - Fail `.src.rpm` mengandungi kod sumber asal dan fail spesifikasi `.spec` untuk membina pakej binari RPM.
   - Langkah prasyarat memasang perkakasan pembangunan: `rpm-build`, `rpmdevtools`, `gcc`, `gcc-c++`, `make`, serta pemalam `dnf-plugins-core` (AlmaLinux/RHEL) atau `dnf5-plugins` (Fedora 43).
   - Gunakan `dnf builddep` (pada AlmaLinux 10 / RHEL) atau `dnf5 builddep` (pada Fedora 43) untuk menyelesaikan kebergantungan binaan `BuildRequires`:

   ```bash
   # 1. Pasang alatan pembangunan binaan RPM (termasuk pemalam dnf/dnf5)
   # Pada AlmaLinux 10 / RHEL:
   sudo dnf install -y rpm-build rpmdevtools gcc gcc-c++ make dnf-plugins-core
   # Pada Fedora 43 (DNF5):
   # sudo dnf5 install -y rpm-build rpmdevtools gcc gcc-c++ make dnf5-plugins

   # 2. Sahkan tandatangan pada fail SRPM (.src.rpm)
   rpmkeys --checksig openssh-9.8p1-1.src.rpm || exit 1

   # 3. Selesaikan kebergantungan binaan (BuildRequires mengikut edaran)
   # Pada AlmaLinux 10 / RHEL 10:
   sudo dnf builddep -y openssh-9.8p1-1.src.rpm
   # Pada Fedora 43 (DNF5):
   # sudo dnf5 builddep -y openssh-9.8p1-1.src.rpm

   # 4. Mengompil pakej sumber RPM kepada pakej binari RPM
   rpmbuild --rebuild openssh-9.8p1-1.src.rpm
   ```

3. **Pengompilan Manual daripada Arkib Kod Sumber Tarball (`.tar.gz` / `.tar.zst`):**
   - Pengompilan manual hanya dilakukan sekiranya tiada pakej binari atau apabila pengubahsuaian kod sumber diperlukan.
   - **Penting:** Sentiasa semak fail `README` atau `INSTALL` di dalam arkib untuk menentukan sistem binaan yang digunakan (seperti Autotools `./configure`, CMake `cmake`, atau Meson `meson`). Arahan `./configure` hanya terhad untuk projek berasaskan Autotools.
   - **Langkah Keselamatan:** Dapatkan fail checksum (`sha256sum`) dan kunci GPG rasmi vendor. Sahkan tandatangan manifesto menggunakan kunci rasmi (contoh: `gpgv` atau `gpg --verify`) sebelum menjalankan `sha256sum -c`.
   - **Amaran:** Penggunaan `sudo make install` tidak dijejak oleh pangkalan data pakej sistem (`dpkg`/`rpm`). Adalah disyorkan untuk menguruskan inventori di `/usr/local` atau membina pakej binari rasmi.

   ```bash
   # 1. Sahkan kunci GPG rasmi vendor & integriti checksum sha256sum daripada saluran rasmi
   gpg --keyring /etc/apt/trusted.gpg.d/vendor.gpg --verify sampel-aplikasi-1.0.tar.gz.sha256.asc sampel-aplikasi-1.0.tar.gz.sha256
   sha256sum -c sampel-aplikasi-1.0.tar.gz.sha256 || exit 1

   # 2. Ekstrak arkib kod sumber tarball
   tar -zxvf sampel-aplikasi-1.0.tar.gz
   cd sampel-aplikasi-1.0

   # 3. Semak dokumen README/INSTALL untuk mengenal pasti sistem binaan
   cat README || cat INSTALL

   # 4. Bagi projek Autotools, sediakan persekitaran dan kompilkan
   ./configure --prefix=/usr/local
   make -j$(nproc)

   # 5. Pasang binari secara terurus ke /usr/local
   sudo make install
   ```

---

### 2. Pemasangan Pakej Universal (Flatpak & Snap)

Untuk aplikasi desktop moden yang terpencil (*sandboxed*) demi keselamatan persekitaran pejabat:

#### A. Flatpak (Flathub Repository)

```bash
# 1. Pastikan perkhidmatan Flatpak terpasang dan tambah repositori Flathub
sudo apt install -y flatpak   # Ubuntu
# sudo dnf install -y flatpak # AlmaLinux / Fedora

sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 2. Pasang dan jalankan aplikasi (contoh: LibreOffice / GIMP)
flatpak install flathub org.gimp.GIMP -y
flatpak run org.gimp.GIMP
```

#### B. Snap (Ubuntu Canonical Ecosystem)

```bash
# 1. Semak status dan pasang aplikasi Snap
snap list
sudo snap install code --classic  # VS Code
sudo snap install chromium
```

---

### 3. Konfigurasi Pemboleh Ubah Persekitaran `$EDITOR` & `$VISUAL`

Pemboleh ubah persekitaran menentukan aplikasi lalai yang digunakan oleh utiliti sistem (seperti `git`, `crontab`, `visudo`) apabila membuka editor teks.

#### A. Konfigurasi Persekitaran Pengguna Individu (`~/.bashrc`)

Gunakan penyunting teks untuk menambah eksport pemboleh ubah dalam fail profil pengguna:

```bash
# Tetapkan Vim atau Nano sebagai editor CLI lalai pengguna
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim

# Muat semula fail .bashrc untuk menguji perubahan
source ~/.bashrc

# Sahkan nilai pemboleh ubah persekitaran
echo $EDITOR
echo $VISUAL
```

#### B. Konfigurasi Persekitaran Sistem Global (`/etc/environment` & `/etc/profile.d/editor.sh`)

Untuk menetapkan penyunting lalai bagi kesemua pengguna pelayan/desktop sektor awam:

1. Gunakan `sudoedit` untuk membuka fail `/etc/environment` secara selamat:
```bash
sudoedit /etc/environment
```

2. Masukkan baris pemboleh ubah persekitaran berikut di dalam fail `/etc/environment` (format penetapan pasangan nama=nilai):
```ini
EDITOR="/usr/bin/vim"
VISUAL="/usr/bin/vim"
```

3. Sebagai alternatif bagi persekitaran shell interaktif, cipta skrip profil global di `/etc/profile.d/editor.sh`:
```bash
sudo tee /etc/profile.d/editor.sh << 'EOF'
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
EOF

sudo chmod +x /etc/profile.d/editor.sh
```

> [!NOTE]
> Secara lalai, arahan `sudo` menjalankan pembersihan persekitaran (`env_reset`). Pemboleh ubah `$EDITOR` atau `$VISUAL` pengguna hanya diwariskan semasa `sudo` jika konfigurasi `/etc/sudoers` membenarkannya (contohnya melalui arahan `Defaults env_keep += "EDITOR VISUAL"`).

---

### 4. Pengesanan & Pemasangan Pemacu Peranti (GPU & Rangkaian Tanpa Wayar)

#### A. Pengesanan Perkakasan Peranti

```bash
# Senaraikan peranti PCI (GPU, Rangkaian, Pengawal Storan)
lspci -nnk | grep -A3 -i vga
lspci -nnk | grep -A3 -i network

# Senaraikan peranti USB
lsusb

# Semak modul isirung (kernel modules) yang diloadkan
lsmod | grep -iE 'nvidia|amdgpu|iwlwifi'
```

#### B. Pemasangan Pemacu NVIDIA GPU pada Ubuntu 26.04 LTS

```bash
# 1. Kesan pemacu yang disyorkan oleh peranti
ubuntu-drivers devices

# 2. Pasang pemacu NVIDIA terkini secara automatik
sudo ubuntu-drivers install

# 3. Sahkan pemacu NVIDIA berfungsi selepas but semula
nvidia-smi
```

#### C. Pemasangan Pemacu NVIDIA pada Fedora 43 & AlmaLinux 10 (RPM Fusion)

```bash
# Untuk Fedora 43:
sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Untuk AlmaLinux 10:
# sudo dnf install -y https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-10.noarch.rpm
# sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-10.noarch.rpm

# Pasang pemacu akmod-nvidia:
sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
```

#### D. Pengesanan & Konfigurasi Pemacu AMD Radeon & Kad Rangkaian Tanpa Wayar

```bash
# Pemacu AMD Radeon (Sumber Terbuka disertakan secara asal dalam Isirung Linux):
sudo apt install -y mesa-vulkan-drivers mesa-utils   # Ubuntu
# sudo dnf install -y mesa-dri-drivers mesa-vulkan-drivers # AlmaLinux / Fedora
glxinfo | grep "OpenGL vendor"

# Pemacu Kad Rangkaian Tanpa Wayar (Wi-Fi Firmwares):
sudo apt install -y linux-firmware                   # Ubuntu
# sudo dnf install -y linux-firmware                 # AlmaLinux / Fedora
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001

1. **Verifikasi Kunci GPG APT:** Bagi repositori pihak ketiga pada sistem Debian/Ubuntu, gunakan fail kunci tersimpan di `/etc/apt/keyrings/` dengan opsyen `[signed-by=/etc/apt/keyrings/...]` dalam fail `.list` repositori.
2. **Pengesahan Kunci DNF:** Tetapkan `gpgcheck=1` pada semua repositori DNF untuk mengelakkan suntikan pakej yang tidak disahkan.
3. **Pakej Berdaftar Sahaja:** HANYA pasang perisian daripada repositori rasmi atau Flathub berverifikasi di komputer pejabat sektor awam.
4. **Audit Pemasangan:** Simpan log pemasangan di `/var/log/dpkg.log` atau `/var/log/dnf.log` sebagai sebahagian daripada audit keselamatan ISO 27001.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya mengemaskini repositori dan menaik taraf pakej sistem menggunakan APT dan DNF.
- [ ] Berjaya memasang dan mengendalikan pakej perisian menggunakan antara muka grafik (GNOME Software & Synaptic).
- [ ] Berjaya mengompil perisian daripada arkib kod sumber Tarball (`.tar.gz` - `./configure`, `make`, `make install`).
- [ ] Berjaya memasang aplikasi desktop menerusi Flatpak/Snap.
- [ ] Berjaya menetapkan pemboleh ubah persekitaran `$EDITOR` dan `$VISUAL` dalam `~/.bashrc` dan `/etc/environment`.
- [ ] Berjaya mengenal pasti cip grafik dan kad Wi-Fi menggunakan `lspci` serta memasang pemacu peranti berkaitan.
- [ ] Mengesahkan modul pemacu dimuatkan ke dalam isirung Linux (`lsmod` / `nvidia-smi` / `glxinfo`).

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bandingkan kelebihan dan kekurangan seni bina pembungkusan pakej APT/RPM berbanding ketersendirian kontena Flatpak dan Snap dari sudut keselamatan sektor awam."*
2. *"Apakah perbezaan antara pemboleh ubah persekitaran $EDITOR dan $VISUAL mengikut standard POSIX dan utiliti Linux?"*
3. *"Tuliskan skrip Bash untuk menyemak sama ada pemacu peranti NVIDIA atau AMD telah dimuatkan dengan betul dalam Kernel Linux 6.14."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Pengurusan Pakej Ubuntu](https://ubuntu.com/server/docs/package-management)
- [Dokumentasi Synaptic Package Manager Guide](https://help.ubuntu.com/community/SynapticHowto)
- [Dokumentasi Rasmi DNF5 Fedora / AlmaLinux](https://dnf5.readthedocs.io/)
- [Panduan Pengurusan Flathub](https://flathub.org/)
- [Garis Panduan Keselamatan Perisian MAMPU / JDN](https://www.jdn.gov.my/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Linux Administration Handbook (Edisi Terkini)** oleh Evi Nemeth et al.
- **The Linux Command Line, 2nd Edition** oleh William Shotts.
- **Nota Pentadbiran Sistem Linux Malaysia** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
