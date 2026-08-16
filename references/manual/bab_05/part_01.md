---
okf_version: 0.1
name: Bab 5 - Bahagian 1
topics: [linux, manual, references, chapter-5]
tags: [noss, dbp]
---
# Bab 5 - Bahagian 1

bahkan menggugurkan akaun pengguna lain. Pemuatan aplikasi juga perlu dilakukan
melalui pengguna ini. Biasanya akaun ini diberikan kepada pengendali sistem tersebut.
14.1 Mengubah Kedudukan Melalui Arahan cd
Arahan cd merupakan arahan asas yang digunakan bagi membolehkan pengguna untuk
bergerak dari satu tempat ke tempat lain di dalam sistem Linux. Pengguna akan berada di
lipatan perumah  (home direktory) selepas mereka log masuk (login) ke dalam sistem
Linux. Nama direktori itu bermula dengan /home dan diikuti dengan akaun pengguna.
Sebagai seorang pengguna Linux anda boleh berhijrah ke direktori lain hanya dengan
menggunakan arahan dan diikuti dengan pathname. Sebagai contoh anda boleh berpindah
ke /usr/bin direktori dengan menggunakan arahan:
# cd /usr/bin
dari direktori itu untuk berpindah ke /usr direktori anda boleh menggunakan arahan:
# cd ..
atau semasa anda berada di direktori /usr/bin,anda boleh maju 2 langkah ke atas sehingga
root direktori dengan menggunakan arahan:
# cd ../..
Pada bila-bila masa, anda boleh kembali ke home direktori dengan arahan:
# cd atau
# cd ~

14.2 Mengetahui Kedudukan Melalui Arahan pwd
Dengan menggunakan arahan pwd anda boleh mengetahui di mana anda berada di dalam
sistem dan arahan itu juga membolehkan anda untuk mencetak direktori yang sedang
anda gunakan secara aktif. Seperti contoh semasa anda larikan arahan seperti di bawah:
# cd /usr/bin
dan taip:
# pwd
anda akan dapat melihat:
/usr/bin
Ada kemungkinan pwd yang anda gunakan itu berasal dari  arahan terbina dalam shell.
Anda akan mendapat satu mesej ralat jika anda menggunakan arahan:
# pwd -help
Arahan yang sepatutnya digunakan adalah:
# /bin/pwd -help
Arahan pwd di atas dilarikan pwd dari direktori /bin dan bukan pwd yang sedia ada di
dalam shell.

14.3 Penyenaraian Direktori Dengan Arahan ls
Arahan ls merupakan salah satu program yang mempunyai penggunaan yang sangat
tinggi. Ia boleh digunakan untuk "list out" fail-fail dan sub-direktori di dalam sistem.
Gambar Rajah 144 : Penyenaraian direktori dengan arahan “ls”
Anda juga boleh senaraikan fail-fail di dalam satu baris diasingkan dengan koma,
menggunakan pilihan -m
# ls -m
Gambar Rajah 145 : Penyenaraian direktori dengan arahan “ls –m”
Jika anda inginkan fail-fail untuk disusun secara mendatar,gunakan pilihan -x:

# ls ±x
Gambar Rajah 146 : Penyenaraian direktori dengan arahan “ls –x”
Jika anda ingin menyenaraikan kesemua fail-fail dan sub-direktori di direktori semasa
termasuk fail tersembunyi, anda boleh pilihan -a seperti berikut:
# ls -a
Jika anda ingin mengetahui lebih banyak mengenai direktori semasa, saiz fail, pemilik
fail dan sebagainya,anda boleh menggunakan  arahan:
# ls -l
Arahan ls boleh digunakan untuk melihat isi kandungan direktori lain dengan
menentukan direktori atau "pathname" di arahan shell. Sebagai contoh, untuk melihat
kesemua fail-fail di /usr/bin direktori, anda boleh menggunakan arahan yang berikut:
# ls /usr/bin
Jika anda ingin mencari hanya fail ekstensi .txt, anda boleh menggunakan arahan berikut:

# ls *.txt
Dari sini jika anda ingin melihat keseluruhan fail-fail di dalam sistem,anda boleh
menggunakan ls-R. Ini akan membolehkan sistem untuk memaparkan keseluruhan isi
kandungan. Proses ini mungkin akan mengambil beberapa saat.
14.4 Memaparkan Kandungan dan Menggabungkan Fail
Dengan cat
Anda boleh menggunakan cat (concatenate) arahan untuk membolehkan isi kandungan
fail-fail dipaparkan di kaca monitor. Anda juga boleh menggunakan arahan ini untuk
menghantar satu isi kandungan fail kepada fail yang lain dengan menggunakan output
“redirector operator" contohnya ">" atau ">>".
Kami akan menunjukkan beberapa kegunaan arahan asas cat yang sangat berguna apabila
ia digunakan untuk membaca fail-fail pendek, ia juga boleh digunakan untuk
menyambung, membina, tulis ganti atau menambah kandungan fail-fail.
Untuk melihat kandungan fail-fail ringkas (short file), anda boleh menggunakan arahan
seperti berikut:
# cat test.txt
Gambar Rajah 147 : Melihat kandungan fail dengan arahan “cat”

Terdapat beberapa pilihan untuk menggunakan arahan cat. Untuk melihat fail-fail dalam
turutan mengikut nombor,anda boleh menggunakan pilihan -n seperti yang ditunjukkan di
bawah:
# cat -n test.txt
Anda juga boleh menggunakan cat untuk melihat beberapa fail dalam satu masa, kerana
ia menerima "wildcards". Contoh penggunaan "wilcard" * adalah seperti tertera di bawah:
# cat -n test*
cat juga boleh digunakan dengan "redirect operator" (>) untuk menggabungkan fail-fail.
Katakan anda ingin gabungkan test.txt dan test2.txt,anda boleh menggunakan :
# cat test* > test3.txt
Selain daripada itu,anda juga boleh mencuba menggunakan arahan seperti:
# ls - test*
# cat test.txt >> test2.txt
# cat test2.txt
# cat -n test.txt >> test2.txt
# cat -test2.txt

14.5 Membaca Fail Dengan more
Arahan more merupakan salah satu arahan daripada keluarga Linux yang dipanggil
"pagers". "Pagers" membolehkan anda untuk melayari fail-fail dan membacanya "screen
by screen" atau "line at a time".
more merupakan alat kelui (pager) tradisional yang memberi ciri-ciri alat kelui (pagers)
yang awal. Salah satu penggunaan arahan more adalah seperti berikut:
# more longlife.txt
Jika anda memerlukan bantuan (Help), tekan H. Anda juga boleh memberikan arahan lain
semasa menggunakan more, ini boleh dibuat dengan menggunakan tanda seruan (!).
Adalah mudah untuk membaca fail teks paparan demi paparan  (text file screen by
screen), ini boleh dilakukan dengan menekan langkauan (spacebar) dan untuk undur ke
belakang tekan "B".
more juga mempunyai beberapa "arahan-line options". Sebagai seorang pengguna, anda
boleh "customise" skrin prom, menentukan saiz, menggunakan "multiple filename" atau
"wildcard" dan sebagainya.
14.6 Membaca Fail Dengan less
Arahan less adalah lebih kurang sama dengan more. Ia merupakan salah satu daripada
arahan "pager". Kelebihan less jika dibandingkan kepada more adalah seperti berikut:
• Pengguna boleh pergi ke hadapan dan ke belakang ketika menggunakan fail teks
dengan bantuan kekunci anak panah (cursor).
• Pengguna boleh menggemudi sebahagian daripada file dengan menyatakan
"bookmarks", "line numbers" atau peratusan dari fail yang hendak dikemudikan.

• Arahan less tidak akan "quit" sekiranya anda sudah sampai kepada penghujung
fail.
• Pengguna mempunyai pilihan untuk melakukan pencarian kompleks, "pattern
option" dan "highlighting" melalui beberapa fail
• Arahan less juga memberikan kepelbagaian pilihan,ini termasuk "key setup
program" lesskey ini membolehkan anda untuk "customise key to control less
arahan".
• "Keystrokes" adalah sesuai digunakan dengan program "word processing" seperti
emacs.
• Prom maklumat terletak pada dasar screen, ia mudah untuk "dicustomkan" dan
juga ia mempunyai banyak maklumat.
• Semasa proses pemuatan Linux, less merupakan "default pager" yang digunakan
oleh beberapa program seperti man arahan.
14.7 Mencari Fail Dengan find
Arahan find merupakan satu utiliti yang sangat berkuasa  yang membolehkan anda untuk
mencari fail-fail di dalam cakera anda.
Katakan anda ingin mencari ispell arahan dalam /usr direktori,anda boleh menggunakan:
# find /usr -name ispell -print
Anda juga boleh mencari fail-fail mengikut tarikh atau menggunakan "time period".
Sebagai contoh, katakan anda ingin mencari program di /usr/bin direktori yang anda tidak
guna lebih daripada 50 hari. Arahannya adalah seperti berikut:
# find /usr/bin -type f -atime +50 -print
Pilihan -atime yang diikuti dengan bilangan hari

Pilihan -mtime yang diikuti dengan bilangan hari mencari fail yang telah diubah suai.
Sebagai contoh,anda ingin mencari fail yang telah diubah suai di dalam tempoh 24 jam
yang lalu. Arahannya adalah seperti berikut:
# find /usr/bin -type f -mtime -1 -print
Arahan find juga boleh menerima "wildcards" di dalam "search strings". Contohnya, anda
boleh menggunakan find untuk menunjukkan kesemua "PostScript" fail didalam /usr
direktori. Arahannya seperti:
# find /usr -name ' *.ps' -print
Satu lagi kegunaan find ialah -xdev. Ia membolehkan carian dibuat di dalam lingkungan
fail semasa. Tanpa -xdev, find akan mencari keseluruhan cakera dan juga CAKERA
PADAT (CD-ROM). Ini akan memperlahankan proses pencarian dan kemungkinan akan
mencari fail yang tidak berkenaan.
Dengan menggunakan -xdev anda boleh hadkan pencarian kepada hanya pecahan
Windows. Untuk mencari kesemua fail yang berakhir dengan .sys di dalam "mounted
Windows Partition" di dalam /mnt/dos direktori, anda boleh gunakan arahan yang
berikutnya:
# find  /mnt/dos -name *.sys -print ±xdev

14.8 Mencari Fail Sistem Dengan whereis
Sebagai tambahan kepada arahan find, terdapat satu lagi cara untuk mencari fail-fail
sistem secara pantas. Arahan whereis dengan pantas mencari fail-fail dan menunjukkan
fail binari, fail sumber dan manual.
Sebagai contoh :
# whereis find
find:/usr/bin/find/usr/lib/find/usr/man/find.1.gz
sebagai seorang pengguna anda mungkin menggunakan whereis untuk hanya mencari
halaman man (manual) daripada program:
#whereis -m find
find: /usr/man/man1/find.1.gz
Jikalau whereis tidak dapat mencari apa yang anda kehendaki, anda akan mendapat
kembali "string" seperti berikut:
#whereis foo
foo:
14.9 Mencari Fail Dengan locate
Arahan locate merupakan arahan yang lebih cepat daripada whereis. Ia menggunakan
pangkalan data yang dinamakan slocate berdasarkan inode setiap fail. Ia menjimatkan
masa kerana ia mencari hanya satu pangkalan data sahaja. Ia akan pergi terus kepada
pangkalan data slocate dan mencari fail yang dikehendaki.

Contoh Arahan:
# locate *.ps
Fail-fail akan dipaparkan di skrin. Ia berfungsi lebih pantas dari find dan whereis, tetapi
ia memerlukan pangkalan data untuk semua fail-fail yang ada di sistem.
Selepas pemuatan Linux, pangkalan data slocate dibina di direktori /var/run. Untuk
menghasilkan versi terbaru slocate, anda harus menggunakan arahan updatedb seperti di
bawah. Sebelum itu anda harus "login" sebagai “root operator”.
# updatedb
Proses ini mungkin akan mengambil beberapa minit. Gunakan man locate untuk
mendapatkan bantuan menggunakan locate.

14.10 Mencari Fail Dengan apropos
Arahan ini membolehkan anda untuk mencari fail yang mengandungi perkataan, di mana
anda mungkin telah lupa nama fail ataupun lokasi fail.
# apropos search
Anda akan menerima "list" program daripada pangkalan data whatis di skrin. Arahan
apropos menggunakan pangkalan data untuk mencari kata kunci yang telah anda
masukkan.
14.11 Mendapatkan Bantuan Dengan whatis
Arahan ini membolehkan anda untuk mengetahui secara pantas akan kebolehan sesuatu
program dengan memaparkan sinopsis program itu yang diambilnya dari halaman
manual. Contoh; anda boleh mencari kegunaan arahan who dengan menggunakan :
# whatis who
Skrin akan memaparkan seperti berikut:
who(1) -show who is logged on
Anda mungkin terpaksa mengemaskinikan arahan pangkalan d
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
