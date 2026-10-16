'''
Number Guessing Game is a game in which the computer randomly selects a number between 1 and 100. 
The user must guess the number within a limited number of attempts. 
After each incorrect guess, the program provides a hint indicating whether the guess is too low or too high.

In this game, randint() is used to generate a random number within the specified range.

Winning Rules
Computer generates a random number between 1 and 100.
User has a maximum of 7 attempts to guess the number.
User wins immediately if the guess matches the randomly generated number.
If the guess is lower than the selected number, the program displays "Too Low" and the user should try a higher number.
If the guess is higher than the selected number, the program displays "Too High" and the user should try a lower number.
Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.
If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.

'''

import random

def pick_number():
    answer = random.randint(1,100)
    user_guess = int(input("enter a number, between 1 and 100: "))
    attempts = 1
    max_attempts = 6
    print("answer is: ",answer)

    while user_guess != answer and attempts <= max_attempts:
        if user_guess > answer:
            user_guess = int(input("you have to go lower: "))
        elif user_guess < answer:
            user_guess = int(input("you have to go higher: "))
        max_attempts = max_attempts - 1
        print(max_attempts," attempts remaining.")
    if user_guess == answer:
        print("the number was ",answer,". You picked ",user_guess,"in ",7 - max_attempts," tries !")
    else:
        print("you failed! the answer was: ",answer)

print("\nWelcome to number guessing game! you have 7 tries to guess the number (1-100)\n")
pick_number()