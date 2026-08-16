---
okf_version: 0.1
name: Bab 4 - Bahagian 1
topics: [linux, manual, references, chapter-4]
tags: [noss, dbp]
---
# Bab 4 - Bahagian 1

13.4.7.1 Pemecahan Melalui fdisk
Anda diminta menekan ALT+CTRL+F2 untuk memberikan anda pengesa shell.
Sebahagian mungkin akan berasa kurang selesa dengan kaedah ini. Tapi percayalah
bahawa anda akan menjadi seorang pakar Linux jika anda dapat menguasai bahagian ini
dengan baik.
Larikan arahan seperti di bawah
# fdisk /dev/hda
Sebaik sahaja anda melarikan arahan tersebut anda akan dipertontonkan dengan menu
fdisk. Jika anda tidak pasti sebarang arahan yang perlu diberikan, anda boleh menaip
huruf [m] pada prom untuk mendapatkan bantuan.
Jadual di bawah menunjukkan sebahagian daripada arahan dalam fdisk:
Arahan  Ulasan
p  Memaparkan jadual pecahan cakera
t  Mengubah jenis pecahan
n  Menambah pecahan
d  Membuang pecahan
a  Set bendera but ke atas pecahan
w  Menulis perubahan pecahan dan keluar dari fdisk
q  Keluar tanpa melakukan sebarang perubahan ke atas jadual
Pecahan
Jadual 11 : Arahan dalam perlaksanaan fdisk
Di dalam arkitektur x86, kita dibenarkan untuk mempunyai 4 pecahan utama sahaja. Jika
kita ingin mempunyai lebih dari nilai tersebut, kita perlu mengambil salah satu pecahan
utama untuk menjadi pecahan lanjutan.

Namun pecahan lanjutan itu juga mempunyai had maksimum untuk pecahan pendua iaitu
hanya 12 pecahan sahaja. Pendek kata nilai pecahan maksimum yang dibenarkan ialah 3
pecahan utama, 1 pecahan lanjutan dan 12 pecahan pendua.
Gambar Rajah 138 : Kekotak dialog disk druid

13.4.7.2 Memilih Pecahan Untuk Proses Pembentukan
Anda dibenarkan untuk membuat pilihan pecahan mana yang anda ingin bentukkan.
Pastikan anda tidak membentuk pecahan yang mengandungi data yang penting. Pastikan
juga anda telah menyalin dua data-data anda, kerana selepas proses ini tiada jalan pulang.
Program Anaconda akan membentuk pecahan anda kepada sistem fail Linux iaitu ext3.
Anda boleh memilih untuk “Check for bad blocks while formatting” namun ia akan
mengambil masa yang amat lama.

Gambar Rajah 139 : Memilih pecahan untuk proses pembentukan

13.4.8 Penetapan LILO
Kemudian anda akan ditanya lokasi peletakan LILO (LInux LOader) dalam sistem anda.
Adalah dinasihatkan anda meletakkan LILO di dalam MBR.
Gambar Rajah 140 : Kekotak Dialog LILO

13.4.9 Memilih Kumpulan Pakej
Pada peringkat ini anda telah bersedia untuk memuatkan pakej ke dalam sistem anda.
Kita akan teruskan proses pemuatan dengan memilih semua pakej.
Gambar Rajah 141 : Kekotak dialog pemilihan pakej

13.4.10 Memuatkan Pakej
Anda akan dipaparkan dengan dialog di bawah. Pada ketika ini anda mungkin perlu
memikirkan untuk mengambil sedikit makanan untuk mengalas perut. Ini adalah kerana
ia akan mengambil masa yang agak lama untuk disiapkan.
Bar penunjuk akan menunjukkan prestasi kemajuan pemuatan
Gambar Rajah 142 : Kemajuan proses pemuatan

13.4.11 Pe mbikinan Cakera liut But
Masukkan sekeping cakera liut 3.5” ke dalam pemacu cakera liut anda. Pastikan anda
berbuat demikian untuk memastikan anda tidak menghadapi masalah di hari muka.
Gambar Rajah 143 : Kekotak dialog pembikinan cakera liut but

13.4.12 Pemuatan  Selesai
Tahniah anda telah melepasi peringkat pertama dalam pengembaraan penuh cabaran ini.
13.5 Prosedur Selepas Pemuatan
Selepas anda menyudahkan proses pemuatan Linux anda, sistem anda akan di”reboot”
dan tunggu sehingga ia selesai. Log masuk (login) sebagai “root” dan mulakan eksplorasi
ke dalam sistem tersebut. Langkah pertama yang perlu kita buat ialah mengemaskinikan
beberapa penetapan.
13.6 Mencipta Akaun Pengguna Lain
Setiap kali Linux telah siap dimuatkan di dalam sistem anda, terdapat beberapa akaun
terbina sendiri yang sebahagian besarnya wajib hadir dalam sistem anda. Contohnya
akaun “root” tidak boleh dibuang dan diperlukan untuk kelebihan sebagai pengendali
sistem. Namun anda tidak digalakkan untuk menggunakan akaun ini walaupun anda
layak berbuat demikian. Hal ini adalah kerana dikhuatiri anda akan merosakkan sistem
tersebut secara tidak sengaja. Ini selalu berlaku kepada sesiapa sahaja walaupun
penggunanya merupakan pengguna berpengalaman. Selain itu kaedah ini juga dapat
mempertingkatkan sekuriti sistem anda. Oleh itu biasakanlah log masuk (login) sebagai
pengguna biasa.
Kebanyakan pecahan Linux telah pun menyediakan skrip untuk penambahan pengguna
sistem. Antara program yang biasa digunakan ialah useradd dan adduser. Contohnya,
anda boleh menambah akaun pengguna iena yang mempunyai kata kunci (password)
dengan arahan seperti di bawah:
# adduser linux  -p passw0rd

Anda juga boleh mengubah kata laluan akaun (account password) nama pengguna
dengan melarikan arahan:
# passwd <username>
Nota : <username> adalah nama pengguna anda
13.6.1  Kemas kini Pangkalan data Fail
Linux mempunyai pangkalan data terbina dalam yang dikenali sebagai slocate. Kehadiran
pangkalan data ini memberikan banyak kelebihan kepada pengguna Linux terutamanya
dalam mencari fail atau lipatan. Anda boleh mengemaskinikan pangkalan data tersebut
dengan melarikan arahan
# updatedb
Untuk menggunakan kelebihan pencarian fail yang dimaksudkan anda bolehlah
melarikan arahan seperti sintaks berikut:
# locate <fail atau lipatan>
Muslihat penggunanya ialah pastikan anda selalu melarikan arahan ini, walaupun
sebenarnya arahan ini akan dijalankan secara automatik setiap hari melalui aplikasi
“cron”.

13.7 Mendapatkan Talian Bantuan (Online Help)
Budaya suka membaca dan berbincang adalah amat penting dalam Linux. Oleh itu Linux
telah menyediakan halaman panduan yang dipanggil man. Setiap masa jika anda
memerlukan bantuan atau ingin mengetahui lebih mendalam berkenaan sesuatu konsep
dalam Linux bolehlah anda melarikan arahan seperti di bawah:
# makewhatis
# man ±k <subjek yang dikehendaki>
Kemudian pilihlah dari pilihan subjek yang tepat dan contohnya anda ingin mengetahui
lebih mendalam berkenaan kata laluan, oleh itu larikan arahan seperti di bawah:
# man password
Sebaik sahaja anda melarikan arahan tersebut anda akan diberikan sebuah halaman
informasi berkenaan password. Halaman man ini dibahagikan kepada beberapa seksyen
seperti panggilan sistem, fungsi perpustakaan, format fail konfigurasi dan dalaman
isirung (kernel).
13.8 Penutupan Sistem
Anda tidak seharusnya but semula atau menutup sistem tanpa melalui kaedah yang sah
dan betul. Seperti sistem Unix yang lain, Linux akan menyembunyikan data di lipatan
sementara dan memori sebelum menulisnya kepada cakera, oleh itu sebarang tindakan
yang menyebabkan sistem tidak ditutup dengan kaedah yang betul akan menyebabkan
kehilangan atau kerosakan data yang serius.
Dalam sistem Linux, jika anda menekan butang CTRL+ALT+DEL serentak akan
menyebabkan memerangkap isirung (kernel) untuk memulakan proses penutupan secara

selamat. Namun ada banyak kaedah lain untuk membolehkan sistem anda ditutup dengan
selamat.
Contohnya jika anda ingin menutup sistem dengan pantas anda boleh larikan arahan
seperti di bawah melalui akaun “root"
# shutdown -r now
# shutdown -h now
atau
# init 6
# init 0
atau
# reboot
# poweroff
Kesemua arahan ini akan membolehkan sistem Linux anda ditutup terus atau but semula.
Halaman man akan memberikan anda opsyen-opsyen lain yang boleh anda gunakan
dalam sistem Linux, seperti memberikan sela masa sebelum penutupan mahupun
memberikan amaran kepada semua pengguna sistem sebelum penutupan.

PANDUAN PENGAJAR
Pelajaran 14 : Pelayaran & Konfigurasi

Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada beberapa arahan asas shell.
Keselesaan dalam menggunakan shell adalah amat penting dalam Linux kerana ia
memainkan peranan utama dalam penyelenggaraan dan penentuan ketetapan sistem
(Sistem Setting) Linux.
Objektif:
1. Mengetahui kepenggunaan arahan cd
2. Mengetahui kepenggunaan arahan pwd
3. Mengetahui kepenggunaan arahan ls
4. Mengetahui kepenggunaan arahan cat
5. Mengetahui kepenggunaan arahan more
6. Mengetahui kepenggunaan arahan less
7. Mengetahui kepenggunaan arahan find
8. Mengetahui kepenggunaan arahan whereis
9. Mengetahui kepenggunaan arahan locate
10. Mengetahui kepenggunaan arahan apropos
11. Mengetahui kepenggunaan arahan whatis
12. Mengetahui kepenggunaan arahan man
13. Mengetahui arahan asas berkenaan sistem dan kegunaannya

14 Pelayaran Sistem Fail
Buku ini ditulis untuk pembaca yang tidak mempunyai sebarang pengetahuan mengenai
Linux. Tidak dinafikan dengan versi GNOME yang baru sistem Linux kini telah menjadi
sistem yang lebih serasi kepenggunaan, namun anda tetap perlu memahami beberapa
perkara asas seperti struktur hierarki direktori dalam Linux dan konsep pengguna dalam
Linux. Pemahaman mengenai konsep-konsep berkenaan akan memudahkan anda untuk
bergerak di dalam sistem anda tanpa ragu-ragu.
Linux merupakan suatu sistem operasi yang mampu mengendalikan permintaan lebih dari
satu pengguna dalam sesuatu masa secara serentak melalui sambungan rangkaian
setempat dan berselerak selain penggunaan terminal maya di konsol. Linux memerlukan
anda untuk menyatakan keempunyaan diri anda melalui nama laluan dan kunci laluan
yang betul. Kedua-dua elemen ini merupakan diperlukan untuk mencapai akaun anda di
dalam sesuatu komputer.
Oleh kerana hanya anda sahaja yang mengetahui kunci laluan anda, tiada pengguna lain
yang boleh memasuki sistem tersebut dengan menggunakan nama laluan anda. Biasanya
pengguna akan memilih nama laluan berdasarkan nama mereka, oleh itu jika nama anda
Haslina, maka anda mungkin akan memilih iena sebagai nama laluan.
Setiap akaun akan mempunyai lipatan perumah (home directory) tersendiri untuk
pengguna meletakkan failnya. Linux mempunyai sistem sekuriti terbina yang memastikan
setiap pengguna hanya mempunyai kuasa untuk mengubah ketetapan (setting) dan
perubahan fail serta lipatannya (directory) pada kedudukan lipatan perumah (home
directory) mereka sendiri sahaja. Keadaan ini membolehkan setiap pengguna mempunyai
akaun sendiri tanpa menjejaskan pengguna lain dalam sistem yang sama.
Dalam Linux terdapat sistem akaun mutlak yang mempunyai kuasa agung iaitu pengguna
root. Akaun ini akan mampu mengubah apa sahaja penetapan, membuat akaun pengguna

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
