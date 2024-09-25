shopping_list = ["eggs", "bread", "banana", "biscuits", "milk"]

# Print the list
print(shopping_list)

# Print the data type
print(type(shopping_list))

# Print the first item in the list
print(shopping_list[0])

# Print the last item in the list
print(shopping_list[-1])

# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to
# prove it's been changed

shopping_list[1] = "rice"

print(shopping_list)

# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='),
# then check the length of the list (which should now have 6 rather than 5)

shopping_list.append("carrots")
print(shopping_list)  # All 6 food items
print(len(shopping_list))  # Output 6

# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods
# to add the two items in one go.

new_list = ["toffee", "coffee"]  # Build new list

shopping_list.extend(new_list)  # Extend the original list with the new list
print(shopping_list)

# Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
shopping_list.remove("banana")
print(shopping_list)

# Remove the last item ('coffee') from 'shopping_list' using the pop method.
# Check it worked by printing 'shopping_list'

shopping_list.pop()  # Pop always removes the last item from the list if empty
print(shopping_list)

