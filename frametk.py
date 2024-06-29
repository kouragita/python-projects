from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack(side=TOP)

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="BUY", fg="White", bg="Blue")
button2 = Button(otherframe, text="SELL", fg="Orange", bg="Red")

button1.pack(padx=2, pady=3)

button2.pack(padx=2, pady=3)

root.mainloop()
