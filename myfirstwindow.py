import tkinter
import random

window = tkinter.Tk()
w=50
h=50
x=7

kleuren = ("blue", "yellow", "orange", "red" , "pink", "purple")
window.title("My First Window")
window.config(bg='white')
window.geometry('50x50')

for i in range(7):
    window.after(2000)
    window.config(bg=random.choice(kleuren))
    window.geometry("{width}x{height}".format(width=w,height=h))
    w = w + 50
    h = h + 50
    window.update()
    x=x-1
    if x == 0:
        print("BOOM!")
        window.destroy()
    else:
        print(x)



window.mainloop()
