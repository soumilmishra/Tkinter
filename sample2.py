import tkinter
from tkinter import *

app = Tk()
app.title("Welcome")
#image2 =Image.open('sad1.png')
image1 = PhotoImage(file="gradecap1.png")
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))
#app.geometry("800x600")
#app.configure(background='C:\\Usfront.png')
#app.configure(background = image1)

labelText = StringVar()
labelText.set("Welcome !!!!")
#labelText.fontsize('10')

label1 = Label(app, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER,  fg="white")
label1.pack(pady=(100,400))

app.mainloop()