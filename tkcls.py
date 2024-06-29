from tkinter import *


root = Tk()
def printmessage():
    print('Button Clicked')


class Mybuttons:

    def __init__(self, rootone):

        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

b = Mybuttons()


root.mainloop()
