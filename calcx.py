from tkinter import *
import math
import pyparrsing

# Global variable to track user input
i = 0

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def calculate():
    entire_string = display.get()
    try:
        result = pyparsing.nums.parseString(entire_string)[0]
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

def factorial():
    entire_string = display.get()
    try:
        result = math.factorial(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

root = Tk()
root.title('Calculator')

# Adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# Adding buttons to the calculator
for num in range(1, 10):
    Button(root, text=str(num), command=lambda n=num: get_variables(n)).grid(row=(num-1)//3 + 2, column=(num-1)%3)

Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

# Operator buttons
Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

Button(root, text="^", command=lambda: get_operation("**")).grid(row=2, column=4)  # Exponent button

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=4)
Button(root, text="x!", command=lambda: factorial()).grid(row=3, column=4)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=4)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=4, column=4)

root.mainloop()
