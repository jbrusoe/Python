#Slope of a line - Version 3

#Version 2 adds code to check for valid user input (acutally a number not a string or just hitting the enter key)

#Written by: Jeff Brusoe
#Last Updated: August 10, 2019

#First Point
x1 = float(input("Enter the first x coordinate: "))
y1 = float(input("Enter the first y coordinate: "))

#Second Point
x2 = float(input("Enter the second x coordinate: "))
y2 = float(input("Enter the second y coordinate: "))

try:
    slope = (y2-y1)/(x2-x1)
except ZeroDivisionError:
    print("The x values are equal. The slope is undefined.")
except:
    print("An error occurred.")
else:
    print("The slope of the line is " + str(slope) + ".")
