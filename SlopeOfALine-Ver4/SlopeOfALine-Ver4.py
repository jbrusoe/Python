#Slope of a line - Version 4

#Version 4 adds code to check for valid user input with a function unlike version 3.
#This does not use the built in isdigit() function. That will be done in version 5.

#Written by: Jeff Brusoe
#Last Updated: August 10, 2019

def get_valid_input(InputString):
#InputSring is the message displayed by the input statement.
    while True:
        
        try:
            UserInput = float(input(InputString))
        except:
            print("Please enter a number.")
        else:
            return UserInput

#First Point
x1 = get_valid_input("Enter the first x coordinate: ")
y1 = get_valid_input("Enter the first y coordinate: ")


#Second Point
x2 = get_valid_input("Enter the second x coordinate: ")
y2 = get_valid_input("Enter the second y coordinate: ")                              

try:
    slope = (y2-y1)/(x2-x1)
except ZeroDivisionError:
    print("The x values are equal. The slope is undefined.")
except:
    print("An error occurred.")
else:
    print("The slope of the line is " + str(slope) + ".")
