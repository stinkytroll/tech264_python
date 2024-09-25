# 1. Loop until age is all digits

# Ask user for their age

age = input("What is your age? ")

print(f" Your age is {age}")

# The problem with this code is that even if the user is 20, they could enter "20" or "twenty". Let's standardise
# the input to get the age as digits...

user_prompt = True

while user_prompt is True:  # While it's true, spit out the input request
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 117:  # If user inputs digits, set to false, stopping the while loop
        user_prompt = False
        print(f"Your age is {age}")
    else:  # If the input does not consist of exclusively digits, print a message and continue the loop
        print("You must input digits rather than text and cannot be older than 117 (you liar)!")

# 2. Also check age is in the correct range

# Our code now works to stop our user from inputting strings, floats, and negative numbers,
# but at the moment the user could say they are 356000 years old if they want.
# Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age.

