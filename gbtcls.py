from tkinter import *


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Example")

        self.button1 = Button(root, text="Click Me", command=self.print_message)
        self.button1.pack(pady=10)

        self.button2 = Button(root, text="Exit", command=self.quit_app)
        self.button2.pack()

    def print_message(self):
        print("Button Clicked!")

    def quit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = SimpleApp(root)
    root.mainloop()
