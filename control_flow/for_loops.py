list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1, 2, 3], [4, 5, 6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# 1. Loop through a list

# Under the starting code, write a for loop to print the double of each number in the list 'list_data'.
# - It should loop through the numbers in list_data - each item in the list should be called 'num' (for number)
# - Inside the loop, it should print out the double of each number in the list.

for num in list_data:
    print(num * 2)

print("TASK 1 COMPLETE.")
# 2. Loop through the 'embedded_lists' list

# Write another for loop to print the items inside 'embedded_lists'. Each item in the list should be called 'data'.

for data in embedded_lists:
    print(data)

print("TASK 2 COMPLETE.")

# 3. Loop through the lists embedded inside a list

# We need to access the data within the lists, so now we need an embedded loop. Create another loop inside the
# 'embedded_lists' for loop to list the individual items in the lists.

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

print("TASK 3 COMPLETE.")

# 4. Loop through a dictionary
# Write another for loop to loop through the dictionary 'dict_data'.

for data in dict_data:
    print(data)

print("TASK 4 COMPLETE.")

# 5. Loop through a dictionary and print its values

# Write another for loop to loop through the dictionary 'dict_data'. Use to the dictionary's
# value() method to print the value for each key in the dictionary.

for data in dict_data.values():
    print(data)

print("TASK 5 COMPLETE.")

# 6. Loop to print the values of the dictionary items inside a dictionary
# Copy and paste the last for loop as a starting point for this loop. Generate an embedded for loop
# (a loop within a loop) to extract and print the values within the dictionary of each item in the dictionary.

for data in dict_data.values():
    for key, value in data.items():
        print(value)

print("TASK 6 COMPLETE.")

# 7. Loop to print specific values of the dictionary items inside a dictionary
# Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values.

for data in dict_data.values():
    print(data["money"])

print("TASK 7 COMPLETE.")

# 8. Loop through a list with a nested if statement
# Write another loop to loop through the items in 'list_data' and include a nested (indented) if
# statement inside the loop so that when it loops it checks the number/item in list:
# - if the number is less than 3, it prints 'less than 3'
# - if the number equals 3, it prints 'I found three'
# - if the number is greater than 3, it prints 'greater than 3'

for data in list_data:
    if data < 3:
        print("Less than 3")
    elif data == 3:
        print("I found three")
    else:
        print("greater than 3")

print("TASK 8 COMPLETE.")
