# Simple-music-player-with-Python

Harus Dilakukan  1. Install pygame (pip install pygame)

2. Install mutagen (pip install mutagen)

3. Disediakan 2 file(.py dan .ipynb) jika error running file .py melalui
vscode silahkan running langsung file tersebut melalui file explorer
dengan cara klik kanan \--\> open with \--\> Python maka otomatis akan
run program. Jika masi error silahkan run file .ipynb Jika tetap error
silahkan ikuti cara di bawah ini

Note (Dilakukan jika terjadi error saja) 1. jika terdapat error \"no
such file or directory\" silahkan rubah lokasi logo dan lagu pada source
code sesuai lokasi menyimpan

Rubah source code di bawah menjadi contoh: file=
\'c:\\\\\...\\\\start.png\' (sesuai lokasi menyimpan)

\# Membuat tombol tombol_start= PhotoImage(file=\'logo/start.png\')
tombol_play= PhotoImage(file=\'logo/play.png\') tombol_next=
PhotoImage(file=\'logo/next.png\') tombol_back=
PhotoImage(file=\'logo/back.png\') tombol_stop=
PhotoImage(file=\'logo/stop.png\') speaker_on=
PhotoImage(file=\'logo/on.png\')
speaker_off=PhotoImage(file=\'logo/off.png\')

Rubah source code di bawah menjadi contoh:
initialdir=\'\'c:\\\\\...\\\\lagu\' (sesuai lokasi menyimpan)

def tambah_lagu(): \# Fungsi untuk menambah lagu ke Playlist
penyimpanan=filedialog.askopenfilenames(initialdir=\'lagu/\',
title=\"Pilih Lagu\", filetypes=((\"mp3 file\",\"\*mp3\"),)) global
folder folder=penyimpanan for lagu in penyimpanan: \# Untuk menambahkan
lagu ke dalam array array_playlist.append(lagu) for i in penyimpanan: \#
Untuk menambah lagu ke dalam listbox(tuple) ui_playlist.insert(END,i)

2\. Jika terdpat error \"TclError: image \"pyimage2\" doesn\'t exist\"
silahkan restart vscode
