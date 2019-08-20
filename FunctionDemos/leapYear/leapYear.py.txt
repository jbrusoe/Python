#Function Demo - Leap Year Calculation
#Written by: Jeff Brusoe
#Last Updated: April 30, 2019

#Based on Problem 3 from this homework set:
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/hw/hw05-functions.pdf

def leapYear(Year):
    print("Input Year: " + str(Year))

    if Year%4 == 0 and Year%100 > 0:
        #This is a leap year
        ReturnValue = "is a leap year."
    elif Year%4 == 0 and Year%100 == 0 and Year%400 == 0:
        #This is a leap year.
        ReturnValue = "is a leap year."
    else:
        ReturnValue = "is not a leap year."

    return ReturnValue

for i in range(1900,2101):
    print(str(i) + " " + leapYear(i))
    print("***********************")

