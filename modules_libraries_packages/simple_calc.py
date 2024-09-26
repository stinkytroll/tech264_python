from math_operations import *

# Mini-calculator
user_input = input("Enter a number to access a particular operation (1 = Addition, 2 = Subtraction, "
                   "3 = Multiplication, 4 = Division):")

# Add
if user_input == "1":
    print("You selected addition!")
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the first number: "))
    result = add(first_num, second_num)
    print(f"{first_num} + {second_num} = {result}")

# Subtract
if user_input == "2":
    print("You selected subtraction!")
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the first number: "))
    result = subtract(first_num, second_num)
    print(f"{first_num} - {second_num} = {result}")

# Multiply
if user_input == "3":
    print("You selected multiplication!")
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the first number: "))
    result = multiply(first_num, second_num)
    print(f"{first_num} * {second_num} = {result}")

# Divide
if user_input == "4":
    print("You selected division!")
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the first number: "))
    result = division(first_num, second_num)
    print(f"{first_num} / {second_num} = {result}")
