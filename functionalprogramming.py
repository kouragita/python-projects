def add_twenty(x):
    return x+20

def twice(func, arg):
    return func(func(arg))
print(twice(add_twenty, 10))
