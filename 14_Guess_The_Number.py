# Guess the number Game

import random

number = random.randint(0,101)
attempt=1
guess = int(input("Guess the number between 0 and 100\n"))

while(True):
    if(guess>number):
        guess = int(input("Guess another 'cause it's greater than the number\n"))
        attempt+=1
    elif(guess<number):
        guess = int(input("Guess another 'cause it's smaller than the number\n "))
        attempt+=1
    else:
        print(f"Yo that's the number, You guessed it in {attempt} attempt(s)")
        break