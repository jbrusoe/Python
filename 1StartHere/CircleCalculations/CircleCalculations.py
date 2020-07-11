#Circle Calculations
#Filename: CircleCalc.py
#Version: 1.0
#Language: Python
#
#Written By: Jeff Brusoe
#Date: February 2, 2015
#Email: jbrusoe@gmail.com
#
#This program is a sample program written for a Programming merit badge class.
#I used this as an example of how to do output, input, loops, and if/then statements in Python.
#
#The purpose of this program is to take the radius of a circle and 
#calculate the circle's area and circumference.
#
#Some possible changes to this program include the following.  
#These are only suggestions, and many other things can be changed.
#
#1.  Calculate the circle's diameter and display it.
#
#2.  Prevent certain numbers from being entered as a radius.  
#    For example, don't allow the radius to be above 30 cm.
#
#3.  Ensure a standardized format for number output.

#Variable declarations
Radius = 0.0
Circumference = 0.0
Area = 0.0
PI = 3.14

print ("This program calculates the circumference and area of a circle.\n")

#See https://wiki.python.org/moin/WhileLoop for the reason behind while true
while True:
    try:
        Radius = float(input("Enter the radius in cm: "))

        if Radius > 0:
            break
        else:
            print ("The radius must be greater than zero.")
    except:
        #This gets executed if letters or other non-numeric characters are entered for the radius.
        print ("The radius can't have letters in it.")

#Calculations and Output
print ("Radius(cm): " +  str(Radius))

Circumference = 2*PI*Radius
print ("Circumference(cm): " + str(Circumference))

Area = PI*Radius*Radius
print ("Area(sq cm): " + str(Area))

input ("\nPress the enter key to close window.")
