def fizzbuzz(n):  # n represents the number that will be inputted in the function
    for count in range(1, n + 1):  # For the variable count in the range of 1 to the written number
        if count % 3 == 0 and count % 5 == 0:  # If when count is divided by 3 or 5 = 0, then print FizzBuzz
            print("FizzBuzz")
        elif count % 3 == 0:  # If when count is divided by 3 = 0, print fizz
            print("Fizz")
        elif count % 5 == 0:  # If when count is divided by 5 = 0, print buzz
            print("Buzz")
        else:  # If none are applicable, print the number
            print(count)


fizzbuzz(100)

