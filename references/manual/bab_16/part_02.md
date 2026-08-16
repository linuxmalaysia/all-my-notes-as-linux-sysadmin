---
okf_version: 0.1
name: Bab 16 - Bahagian 2
topics: [linux, manual, references, chapter-16]
tags: [noss, dbp]
---
# Bab 16 - Bahagian 2

/init.d/dhcpd
Fail Konfogurasi Utama:  /etc/dhcpd.conf
/etc/sysconfig/dhcpd
Fail Lease:   /var/lib/dhcp/dhcpd.leases
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 216 : Contoh fail bagi konfigurasi perkhidmatan DHCP
Rajah dibawah menerangkan nilai konfigurasi yang selalu digunakan dalam pelayan dhcp
atau lebih tepat lagi didalam konfigurasi failnya di /etc/dhcpd.conf

Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Pilihan Contoh Nilai Deskripsi
subnet 192.168.100.0
Subnet dimana pelayan DHCP wajar mengiklankan
layanannya
netmask 255.255.255.0
Mask rangkaian yang menunjukkan alamat subnet dimana
DHCP perlu berikan layanan
subnet-mask 255.255.0.0
Mask rangkaian yang diberikan kepada host dimana layanan
DHCP diterima
routers 192.168.100.1 Alamat penghala rangkaian untuk host
domain-name aljufry.org.my Alamat domain untuk host
domain-name-servers 192.168.100.2 Alamat pelayan nama untuk host
range dynamic-bootp
192.168.100.30
192.168.100.100 Kolam alamat yang boleh diberikan kepada pelanggan
default-lease-time 21600
Nilai asal dalam saat yang menentukan berapa lama maklumat
yang diberikan pelayan sah untuk pelanggan
max-lease-time 43200
Nilai maksimum dalam saat yang menentukan berapa lama
maklumat yang diberikan pelayan sah untuk pelanggan
Jadual 37 : Nilai konfigurasi yang digunakan oleh pelayan DHCP
24.2.1 Asah Bakat 1 : Konfigurasi Pelayan DHCP
Anda diminta untuk membangunkan pelayan DHCP
1. “login” sebagai root
2. Pastikan pakej telah sediapakai dengan rpm
3. Salin fail contoh yang telah disediakan dengan melarikan arahan cp
/usr/share/doc/dhcp-3.0pl1/dhcpd.conf.sample /etc/dhcpd.conf
4. Ubah fail /etc/dhcpd.conf mengikut spesifikasi dibawah dengan menggunakan
editor teks kegemaran anda. Anda boleh mengubahnya mengikut keadaan semasa.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
5. Larikan arahan touch /var/lib/dhcp/dhcpd.leases  untuk membina sebuah fail
kosong yang akan digunakan oleh dhcpd dalam menyimpan rekod lease
pelanggannya.
6. Larikan arahan /etc/rc.d/init.d/dhcpd start untuk memulakan perkhidmatan
pelayan DHCP.
24.2.2 Asah Bakat 2 : Konfigurasi Pelanggan DHCP
Anda diminta untuk membangunkan pelanggan DHCP
1. Log Masuk (Login) sebagai “root”
2. Larikan arahan ifconfig dan rekodkan alamat IP semasa anda
3. Larikan arahan netconfig dan anda akan melihat sebuah  menu
4. Pilih Yes untuk soalan “Would you like to set up networking?”
5. Pastikan anda memilih “ [*] Use dynamic IP configuration (BOOTP/DHCP)”
dengan memastikan tanda * di petak berkenaan
6. Tekan Tab sekali untuk ke butang menu OK dan tekan Enter sekali.
7. Larikan ifdown eth0 dan kemudian larikan arahan ifup eth0
8. Ulang Langkah 2.
subnet 10.0.11.0     atau subnet rangkaian anda
netmask 255.255.255.0   atau subnet rangkain anda
option routers 10.0.11.254   atau default gateway rangkaian anda
option domain-name kelas.my  atau Nama doamin rangkaian anda
option domain-name-servers 202.188.0.133 atau pelayan DNS rangkaian anda
range dynamic-bootp 10.0.11.20 10.0.11.250  Dalam kes ini kita gunakan IP
bermula dari 10.0.11.20 dan
berakhir dengan 10.0.11.250
untuk pelanggan rangkaian.
default-lease-time 21600    IP tersebut akan kekal selama 6 jam
max-lease-time 43200    Maksimum akan kekal selama 12 jam
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Pelajaran 25: Perkhidmatan Web

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
