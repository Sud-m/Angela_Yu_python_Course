import art
import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    os.system("cls")
    print(art.logo)
    num1 = float(input("Enter the first number: "))
    while True:
        num2 = float(input("Enter the next number: "))
        for key in operations:
            print(key)
        symbol = input("Pick an operation from the given symbols: ")
        operation = operations[symbol]

        result = operation(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start over.: ").lower()
        if not cont == 'n':
            num1 = result
        else:
            calculator()


calculator()
