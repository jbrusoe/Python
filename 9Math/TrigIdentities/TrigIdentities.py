#TrigIdentities.py
#Written by: Jeff Brusoe
#Last Updated: October 5, 2019
#
#This file demonstrates the validitiy of sin^2+cos^2 = 1 and tan = sin/cos.

import math

print("Degrees\tRadians\tSin(x)\tSin(x)^2\tCos(x)\tCos(x)^2")
print("======\t=======")
for i in range(0,360):
    print(str(i) + "\t" + str(math.radians(i)))
