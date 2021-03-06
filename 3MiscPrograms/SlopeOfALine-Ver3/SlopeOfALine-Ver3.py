#Slope of a line - Version 3

#Version 3 adds code to check for valid user input (acutally a number not a string or just hitting the enter key)
#It is not done with a function which will be done in version 4.

#Written by: Jeff Brusoe
#Last Updated: August 10, 2019

#First Point
while True:
    try:
        x1 = float(input("Enter the first x coordinate: "))
    except:
        print("Plesae enter a valid number for the first point")
    else:
        break

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
