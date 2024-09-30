# 6. Make a function that accepts any number of arguments
# Design a function called 'print_every_number' which accepts a tuple of numbers as an argument
# The function should do 2 things:
# Print the type of the tuple that was passed in as an arguments
# Loop through the tuple and print each item in the tuple on a separate line
# After calling the function, the output should be:
# <class 'tuple'>
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# Explain what character allows your function to accept multiple arguments

def print_every_number(*args):  # Groups all arguments into a tuple.
    print(type(args))

    for n in args:  # Loop through the tuple. n represents each item in the tuple.
        print(n)


print_every_number(1, 2, 2, 3, 3, 4, 4, 5, 5)