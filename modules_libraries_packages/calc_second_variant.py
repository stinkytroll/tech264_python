from math_operations import *

#  Cleaner version from work friend

def calculator():
    operator = input("Choose operator(+, -, *, /, **:")
    num1 = float(input("Choose first number:"))
    num2 = float(input("Choose second number:"))

    if operator == "+":
        print(add(num1, num2))

    elif operator == "-":
        print(subtract(num1, num2))

    elif operator == "*":
        print(multiply(num1, num2))

    elif operator == "/":
        print(division(num1, num2))

    elif operator == "**":
        print(exponentiation(num1, num2))

    else:
        print("Error")


calculator()
