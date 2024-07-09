import random

user_wins = 0
computer_wins = 0

option = ["Rock, Paper, Scissors"]

while True:
    user_input = input("Enter Rock, Paper, Scissors or q to quit").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue

    random_number = random.randit(0, 2)

    computer_pick = options[random_number]

    if user_input == "Paper" and computer_input == "Rock":
        print("You won!!!!!")
        user_win += 1
        continue

    elif user_input == "Rock" and computer_input == "Scissors":
        print("You won!!!!!")
        user_win += 1
        continue

    elif user_input == "Scissors" and computer_input == "Paper":
        print("You won!!!!!")
        user_win += 1
        continue

    else:
        print("You Lost!!!!")
        computer_wins += 1
print("You won", user_wins, " times.")
print("The computer won", computer_wins, "times.")
print("BYE!!!!")