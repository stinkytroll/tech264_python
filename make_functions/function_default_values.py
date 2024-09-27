# 5. Make a function with default values
# - Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
# - Replace line of code to call the function with this:
# print(addition())
# -  Run your code - you should get an error
# - Modify your function so that int1 and int2 both have the default value of 2
# - Run your code and make sure the result is 4
# - Now call your function with this line of code:
# - print(addition(4, 4))
# - Explain why the answer is now 8

def addition(int1=2, int2=2):  # By declaring the number inside the variables, we do not need when we call the function.
    return int1 + int2


print(addition(4, 4))  # If we were to pass a value in here, it would overwrite the default.
