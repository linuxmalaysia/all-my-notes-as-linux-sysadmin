---
okf_version: 0.1
name: Bab 3 - Bahagian 1
topics: [linux, manual, references, chapter-3]
tags: [noss, dbp]
---
# Bab 3 - Bahagian 1

Oleh itu satu kaedah yang betul dan tepat ialah dengan mengumpulkan seberapa banyak
maklumat berkenaan sistem perkakasan anda terlebih dahulu. Adalah menjadi tabiat yang
elok jika anda membaca panduan yang diberikan oleh pembekal terlebih dahulu ataupun
membuka sarung CPU untuk melihat perkakasan anda dengan lebih dekat. Sentiasa
pastikan anda mematuhi peraturan anti-statik dan mengenakan kaedah yang betul
sewaktu melakukannya.
• Cakera
Pastikan anda mengetahui jumlah sebenar saiz HDD anda (dalam Mbyte) dan
bilangan silinder HDD tersebut. Sekiranya anda mempunyai lebih dari satu HDD,
pastikan anda mengetahui yang mana merupakan Master dan slave. Kaedah
melabel adalah satu praktis yang baik sekiranya anda mempunyai lebih dari satu
HDD yang sama saiz dan model pengeluar.
• Memori
Jumlah memori RAM anda (contohnya 64Mb, 512 Mb)
• Pemacu Cakera Padat (CD-ROM drive)
Jenis antara muka (IDE atau SCSI)
• Tetikus
Jenis penyambung tetikus anda adalah penting seperti PS/2 atau serial. Jika serial,
di port manakah ianya diletakkan. Bilangan butang yang ada pada tetikus anda
juga adalah penting. Mempunyai tetikus 3 butang memberikan kelebihan dalam
menggunakan aplikasi X Windows.
• Video
Model pengeluar, cip video dan jumlah video RAM yang anda ada
• Monitor

Model pengeluar, frekuensi monitor dan nisbah kebolehan kadar segar semula
secara melintang dan menegak. Biasanya maklumat ini dapat diperolehi dari label
di belakang monitor anda.
• Kad Eternet
Pengeluar dan model cip (contohnya Dlink DFE-538TX 10/100 Adapter), anda
juga seharusnya mengetahui alamat MAC terutamanya jika anda memerlukan
sistem “boot” (booting sistem) dari rangkaian. Alamat MAC ini dapat diperolehi
dengan cara melihat kepada label di NIC tersebut, alamat MAC ini terdiri dari 12
oktet (48bit) contohnya 00:08:0D:CC:E5:33, tiga bahagian pertama oktet ini
mewakili informasi pengeluar dan keseluruhannya mewakili alamat perkakasan
NIC tersebut. Mengetahui alamat IP perumah, alamat IP penghala, netmask dan
alamat IP pelayan nama juga adalah perlu jika anda bercadang untuk
menyambungkan PC anda ke rangkaian setempat (LAN) anda. Merujuk kepada
pengendali sistem merupakan perkara bijak yang boleh anda lakukan untuk
mendapatkan maklumat yang diperlukan berkenaan rangkaian setempat anda.
• Pencetak (printer)
Model pengeluar dan port di mana ia disambungkan (kebiasaannya LPT1). Jika
anda menggunakan pencetak (printer) rangkaian, pastikan anda tahu alamat IP
atau DNS serta protokol yang disokong oleh pencetak (printer) tersebut.
• Modem
Model pengeluar, kelajuan maksimum, dan port di mana ia disambungkan
(sekiranya modem luaran)
Beberapa peralatan tambahan seperti alat pengimbas, CDR dan kad TV juga serasi
dengan Linux. Namun anda tetap dinasihatkan supaya memastikan keserasiannya dengan
Linux melalui Senarai Keserasian yang boleh diperolehi dari tapak web Red Hat. Secara
amnya, anda perlu mempunyai ruang yang cukup untuk isirung (kernel) Linux anda dan

perisian aplikasi yang anda ingini. Kebanyakan pengguna akan melakukan salah satu dari
3 keadaan di bawah ini:
1. Linux merupakan satu-satunya sistem operasi yang ada di dalam cakera anda.
2. Linux dan satu atau lebih sistem operasi di dalam cakera yang sama.
3. Linux dan sistem operasi lain berada di dalam cakera yang berlainan tetapi masih
dalam satu sistem yang sama.
Sekiranya anda melakukan pilihan kedua iaitu Linux dan sistem operasi lain berada di
dalam cakera yang sama, anda perlu memastikan cakera anda telah dipecahkan kepada
pecahan yang secukupnya. Jika tidak anda perlu membuat perubahan ke atasnya.
Bahagian seterusnya akan memerihalkan pengubahsuaian pecahan ini dengan mengambil
kira sistem operasi selain dari Linux ialah Windows.
13.3 Mengubah Sekatan Dengan FIPS
Terdapat utiliti dari sumber terbuka yang dikenali sebagai fips yang mampu mengubah
penyekatan cakera untuk membolehkan anda memberi ruang untuk memuatkan Linux di
dalam sistem anda. Namun aplikasi ini hanya akan berfungsi kepada sekatan jenis FAT
sahaja dan tidak berfungsi untuk sekatan jenis NTFS. Sekiranya anda perlu mengubah
sekatan NTFS, anda dinasihatkan menggunakan aplikasi Partition Magic ataupun aplikasi
sumber terbuka
Sebelum anda mengubah sekatan cakera anda, pastikan anda melakukan tugasan ini di
dalam sistem Windows anda terlebih dahulu:
1. Salin duakan semua data penting ke dalam media salinan yang lain.
2. Larikan aplikasi scandisk
3. Larikan aplikasi defragmant

Setelah anda bersedia, anda boleh mulakan proses yang paling bahaya ini:
1. Buat satu cakera liut but untuk sistem Windows anda.
2. Salin semua fail di dalam /dosutils/fips/ dari CD 1 Red Hat anda kepada cakera
liut but tersebut.
i. /dosutils/fips20/fips.exe
ii. /dosutils/fips20/restorrb.exe
iii. /dosutils/fips20/errors.txt
iv. /dosutils/fips20/fips.doc
v. /dosutils/fips20/fips.faq
3. Rebut sistem anda dan masukkan cakera liut tersebut ke dalam pembaca cakera
liut anda.
4. But sistem anda dengan menggunakan cakera liut tersebut.
5. Pada prom DOS tersebut, taipkan fips
6. Apabila fips telah dilarikan, anda akan melihat informasi
7. Tekan apa sahaja butang di papan kekunci untuk meneruskan operasi
8. Tekan butang “y” pada papan kekunci untuk membuat salinan sektor “boot”
Kemudian anda akan diberikan soalan, jawab “y”
9. Setelah sektor “boot” disalin ke dalam cakera liut but anda, anda akan ditanya
soalan lagi
10. Nilai yang diberikan merujuk kepada ruang kosong yang akan dibuat ke atas
cakera. Tekan butang arah-kanan pada papan kekunci untuk menambahkan saiz
pecahan (FAT, Windows) dan mengecilkan saiz pecahan kosong (untuk Linux)
sehingga anda mencapai keluasan pecahan yang dikehendaki, dan tekan Enter.
Periksa pilihan yang telah anda buat sekali lagi.
11. Jika anda ingin mengubah saiz tersebut, tekan r; atau tekan c untuk meneruskan
proses ini.
12. Anda akan diberikan pilihan seperti di bawah, tekan y untuk mengakhiri pilihan
dalam proses ini.

13. Jika tiada masalah yang berlaku, anda akan memperoleh dua sekatan; satu untuk
Windows dan satu lagi sekatan kosong yang membolehkan anda memuatkan
Linux.
14. “Reboot” sistem anda dan anda sepatutnya mampu memasuki sistem Linux anda
tanpa sebarang masalah.
Jika sekiranya Windows anda tidak boleh didirikan selepas proses pemecahan dengan
fips, anda boleh mengundurkan kesilapan anda dengan melarikan arahan restorrb.exe
melalui disket but yang telah anda buat tadi. Keadaan terburuk yang mungkin terjadi
ialah anda terpaksa memuatkan sistem anda dengan Windows sekali lagi dan
menyimpan semula semua data yang telah anda salin duakan.
New boot sector:
Boot sector:
Bytes per sector: 512
Sectors per cluster: 8
Reserved sectors: 1
Number of FATs: 2
…….
……………..
…………………
Checking boot sector … OK
Ready to write new partition scheme to disk
Do you want to proceed (y/n)?

13.4 Kaedah Menginstalasi
Untuk menuju ke sesuatu destinasi yang sama kadangkala kita mempunyai pelbagai
pilihan. Pilihan ini biasanya bergantung kepada keadaan sekeliling dan keperluan kita.
Linux juga ada menyediakan pelbagai pilihan untuk kita melakukan proses pemuatan.
Persoalannya yang manakah lebih sesuai?
Ringkasnya terdapat 4 mod pemuatan, iaitu pemacu cakera padat (CD-ROM drive),
pemacu cakera keras (Hard Disk Drive), tapak FTP dan pelayan NFS. Kaedah pemuatan
dari pemacu cakera padat (CD-ROM drive) merupakan kaedah paling senang dan
popular, bahkan kita akan meneruskan pemuatan kita dengan menggunakan kaedah ini.
Untuk itu anda seharusnya mempunyai cakera padat (CD-ROM) pemuat yang mampu
di”boot”kan secara automatik untuk mempermudah proses pemuatan.
Sistem berasaskan Intel/IBM memerlukan cakera liut “boot” (bootable floppy disk) dan
cakera liut tambahan (additional floppy disk) jika menggunakan PCMCIA. Kebanyakan
PC sekarang mampu “boot” dari pemacu cakera padat (CD-ROM), oleh itu anda tidak
perlu risau akan kaedah dan keperluan untuk membuat cakera liut “boot” (bootable
floppy disk) ini. Selain itu untuk membuat cakera liut ‘boot” (bootable floppy disk), anda
besar kemungkinan anda terpaksa menggunakan DOS atau Windows, dan ini adalah
suatu perkara yang kurang kita gemari bukan?
Kita tidak akan membincangkan dengan lebih lanjut mengenai tiga lagi mod pemuatan
untuk kali ini, namun jadual di bawah menunjukkan perbandingan antara kaedah mod
pemuatan.

Kaedah Muat
Cakera liut Boot
(Bootable Floppy
Disk)
Cakera liut Tambahan
(Additional Floppy
Disk)
Nisbah Kelajuan
CDROM  Tidak diperlukan  Tidak diperlukan  Cepat & Mudah
Cakera Keras  Tidak diperlukan  Diperlukan  Cepat
NFS  Tidak diperlukan  Diperlukan  Sederhana
FTP  Tidak diperlukan  Diperlukan  Lambat
HTTP  Tidak diperlukan  Diperlukan  Paling Lambat
Jadual 9 : Perbandingan Kaedah Muat yang dibenarkan dalam Red Hat Linux
13.4.1 Meneruskan Mod Pemuatan Bergrafik Pemacu Cakera Padat
(CD-ROM Drive)
1. Hidupkan komputer anda.
2. Tekan CTRL+ALT+ESC atau F2 atau DEL (sila semak dokumentasi mengubahsuai
penetapan BIOS anda).
3. Pastikan komputer anda ditetapkan untuk “boot” melalui CDROM sebagai pilihan
pertama dan aktifkan penetapan baru tersebut.
4. Masukkan cakera padat (CD-ROM)  Red Hat Linux yang pertama dan kemudian ulang
“boot” (reboot) komputer anda.
5. Setelah beberapa ketika, anda akan “boot” dari pemacu cakera padat (CD-ROM)
tersebut dan dipaparkan menu pemuatan di bawah. Sebenarnya sebaik sahaja anda

menghidupkan Komputer anda, BIOS akan melakukan proses yang dinamakan
Kekuasaan Cuba Lengkap (POST), proses POST ini akan membaca semua konfigurasi
yang telah anda tetapkan sebelum ini, maka ia akan cuba mencari rekod “boot” dari
CDROM. Setelah itu anda akan dibawa kepada Skrin 1 seperti di bawah.
Kita akan meneruskan dengan mod Umum dengan hanya menekan butang <ENTER>
pada papan kekunci dan tunggu sehingga anda di alu-alukan oleh proses pemuatan
dengan kata-kata seperti selamat datang ke Red Hat Linux 9.
Berbeza dengan OS lain, Linux telah menunjukkan kelebihannya sejak di peringkat
pemuatan lagi. Linux menyediakan 6 skrin konsol untuk pengguna melihat segala
perubahan yang sedang dilakukan sewaktu pemuatan. Kebiasaannya, anda tidak perlu
berubah dari konsol asal (Konsol Maya #7) ke konsol lain, melainkan untuk melakukan
diagnostik masalah yang timbul sewaktu proses pemuatan. Namun yang demikian
sebagai seorang pengguna Linux yang sentiasa ingin mempunyai pengetahuan yang
mendalam anda bolehlah kerap bertukar konsol untuk memastikan anda tahu apa yang
sedang dilakukan oleh program pemuatan (Anaconda) ke atas sistem anda.
- To install or upgrade Red Hat Linux in graphical mode,
press the <ENTER> key.
- To install or upgrade Red Hat Linux in text mode, type:
linux text <ENTER>.
- Use the function keys listed below for more information.
[F1-Main]     [F2-Options]     [F3-General]     [F4-Kernel]     [F5-Rescue]
boot:
Gambar Rajah 132 : Kekotak Dialog Pemilihan Mod

Konsol  Kekunci Kombo  Ulasan
1  Ctrl + Alt + F1  Kekotak dialog pemuatan
2  Ctrl + Alt + F2  Pengesa Shell
3  Ctrl + Alt + F3  Mesej dan log pemuatan
4  Ctrl + Alt + F4  Mesej berkaitan sistem
5  Ctrl + Alt + F5  Mesej-mesej lain
7  Ctrl + Alt + F7  Skrin grafik X, jika anda memilih kaedah muat bergrafik
Jadual 10 : Penghuraian fungsi kek
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
