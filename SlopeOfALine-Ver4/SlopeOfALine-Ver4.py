#Slope of a line - Version 4

#Version 4 adds code to check for valid user input with a function unlike version 3.
#This does not use the built in isdigit() function. That will be done in version 5.

#Written by: Jeff Brusoe
#Last Updated: August 10, 2019

def isValidInput(UserInput):

    try:
        float(UserInput)
    except:
        print("Please enter a number.")
        return False
    else:
        return True

#First Point

UserInput = ""
while not isValidInput(UserInput):
        UserInput = input("Enter the first x coordinate: ")

x1 = float(UserInput)
UserInput = ""

while True:
    try:
        y1 = float(input("Enter the first y coordinate: "))
    except:
        print("Plesae enter a valid number for the first point")
    else:
        break


#Second Point
while True:
    try:
        x2 = float(input("Enter the second x coordinate: "))
    except:
        print("Plesae enter a valid number for the first point")
    else:
        break

while True:
    try:
        y2 = float(input("Enter the second y coordinate: "))
    except:
        print("Plesae enter a valid number for the first point")
    else:
        break


try:
    slope = (y2-y1)/(x2-x1)
except ZeroDivisionError:
    print("The x values are equal. The slope is undefined.")
except:
    print("An error occurred.")
else:
    print("The slope of the line is " + str(slope) + ".")
