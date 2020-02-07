#Python Even/Odd function demo

#Written by: Jeff Brusoe
#Last Updated: March 30, 2019

import random

def EvenOdd(TestNumber):
    if TestNumber%2 == 0:
        print(str(TestNumber) + " is even.")
    else:
        print(str(TestNumber) + "Is odd.")

for i in range(1,21):
    EvenOdd(random.randint(1,100))
    
