def add(a, b):
    return a+b

def subtract (a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        raise ZeroDivisionError
    return a/b

PI=3.14159