#Function Demo with Multiplication

#Written by: Jeff Brusoe
#Last Updated: March 28, 2019

import random

def Multiplication(First,Second):
    print(str(First) + " * " + str(Second) + " = " + str (First*Second))
    
for i in range (0,21):
    FirstNumber = random.randint(1,20)
    SecondNumber = random.randint(1,20)
    Multiplication(FirstNumber,SecondNumber)
    
