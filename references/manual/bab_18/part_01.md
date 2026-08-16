---
okf_version: 0.1
name: Bab 18 - Bahagian 1
topics: [linux, manual, references, chapter-18]
tags: [noss, dbp]
---
# Bab 18 - Bahagian 1

Gambar Rajah 223 : Pemetaan terus domain upm.edu.my. secara grafik
26.3 Asas BIND
Pembinaan BIND selaku pelayan nama sebenarnya amat mudah dan ringkas, namun
kesilapan sangat mudah dilakukan hingga menyebabkan segalanya tidak berfungsi.
Bahkan telah terbukti bahawa antara perkhidmatan yang paling banyak kesilapan ialah
DNS. Hal ini dapat dielakkan sekiranya, anda berhati-hati dan melakukan percubaan
acah-tanya untuk melihat respons dari pelayan anda terlebih dahulu sebelum
meletakkannya di produksi.

Terdapat dua jenis pemetaan yang dibenarkan di BIND, yang pertama ialah Pemetaan
Terus (Forward Mapping) dan yang kedua Pemetaan Songsang (Reverse Mapping).
Asasnya pemetaan terus merujuk kepada pemetaan nama kepada alamat IP manakala
pemetaan songsang merujuk kepada keadaan yang sebaliknya.
Kedua-dua jenis pemetaan ini diwakili oleh dua fail yang berlainan di lipatan /var/named.
Contohnya untuk domain upm.edu.my, deklarasi domain perlu dilakukan di
/etc/named.conf dan semua rekod zon akan disimpan di /var/named/upm.forward untuk
pemetaan terus dan /var/named/upm.reverse untuk pemetaan songsang.
BIND mempunyai beberapa komponen, iaitu :
i) Penukar Nama (NAME RESOLVER)
Penukar nama merupakan program yang mengekstrak informasi dari pelayan
DNS berdasarkan respons yang diberikan oleh permintaan pelanggan. Penukar
akan menggunakan informasi dari pelayan nama yang terpilih atau bertanya
terus kepada pelayan nama lain. Penukar biasanya adalah sebahagian daripada
rutin sistem, oleh itu tiada protokol khas diperlukan di antara penukar dan
program pengguna.
Red Hat 9 (Shrike)
Pakej RPM:   bind
Skrip Pelayan:   /etc/rc.d/init.d/named
Fail Konfogurasi Utama:  /etc/named.conf
Fail Zon:   /var/named
Fail Log:   /var/log/named

ii) Pelayan Nama (NAME SERVER)
Pelayan nama merupakan program yang melengkapkan informasi ruang nama
di dalam pokok domain yang mungkin mengandungi petunjuk kepada pelayan
nama lain yang boleh digunakan untuk memperolehi informasi berkenaan
bahagian lain dalam pepohon domain. Ringkasannya pelayan nama harus tahu
dan cekap untuk bertanya kepada pelayan lain untuk mengetahui domain lain
yang tidak dikuasai mereka. Sesebuah pelayan nama dipanggil pelayan nama
autoriti jika ia memegang rekod-rekod zon sesuatu domain.
iii) Peny impan (Cache)
Penyimpan akan menyimpan hasil pencarian respons sebelumnya. Pendek
kata BIND akan sentiasa mempelajari sesuatu dan akan menyimpannya untuk
beberapa ketika. Oleh itu untuk permintaan yang sama atau hampir sama, ia
akan cuba memperolehi maklumat dari penyimpan terlebih dahulu. Kaedah ini
akan mempercepatkan kadar respons.
iv) Rekod Sumber (RESOURCE RECORD)
Informasi sumber berkaitan dengan sesuatu nod dan nama dipanggil Rekod
Sumber (RR). Rekod sumber ini terletak di dalam fail zon dan digunakan
untuk mendefinisikan objek di dalam domain.
Beberapa jenis rekod asas RR adalah:
• SOA, Start Of Authority
Rekod SOA mengenal pasti sumber terbaik untuk mendapatkan
data berkenaan sesuatu domain. Ia juga menjadi penanda
permulaan RR. Hanya satu SOA sahaja dibenarkan di dalam
satu zon fail.
SYED.COM    IN      SOA    NS.SYED.COM. HOSTMASTER.SYED.COM.

• NS, Name Server
Rekod NS mengenal pasti pelayan autoriti untuk sesuatu
domain.
• A, Address
Rekod A memetakan nama perumah kepada alamat IP
HASHIM.SYED.COM.   518400    A      212.55.67.88.9
• CNAME, Canonical NAME
Rekod CNAME memetakan nama samaran kepada nama
sebenar (berkanun).
HASHIM.SYED.COM    CNAME   ABAH.SYED.COM.
• PTR, PoinTeR
Rekod PoinTeR memetakan alamat IP kepada nama
9.88.67.55.212 IN      PTR   HASHIM.SYED.COM.
• MX, Mail eXchange
Rekod Mail eXchange pula menunjukkan perumah yang
sepatutnya memproses atau menerima e-mel (MTA) untuk
sesuatu domain.
IN      MX    10 MAIL.SYE

26.3.1 Jenis-jenis Konfigurasi BIND Selaku Pelayan DNS
Utama (PRIMARY )
Pelayan utama DNS merupakan pelayan yang memegang informasi fail zon sesuatu
domain.
Pendua (SECONDARY)
Pelayan pendua (Secondary) sepatutnya hanya melakukan perpindahan domain (domain
transfer). Selain itu pelayan pendua digunakan untuk load-balancing dan mengambil alih
tugas pelayan utama, jika berlaku ralat.
IN-ADDR (Pemetaan Songsang)
Menyediakan pemetaan dari alamat IP kepada nama dengan menggunakan domain
IN_ADDR. Kaedah ini diselesaikan dengan mengambil alamat IP dan dipadankan dengan
rekod perumah domain.
26.3.2 Asah Bakat 1: Konfigurasi BIND
Anda diminta untuk membangunkan domain aljufry.org.my yang mempunyai 2 pelayan
DNS, 1 pelayan e-mel dan beberapa perumah lain.
7. Untuk memudahkan pembangunan perkhidmatan DNS kita perlulah
membangunkan rajah konfigurasi terlebih dahulu. Isu permohonan juga perlu
diambil kira sekiranya kita membangunkan domain yang sah. Di Malaysia badan
yang bertanggungjawab ialah MyNic yang terletak di Taman Teknologi Malaysia.

8. Tambah informasi domain kedalam fail /etc/named.conf
9. Buat fail pemetaan terus di /var/named/aljufry.forward
10. Buat fail pemetaan songsang di /var/named/aljufry.reverse
11. Pastikan semua penetapan keizinan dan pemilik fail dan lipatan adalah betul
12. Mulakan perkhidmatan dengan menjalankan arahan service named start
13. Kadangkala anda mungkin akan mengalami masalah menutup perkhidmatan di
Red Hat 9 kerana ia mengandungi pepijat. Oleh itu anda boleh melakukan
penutupan secara manual dengan menggunakan arahan kill.
Domain:  aljufry.org.my.
Rekod DNS:  dns1.aljufry.org.my.
dns2.aljufry.org.my.
Rekod MX:  mail.aljufry.org.my.
Rekod Perumah:  dns1.aljufry.org.my.    202.187.33.2
dns2.aljufry.org.my.    66.44.73.1
mail.aljufry.org.my.    202.187.33.3
www.aljufry.org.my.    202.187.33.10
khalid.aljufry.org.my.  linux.aljufry.org.my. 202.187.33.11
hashim.aljufry.org.my.   202.187.33.12
alaweeyah.aljufry.org.my.   202.187.33.13

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
