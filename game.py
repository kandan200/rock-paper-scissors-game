import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = input("rock, paper, or scissors?: ").lower()
    while player not in choices:
        print("wrong selection, try again")
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Player: ", player, ": CPU: ", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Player: ", player, ": CPU: ", computer)
            print("You Lose")
        if computer == "scissors":
            print("Player: ", player, ": CPU: ", computer)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("Player: ", player, ": CPU: ", computer)
            print("You Lose")
        if computer == "paper":
            print("Player: ", player, ": CPU: ", computer)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("Player: ", player, ": CPU: ", computer)
            print("You Lose")
        if computer == "rock":
            print("Player: ", player, ": CPU: ", computer)
            print("You win")
    aftermath = input("Would you want to play again? [yes/no]").lower()
    if aftermath == "yes":
        pass
    elif aftermath == "no":
        print("Thank you")
        break
