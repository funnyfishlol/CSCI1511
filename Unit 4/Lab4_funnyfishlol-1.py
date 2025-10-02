"""Card Dealer - Nathan Henneman - Randomly create hand of cards - September 21"""
import random
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9' ,'10', 'J', 'Q', 'K']
suits = ['c', 'h', 's', 'd']
deckSize = input("How many cards in the hand?: ")

for i in range(0, int(deckSize)):
    print(random.choice(ranks) + random.choice(suits))
