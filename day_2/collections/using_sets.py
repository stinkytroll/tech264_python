# Explain 2 main ways that sets are different to lists and tuples
# Sets are used to store multiple unique elements. They are mutable, unlike tuples.

# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}

# Print the set 'fruits'
print(fruits)

# Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")

# Print the set 'fruits' - check it's added
print(fruits)

# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")

# Print the set 'fruits' - check it's removed
print(fruits)

# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple")  # Will not add, as it only allows for unique elements.

# Print the final fruits set.
print(fruits)

# Print the 2nd item in the set. If there is any problem doing this, explain.
# This is not possible as the list is unordered. You must first convert it to a list.

fruits_list = list(fruits)
print(fruits_list[1])

