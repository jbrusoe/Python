#CalculationOfe.py
#Written by: Jeff Brusoe
#Last Updated: October 5, 2019
#
#This program simulates calculating lim n-> infinity (1+1/n)^n
#See https://en.wikipedia.org/wiki/E_(mathematical_constant)

def Calce(n):
    return pow((1+(1/n)),n)

NumberOfIterations = int(input("Maximum number: "))
print("Number of iterations: " + str(NumberOfIterations))

print("\n i\te Calculated")
print("===\t============")
for i in range (1,NumberOfIterations):
    print(str(i)+"\t" + str(Calce(i)))

