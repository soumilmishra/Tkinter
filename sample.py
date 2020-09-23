import tkinter
from tkinter import *

root = Tk()
root.title("Name and School")
root.geometry("800x600")
root.config(background="sad1.png")


lbl_name = Label(
    root,
    text="enter your name",
    font = ("Consolas",24,"bold"),
)
lbl_name.pack()

name = StringVar()
nameEntered = Entry(
    root,
    width = 15,
    textvariable = name,
)
nameEntered.pack()

def ispressed():
    lbl_name.destroy()
    nameEntered.destroy()
    btn.destroy()
    x = name.get()
    show_name = Label(
        root,
        text = "Hello" + str(x),
        font= ("Consolas",24,"bold"),
    )
    show_name.pack()

btn = Button(
    root,
    text = "Continue",
    command = ispressed,
)
btn.pack()
root.mainloop()
