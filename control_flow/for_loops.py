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

# 2. Loop through the 'embedded_lists' list

# Write another for loop to print the items inside 'embedded_lists'. Each item in the list should be called 'data'.

for data in embedded_lists:
    print(data)

# 3. Loop through the lists embedded inside a list

# We need to access the data within the lists, so now we need an embedded loop. Create another loop inside the
# 'embedded_lists' for loop to list the individual items in the lists.

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

# 4. Loop through a dictionary
# Write another for loop to loop through the dictionary 'dict_data'.


