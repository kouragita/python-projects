from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Tittle", "This is awesome")

response = tkinter.messagebox.askquestion("Question 1", "Do yu have a working strategy Noman Iqbal?")

if response == 'yes':
    print("Fuck yeah yu do. That's  why they can't  stand yu. mother facker yu winning!!!")

else:
    print("Get the fuck out of here, dogshit!!!.")

root.mainloop()
