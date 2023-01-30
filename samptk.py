import tkinter as tk
from tkinter import *


my_w = tk.Tk()
my_w.geometry("400x100+100+100")   
my_w.title("Image Scrapping") 

my_w.minsize(400,100)
my_w.maxsize(400,100)


def validate(u_input):
    return u_input.isdigit()

my_valid = my_w.register(validate) 

l1=tk.Label(my_w,text='Enter no:of images to download')
l1.grid(row=1,column=1,padx=20,pady=20)

e1 = Entry(my_w,validate='key',validatecommand=(my_valid,'%S'))
e1.grid(row=1,column=2,padx=20)



obtn = Button(my_w, text="Search")
obtn.grid(row=2, column=2)


my_w.mainloop()