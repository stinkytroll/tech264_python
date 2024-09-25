# Use your code from the "Task: Get name, age and DOB details from a user".

# Get the user's name, age and DOB.
user_name = input("Tell me you name: ")
user_age = input("Tell me you age: ")
user_dob = input("Tell me you DOB DD/MM/YYYY: ")

# Print the user's name, age and DOB to the screen
print(f"Hello {user_name}. You are {user_age} and you were born {user_dob}")

# Mix the name, age and DOB into one list user_details_list
user_details_list = [user_name, user_age, user_dob]

# Print the user's name, age and DOB from the list
print(user_details_list)

# Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and
# add the age integer to the list.
int_user_age = int(user_age)  # Covert age to int
print(type(int_user_age))  # Check type class, should be int
user_details_list.append(int_user_age)  #

# Ask the user for their height in cm and save it to the variable height
user_height = input("Tell me you height in CM: ")

# Save height as a float in the list, and print the height from the list.
float_user_height = float(user_height)

user_details_list.remove(user_age)  # Remove the unused variable
user_details_list.append(float_user_height)  # Add the height to the list

print(user_details_list[-1])  # Print the height
print(user_details_list)  # Print the entire list

