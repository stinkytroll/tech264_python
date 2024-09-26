x = 0

while x < 10:
    print(x)
    x += 1  # If you don't increment x, it will print x indefinitely as it will never become less than 10.


# Once your code works, find out what happens when you run the code if you comment out the first
# line which initialises 'x'.

# You get an error due to x not being defined.

# Write a brief comment on the line before the code which increments x to explain what would happen
# if you don't increment x.


# Copy and paste your working 'while loop' underneath the 'while loop'. Modify the second copy of the
# 'while loop' so that it breaks out of the loop when x equals 4.

while x < 10:
    print(x)
    x += 1
    if x == 4:
        break
