# Google images
import os
from PIL import Image
from tkinter import *
from tkinter import filedialog
import tkinter as tk



win = Tk()
win.title('Image Downloader')
win.iconbitmap(r'icon.ico')

win.geometry('740x400+100+100')
win.minsize(740,400)
# win.maxsize(610,420)


bgimg = PhotoImage(file=r"flower.png")

l2 = Label(
    win,
    image=bgimg
)
l2.place(x=0, y=0)


# Box entering the details
Box = Text(l2, height = 20, width = 85)
Box.place(x = 45, y = 53)
Box.config(state='disabled', bg="#F0F0F0", highlightthickness =0, highlightbackground="#E0E0E0", borderwidth=0.5)


l3 = Label(
    Box,
    image=bgimg
)
l3.place(x=0, y=0)




nombreImg=StringVar()
directorioPath=StringVar()



def establecerDirectorio():
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    directorioPath.set(path)


def Queryword():

    spacer1 = tk.Label(Box, text="")
    spacer1.grid(row=0, column=0)

    url2Imagenes=Text(Box, width=50, height=3)
    url2Imagenes.grid(row=1, column=1, sticky="w", padx=1, pady=5)

    comentLabel=Label(Box, text="Query Keyword: ", font=('Calisto MT', 10 ))
    comentLabel.grid(row=1, column=0, sticky="w", padx=(10,0), pady=10)


    scrollVert=Scrollbar(Box, command=url2Imagenes.yview)
    scrollVert.grid(row=1, column=2, sticky="nsew")

    url2Imagenes.config(yscrollcommand=scrollVert.set)

    spacer1 = tk.Label(Box, text="")
    spacer1.grid(row=2, column=0)


def url_name():

    urlImagenes=Text(Box, width=50, height=3)
    urlImagenes.grid(row=3, column=1, sticky="w", padx=1, pady=5)

    scrollVert=Scrollbar(Box, command=urlImagenes.yview)
    scrollVert.grid(row=3, column=2, sticky="nsew")

    urlImagenes.config(yscrollcommand=scrollVert.set)

    comentariosLabel=Label(Box, text="Image URLs: ", font=('Calisto MT', 10 ))
    comentariosLabel.grid(row=3, column=0, sticky="w", padx=(10,0), pady=10)

    spacer1 = tk.Label(Box, text="")
    spacer1.grid(row=4, column=0)




def Output():

    folderFrame=Frame(Box)
    folderFrame.grid(row=6, column=0, columnspan=4, padx=20, pady=35, sticky='w')

    folderFrameLabel=Label(folderFrame, text="Output path :          ", font=('Calisto MT', 10 ))
    folderFrameLabel.pack(side='left')

    folderFrameEntry=Entry(folderFrame, textvariable=directorioPath, width=57, font=('Calisto MT', 10 ))
    folderFrameEntry.pack(side='left')

    botonDir=Button(folderFrame, text="Folder", font=('Calisto MT', 10 ), command=establecerDirectorio)
    botonDir.pack(side='left')


b4 = Button(win, text = " Search ", width = 20)  
b4.pack(padx = 10, pady = 10, side=BOTTOM)  


Queryword()
url_name()
Output()



win.mainloop()
         
