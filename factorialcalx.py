import tkinter as tk
import math

def calculate_factorial():
    try:
        input_number = int(entry.get())
        if input_number < 0:
            result_label.config(text="Error: Enter a non-negative integer")
            return
        factorial_result = math.factorial(input_number)
        result_label.config(text=f"{input_number}! = {factorial_result}")
    except ValueError:
        result_label.config(text="Error: Enter a valid integer")

# Create tkinter GUI
root = tk.Tk()
root.title("Factorial Calculator")

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
