# 7. Make a function which gives a hint about an argument's data type

# Some people think stricter typing should be used with Python as best practice, let's find out why
# 1. See what happens if you call your earlier greet function with this line of code:


# greet(24601)


# 2. To HELP us avoid this type of error, define the type of argument accepted into our function so that
# we are given a warning BEFORE we even run out Python script:
# - Define that data type accepted by your greet function is a string
# - Notice that PyCharm now gives the warning Expected type 'str', got 'int' instead BEFORE you even run your code

def greet(name: str):
    print("Hello, my name is " + name)


greet(name="Susan")
