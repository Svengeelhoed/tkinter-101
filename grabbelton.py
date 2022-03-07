import tkinter
from random import shuffle
grabbels = 10

root=tkinter.Tk()

root.geometry("500x500")

GrabbelLijst = ["1 kilo kaas", "2 liter melk", "3 potten pindakaas", "4 bananen", "5 auto's", "6 aardapppels", "7 stoelen", "8 voetballen", "9 bakstenen", "10 aspergers", "11 keukentafels"]
shuffle(GrabbelLijst)


button = tkinter.Button(root)
button.configure(text="grabbelen", font=14)
button.pack(padx=100, pady=100)

AantalGrabbels = tkinter.Label(root,text=grabbels)
AantalGrabbels.pack()

GrabbelResult = tkinter.Label(root)
GrabbelResult.pack()

def UpdateWindow():
    global grabbels
    GrabbelResult.configure(text="gefeliciteerd, je hebt "+ str(GrabbelLijst[1]) + " gegrabbeld!",font=12)
    GrabbelLijst.pop(1)
    grabbels=grabbels-1
    AantalGrabbels.configure(text=grabbels)
    if grabbels == 0:
        button.destroy()


button.configure(command=UpdateWindow)

root.mainloop()