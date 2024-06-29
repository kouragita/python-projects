try:
    a = 3
    b = 1
    print(a / b)
except ZeroDivisionError:
    print("there is  a zero division error")
finally:
    print('this line of code will work regardless of the exceptions above')
