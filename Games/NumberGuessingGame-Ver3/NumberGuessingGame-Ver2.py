#Python - Number Guessing Game
#Version 2 - Includes Exception Handling
#Written By: Jeff Brusoe
#Laast Updated: April 25, 2019

import random

RandomNumber = random.randint(1,100)

while True:
    InputNumber = int(input("Enter your guess: "))

    if InputNumber == RandomNumber:
        print("Correct!")
        break
    elif InputNumber > RandomNumber:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
