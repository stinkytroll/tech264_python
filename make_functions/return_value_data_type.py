# 8. Make a function which gives a hint about a return value's data type

# Let's make a new function to bring it all together, also to provide type hints for all arguments,
# function return values and variables used...
# The function should be named division:
# It should divide 2 integers accepted as arguments
# It should return the result of the division
# The arguments should:
# have their types defined
# have the default values of 2 and 5 (therefore, by default 2 will be divided by 5 and have the result 0.4)
# NEW! Define the value returned as a float for the type hint
# NEW! Before calling the function, define variables a and b in Python as strongly-typed integers
# with the values 4 and 6
# You should call the function with this line of code:
# print(division(a, b))
# Also check the default values work if no values are passed into the function


def division(num1: int = 2, num2: int = 5) -> float:
    return num1 / num2


print(division())

a: int = 4
b: int = 6

print(division(a, b))
