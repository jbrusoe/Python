#Python Square Root & While Loop Demo
#Written by: Jeff Brusoe

import math #Needed for square root function

#This block of code is used to ensure that a valid number is entered.
#Note: Entering a non-integer value is not caught in this version.
while True:
    UserInput = int(input("Enter a number between 0 and 1000: "))

    print("You entered: " + str(UserInput))

    if UserInput < 0 or UserInput >1000:
        print("That is an invalid number. Please try again.")
    else:
        print("That is a valid number. Program is proceeding.")
        break

#Now that a valid number has been entered, use a loop to print the table.
count = 0
print("Current Number\tSquare Root")

while count <= UserInput:
    print(str(count) + "\t\t" + str(math.sqrt(count)))
    count += 1 #Same as count = count + 1

