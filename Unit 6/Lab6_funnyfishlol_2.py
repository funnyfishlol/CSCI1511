"""Guess My Number - Nathan Henneman - Promts the user to guess a random int from 1-100 - October 2, 2025"""

import random
guesses = 0
random_number = random.randint(1,100)
user_guess = int(input("Guess a number between 1-100: "))

while(user_guess != random_number):
    if(user_guess < random_number):
        print("Your guess was too low!")
    else:
        print("Your guess was too high!")
    user_guess = int(input("Guess another random number between 1-100: "))
    guesses+=1

print(f"Congratulations! The number was {random_number} and you got it in {guesses} guesses!")