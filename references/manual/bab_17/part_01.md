---
okf_version: 0.1
name: Bab 17 - Bahagian 1
topics: [linux, manual, references, chapter-17]
tags: [noss, dbp]
---
# Bab 17 - Bahagian 1

Mukadimah:
Dalam pelajaran ini, anda akan diberi penekanan kepada pelayan web yang amat popular
dan mendominasi 60% pasaran iaitu pelayan Apache. Apache menjadi pilihan
kebanyakan pembangun sistem kerana ia mudah digunakan dan yang penting sekali
mudah dibentuk jika perlu sebarang perubahan dilakukan.
Objektif:
1. Mengenali konsep-konsep perkhidmatan web
2. Mengetahui konfigurasi asas pelayan Apache
3. Mengetahui asas dan sejarah Apache
4. Memulakan perkhidmatan Apache

25 PERKHIDMATAN WEB
25.1 Pengenalan
Apache merupakan pelayan web yang paling banyak dipergunakan di Internet. Program
ini pertama kali dimulakan untuk sistem operasi lingkungan UNIX. Namun demikian,
pada beberapa versi berikutnya Apache mengeluarkan programnya yang dapat dijalankan
di Windows NT.
Berdasarkan sejarahnya, Apache dimulai oleh pembangun veteran NCSA httpd (National
Center for Supercomputing Application). Saat itu pengembangan NCSA httpd sebagai
pelayan web mengalami zaman malap. Rob Mc. Cool meninggalkan NCSA dan memulai
sebuah projek baru bersama para webmaster lainnya, menambal pepijat, dan
menambahkan ciri-ciri pada NCSA httpd. Mereka mengembangkan program ini melalui
kumpulan perutusan e-mel.
Dengan berpijak pada NCSA httpd versi 1.3, kumpulan Apache mengeluarkan keluaran
pertama kali secara rasmi Apache versi 0.6.2. Ahli yang menjadi inti-pati pengembang
Apache waktu itu ialah:
• Brian Behlendorf
• Roy T. Fielding
• Rob Hartill
• David Robinson
• Cliff Skolnick
• Randy Terbush
• Robert S. Thau
• Andrew Wilson
Dengan tambahan sokongan daripada:

• Eric Hagberg
• Frank Peters
• Nicolas Pioch
Nama Apache diambil dari kata "A Patchy Server", pelayan perbaikan yang penuh
dengan tampalan (patch). Tampalan yang dimaksudkan adalah penambahan ciri-ciri dan
penampalan ralat dari NCSA httpd Versi 1.3.
Saat ini Apache dipergunakan secara luas. Hal ini disebabkan karena programnya yang
menakjubkan, dengan hasil yang relatifnya stabil. Dalam pengembangannya pun
mempergunakan sistem Bazaar, yakni tiap orang dibuka kesempatan seluas-luasnya
untuk dapat memberikan sokongan dalam mengembangkan program. Sokongan
dikomunikasikan melalui kumpulan e-mel.
Kumpulan Apache mempunyai kumpulan e-mel yang terbuka untuk siapa saja yang ingin
ambil bahagian. Untuk mendaftar cukup kirim e-mel ke majordomo@apache.org dengan
baris pertama dari email bertuliskan "subscribe new-httpd". Perlu dicatat bahawa projek
pengembangan Apache ini mempunyai sistem meritokrasi. Semakin banyak yang anda
sumbangkan, semakin banyak yang boleh dikerjakan.
Apache mempunyai program pendukung yang cukup banyak. Hal ini memberikan
layanan yang cukup lengkap bagi penggunanya. Beberapa dukungan Apache :
• Kontrol Akses Kontrol ini dapat dijalankan berdasarkan nama host atau alamat IP
• CGI (Common Gateway Interface), yang paling terkenal untuk digunakan adalah
• Perl (Practical Extraction and Report Language
• PHP (Personal Home Page / PHP Hypertext Processor)

Gambar Rajah 217 : Pelayar web lynx mempertontonkan halaman dari Apache
25.2 Konfigurasi
Fail konfigurasi Apache terletak di lipatan /etc/httpd/conf/. Nama failnya adalah
httpd.conf, srm.conf dan access.conf.
httpd.conf merupakan fail yang dilihat pertama kali apabila Apache dijalankan. Di
dalamnya terletak konfigurasi secara umum. srm.conf adalah fail konfigurasi yang dibaca
setelah httpd.conf. Disarankan untuk membiarkan fail konfigurasi ini tetap kosong. Dan
access.conf merupakan konfigurasi untuk menuras perumah-perumah yang boleh
menerima layanan Apache.
25.2.1 Fail Konfigurasi Apache
Secara amnya, Apache memisahkan fail konfigurasinya menjadi 3 bahagian, yakni
httpd.conf, srm.conf dan access.conf. Namun semua binari program dalam Red Hat
menyatukannya dalam satu fail yakni httpd.conf. Fail ini dibahagi menjadi 3 bahagian
utama :

1. Global environment
Berisi konfigurasi Apache secara umum, seperti berapa banyak pengguna dapat
akses pada waktu yang sama.
2. Section (Main) Configuration
Konfigurasi utama yang tidak termasuk dalam virtual host. Bahagian ini juga
termasuk penetapan dasar untuk virtual host.
3. Virtual host
Konfigurasi untuk virtual host, yakni memanggil alamat IP dan DNS yang
berbeza meskipun masih dalam satu kawalan pelayan Apache yang sama.
Berikut pembahasan beberapa contoh pilihan konfigurasi file httpd.conf. Pilihan yang
disampaikan di sini mengacu pada file httpd.conf yang diberikan secara dasar oleh
Apache selesai pemuatan..
Gambar Rajah 218 : Global Environment dalam fail /etc/httpd/conf/httpd.conf

Gambar Rajah 219 : Bahagian Virtual Host dalam fail /etc/httpd/conf/httpd.conf
25.3 Ringkasan
Pada bahagian ini, telah dipelajari bagaimana menghidupkan Apache Versi 2.0. Selain itu
juga telah direnung fail konfigurasi penting yang digunakan oleh Apache, yakni
httpd.conf (di mana yang dibahaskan di sini mencakupi tiga fail, yakni httpd.conf,
berserta srm.conf dan access.conf).
Untuk dapat memanfaatkan secara maksimum kemampuan Apache ini, anda harus
memahami benar pilihan-pilihan yang tersedia, dan modul-modul mana yang
mendukungnya. Daftar modul yang diberikan Apache, serta pilihan-pilihan yang
didukung olehnya, dapat dibaca di dokumentasi Apache yang disertakan dalam Red Hat.
Fail ini terletak di lipatan /var/lib/apache/htdocs. Dokumentasi online dapat di akses di
http://www.apache.org/docs.

PANDUAN PENGAJAR
Pelajaran 26: Perkhidmatan DNS

Mukadimah:
Dalam pelajaran terakhir ini, anda akan diperkenalkan kepada aplikasi terpenting iaitu
BIND yang memberikan perkhidmatan DNS. BIND yang dibangunkan oleh ISC amat
popular dan digunakan secara meluas.
Objektif:
1. Mengetahui asas dan sejarah BIND
2. Mengenali konsep-konsep perkhidmatan DNS
3. Mengetahui konfigurasi asas pelayan BIND
4. Memulakan perkhidmatan BIND

26 PERKHIDMATAN DNS
26.1 Pengenalan
Sudah menjadi tabiat manusia untuk mudah menghafal perkataan berbanding nombor.
Sifat semula jadi ini kadangkala memberikan masalah; kerana pada komputer semuanya
hanyalah binari sifar, binari satu ataupun gabungan kedua-duanya.
Seperti mana kita telah pelajari sebelum ini, alamat IP biasanya dibayangkan dalam
bentuk asas persepuluhan seperti 202.188.25.173 yang mana ia merujuk kepada satu
sistem komputer yang unik dan tersendiri. Namun, hampir semua orang akan mudah
terlupa atau sukar mengingati alamat IP tersebut. Masalah ini harus diatasi, satu
perkhidmatan tambahan untuk menukarkan alamat IP kepada nama domain amat
diperlukan.
Pada awalannya perkhidmatan ini hanya dibekalkan oleh satu fail ASCII iaitu /etc/hosts
untuk sistem Linux dan %windir%\system32\drivers\etc\hosts untuk sistem Windows.
Namun kini adalah mustahil untuk memetakan alamat IP dan nama domain seluruh
Internet ke dalam satu fail sahaja.

Gambar Rajah 220 : Fail /etc/hosts

Gambar Rajah 221 : Fail %windir%\system32\drivers\etc\hosts
Lalu pada tahun 1984, Paul Mockapetris mengusulkan sistem penamaan domain (DNS)
yang diterapkan dalam RFC 882  dan RFC 883.  Ia menyatakan bahawa perkhidmatan
DNS perlulah menjadi satu sistem yang teragih, berhierarki, statik (kini terdapat dalam
bentuk dinamik) dan yang terpenting sekali ialah mempunyai pangkalan data untuk
menyokong segala bentuk pertanyaan dan pengubahsuaian.
Struktur pangkalan data DNS mirip dengan sistem fail yang ada di Linux. Jika dalam
sistem fail Linux memiliki direktori root (/)  kemudian di bawahnya ada direktori usr
(/usr), bin (/bin) dan seterusnya, maka dalam struktur pangkalan data DNS juga memiliki
root (.), kemudian com (com.), net (net.) dan seterusnya.

Organisasi Internet Assigned Numbers Authority (IANA) yang beroperasi di Universiti
Southern California, merupakan badan yang dipertanggungjawabkan untuk
mengkoordinasi pembahagian alamat IP dan perkhidmatan DNS. Mereka telah
membahagikan dunia ini kepada 3 organisasi setempat iaitu:
• ARIN:
o American Registry for Internet Numbers beroperasi untuk benua Amerika
dan sebahagian Afrika-Sahara
• RIPE:
o Resias IP Europeans beroperasi di Afrika Utara dan Eropah
• APNIC:
o Asia-Pasific Network Information Center beroperasi di Asia dan Australia
Setiap organisasi di bawah IANA ini berfungsi untuk menjaga kepentingan setiap benua
dan sekali gus mengkoordinasi segala bentuk masalah dan pertanyaan berkenaan IP dan
nama domain.
Contoh sebuah nama domain yang lengkap atau FQDN ialah www.eng.upm.edu.my.. Di
mana “www” merujuk kepada sistem yang unik, “eng” pula merujuk kepada cabang
organisasi kepada “upm” dan “edu” pula merujuk kepada cabang pendidikan untuk
negara Malaysia, “my” dan “.” pula digelar sebagai titik helaan (trailing period) merujuk
kepada pelayan akar.
Kini di seluruh dunia terdapat hanya 13 buah pelayan akar. Rajah 2 di bawah
menerangkan nama, lokasi dan alamat IP kesemua pelayan akar.

Pelayan Akar Alamat IP Organisasi Lokasi
A.ROOT-SERVERS.NET 198.41.0.4 NSF-NSI Herndon, VA
B.ROOT-SERVERS.NET 128.9.0.107 DISA-USC Marina delRey, CA
C.ROOT-SERVERS.NET 192.33.4.12 PSI Herndon, VA
D.ROOT-SERVERS.NET 128.8.10.90 UMD College Pk., MD
E.ROOT-SERVERS.NET 192.203.230.10 NASA Moffet Field, CA
F.ROOT-SERVERS.NET 192.5.5.241 ISC Woodside, CA
G.ROOT-SERVERS.NET 192.112.36.4 DISA-Boeing Vienna, VA
H.ROOT-SERVERS.NET 128.63.2.53 USArmy Aberdeen, MD
I.ROOT-SERVERS.NET 192.36.148.17 NORDU Stockholm, Sweden
J.ROOT-SERVERS.NET 198.41.0.10 NSF-NSI Herndon, VA
K.ROOT-SERVERS.NET 193.0.14.129 LINX/RIPE London, England
L.ROOT-SERVERS.NET 198.32.64.12 DISA-USA Marina delRay, CA
M.ROOT-SERVERS.NET 202.12.27.33 WIDE Keio, Jepun
Jadual 38 Pelayar Akar DNS

Gambar Rajah 222 : Peta yang menunjukkan pelayan akar DNS yang diperoleh dari laman web
www.wia.org
26.2 Bagaimana DNS Berfungsi
DNS bekerja dalam modus operasi pelayan-pelanggan. Dalam erti kata lain pelanggan
akan bertanya nama atau alamat IP, kemudian pelayan akan memberikan informasi nama
atau alamat IP, sekiranya pelayan tersebut tidak mengetahuinya ia akan bertanya kepada
pelayan lain. Pelayan DNS yang paling banyak digunakan di Linux adalah BIND yang
dibangunkan oleh Internet Software Consortium (ISC).

Andai kata anda ingin melihat laman web di http://www.upm.edu.my.. Menggunakan
perisian pelayaran web Mozilla, maka isirung (kernel) akan melihat fail /etc/host.conf;
berdasarkan fail tersebut, isirung (kernel) sedar ia perlu menurut turutan pencarian di fail
/etc/hosts terlebih dahulu, sekiranya gagal ia akan menghubungi fail /etc/resolv.conf
untuk mengetahui senarai pelayan DNS (maksimum 3 pelayan) untuk mencari alamat IP
perumah www.upm.edu.my..
Setelah terhubung melalui proses penghalaan, pelayan DNS yang tersenarai di
/etc/resolv.conf ak
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
