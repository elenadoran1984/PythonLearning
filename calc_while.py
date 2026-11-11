on = True

def add():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a + b)

def substraction():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a - b)

def multiply():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a * b)

def divide():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a / b)

while on:
    operation = input("Please type +, -, *, / or q ")
    if operation == '+':
        add()
    elif operation == '-':
        substraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("That operation is not available. ")