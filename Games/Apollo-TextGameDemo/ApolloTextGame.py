#Pyton - Apollo to the Moon Text Based Game
#Written by: Jeff Brusoe
#Last Updated: April 25, 2019

import random

def InputParser(UserInput):
    
    

def CommandModule(Emergency):
    print("You are in the Apollo command module. There are many intstrument panels here.")
    print("A hatch to the lunar module is \"above\" your head and storage lockers are \"beneath\" you.")

    if Emergency==0:
        print("\nEverything is smooth so far in the mission.")
    elif Emergency==1:
        print("\nYou hear a loud bang and see a warning light which says \"Main B Bus Undervolt\"!")

    UserInput = input("\n>>>")

def LunarModule():
    print("You are in the lunar module.")

    UserInput = ("\n>>>")
    

while True:
    Emergency = random.randint(0,1)
    CommandModule(Emergency)

    if Emergency > 0:
        break
