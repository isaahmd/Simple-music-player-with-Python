from tkinter import *
from pygame import mixer
from tkinter import ttk
from tkinter import filedialog
import time
import random
from mutagen.mp3 import MP3



# DEKLARASI FUNGSI
paused=False 
def pause(): # Fungsi untuk pause dan unpause lagu
    global paused
    if paused==True:
        mixer.music.unpause()
        paused=False
    else:
        mixer.music.pause()
        paused=True
def next(): # Fungsi untuk next lagu
    lanjut=ui_playlist.curselection()
    lanjut=lanjut[0]+1
    lagu=ui_playlist.get(lanjut)

    mixer.music.load(lagu)
    mixer.music.play()

    ui_playlist.selection_clear(0,END)

    ui_playlist.activate(lanjut)

    ui_playlist.select_set(lanjut,last=None)

    song_slider.config(value = 0)

    info_waktu.config(text = " ")
def back(): # Fungsi untuk back lagu
    lanjut=ui_playlist.curselection()
    lanjut=lanjut[0]-1
    lagu=ui_playlist.get(lanjut)

    mixer.music.load(lagu)
    mixer.music.play()
        
    ui_playlist.selection_clear(0,END)

    ui_playlist.activate(lanjut)

    ui_playlist.select_set(lanjut,last=None)
    song_slider.config(value = 0)

    info_waktu.config(text = " ")
stopped = False
def stop(): # Fungsi untuk stop lagu
    mixer.music.stop()
    song_slider.config(value = 0)
    info_waktu.config(text = " ")
    global stopped
    stopped = True
def volume(sound): # Fungsi untuk mengatur volume lagu
    mixer.music.set_volume(volume.get())
muted = False
def mute():
    global muted
    if(muted == True):
        mixer.music.set_volume(1)
        speaker.configure(image=speaker_on)
        volume.configure(value = 1)
        muted = False
    else:
        mixer.music.set_volume(0)
        speaker.configure(image=speaker_off )
        volume.configure(value = 0)
        muted = True
def tambah_lagu(): # Fungsi untuk menambah lagu ke Playlist
    penyimpanan=filedialog.askopenfilenames(initialdir='lagu/', title="Pilih Lagu", filetypes=(("mp3 file","*mp3"),))
    global folder
    folder=penyimpanan
    for lagu in penyimpanan:        # Untuk menambahkan lagu ke dalam array
        array_playlist.append(lagu) 
    for i in penyimpanan:        # Untuk menambah lagu  ke dalam listbox(tuple)
        ui_playlist.insert(END,i)         
def remove(): # Fungsi untuk menghapus lagu dari playlist
    ui_playlist.delete(ANCHOR)
    z=ui_playlist.get(0,END)
    global array_playlist
    array_playlist=list(z)
    mixer.music.stop() 
    song_slider.config(value = 0)
    info_waktu.config(text = " ")
def remove_all(): # Fungsi tambahan untuk shuffle
    ui_playlist.delete(0,END)  
def shuffle(): # Fungsi untuk mengacak playlist
    random.shuffle(array_playlist) # Library random untuk mengacak array
    remove_all() # Untuk menghapus lagu sehingga hasil shuffle tidak bertumpuk
    for i in array_playlist: # Untuk membuat playlist baru setelah array diacak
        ui_playlist.insert(END,i)
    mixer.music.stop()
    lagu=ui_playlist.get(ACTIVE)
    mixer.music.load(lagu)
    mixer.music.play(-1)
    song_slider.config(value = 0)
    play_time()
    info_waktu.config(text = " ")
def start(): # Fungsi untuk play lagu
    global stopped
    stopped=False
    lagu=ui_playlist.get(ACTIVE)
    mixer.music.load(lagu)
    mixer.music.play(-1)
    song_slider.config(value = 0)
    play_time()
def play_time(): 
    if (stopped== True):
        return
    current_time = int(mixer.music.get_pos()/1000)   #posisi lagu yang sedang diputar dalam detik
    
    convert_time = time.strftime('%M:%S', time.gmtime(current_time)) #ubah format current_time jadi menit:detik
    
    current_song = ui_playlist.get(ACTIVE)  #lagu yang sedang dimainkan
   
    song_mutagen = MP3(current_song)
    global durasi_lagu 
    durasi_lagu = song_mutagen.info.length  #durasi dari lagu yang sedang dimainkan
    convert_durasi = time.strftime('%M:%S', time.gmtime(durasi_lagu))   #ubah format durasi
    
    current_time += 1
    if (int(song_slider.get()== int(durasi_lagu))):
        info_waktu.config(text= f'{convert_durasi} of {convert_durasi}')
    elif(paused == True):
        pass
    elif(int(song_slider.get())==int(current_time)):
        #slider belum digeser
        slider_position = int(durasi_lagu)
        song_slider.config(to = slider_position, value = int(current_time))

    else:
        #slider digeser
        slider_position = int(durasi_lagu)
        song_slider.config(to = slider_position, value = int(song_slider.get()))
        convert_time = time.strftime('%M:%S', time.gmtime(int(song_slider.get())))
        info_waktu.config(text= f'{convert_time} of {convert_durasi}')

        next_time = int(song_slider.get())+1
        song_slider.config(value = next_time)
    
    info_waktu.after(1000, play_time)
#FUNGSI SLIDER PLAY
def slide_play(value):
    lagu=ui_playlist.get(ACTIVE)
    mixer.music.load(lagu)
    mixer.music.play(start = int(song_slider.get()))

# Memulai modul pygame
mixer.init()


# Membuat ui utama
root=Tk()
root.title("Spotify STEI ITB")
root.geometry('600x470')

# Membuat array dan playlist box(tuple)
array_playlist=[]
ui_playlist= Listbox(root, bg="Wheat1", fg="Black", width=60)
ui_playlist.pack(pady = 20)

 
# Membuat tombol
tombol_start= PhotoImage(file='logo/start.png')
tombol_play= PhotoImage(file='logo/play.png')
tombol_next= PhotoImage(file='logo/next.png')
tombol_back= PhotoImage(file='logo/back.png')
tombol_stop= PhotoImage(file='logo/stop.png')
speaker_on= PhotoImage(file='logo/on.png')
speaker_off=PhotoImage(file='logo/off.png')

# Membuat frame kontrol
myframe= Frame(root)
myframe.pack()

myframe2= Frame(root)
myframe2.place(x=250,y=310)

volume_frame= LabelFrame(root, text = "Volume")
volume_frame.place(x=227,y=350)

#LABEL SLIDER
slider_label = Label(root)
slider_label.pack()

#BUAT STATUS BAR
info_waktu= Label(root, text = '')
info_waktu.place(x=265,y=425)


#BUAT POSISI SLIDER
song_slider = ttk.Scale(slider_label, from_= 0, to = 100, orient = HORIZONTAL, value = 0, length= 380, command= slide_play)
song_slider.pack()

# Membuat Button kontrol

start = Button(myframe, image=tombol_start, command = start, borderwidth= 5)
start.grid(row = 1, column=0, padx=10)
pause_ = Button(myframe, image=tombol_play, command = pause , borderwidth = 5)
pause_.grid(row = 1, column=1, padx=10)
stop = Button(myframe, image=tombol_stop, command = stop, borderwidth = 5)
stop.grid(row =1, column=2, padx=10)
back = Button(myframe, image=tombol_back, command = back, borderwidth= 5)
back.grid(row=1, column=3, padx=10)
next = Button(myframe, image=tombol_next, command = next, borderwidth= 5)
next.grid(row=1, column=4, padx=10)
shuffle=Button(myframe2, text="Shuffle", command = shuffle, width= 10)
shuffle.grid(row=2, padx=10)
volume = ttk.Scale(volume_frame, from_= 0, to= 1, orient= HORIZONTAL, value = 1, length=120, command= volume)
volume.grid(row = 3,  padx=10)
speaker = Button(volume_frame, text="mute", command = mute)
speaker.grid(row = 1, column = 0)

# Membuat menu (bar atas)
playlist= Menu(root)
root.config(menu=playlist)

# Membuat Playlist (Button berada di atas bar)
buat_playlist= Menu(playlist)
playlist.add_cascade(label="Buat Playlist", menu=buat_playlist)
buat_playlist.add_command(label="Pilih Lagu", command=tambah_lagu)

# Menghapus lagu dari Playlist (Button berada di atas bar)
hapus_lagu=Menu(playlist)
playlist.add_cascade(label="Hapus Lagu", menu=hapus_lagu)
hapus_lagu.add_command(label="Hapus Lagu", command=remove)



root.mainloop() # Agar Tkinter(ui) muncul terus menerus