from tkinter import *

class MyButtons:

    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("Button Clicked")


root = Tk()
b = MyButtons(root)

root.mainloop()
