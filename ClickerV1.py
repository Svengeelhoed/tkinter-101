import tkinter
root = tkinter.Tk()
root.geometry("250x200")
root.config(bg="grey")
nummerdisplay=0

button = tkinter.Button(root,text="Up", bg="white", width="30")
button.pack(padx=10, pady=30)

nummer = tkinter.Label(root, text=nummerdisplay, bg="white", width="30")
nummer.pack()

button2 = tkinter.Button(root,text="Down", bg="white", width="30")
button2.pack(padx=10, pady=30)

def buttonUp():
    global nummerdisplay
    nummerdisplay = nummerdisplay + 1
    nummer.config(text=nummerdisplay)
    if nummerdisplay >= 1:
        root.config(bg="green")
    elif nummerdisplay == 0:
        root.config(bg="grey")

button.config(command=buttonUp)

def ButtonDown():
    global nummerdisplay
    nummerdisplay = nummerdisplay - 1
    nummer.config(text=nummerdisplay)
    if nummerdisplay < 0:
        root.config(bg="red")
    elif nummerdisplay == 0:
        root.config(bg="grey")

button2.config(command=ButtonDown)

root.mainloop()