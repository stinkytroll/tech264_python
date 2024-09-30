# Before finishing the game below, answer these questions:

# How are tuples similar to lists?
# Tuples used to store multiple items in a single variable. They are ordered and unchangeable.

# Are tuples immutable and what does this mean?
# Yes, as they cannot be changed once created. This means we cannot append it like we could a list.

# What other data types are immutable?
# Numbers, boolean, and strings.

# What is a good use case for tuples?
# Useful for storing data that you do not want to change later, preventing accidental changes. They are
# also good for storing coordinates in 2D or 3D spaces, as they are an ordered pair of set values.

# What does the following piece of code do?
# Prints the list "essentials" and prints the number of times bread appears.
essentials = ("bread", "eggs", "milk")

print(essentials)

print(essentials.count("bread"))

# "Stranded on a Desert Island" game

# Rationale: Practice tuples

# Type of exercise: Finish the code

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ")

essential_item2 = input("What is an essential item you would take? ")

essential_item3 = input("What is an essential item you would take? ")

# save the items as a tuple

essentials_tuple = (essential_item1, essential_item2, essential_item3)

# print the tuple

print("Here are your items as a tuple:", essentials_tuple)

print("")

print("I lied. You can take one more item.")

essential_item4 = input("What is one more essential item you would take? ")


# try to add the 4th item to the tuple

# if you can't add the 4th item, work out how to save the 4th item to the tuple

new_tuple = (essentials_tuple, essential_item4)
print(new_tuple)
