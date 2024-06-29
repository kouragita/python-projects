from tkinter import*

root = Tk()

label1 = Label(root, text="Hello Sensei", bg="Red", fg="White")
label1.pack(fill=X)

label2 = Label(root, text="Hello ICT", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y)

root.mainloop()
