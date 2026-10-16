'''
rock paper scissors game
user will input their pick, computer will randomly select a pick, and winner will be calculated and displayed. 
'''

import random

looping = True
while looping == True:
    user_pick = input("""select one: 
    rock
    paper
    scissors
    \n
    """)
    print()
    print("you have picked: ",user_pick)
    computer_pick = random.choice(["rock", "paper", "scissors"])
    print("computer has picked: ",computer_pick)
    print()

    if user_pick == "rock":
        if computer_pick == "rock":
            print("draw")
        elif computer_pick == "paper":
            print("you lose")
        else:
            print("you win")

    elif user_pick == "paper":
        if computer_pick == "rock":
            print("you win")
        elif computer_pick == "paper":
            print("draw")
        else:
            print("you lose")

    else:
        if computer_pick == "rock":
            print("you lose")
        elif computer_pick == "paper":
            print("you win")
        else:
            print("draw")
    play = input("again?: y / n\n")
    print()
    if play == "y":
        looping = True
    else:
        looping = False