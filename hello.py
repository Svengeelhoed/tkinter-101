import tkinter

root = tkinter.Tk()
root.title('Hello')
root.geometry("300x200")

box1 = tkinter.Label(
    root,
    text="Hello tkinter!",
    bg="green",
    fg="white"
)

box1.pack(
    ipadx=80,
    ipady=60,
    expand=True,
)

root.mainloop()

