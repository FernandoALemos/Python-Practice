from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root,
            font=("Courier", 80),
            background="black",
            foreground="cyan")
label.pack(ancho="center")

time()
root.mainloop()