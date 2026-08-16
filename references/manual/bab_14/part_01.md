---
okf_version: 0.1
name: Bab 14 - Bahagian 1
topics: [linux, manual, references, chapter-14]
tags: [noss, dbp]
---
# Bab 14 - Bahagian 1

Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
$ /usr/bin/kppp
Ini akan melarikan tetingkap KPPP
Gambar Rajah 188 ; Tetingkap KPPP
Sebelum anda boleh menggunakan KPPP untuk menyambung ke Internet melalui ISP,
anda perlu membuat konfigurasi. KPPP mudah untuk dikonfigurasikan.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
1. Kali pertama anda mulakan KPPP, klik Setup di tetingkap KPPP.
Gambar Rajah 189 : Tetingkap konfigurasi KPPP
2. Di tetingkap konfigurasi KPPP, pilih Accounts dan klik New.
Gambar Rajah 190 : Skrin penambahan akaun baru untuk KPPP
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
3. Pilih Dialog Setup dan bukan Wizard untuk dikonfigurasi. Wizard Wizard tidak sesuai
jika anda membuat penetapan akaun ISP di Malaysia.
Gambar Rajah 191 : Tetingkap Penetapan akaun baru untuk penyambungan KPPP
Ini akan membuka tetingkap baru. Dalam kebanyakan senario, anda harus mengisi:
/checkbldConnection Name  Anda boleh pilih apa juga sambungan. Contohnya Jaring,
TMNet, Maxis dan sebagainya.
/checkbldPhone Number   Klik pada add untuk tambah nombor dail untuk ISP anda.
/checkbldAuthentication   Pilih PAP/CHAP
/checkbldStore password   Untuk mengingatkan kata laluan tanpa mengisi semula.
/checkbldCustomize pppd.... Mengemaskan lagi  jika anda mahu, jika tidak hanya
gunakan tetapan tersedia (default value).
Selepas mengisi maklumat di atas, anda akan melihat suatu skrin  seperti di bawah.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 192 : Penambahan nombor telefon untuk Pemberian Perkhidmatan Internet
4. Jika anda ingin Linux mengawal selia  masa dan juga kos semasa anda  di dalam
talian, klik Accounting dan pilih Enable Accounting . Selepas itu pilih Malaysia
/TMNet Jaring dari senarai. Klik OK jika selesai.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 193 : Pemilihan ISP untuk mengaktifkan akaun
5. Klik tab Device dan pastikan bahawa tetapan tersedia (default value) untuk Modem
Device adalah  /dev/modem, flow control CRTCTS, Line Termination CR dan
Anda juga boleh klik pada tab Modem untuk menguji modem anda. Klik OK jika
selesai.
6. Ini akan membawa anda ke tetingkap utama KPPP. Masukkan  kata pengguna di
Login ID dan kata laluan di Password dan aktifkan akaun yang baru anda cipta  di
butang Connect.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 194 : Tetingkap penyambungan kepada internet
Klik pada Connect dan anda boleh mula melayari Internet.
Semasa anda dalam talian, anda dapat lihat  masa dalam talian dan juga kos. Jika anda
klik pada Details, anda boleh melihat juga melihat statistik modem.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Pelajaran 23: E-Mel & WWW
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Mukadimah:
Dalam pelajaran ini, penekanan akan diberikan kepada penggunaan beberapa perisian
pelayaran web yang tersedia dalam Linux di samping membincangkan aplikasi pembaca
e-melnya.
Objektif:
1. Mengenali perisian pelanggan e-mel dan kelebihan setiap satunya
2. Mengetahui cara menggunakan Ximian Evolution dan tatacara penetapannya
3. Mengetahui cara menggunakan Mozilla Mail dan tatacara penetapannya
4. Mengetahui cara menggunakan Kmail dan tatacara penetapannya
5. Mengenali perisian pelayaran web dan kelebihan setiap satunya
6. Mengetahui cara menggunakan Mozilla dan tatacara penetapannya
7. Mengetahui cara menggunakan Nautilus dan tatacara penetapannya
8. Mengetahui cara menggunakan Konqueror dan tatacara penetapannya
9. Mengetahui cara menggunakan Galeon dan tatacara penetapannya
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
23 E-MEL & WWW
23.1 Perisian Pelanggan E-Mel
E-mel merupakan suatu saluran untuk berkomunikasi yang masyhur melalui Internet.
Anda boleh menggunakan e-mel dengan perisian pelanggan e-mel, suatu aplikasi yang
mengerti pelbagai piawaian penyiaran  dan membolehkan anda untuk menerima,
menghantar dan membaca e-mel.
Terdapat berbagai aplikasi e-mel di RED HAT Linux seperti perisian pelanggan e-mel
berasaskan grafik  contohnya Evolution dan Mozilla Mail, berasaskan teks Pine dan Mutt
yang boleh memenuhi cita rasa pelbagai pengguna dan setiapnya mempunyai kelebihan
masing-masing.
Di sini, anda akan ditunjukkan bagaimana cara untuk menyedia pakai perisian pelanggan
e-mel tersebut. Pelanggan juga dapat dapat mengetahui cara menghantar e-mel, menerima
e-mel, membaca dan sebagainya. Anda juga dapat melihat bagaimana cara untuk
menyedia pakai dan mengkonfigurasi e-mel tersebut:
-E v o l u t i o n
- Mozilla Mail
- Kmail
23.1.1 Sebelum Anda Memulakannya
Sebelum anda bermula, anda harus mengetahui maklumat-maklumat di bawah
1) Alamat e-mel anda – Anda boleh menghantar dan menerima melseperti berikut
memanda@pulaucendana.net.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
2) Pelayan e-mel (POP atau IMAP server) – Anda boleh menerima mel dari pelayan
dan  juga harus tahu apakah nama pelayan anda dan bagaimana pentadbir
rangkaian atau ISP menggunakannya.
3) Simple Mail Transfer Protocol (SMTP) – protokol ini akan menghantar mesej dari
satu pelayan kepada pelayan yang berlainan melalui Internet. Kebanyakan sistem
e-mel yang menghantar e-mel melalui Internet menggunakan SMTP untuk
menghantar mel dari satu pelayan kepada pelayan yang lain. E-mel tersebut akan
di muat turun  oleh protokol pelanggan e-mel sama ada POP atau IMAP. STMP
juga digunakan untuk menghantar e-mel dari perisian pelanggan e-mel kepada
pelayan e-mel.  Inilah sebab kenapa anda harus menyatakan pelayan POP/IMAP
dan juga pelayan SMTP bila mengkonfigurasi perisian e-mel anda.
IMAP (Internet Message Access Protocol)  adalah protocol untuk memuat turun e-mel
dari pelayan e-mel ISP anda. IMAP berbeza dari POP di mana e-mel dari pelayan IMAP
disimpan di pelayan dan tetap berada di pelayan walaupun anda telah memuat turun dan
membaca e-mel anda manakala mel POP akan dimuat turun terus ke pelanggan e-mel dan
tidak disimpan di pelayan.
TIP : POP (Post Office Protocol) adalah sekumpulan peraturan untuk menghantar e-
mel dari pelayan mel ke petisurat terima e-mel pelanggan e-mel  yakni tempat di mana
e-mel diterima disimpan. Kebanyakan ISP menggunakan protokol POP ada juga yang
men
ggunakan protokol baru IMAP.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
23.2Evolution
Gambar Rajah 195 : Langkah-langkah untuk membuka e-mel
Evolution adalah perisian pelanggan e-mel yang mempunyai ramai pengguna. Pelbagai
kemudahan yang disediakan oleh perisian pelanggan e-mel ini di antaranya ialah
pentadbiran petisurat (mailbox) yang berkesan, penapis mel tetapan pengguna (user-
defined filters) dan pencarian pantas. Sebagai tambahan, ia mempunyai perisian
penjadualan kerja serta kalender yang membolehkan pengguna untuk membentuk dan
menetapkan mesyuarat kumpulan dan acara-acara secara dalam talian. Ia juga merupakan
satu perisian pentadbiran maklumat persendirian dan berkumpulan berfungsi penuh untuk
Linux dan UNIX  dan ia adalah perisian pelanggan e-mel tersedia guna untuk Red Hat
Linux.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
23.2.1 Menyedia Pakai Akaun E-Mel
Untuk melancarkan Evolution, sila klik ke Main Menu > Internet > Email.
Anda akan disajikan dengan  ‘Welcome Screen’ di mana anda boleh mengkonfigurasi e-
mel  anda. Ia adalah proses yang mudah. Cuma ikut arahan di atas skrin dan isikan
dengan maklumat yang anda dapati dari ISP anda di dalam kekotak yang disediakan.
Berikut adalah contoh skrin semasa anda mengisi maklumat.
Gambar Rajah 196 : Skrin untuk mengkonfigurasi program Evolution
1) Klik Next pada skrin selamat datang (welcome screen) untuk menyedia pakai dan
seterusnya isikan nama dan alamat emel pada ruang yang disediakan.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 197 : Melengkapkan informasi identiti pengguna
2) Seterusnya, anda hendaklah memasukkan maklumat di  pilihan  ‘Receiving Mail’.
Di Malaysia, kebanyakan ISP menyokong POP, jadi anda boleh memilih POP
sebagai jenis pelayan (Server Type). Selepas itu, untuk bahagian Host, anda boleh
mendapat maklumat dari ISP, sebagai contoh untuk Jaring adalah mbox.jaring.my
manakala untuk TMNet adalah pop.tm.net.my.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 198 : Melengkapkan informasi pelayan penerima e-mel
3) Selepas itu, anda boleh menggunakan nilai tetapan tersedia (delault values) dan
klik Next.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 199 : Pemilihan masa untuk muat turun e-mel daripada pelayan
4) Selepas ini, anda harus mengkonfigurasi pilihan Sending Email . Di sini, pilih
SMTP untuk jenis pelayan (Server Type) yakni yang biasa di gunakan di
Malaysia. Selepas itu, untuk bahagian Host, anda boleh mendapat maklumat dari
ISP, sebagai contoh untuk Jaring adalah smtp..jaring.my manakala untuk TMNet
adalah smtp.tm.net.my.Untuk nilai yang lain biarkan kepada nilai tetapan tersedia
(delault values). Kemudian klik Next.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
