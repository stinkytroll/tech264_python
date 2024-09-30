# What is a variable?
# A variable is a name / container used to store data values. It allows you to store data like numbers, text etc. by
# referencing them through the given name.

# Why is it called a variable?
# Because the value it holds can vary / change throughout the execution of a program. You can assign different values
# to the same variable.

name = 'Kagan'
age = 24
price = 25.00


print("Name:", name)
print("Age:", age)
print("Price:", price)


# Dynamically typed languages do not require you to declare the data, whereas strong typed languages require you to
# explicitly state it in order for it to be recognised. You can change the data later in the code without issue.

x = 10
print("x is 10 before overwriting it", id(x))

x = 'Hello world'

print("Now it will be hello world, as it was overwritten", id(x))

# The ID has changed because it is currently pointing to a different object. It's referenced in a different memory
# location.

user_input = input("Say something funny: ")
print("Wasn't very funny, but you said:", user_input)

# What's the difference between an operator and an operand?

# An operator is a symbol that tells the compiler to perform a certain mathematical or logical manipulation.
# an operand is the data that the operator works on.

x = 5
y = 10

# Addition
addition = x + y
print("Addition (x + y):", addition)  # Output: 15

# Subtraction
subtraction = x - y
print("Subtraction (x - y):", subtraction)  # Output: -5

# Multiplication
multiplication = x * y
print("Multiplication (x * y):", multiplication)  # Output: 50

# Division
division = x / y
print("Division (x / y):", division)  # Output: 0.5

# Remainder (Modulo)
remainder = x % y
print("Remainder (x % y):", remainder)  # Output: 5

# Greater than
is_greater = x > y
print("Is x greater than y (x > y):", is_greater)  # Output: False

# Less than
is_less = x < y
print("Is x less than y (x < y):", is_less)  # Output: True

# Check if equal to each other
is_equal = x == y
print("Is x equal to y (x == y):", is_equal)  # Output: False

# Check if not equal
is_not_equal = x != y
print("Is x not equal to y (x != y):", is_not_equal)  # Output: True

# Greater than or equal to
is_greater_equal = x >= y
print("Is x greater than or equal to y (x >= y):", is_greater_equal)  # Output: False

# Less than or equal to
is_less_equal = x <= y
print("Is x less than or equal to y (x <= y):", is_less_equal)  # Output: True

# An integer is a whole number, positive or negative.
age = 24
print("Age:", age)  # Output: 24
print("Type of age:", type(age))  # Output: <class 'int'>

# A floating point number is a number with a decimal point.
price = 25.00
print("Price:", price)  # Output: 25.00
print("Type of price:", type(price))  # Output: <class 'float'>

# Demonstration

age = 24  # Int
price = 25.00  # Float

print("Age:", age, "/ Type:", type(age))  # Output: <class 'int'>
print("Price:", price, "/ Type:", type(price))  # Output: <class 'float'>

# What is none in python?
# A special constraint that represents the absence of a value. It's an object of its own data type.
# Commonly used to initialise a variable when you don't have a value for it.

# In other coding languages...
# Java: null
# C/C++: NULL

# What happens when you convert None to boolean?
# None converts to false.

print("Boolean value of None:", bool(x))  # Output: False


x = None

if x is None:
    print("x is equal to None")
else:
    print("x is not equal to None")

hi = "Hello World!"

# find out if 'hi' is made up of letters only (use one of the strings methods) - print the boolean to the screen
print(hi.isalpha())  # False

# find out if 'hi' is made up only of lowercase letters (use one of the strings methods) - print the boolean to the
# screen
print(hi.islower())  # False

# find out if 'hi' is made up only of uppercase letters (use one of the strings methods) - print the boolean to the
# screen
print(hi.isupper())  # False

# find out if 'hi' ends with an exclamation mark (use one of the strings methods) - print the boolean to the screen
print(hi.endswith("!"))  # True

# find out if 'hi' starts with a capital "h" (use one of the strings methods) - print the boolean to the screen
print(hi.startswith("H"))  # True
