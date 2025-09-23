"""Dice Roller - Nathan Henneman - Rolls Dice and Returns Term - September 23, 2025"""
import random
game_continue = "y"

while(game_continue == "y"):
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    dice_total = die_1 + die_2
    print(f"Die 1: {die_1} | Die 2: {die_2} | Total: {dice_total}")

    if(dice_total == 2):
        print("Snake Eyes!")
    elif(dice_total == 3):
        print("Ace Caught a Deuce!")
    elif(dice_total == 5):
        print("Little Phoebe!")
    elif(dice_total == 9):
        print("Nina from Pasadena!")
    elif(dice_total == 12):
        print("Boxcars!")

    if(die_1 == 2 and die_2 == 2):
        print("Little Joe from Kokomo!")
    elif(die_1 == 3 and die_2 == 3):
        print("Jimmy Hicks from the Sticks!")
    elif(die_1 == 4 and die_2 == 4):
        print("Eighter from Decatur!")
    elif(die_1 == 5 and die_2 == 5):
        print("Puppy Paws!")
    elif((die_1 == 6 and die_2 == 1) or (die_1 == 1 and die_2 == 6)):
        print("Six Ace!")
    elif((die_1 == 6 and die_2 == 5) or (die_1 == 5 and die_2 == 6)):
        print("Six Five no Jive!")
    game_continue = input("Do you want to roll again? (y/n) ").lower()