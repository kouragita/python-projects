from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100, bg="pink")
canvas.pack()

newline = canvas.create_line(0, 0, 50, 100)
otherline = canvas.create_line(50, 0, 50, 100, fill="green")

root.mainloop()
