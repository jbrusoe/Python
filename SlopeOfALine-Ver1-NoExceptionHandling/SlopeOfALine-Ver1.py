#Slope of a line - Version 1

#This version doesn't have the following which will be added in subsequent versions:
#   1. Exception handling (such as verifying input points are numbers, avoiding division by zero, etc.)
#   2. Output formatting
#   3. Array demo to show a better way to handle multiple points
#   4. Function to validate user input

#Written by: Jeff Brusoe
#Last Updated: August 10, 2019

#First Point
x1 = float(input("Enter the first x coordinate: "))
y1 = float(input("Enter the first y coordinate: "))

#Second Point
x2 = float(input("Enter the second x coordinate: "))
y2 = float(input("Enter the second y coordinate: "))

slope = (y2-y1)/(x2-x1)

print("The slope of the line is " + str(slope) + ".")
