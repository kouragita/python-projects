from tkinter import *
import parser
import math

def get_variables(num):
    display.insert(END, num)

def get_operation(operator):
    display.insert(END, operator)

def calculate():
    try:
        result = parser.expr(display.get()).compile()
        result = eval(result)
        clear_all()
        display.insert(END, result)
    except Exception:
        clear_all()
        display.insert(END, "Error")

def clear_all():
    display.delete(0, END)

def factorial():
    entire_string = display.get()
    try:
        result = parser.expr(entire_string).compile()
        result = eval(result)
        result = math.factorial(result)
        clear_all()
        display.insert(END, result)
    except Exception:
        clear_all()
        display.insert(END, "Error")

root = Tk()
root.title('Calculator')

# Adding the input field
display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Adding buttons to the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('^', 5, 0), ('x!', 5, 1)
]

for button_text, row, col in buttons:
    Button(root, text=button_text, padx=20, pady=20, command=lambda t=button_text: handle_button(t)).grid(row=row, column=col)

Button(root, text="AC", padx=20, pady=20, command=lambda: clear_all()).grid(row=5, column=0, columnspan=2)
Button(root, text="<-", padx=20, pady=20, command=lambda: display.delete(len(display.get()) - 1)).grid(row=5, column=2, columnspan=2)

def handle_button(button_text):
    if button_text == '=':
        calculate()
    elif button_text == '^':
        get_operation("**")
    elif button_text == 'x!':
        factorial()
    else:
        get_variables(button_text)

root.mainloop()
