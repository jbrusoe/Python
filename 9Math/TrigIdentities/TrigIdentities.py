#TrigIdentities.py
#Written by: Jeff Brusoe
#Last Updated: October 5, 2019
#
#This file demonstrates the validitiy of sin^2+cos^2 = 1 and tan = sin/cos.

import math

print("Degrees\tRadians\t\tSin(x)\tSin(x)^2\tCos(x)\tCos(x)^2\tSin(x)^2 + Cos(x)^2\tTan(x)\tSin(x)/Cos(x)")
print("=======\t=======\t\t======\t=======\t\t======\t======\t\t===================\t=======\t=========")

for i in range(0,360):
    OutputString = ""
    
    Radians = round(math.radians(i),4)
    OutputString = str(i) + "\t" + str(Radians) + "\t\t"

    Sin = round(math.sin(Radians),4)
    OutputString += str(Sin) + "\t"
    
    SinSquared = round(pow(math.sin(Radians),2),4)
    OutputString += str(SinSquared) + "\t\t"

    Cos = round(math.cos(Radians),4)
    OutputString += str(Cos) + "\t"

    CosSquared = round(pow(Cos,2),4)
    OutputString += str(CosSquared) + "\t\t\t"

    Sum = round((SinSquared + CosSquared),3)
    OutputString += str(Sum) + "\t\t"

    if Cos != 0:
        Tan = round(math.tan(Radians),4)
        OutputString += str(Tan) + "\t"

        SinDivCos = round((Sin/Cos),4)
        OutputString += str(SinDivCos)
        
    else:
        OutputString += "Undefined\tUndefined"
        
    print(OutputString)
