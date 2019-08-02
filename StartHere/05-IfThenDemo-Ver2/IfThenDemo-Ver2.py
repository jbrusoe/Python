#Python If/Then Demo
#Written by: Jeff Brusoe
#Last Updated: February 25, 2019

import random

Number1 = random.randint(0, 9)
Number2 = random.randint(0, 9)

print("First Number:",Number1)
print("Second Number:",Number2)

if Number1 >= 5:
    print("Number1 is greater than or equal to 5.")
else:
    print("Number1 is less than 5.")

if Number2 >= 5:
    print("Number2 is greater than or equal to 5.")
else:
    print("Number2 is less than 5.")

if Number1 > Number2:
    print("Number 1 is greater than Number 2.")
elif Number1 < Number2:
    print("Number 1 is less than Number2.")
else:
    print("Number1 equals Number2")
