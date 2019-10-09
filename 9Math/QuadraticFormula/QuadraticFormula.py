#Python - Quadratic Equation Solver
#Written by: Jeff Brusoe
#Last Updated: July 8, 2019

import math

print("General form of a quadratic equation:\nax^2+bx+c=0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b**2 - 4*a*c

print("Discriminant: " + str(discriminant))

if discriminant < 0:
    print("The discriminant is less than 0. The answers will involve complex numbers")
else:
    print("The discriminant is greather than or equal to zero.")
    print("Therefore, real number solutions exist.")

    if discriminant == 0:
        Solution = (-b/(2*a))
        print ("x = " + str(Solution))
    else:
        Solution1 = (-b + math.sqrt(discriminant))/(2*a)
        Solution2 = (-b - math.sqrt(discriminant))/(2*a)

        print("Solution 1: " + str(Solution1))
        print("Solution 2: " + str(Solution2))

    

