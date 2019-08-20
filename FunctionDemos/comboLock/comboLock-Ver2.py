#comboLock
#Purpose: Select the largest of three floating point numbers
#Based on problem 5 from -
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/hw/hw05-functions.pdf
#
#Written by: Jeff Brusoe
#Last Updated: May 2, 2019
#
#Note: This would be better done with Python lists. However, the problem
#statement states to do this with the individual variables.
#
#Lock is opened if all numbers are between 1 and 9.
#Number order should be odd,even,odd,even,odd


def CheckNumber(num,VariableName,EvenOrOdd):
    #num -> The actual number to be evaluated
    #VariableName -> Name of variable used in program for output purposes
    #EvenOrOdd -> Whether num should be even or odd
    #Returns -> 0(Invalid) or 1 (Valid)

    print(VariableName + ": " + str(num))
    if num < 10 and num > 0:
        print(VariableName + "is valid")

        if num%2 == 0 and EvenOrOdd == "Even":
            print(VariableName + " is even.")
        elif num%2 ==1 and EvenOrOdd == "Odd":
            print(VariableName + " is odd")
        else:
            print(VariableName + " is not " + EvenOrOdd) 
            print("You are locked out!")
            return 0
    else:
        print(VariableName + " is invalid.")
        print("You are locked out!")
        return 0

    return 1
        

def comboLock(num1,num2,num3,num4,num5):

    CanContinue = 0
    
    CanContinue = CheckNumber(num1,"num1","Odd")

    if CanContinue == 1:
        CanContinue = CheckNumber(num2,"num2","Even")

    if CanContinue == 1:
        CanContinue = CheckNumber(num3,"num3","Odd")

    if CanContinue == 1:
        CanContinue = CheckNumber(num4,"num4","Even")

    if CanContinue == 1:
        CanContinue = CheckNumber(num5,"num5","Odd")

    if CanContinue == 1:
        print("You opened the lock!")
        

comboLock(9,2,5,4,1)
print("************************")
comboLock(1,8,3,6,8)
print("************************")
comboLock(2,2,5,6,4)
print("************************")
comboLock(9,8,7,8,10)
    
