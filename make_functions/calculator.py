# Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.
#
# Create a Python file called calculator.py and complete a viable basic calculator using functions.
#
# MVP (each of these should be in a separate function):
#
# Can add 2 numbers
# Can subtract 2 numbers
# Can multiply 2 numbers
# Can divide 2 numbers
# Taking it to the next level:
#
# Implement more complex operations, such as handling parentheses, exponentiation
# More advanced operations should continue to be broken into separate functions

chosen_num1 = input("First Number: ")
chosen_num2 = input("Second Number: ")


def addition(num1: int = chosen_num1, num2: int = chosen_num2) -> float:
    if chosen_num1.isdigit() and chosen_num2.isdigit():
        int(chosen_num1) and int(chosen_num1)
        return num1 + num2


print(addition())


def division(num1: int = 2, num2: int = 5) -> float:
    return num1 / num2


print(division())

a: int = 4
b: int = 6

print(division(a, b))
