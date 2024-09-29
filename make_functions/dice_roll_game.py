import random

dice = random.randint(1, 6)

game_choice = input("Yo. Let's play dice. Wanna do a best of 10 or first to 30? "
                    "Say 1 for best of 10, say 2 for first to 30: ")
if game_choice == "1":
    name = input("So you want to roll some dice, eh? Tell me when your name when you're ready: ")
    print(f"{name} is little weird but sure. Let's play.")
    computer_wins = 0
    player_wins = 0

    while computer_wins or player_wins < 10:
        roll = input('Say "Roll" to roll the dice: ')
        if roll == 'Roll':
            player_dice = random.randint(1, 6)
            print(f"You rolled a {player_dice}")
            computer_dice = random.randint(1, 6)
            print(f"I rolled a {computer_dice}")
            if player_dice > computer_dice:
                player_wins += 1
                print(f"Hm. your {player_dice} beat my {computer_dice}. How lucky. You win. "
                      f"The score is {player_wins} to you, {computer_wins} to me.")

            elif player_dice == computer_dice:
                print(f"Seems like we both rolled a {computer_dice}. It's a draw. No points for either of us.")
            else:
                computer_wins += 1
                print(f"Hm. my {computer_dice} beat your {player_dice}. I win, chump. "
                      f"The score is {player_wins} to you, {computer_wins} to me.")

        else:
            print('You need to say "Roll". Try again.')

    if computer_wins == 10:
        print("Looks like I win, loser. You owe me a virtual donut.")
    else:
        print(f"Wow. You actually beat me, good job {name}.")

elif game_choice == "2":
    name = input("So you wanna play first to 30, eh? Tell me when your name when you're ready: ")
    print(f"{name} is little weird but sure. Let's play.")
    computer_score = 0
    player_score = 0

    while computer_score or player_score < 30:
        roll = input('Say "Roll" to roll the dice: ')
        if roll == 'Roll':
            player_dice = random.randint(1, 6)
            print(f"You rolled a {player_dice}")
            computer_dice = random.randint(1, 6)
            print(f"I rolled a {computer_dice}")
            player_score = + player_dice
            computer_score = + player_dice
            print(f"That brings you to {player_score} and me to{computer_score}.")

