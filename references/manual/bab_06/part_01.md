---
okf_version: 0.1
name: Bab 6 - Bahagian 1
topics: [linux, manual, references, chapter-6]
tags: [noss, dbp]
---
# Bab 6 - Bahagian 1

14.13.5 Arahan Penapis
Arahan Ulasan
Grep Menulis baris demi baris setiap paten pencarian yang dipadankan
Sort M engisih barisan dalam fail teks
Wc Menulis bilangan bait, perkataan dan barisan dalam fail
Pr Menyediakan fail teks untuk percetakan
Cut Membuang sebahagian baris dalam fail teks
Sed Teks editor jenis aluran
Awk Mengimbas paten dan bahasa proses
Jadual 17 : Arahan penapis
14.13.6 Uba h Hala Input dan Output
Arahan Ulasan
Arahan > fail Ubah hala standard output kepada teks dalam fail
Arahan >> fail Ubah hala standard output kepada teks dalam fail secara tambahan
pada baris terakhir fail
Arahan < fail Ubah hala standard input dari teks dalam fail
Arahan & > fail Ubah hala mesej ralat standard output kepada teks dalam fail
Jadual 18 : Arahan ubah hala input dan output
14.13.7 Aksar a Khas
Aksara Ulasan
& ; ( ) space tab Aksara meta
|| & && ; ;; ( ) |   <baris baru> Operator kawalan
* Kad liar (wild card) untuk satu atau banyak
# Jika digunakan dalam shell ia merujuk kepada hujah
? Kad liar (wild card) untuk satu aksara sahaja
\ Menghapuskan fungsi khas sesuatu aksara
Jadual 19 : Aksara khas (special charactor)

14.13.8 Arahan Pengurusan
Arahan Ulasan
Init Permulaan kawalan proses
shutdown M enutup sistem
Mount Melekap sesebuah sistem fail
umount Menanggalkan sesebuah sistem fail
adduser / useradd Menambah akaun pengguna
deluser Membuang akaun pengguna
Lsmod Memaparkan senarai modul isirung (kernel)
Rmmod Memunggah keluar modul isirung (kernel)
Insmod Memunggah masuk modul isirung (kernel)
modprob Mengawal modul isirung (kernel) secara automatik
Jadual 20 : Arahan pengurusan
14.13.9 Alatan dan Arahan Rangkaian
Arahan Ulasan
ifconfig Mema parkan dan mengubah penetapan antara muka (interface)
rangkaian
Netstat Memaparkan sambungan rangkaian, jadual penghalaan, statistik
antara muka (interface) dan penyamaran sambungan
Route Mempamerkan dan memanipulasi jadual penghalaan
Ping Menghantar paket gema ICMP
iptables Dinding api dan pentadbiran pengurusan sistem
telnet Antara muka (interface) pengguna kepada protokol telnet
ftp / ncftp Antara muka (interface) pengguna kepada protokol ftp
Lynx Pelayar Internet secara teks pelbagai guna
Jadual 21 : Alatan dan arahan rangkaian

14.13.10 Alatan Pemampat dan Arkib
Arahan Ulasan
Gunzip Pengembang fail ekstensi .gz
Gzip Pemampat fail ekstensi .gz
Bunzip2 Pengembang fail ekstensi .bz2
Bzip Pemampat fail ekstensi .bz2
Tar Membuat dan meleraikan arkib ekstensi .tar
Jadual 22 : Alatan pemampat dan arkib

PANDUAN PENGAJAR
Pelajaran 15 : Asas Operasi Cakera

Mukadimah:
Dalam pelajaran ini, anda akan diberikan pemahaman untuk menjalankan operasi cakera
asas dalam Linux. Banyak konsep-konsep asas seperti membaca cakera padat (CD-ROM)
dan cakera liut (Floppy Drive) diperkenalkan di sini. Ini merupakan asas penting dan
pokok yang perlu dikuasai oleh semua pengguna Linux.
Objektif:
1. Memahami struktur cakera dalam Linux dan seterusnya mampu menyatakan
kenapa lipatan-lipatan tersebut hadir dalam sistem fail Linux
2. Mengetahui bagaimana proses membaca cakera keras dalam Linux
3. Mengetahui bagaimana proses membaca cakera liut dalam Linux
4. Mengetahui bagaimana proses membaca cakera padat (CD-ROM) dalam Linux

15 OPERASI CAKERA  ASAS
15.1 Memahami Struktur Cakera Linux
Dalam persekitaran Microsoft Windows, kita sudah biasa dengan konsep ‘drive letters’
dan ‘logical and physical drives’. Walaupun cakera liut (floppy disk), cakera keras (hard
disk) dan cakera padat (CD-ROM) adalah alat yang berbeza, jurutera perisian Microsoft
telah menyediakan hampir sama ‘look-and-feel’ untuk alat storan ini. Walaupun perisian
rangkaian Microsoft melanjutkan ‘look-and-feel’ itu, pengguna di situ boleh
menyambungkan alat storan yang dilekatkan ke komputer yang berbeza dan masih
menggunakan konsep yang sama bagi ‘drive letter’, mengandungi sub-direktori.
Linux menyusun direktori dan fail dalam corak yang sangat biasa, kecuali direktori dan
fail penting. Pertama sekali, seperti yang anda sudah baca, sistem operasi menggunakan
forward slashes (\) untuk mewakilkan aksara istimewa (special charactor) manakala
Linux menggunakan back slashes (/) untuk mengasingkan fail dan direktori dan
pembahagiannya. Kedua, tiada ‘drive letter’ di sana. Sebagai gantinya, setiap
pembahagian cakera keras, setiap cakera liut, CD ROM, Zip, dan sebagainya akan
muncul menjadi direktori dalam struktur cakera tunggal (single disk).
15.2 Bermula Dengan Cakera Keras
Andaikan anda memiliki PC dengan pembahagian cakera keras yang besar di mana
Linux, iaitu program dan data anda ditempatkan. Andaikan juga yang cakera keras
mengandungi direktori yang dinamakan /etc, /bin, /usr, /sbin, /home dan etc. Kita boleh
memetakan struktur direktori sebagai bentuk di bawah:
Gambar Rajah 148 : Struktur Direktori

Struktur yang paling atas adalah nama direktori yang mudah “/” (disebut sebagai ‘root’).
Sebagai direktori ‘root’ dalam sistem operasi Linux, anda boleh menempatkan kedua-dua
fail dan direktori dalam ‘root’. Jika anda melihat dalam salah satu daripada direktori sub,
anda akan jumpa di mana sistem operasi Linux, anda boleh membina direktori sub di
dalam direktori sub, untuk apa sahaja tahap kompleksiti yang anda ingini. Arahan Linux
menunjukkan direktori adalah ls. Anda boleh memaparkan kandungan direktori ‘root’
dengan menaip :ls /.
Setiap direktori dalam Linux mempunyai tujuannya yang tersendiri. Jadual di bawah
secara ringkasnya menerangkan setiap kandungan direktori, dan apa kegunaannya.
Direktori Penerangan dan kegunaan
/ (direktori ‘root’) Ini adalah direktori ‘root’  bagi semua direktori dam pembahagian
dalam Linux. Ini adalah pertama diletakkan dalam proses ‘boot’.
/ bin Mengandungi alatan dan perlaksanaan fail untuk semua pengguna
sistem. Mesti dalam sama fail iaitu “/”.
/sbin Mengandungi alatan dan perlaksanaan fail untuk digunakan oleh
pentadbir sistem ( biasanya adalah ‘root’). Mesti dalam sama
sistem fail iaitu “/”.
/
home
var
var
dev
proc
boot
sbin
bin
mnt
etcusr
tmp
lost + found
lib

/etc Mengandungi ‘sy stem-wide configuration file’. Mesti berada
dalam sama sistem fail iaitu “/”.
/lib Mengandungi ‘library’ y ang digunakan dalam sistem Linux. Mesti
berada dalam sama sistem fail iaitu “/”.
/mnt Bi asanya digunakan iaitu ‘placeholder’ untuk semua ‘mount
points’ diperlukan untuk ‘mounting non-standard file system’.
Sebagai contoh, /mnt /floppy untuk cakera liut, dan /mnt /cdrom
untuk ‘CD ROM drive’. Mesti berada dalam sama sistem fail iaitu
“/”.
/dev M engandungi fail yang istimewa di mana ia memaparkan
perkakasan dalam sistem anda, atau apa yang disebut- fail alat
(device files). Mesti berada dalam sama sistem fail iaitu “/”.
/root Ini adalah ‘default home directory’ untuk pengguna ‘root’.
/proc Ini adalah sistem fail secara maya di mana wujud hanya dalam
imaginasi bagi isirung (kernel). Ia digunakan untuk akses struktur
data isirung (kernel). Ia dibina secara automatik setiap hari semasa
‘boot’ sistem dan tidak boleh dipadamkan.
/boot Mengandungi fail statik digunakan semasa proses “boot” (pemuat
‘boot’ Linux), termasuk imej isirung (kernel) dan fail lain yang
berkait dengan urutan ‘boot’ Linux. Ini boleh jadi pada sistem fail
yang dibahagikan dari “/”.
/home Biasanya ia adalah direktori ‘home’ bagi semua pengguna dalam
Linux, kecuali untuk ‘root’. Dalam /home, setiap pengguna ada
direktori mereka sendiri, dikenal pasti dengan menggunakan nama
pengguna mereka sendiri. Sering kali ia adalah pembahagian yang
paling besar. Ini boleh jadi pada sistem fail yang dibahagikan dari
“/”.
/tmp Digunakan sebagai ruang storan sementara untuk program dan
semua pengguna pada sistem itu. Ini boleh jadi pada sistem fail
yang dibahagikan dari “/”.

/usr M engandungi arahan pengguna, ‘libraries’, kod sumber, dan
dokumentasi. Direktori ini biasanya agak besar. Ini boleh jadi pada
sistem fail yang dibahagikan dari “/”.
/var Mengandungi semua fail log, dan fail gelendong (spool) yang
dihasilkan oleh Linux. Ini boleh jadi pada sistem fail yang
dibahagikan dari “/”.
Jadual 23 : Penguraian direktori
Linux menamakan fail dan direktori sedikit berbeza daripada MS Windows. Diingatkan
bahawa semua fail dan direktori, bahkan alatan dalam Linux kelihatan seperti fail (atau
nama fail). Jadual di bawah menunjukkan sesetengah nama alat Linux.
Alat Kebiasaan Linux
A:(Cakera Liut ) /dev/fd0, /dev/floppy
B:(Cakera Liut) /dev/fd1
Papan Kekunci /dev/tty
‘Master drive’ pada IDE yang utama /dev/had
Pembahagian yang pertama pada ‘master
drive’ (‘hard disk’)
/dev/hda1
Pembahagian yang kedua pada ‘master
drive’ (‘hard disk’)
/dev/hda2
‘Slave drive’ pada IDE yang utama /dev/hdb
‘Master drive’ pada IDE yang kedua /dev/hdc
‘Slave drive’ pada IDE yang kedua /dev/hdd
CAKERA PADAT (CD-ROM) /d ev/cdrom, atau /dev/hdb (‘slave drive’
pada IDE kedua)
Modem /dev/modem
Kad Bunyi /dev/sound, /dev/dsp
Jadual 24 : Direktori-direktori untuk komponen komputer

15.3 Menggunakan Cakera Liut
Cakera liut (floppy disk) adalah sekali satu komponen yang standard dalam komputer
kini. Tetapi bagaimana anda menggunakannya dalam Linux? Terdapat beberapa langkah
yang perlu anda ambil sebelum anda boleh mengakses cakera liut (floppy disk) dalam
Linux. Ia tidak seperti cara anda mengakses cakera liut (floppy disk) dalam MS
Windows, tapi anda perlu mengetahui cara mengakses cakera liut (floppy liut) dalam
Linux.
Di sini ada beberapa langkah untuk mengakses cakera liut:
Langkah 1     Penggunaan arahan “mount” untuk melampirkan pemacu cakera liut
(floppy disk drive) kepada direktori sub dibina dalam langkah 1:
# mount ±t vfat /dev/fd0 /mnt/floppy
atau
# mount ±t msdos /dev/fd0 /mnt /floppy
Nota: Nama alat bagi pemacu cakera liut (floppy disk drive) adalah /dev /fd0. Jika anda
mempunyai lebih dari satu pemacu cakera liut (floppy disk drive) (contohnya, dua
pemacu cakera liut (floppy disk drive)), kemudian pemacu cakera liut (floppy disk drive)
yang pertama akan menjadi /dev/fd0 dan pemacu cakera liut (floppy disk drive) yang
kedua akan menjadi /dev/fd1.
Langkah 2 Ubah direktori ke dalam direktori sub, dan anda boleh akses kandungan
dalam cakera liut:

#  ls /mnt/floppy
Selepas anda membina, memadam atau mengubah kandungan dalam /mnt/floppy, anda
perlu menyimpan pengubahsuaian anda:
Langkah 3 Jika anda sudah selesai menggunakan cakera liut (floppy disk) tadi atau
anda mahu menukar cakera liut (floppy disk), anda perlu menulis
kandungan kembali ke cakera liut (floppy disk) dan tidak melampirkannya
dari sub-direktorinya :
# umount /mnt/floppy
Nota: Ini akan menulis semua perubahan yang telah anda buat dalam /mnt/floppy kembali
ke dalam /dev /fd0 (cakera liut anda).
Langkah 4 Ulangi Langkah 1 jika anda perlu akses cakera liut (floppy disk) yang lain.
15.4 Memasang Pemacu Cakera Padat (CD-ROM drive)
Menambah cakera padat (CD-ROM) kepada sistem adalah sama seperti menambah satu
pemacu cakera liut (floppy disk drive) ke dalam sistem. Hanya sebelum, anda mesti
memasang cakera padat (CD-ROM) sebelum 
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
