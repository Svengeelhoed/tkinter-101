import tkinter

from time import strftime
 
root = tkinter.Tk()
root.title('Clock')
 
def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)
 
lbl = tkinter.Label(root, font = ("Comic Sans MS", 40, 'bold'),
            background = 'lightblue',
            foreground = 'black')

lbl.pack(anchor = 'center')
time()
 
root.mainloop()
