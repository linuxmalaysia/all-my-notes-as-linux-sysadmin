---
okf_version: 0.1
name: Bab 9 - Bahagian 1
topics: [linux, manual, references, chapter-9]
tags: [noss, dbp]
---
# Bab 9 - Bahagian 1

Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
17.4.2 Pengompilan Tarballs (.tar.gz atau .tgz)
Kadangkala mungkin tidak dapat membuat fail pakej daripada fail sumber RPM , maka
kod sumber boleh dikompilkan daripada sumber tarball yang asal atau mengompil
perisian secara langsung. Dengan melakukannya , peluang untuk pre-kompil pakej binari
harus diabaikan seperti pakej RPM atau Debian, termasuk perlindungan daripada
kemalangan tertulis fail dari pakej lain , kebolehan untuk mengesahkan kandungan pakej,
dan sebagainya.
Berikut menunjukkan langkah-langkah am apabila kompil sumber tarball hendak
dilakukan, tetapi kod sumber yang berlainan mungkin perlu dikompilkan secara
berlainan.
1. Muat turun sumber tarball daripada internet.
2. Buka sumber tarball dengan menggunakan arahan seperti tar zxvf sourcecode. Tgz
atau tar zxvf sourcecode. Tar. Gz  , atau tar xvf sourcecode. tar . Ini akan
menghasilkan sub direktori yang mengandungi distribusi kod sumber.
# tar zxvf sourcecode.tar.gz
3. Tukar kepada direktori dimana tarball telah dinyah-tarkan kepada :
# cd soucecode
4. Baca dokumentasi termasuk lihat bagaimana caar untuk konfigurasi dan kompil
kod sumber.
Secara amnya, kod sumber boleh dikompilkan dengan langkah berikut tetapi selalu rujuk
kepada dokumentasinya sendiri.
5. Konfigurasi sumber yang akan dikompil dalam sistem semasa:
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
# ./configure
6. Kompilkan kod sumber:
# make
7. Instalasikan kod sumber yang telah dikompilkan ( atau kini ianya binari) kepada
sistem :
# make install
Prosedur yang diterangkan di atas menunjukkan langkah-langkah am dalam mengompil
kod sumber; ia adalah mustahil untuk menyediakan suatu prosedur yang lengkap dan tepat
untuk tujuan instalasi kesemua kod sumber tarball. Tiada dua pakej kod sumber yang
hampir sama ; setiap pembangun kod sumber mempunyai stail dan pilihannya sendiri
dalam istilah kompilasi dan prosedur instalasi.
17.5  Perkakas Pakej Lanjutan  Untuk Rpm (ADVANCE PACKAGE
TOOL (APT)
Apt (Advance Package Perkakas) amat masyhur dikalangan pengguna Debian semenjak
ia digunakan dengan format pakej dpkg. Walau bagaimana pun , APT kini telah
dilabuhkan untuk bekerja dengan pakej rpm seperti Conectiva juga, yang
bertanggungjawab menggunakannya untuk suatu tempoh dalam GNU/distribusi Linux.
Kebaikannya ialah apt untuk rpm berkemungkinan besar digunakan dengan apa saja
distribusi berdasarkan-rpm. Apa yang diperlukan adalah pakej RPM yang betul untuk
versi Red Hat Linux (dan versi RPM) dan sekurang-kurangnya penyimpanan pakej rpm
dan metadata apt mereka boleh ditemui.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Anda akan dapat mencari pakej apt yang pra-konfigurasinya bersih untuk Red Hat Linux.
http://apt.freshrpms.net. Muat turunkan pakej apt untuk distribusi Linux daripada halaman
internet. Pakej itu adalah sangat kecil dan ia sepatutnya dimuat turunkan dalam tempoh
yang singkat. Sebaik sahaja muat turun selesai, instalasikan pakej tersebut dengan:
# rpm – ivh apt – 0.5 . 4cnc9 – frl . i 386. rpm
Dan segalanya telah selesai. Anda kini boleh menggunakan apt untuk tujuan instalasi ,
membuang  dan mengemaskini pakej Red Hat Linux.
Klien apt adalah agak mudah untuk digunakan. Jika anda telah biasa menggunakan
arahan rpm dan arahan terbaris (command line) , sepatutnya tiada masalah untuk
menggunakan apt.
Memandangkan apt digunakan untuk tujuan instalasi dan pembuangan pakej RPM
daripada komputer anda , anda harus melaksanakan pakej dalam suasana anda sebagai
superuser atau root. Arahan yang paling lazim digunakan ialah apt ± get.
17.5.1 Untuk Membuang Pakej RPM :
Sintaks : apt – get remove < package_name >
17.5.2 Untuk menginstalasi pakej RPM baru atau menaiktaraf pakej yang
sedia ada
Sintaks : apt – get install < package_name >
Contoh penggunaannya :
Menginstalasikan suatu pakej
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Menaiktaraf suatu pakej
17.5.3 Untuk mendapatkan kemaskini penyimpanan RPM yang mutakhir :
Syntaks : apt ± get update
Contoh penggunaannya :
Fakta Segera:
Suatu penyimpanan (repository) adalah pengkalan perisian yang besar, termasuklah
pakej kemas kini daripada distribusi utama , kemaskini rasmi atau “tidak terlalu
rasmi” dan pakej sumbangan dari pihak ketiga.
17.5.4 Untuk mengemaskini sistem pada penyimpanan kepada pakej RPM
yang mutakhir
Sintaks : apt ± get upgrade
Contoh penggunaannya :
apt membuat kerja yang baik untuk menyelesaikan kebergantungan apabila
menginstalasi, mengalihkan bahkan menaiktaraf sistem Linux itu. Selalunya, dua langkah
sahaaj yang diperlukan untuk memastikan Linux kemas-kinikan dengan semua
perlindungan, bug dan membaiki untuk peningkatan:
# apt – get update
# apt – get upgrade
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
17.6 SYNAPTIK : apt dalam GUI
Jika penggunaan apt berversi GUI lebih digemari sebagai ganti kepada arahan terbaris
(command line) , maka pakej lain perlu diinstalasikan dan ia dikenali sebagai Synaptik.
Memandangkan Synaptik adalah perisian yang mesti ada pada bahagian atas apt , maka ia
boleh diinstalasikan melalui apt sebaik sahaja apt berfungsi !
Untuk mendapatkan synaptik melalui apt :
# apt – get install synaptic
Sebaik sahaja Synaptik diinstalasikan , pilihan diberi samaada ia mahu dilaksanakan
daripada menu Start > System Settings > Synaptic atau jenis synaptik pada prompt arahan.
Setting untuk penyimpanan apt boleh diedit daripada Settings tab.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Pelajaran 18: Meja Kerja GNOME
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada meja kerja Linux yang terkenal dan
menjadi asas kepada hampir kesemua pecahan Linux iaitu GNOME. GNOME yang
dimulakan kira-kira 20 tahun lepas tetap menjadi pilihan utama kebanyakan pengguna
Linux bahkan juga Unix. Oleh itu diharapkan selepas pelajaran ini, anda akan dapat
menyelesakan diri anda dengannya.
Objektif:
1. Memperkenalkan persekitaran GNOME kepada pengguna
2. Mengetahui cara untuk mendapatkan bantuan dalam persekitaran GNOME
3. Mengetahui ciri-ciri asas yang terdapat dalam meja kerja GNOME
4. Mengetahui kaedah penyesuaian sistem dalam GNOME
5. Mengetahui kepelbagaian aplikasi dalam GNOME
6. Mengetahui kaedah menutup, log keluar dan menghidupkan semula sistem dalam
persekitaran GNOME
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
18 GNOME
18.1 Pengenalan Kepada Gnome
Gnome merupakan persekitaran bergrafik asas untuk Red Hat Linux yang membolehkan
penggunanya mengendali sistem mereka dengan mudah dan efisien. Dimulakan pada
tahun 1984, Gnome telah berkembang menjadi aplikasi persekitaran bergrafik paling
popular untuk Linux dan sistem operasi Unix lain.
Pada asasnya, Gnome menyediakan satu panel (untuk memulakan aplikasi dan
mempamerkan status aplikasi), sebuah meja kerja (untuk memperlihatkan dan
meletakkan data dan aplikasi), sekumpulan aplikasi asas dan aplikasi bantuan untuk meja
kerja serta sekumpulan aplikasi konvensi yang memudahkan aplikasi-aplikasi lain untuk
memahami antara satu sama lain.
Pengguna dari sistem operasi lain akan mendapati bahawa Gnome mampu memberikan
prestasi setanding bahkan lebih hebat dari jangkaan mereka. Gnome juga serasi dengan
sistem operasi lain seperti Solaris dan FreeBSD. Gnome merupakan hasil karya sumber
terbuka yang melibatkan beribu-ribu jurukod dari seluruh dunia.
Seperti Linux semua kod dan binari Gnome boleh diperolehi secara percuma di bawah
GNU GPL. Ini bermakna sesiapa sahaja dibenarkan untuk menggunakan, menyalin dan
mengedarkan Gnome. Gnome adalah mudah untuk diubahsuai dan membolehkan anda
mengubahsuainya mengikut selera anda. Gnome dibina supaya serasi dengan bahasa
percakapan yang kita gunakan setiap hari. Gnome juga membolehkan anda untuk
melakukan konsep Tarik dan Letak untuk memberikan kebolehpercayaan tinggi kepada
penggunanya.
Tidak seperti Microsoft Windows atau Mac OS, Linux menyediakan lebih dari satu GUI.
GNOME adalah di antara satu suasana antara muka (interface) grafik yang disediakan
dengan Linux Red Hat.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
GNOME menyediakan suatu suasana mesra pengguna di mana anda boleh dengan
mudahnya mencapai aplikasi dan sistem. Pengguna baru dan berpengalaman akan dapat
menggunakan dengan sepenuhnya kelebihan sistem Linux Red Hat dengan menggunakan
suasana antara muka (interface) grafik GNOME.
Bab ini merangkumi asas-asas penggunaan GNOME. Untuk mempelajari dengan lebih
lanjut, sila lawati halaman rasmi GNOME di http://www.gnome.org.
Jika anda mempunyai GNOME dan KDE dipasang di dalam sistem anda, anda boleh
menggunakan sistem dari suasana antara muka grafik (graphical user interface
environment) yang lain. Sebagai contoh, anda boleh menggunakan  pelanggan e-mel
suasana antara muka grafik KDE (KDE graphical user interface environment) yakni
KMAIL di masa anda menggunakan GNOME. Anda boleh mencapai aplikasi KDE
dalam menu utama (Main Menu) di kaki paparan skrin di menu KDE.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
18.2 Mendapat Bantuan
Dokumentasi tambahan GNOME boleh didapati dengan mengklik di atas menu ‘help’ di
sebelah kanan tetingkap Nautilus. Ini akan menggerakkan pelayar bantuan terbina dalam
yang memberi anda dokumentasi yang lebih lengkap, tersedia untuk digunakan. Anda
boleh klik ikon pada Panel GNOME, di mana ia akan memaparkan ‘GNOME User’s
Guide’.
18.3 Paparan Mejakerja Gnome (Gnome Desktop)
Di bawah adalah paparan meja kerja suasana antara muka grafik GNOME (GNOME
graphical user interface desktop screen):
Gambar Rajah 156 : Paparan Mejakerja GNOME (GNOME Desktop screen)
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Seperti diterangkan sebelumnya, suasana antara muka grafik GNOME membenarkan
anda untuk mencapai aplikasi dan ketetapan (setting) sistem. Anda dapati ia menyediakan
tiga jenis alat untuk menggunakan sistem GNOME.
18.3.1 Ikon Meja kerja (Desktop Icon)
Ikon di atas meja kerja (desktop) mungkin adalah suatu lipatan fail (file directory) atau
pelancar aplikasi (application launcher). Untuk membuka lipatan fail (file directory) atau
melancarkan aplikasi, sila klik berganda di atas ikon tersebut.
18.3.2 Ikon Panel (Panel Icon)
Jaluran yang melintangi di bahagian bawah skrin adalah jaluran GNOME (GNOME
Panel). Jaluran ini mengandungi ikon dan aplikasi kecil yang memudahkan penggunaan
sistem. Aplikasi kecil ini yang digelar aplet (applet) membenarkan pengguna
menjalankan sesuatu tugas, memantau sistem atau perkhidmatan seperti Rangkaian Red
Hat, tanpa mengganggu anda. Jaluran ini juga mengandungi ikon Menu Utama (Main
Menu) yakni ikon yang paling kiri  di bawah skrin yang menjadi pemula untuk mencapai
menu aplikasi yang lain.
18.3.3 Sistem Menu (Menu Sistem)
Sistem menu boleh didapati dengan mengklik di atas menu utama (Main Menu)
GNOME. Mengkliknya akan mengembangkan suatu set menu besar yang membenarkan
anda mencapai aplikasi di sistem anda.
Dari sini, anda dapat melancarkan sebahagian besar aplikasi yang terkandung dalam
Linux. Anda dapati anda boleh mencapai aplikasi KDE di bawah pilihan menu KDE
(KDE Menu) jika KDE dipasang di sistem anda. Sub Menu ini akan membenarkan anda
menggunakan aplikasi-aplikasi di sistem anda.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Dari Menu Utama anda boleh juga keluar sistem, melancarkan aplikasi dari arahan
terbaris, mengunci paparan yang akan menjalankan penyelamat skrin berkata laluan di
man
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
