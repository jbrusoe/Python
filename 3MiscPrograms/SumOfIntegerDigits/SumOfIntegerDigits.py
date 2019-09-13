#Written by: Jeff Brusoe
#Demo for Programming Merit Badge class
#
##Liang Textbook - Chapter 2, Problem 6
#Sum the digits of a number
#
#Version 3 - Using for loop & with exception handling
#
#Note: Version 3 is the same logic as version 2, but it also contains error handling.

while True:
    #First verify that what gets entered is actually an integer
    try:
        EnteredNumber = input("\nEnter a positive integer: ")
        print("Entered number:",EnteredNumber)

        intEnteredNumber = int(EnteredNumber)

        if intEnteredNumber >= 0:
            break
        else:
            print("Please enter a positive integer.")
        
    except:
        print("Please enter a number")


StringLength = len(EnteredNumber)
print("Number Length:", StringLength)

Sum = 0

for i in range(StringLength):
    print("Current Number:", EnteredNumber[i])
    Sum = Sum + int(EnteredNumber[i])

print("Total Sum:",Sum)