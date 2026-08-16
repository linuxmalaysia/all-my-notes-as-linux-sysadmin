---
okf_version: 0.1
name: Bab 7 - Bahagian 1
topics: [linux, manual, references, chapter-7]
tags: [noss, dbp]
---
# Bab 7 - Bahagian 1

Textedit Editor Xview
Vim VI Improved, editor pengatur cara
Xedit Editor untuk X11
Xemacs Emacs untuk X11
Jadual 25 : Jenis-jenis teks editor
Jika anda membuat banyak karangan berasaskan teks, anda perlu tahu beberapa teks
editor yang sangat berkuasa seperti emacs dan vi.
16.1.1 Emacs (Editor MACros)
Emacs paling diterima ramai lengkap dengan ciri-ciri editor secara percuma. Ia boleh
digunakan untuk edit teks, menjadualkan temu janji, menyelenggarakan diari, melayari
web, membaca berita usenet, mengarang dan menghantar mel elektronik (e-mail) dan
sebagainya. Anda boleh guna emacs, dengan atau tanpa sistem X Windows. Ia adalah
sistem yang sempurna menggunakan komputer untuk pembangunan, komunikasi,
pengurusan fail dan sebagainya.
16.1.1.1 Arahan Papan Kekunci
Emacs bergantung pada arahan papan kekunci untuk kawalan. Jadual di bawah
menunjukkan banyak arahan:-
Aksi Kombinasi kunci
Menggagalkan operasi semasa C+g
Mengundurkan anak panah C+b
Membawahkan anak panah C+n
Mendepani anak panah C+f
Memadamkan aksara C+d
Memadamkan baris C+k
Memadamkan perkataan M+d

Memulakan fail M+<
Memulakan baris C+a
Mengakhiri fail M+>
Mengakhiri baris C+a
Bantuan C+x, C+f
Buka fail C+v
Halaman ke bawah M+v
Keluar C+x, C+c
Menyimpan C+x, C+s
Tutorial C+h , t
Buat Asal C_or C+x, u
Jadual 26 : Arahan papan kekunci dalam program Emacs
16.1.1.2 Melarikan GNU Emacs
GNU Emacs mempunyai 22 pilihan baris arahan (command line), ia adalah mudah untuk
dimulakan. Untuk melarikan emacs dan buka fail teks untuk mengarang, beri nama fail
pada baris arahan (command line) seperti.
# emacs myfile.txt
Arahan di atas akan memuatkan editor dan membuka fail yang diminta. Jika anda
kursuskan emacs pada baris arahan (command line) dengan sendirinya, program itu
bermula, paparkan skrin pembuka dan kemudian hilang bila anda menyentuh kunci pada
papan kekunci.

Gambar Rajah 149 : Terminal X11 pada GNU emacs
Jika anda memulakan GNU emacs pada shell bagi X11 terminal Windows, versi X11
bagi GNU emacs, dengan tetikus dan penyokong (support) menu, bermula secara
automatik.
Jika anda ingin melarikan dari konsol, atau bukan versi X11 bagi GNU emacs di dalam
X11 terminal Windows, guna –nw (atau no-window), pilihan baris arahan (command
line) ditunjukkan di bawah
# emacs ±nw myfile.txt
Arahan ini membolehkan anda melarikan GNU emacs di dalam terminal X11 anda tanpa
bar menu (menu bar).

16.1.1.3 Menjalankan ( run ) Xemacs
Untuk memulakan karangan XEmacs semasa sesi X11, taip arahan ini :
# xemacs
editor akan memulakan dan memaparkan ‘page’.
Gambar Rajah 150 : Skrin editor XEmacs.
16.1.1.4 Pilihan Toolkit
GNU emacs dan Xemacs dalam mod X11 mematuhi dan mengikut kebanyakan pilihan
toolkit X11. Sesetengah pilihan dapat membantu seperti contoh di bawah:

-bg color -set background to color (latar belakang)
-cr color -set text cursor to color (teks)
-fg color -set foreground to color (latar depan)
-ms color -set mouse cursor to color (tetikus)
Warna yang boleh digunakan untuk kawalan warna (color setting) disenaraikan dalam fail
rgb.txt. di dalam direktori /usr/X11R6/X11.
16.1.1.5 Mengubah Adat Xemacs
Anda boleh setkan Xemacs kepada mod penggunaan teks dan ‘word-wrap’ secara
automatik, membolehkan perkhidmatan diari setiap hari atau memaparkan masa terkini
atau semasa dalam bentuk mod (bar status dalam ‘window’ utama). Untuk melakukan ini,
buat fail emacs dengan Xemacs:
# xemacs .emacs
kemudian taip ini untuk mengubah adat Xemacs:
(setq default – major – mode ‘text – mode)
(setq text – mode – hook  ‘turn – on – auto – fill)
(require ‘ appt)
(display – time)
(appt – initialize)
Tekan ctrl+x dan ctrl+s untuk simpan fail, dan tekan ctrl+x dan ctrl+c untuk keluar
Xemacs.

16.1.2 VIM ( Variants of The Visual Improved Editor)
Editor vim dibangunkan oleh Bram Moolenaar. Ia adalah teks editor yang sesuai dengan
vi (visual editor, editor yang popular).
Gambar Rajah 151 : Skrin editor VIM

Semasa memuatkan pakej bagi vim ke dalam sistem, beberapa fail dan sambungan
simbolik ke editor vim akan dibuat:
/usr/bin/vi     - vim
/usr/bin/view   -vim
/bin/vim
Editor vim menggantikan editor ex, vi dan view. Ia adalah editor visual yang menyokong
ciri-ciri seperti pergerakan anak panah. Dibandingkan dengan editor vi, editor vim ada
beberapa kelebihan. Kebanyakan dokumen bagi vim ditempatkan dalam
/usr/doc/packages/vim direktori. Fail teks dalam direktori /usr/share/vim/doc
mengandungi petunjuk yang meluas.
16.1.2.1 Operasi dan keluar dari vim
Sambungan antara mod yang berbeza
Vim menyediakan 3 mod untuk pengguna:
1. mod arahan – membolehkan pengguna memasukkan arahan
2. mod input – membolehkan pengguna memasukkan input
3. mod lepas garis – membolehkan pengguna mencari perkataan, satu ayat,
menyimpan fail-fail atau keluar dari kerja-kerja dan sebagainya.
Mod arahan ialah mod tersedia (default mode). Selepas itu, anda perlu memasukkan data
maklumat yang berkaitan dengan mod. Anda juga boleh menggunakan papan kekunci
untuk memasukkan data :
• tekan ‘a’ – masuk perkataan yang baru di tempat yang berikutnya selepas
kedudukan  anak panah (cursor)
• tekan ‘i’ – masuk perkataan yang baru pada kedudukan anak panah (cursor)

• tekan ‘o’ – tambah baris baru atau menukar kedudukan anak panah (cursor) pada
baris baru
Sekiranya anda hendak menukar daripada Mod Input (Input Mode) ke Mod Arahan
(Command Mode), tekan kekunci ‘ESC’. Sekiranya anda menukar ke Mod Baris Akhir,
tekan ‘,’ di dalam Mod Arahan.
Arahan yang sering digunakan.
Mod Arahan (command mode) menggunakan kekunci dan juga gabungan kekunci untuk
melarikan arahan. Di sini kami menerangkan cara-cara menggunakan arahan-arahan yang
selalu digunakan:
1. Menggerakkan lokasi anak panah (cursor)
Gunakan kekunci anak panah (arrow) untuk menggerakkan anak panah tetikus (mouse
cursor). Sekiranya kekunci tersebut tidak dapat digunakan, guna kekunci yang tersenarai
di bawah:
H Kawal anak panah (cursor) bergerak satu ruang ke kiri
L Kawal anak panah (cursor) bergerak satu ruang ke kanan
I Kawal anak panah (cursor) bergerak ke baris seterusnya yang di bawah
K Kawal anak panah (cursor) bergerak ke baris seterusnya yang di atas
G Anak panah (cursor) bergerak ke awal baris terakhir
O Anak panah (cursor) bergerak ke akhir baris terakhir
W atau w Anak panah (cursor) bergerak ke perkataan  seterusnya
E Anak panah (cursor) bergerak ke aksara akhir dalam perkataan tersebut
B Anak panah (cursor) bergerak ke aksara awal dalam perkataan tersebut
{ Anak panah (cursor) bergerak ke awal perenggan
} Anak panah (cursor) bergerak ke akhir perenggan
Jadual 27 : Arahan-arahan papan kekunci untuk perisian VIM

^b Halaman ke atas
^f Halaman ke bawah
^u Gerakan anak panah (cursor) separuh halaman menaik
^d Gerakan anak panah (cursor) separuh halaman menurun
^e Menurunkan baris pada skrin
^y Menaikkan baris pada skrin
Jadual 28 : Arahan-arahan papan kekunci untuk perisian VIM
2. Salin (Copy)
Yy Tekan 2 papan kekunci untuk salin pada baris di mana kedudukan anak
panah (cursor)
Yw Tekan 2 papan kekunci untuk salin pada perkataan
Nyw atau
ynw
N adalah nombor. Tekan 3 yw untuk menyalin sesuatu perkataan pada
lokasi anak panah (cursor) dan juga dua perkataan seterusnya.
Nyy atau
yny
Tekan ‘3 yy’ untuk menyalin seluruh baris tersebut dan baris berikutnya.
P Akan melekatkan perkataan yang disalin pada lokasi anak panah (cursor).
Jadual 29 : Arahan-arahan untuk menyalin fail dalam perisian VIM
3. Padam (Delete)
D  Tekan dahulu kekunci ‘d’, dan:
tekan ‘←’ untuk memadam aksara yang berada sebelum lokasi anak panah
(cursor)
-   tekan ‘→’ untuk memadam aksara di mana anak panah (cursor) terletak.
-   tek an ‘↑’ untuk memadam aksara di mana anak panah (cursor) terletak,
dan yang sebelumnya.
-   tek an ‘↓’ untuk memadam aksara di mana anak panah (cursor) terletak,
dan yang sebelumnya.

Dd Tekan ‘d’ dua kali untuk memadam baris pada anak panah (cursor)
dw  Gerakkan anak panah (cursor) pada aksara yang pertama pada suatu
perkataan, dan tekan ‘dw’ untuk memadam perkataan tersebut. Sekiranya
anak panah (cursor) berada di tengah perkataan, aksara yang berada
selepasnya akan di padam.
Nd ‘n’ adalah nombor. Tekan kekunci ‘3d’ yang bergerak tiga baris ke atas atau
ke bawah.
tekan ‘↑’ untuk memadam aksara di mana anak panah (cursor) terletak, dan
yang sebelumnya. Ini bermakna 4 baris di padam.
Atau tekan ‘↓’ untuk memadam aksara di mana anak panah (cursor) terletak,
dan yang sebelumnya. Ini bermakna 4 baris di padam
Ndd
atau dnd
Tekan kekunci ‘3dd’untuk memadam pada baris di mana anak panah (cursor)
berada dan pada dua baris seterusnya.
D Memadam pada baris selepas kedudukan yang telah anak panah (cursor)
X Memadam aksara di mana anak panah (cursor) berada
X Memadam aksara sebelum kedudukan berada anak panah (cursor) ( d + ←)
Nx Papan kekunci ‘4x’ untuk memadam 4 aksara selepas kedudukan pada anak
panah (cursor) dan aksara di mana anak panah (cursor) di situ.
nX Papan kekunci ‘4x’ untuk memadam sebelum kedudukan pada anak panah
(cursor) tetapi bukan aksara di mana anak panah (cursor) di situ
Jadual 30 : Arahan-arahan untuk memadam fail dalam perisian VIM
4. Baris
^g atau
^G
Tekan pada papan kekunci untuk memaparkan baris nombor pada baris di
mana anak panah (cursor) berada  dan jumlah baris yang terdapat
nG N adalah nombor. Tekan ‘35G’ untuk memasuki baris yang ke 35
Jadual 31 : Arahan-arahan untuk mendapatkan barisan  fail dalam perisian VIM

5. Papan kekunci yang berlainan
R Menukarkan perkataan di mana anak panah (cursor) dengan perkataan yang
baru
U Tekan pada papan kekunci di mana memadam tindakan sebelumnya. Tekan
sekali lagi untuk memadam tindakan tersebut.
Zz Tekan z (2kali) untuk menyimpan dokumen fail dan keluar dari vim
% Pada program kod, perbezaan di antara kurungan yang selalu dibincangkan.
Anda boleh gerakan anak panah (cursor) ke kurungan, nanti tekan pada
papan kekunci untuk mencari maklumat.
Jadual 32 : Arahan-arahan papan kekunci yang berlaianan untuk perisian VIM
6. Melaksanakan baris yang terakhir pada mod
E Melaksanakan fail yang baru, papan kekunci adalah ‘e’ diberi fail baru.
Sebagai contoh, ‘e new file’ dan fail yang baru yang dinamakan name
N Untuk menambahkan fail yang lain iaitu vi, papan kekunci ‘n’ dengan
fail name yang tertentu. Sebagai contoh, taip nfile.txt, dan file.txt  untuk
membaca maklumat
W Untuk menyimpan fail. Jikalau tidak ada spesifik nama fail, anda boleh
menggunakan papan kekunci :w filename.
Q Keluar dari vim, tetapi ia tidak melibatkan apa jua masalah yang
berkaitan dengan fail
q! Keluar dari vim, tanpa menyimpan fail
Wq Menyimpan semua fail dan keluar dari vim
Set nu
command
Tambah baris pada setiap baris yang mengandungi
Set nonu
command
Padam baris nombor
Search
character
Untuk mencari sesuatu aksara di dalam perkataan, papan kekunci adalah
‘/’. Sebagai contoh , papan kekunci :/gz untuk mencari kedudukan g dan
z selepas anak panah (cursor)

Replace
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
