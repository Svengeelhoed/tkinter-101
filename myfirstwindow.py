import tkinter
import random
from turtle import width

window = tkinter.Tk()
w=50
h=50
kleuren = ("blue", "yellow", "orange", "red" , "pink", "purple")
window.title("My First Window")
window.config(bg='white')
window.geometry('50x50')
for i in range(10):
    window.after(2000)
    window.config(bg=random.choice(kleuren))
    window.geometry("{width}x{height}".format(width=w,height=h))
    w = w + 50
    h = h + 50
    window.update()

window.mainloop()
