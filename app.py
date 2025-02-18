# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:12:05 2022

@author: ArianVermana, HanifWidagdo 
"""

from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
## Encrypt
def encrypt1(key, file_input, file_output):
    # Input File txt
    files = open(f'{file_input}')
    word = files.read() #Dibaca
    key = key.upper()

    hasil = ""
    ## BASE INDEX DARI KEY
    indexkey = "".join([key[i%len(key)] for i in range(len(word))])
    
    # seseuai dari huruf pertama dan urutan dari indexkey
    sortedzip = sorted(zip(indexkey, word),key=lambda indexkey: indexkey[0]) 
    result = [a[1] for a in sortedzip]
    for x in range(len(result)):
        hasil += result[x]
    # return hasil
    filer = open (file_output,'w')
    filer.write(hasil)

# Decrypt
def decrypt1 (key, file_input, file_output):
    # Input File txt
    key = key.upper()
    files = open(f'{file_input}')
    word = files.read()

    # Perulangan Key Sesuai huruf dari CipherText
    hasil = ""
    basekey = []  
    for abc in range(len(word)):
        for aba in range(len(key)):
            numa = key[aba]
            basekey.append(numa)
    # Untuk mendapatkan urutan ciphertext berdasarkan basekey
    kolom = []
    curr_row = 0
    curr_col = 0
    for ch in range(len(word)):
        kolom.append(ch)
        curr_row += 1
        if curr_row == len(key):
            curr_row = 0
            curr_col += 1

    # Menyatukan dari basekey dan kolom lalu disortir sesuai basekey
    keyzip = sorted(zip(basekey, kolom))
    newestkey = [a[1] for a in keyzip]
    newzip = sorted(zip(newestkey, word))
    result = [a[1] for a in newzip]
    
    # Perulangan untuk mendapatkan hasil dari proses
    for x in range(len(result)):
        hasil += result[x]
    # return hasil
    filer = open (file_output,'w')
    filer.write(hasil)


window = Tk()

window.geometry("500x500")
window.title("UAS PRAKTIKUM KELOMPOK 8")
window.configure(bg = "#00E7FF")


canvas = Canvas(
    window,
    bg = "#00E7FF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    250.0,
    250.0,
    image=image_image_1
)

canvas.create_rectangle(
    50.0,
    94.0,
    450.0,
    444.0,
    fill="#6ECCAF",
    outline="")

canvas.create_text(
    154.0,
    113.0,
    anchor="nw",
    text="Transposition Cipher",
    fill="#000000",
    font=("RobotoRoman Medium", 20 * -1)
)

canvas.create_text(
    88.0,
    149.0,
    anchor="nw",
    text="Nama File",
    fill="#000000",
    font=("Lancelot", 15 * -1)
)

canvas.create_text(
    88.0,
    214.0,
    anchor="nw",
    text="File Baru",
    fill="#000000",
    font=("Lancelot", 15 * -1)
)

canvas.create_text(
    88.0,
    269.0,
    anchor="nw",
    text="Kunci",
    fill="#000000",
    font=("Lancelot", 15 * -1)
)

canvas.create_text(
    91.0,
    341.0,
    anchor="nw",
    text="Mode",
    fill="#000000",
    font=("Lancelot", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    401.0,
    50.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    244.5,
    181.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFF6BD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=93.0,
    y=173.0,
    width=303.0,
    height=14.0
)

canvas.create_text(
    404.0,
    175.0,
    anchor="nw",
    text=".TXT",
    fill="#000000",
    font=("Lemonada Regular", 10 * -1)
)

canvas.create_text(
    404.0,
    239.0,
    anchor="nw",
    text=".TXT",
    fill="#000000",
    font=("Lemonada Regular", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    244.5,
    245.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFF6BD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=93.0,
    y=237.0,
    width=303.0,
    height=14.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    244.5,
    298.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFF6BD",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=93.0,
    y=290.0,
    width=303.0,
    height=14.0
)
    
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
# Penempatan Button untuk memanggil fungsi Encrypt
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encrypt1(entry_3.get(),entry_1.get(),entry_2.get()),
    relief="flat"
)
button_1.place(
    x=154.0,
    y=357.0,
    width=65.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
# Penempatan Button untuk memanggil fungsi Decrypt
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: decrypt1(entry_3.get(),entry_1.get(),entry_2.get()),
    relief="flat"
)
button_2.place(
    x=284.0,
    y=357.0,
    width=65.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
# Penutup / Exit
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.quit(),
    relief="flat"
)
button_3.place(
    x=219.0,
    y=397.0,
    width=65.0,
    height=28.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    92.0,
    45.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    371.0,
    124.0,
    image=image_image_4
)
# Window tidak bisa diubah
window.resizable(False, False)
window.mainloop()
