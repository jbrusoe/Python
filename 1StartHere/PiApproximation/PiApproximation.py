#Liang - Chapter 1, Problem 1.7
#Written by: Jeff Brusoe
#Last Updated: February 6, 2020

MaxDenominator = int(input("Enter the maximum denominator: "))

paren = 0
Sign = -1

for i in range (1,MaxDenominator,2):
    Sign = -1*Sign
    paren += Sign*(1.0/i)

    Pi = 4*paren
    print("i = ", i)
    print("pi = ", Pi)
    print("***************")


