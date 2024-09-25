# User story 1

# As a user, I want to be able to guess a number and know if I got it correct or not, so that I
# can know if I won or not.


# Define/assign number to a variable called magic_number

# Ask user for input

# Check if this input matches magic_number

# Let the user know if the response was correct or not

# Allow the user 5 guesses

import random

guess = True
attempts = 0
magic_number = random.randrange(1, 50)


while guess is True:  # While guess is true, the input will repeat
    user_guess = input("I've got a magical number floating around in my CPU "
                       "between 1 and 50. Bet you can't guess it in 5, loser: ")

    if user_guess.isdigit():  # Checks to make sure the guess is a digit and converts it to an int
        user_guess_int = int(user_guess)

        if 1 <= user_guess_int <= 50:  # Checks to see if the user's guess is between 1 and 50
            if user_guess_int == magic_number:  # Checks to see if it matches the magic number. If so, game ends
                guess = False
                print("Ok smarty pants... You got lucky. Get out of my sight.")

            elif magic_number > int(user_guess):  # Checks if the magic number is greater than the guess
                print("Too low idiot.")
                attempts += 1  # Add attempt to counter
                print(attempts)
            elif magic_number < int(user_guess):  # Checks if the magic number is lower than the guess
                print("Too high idiot.")
                attempts += 1
                print(attempts)

        if attempts == 5:  # If attempts reaches 5, game ends
            guess = False
            print(f"Wow... You actually SUCK. Go away. The magic number was {magic_number}.")
    else:  # Print error message if user inputs regular text or guesses outside the range
        print("I need numbers fool. I should take an attempt for that... BUT I WON'T. "
              "Also it needs to be between 1 and 50. Idiot.")
