#largest.py
#Purpose: Select the largest of three floating point numbers
#Based on problem 2 from -
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/hw/hw05-functions.pdf
#
#Written by: Jeff Brusoe
#Last Updated: April 30, 2019

def largest(num1,num2,num3):
    LargestNumber = num1

    if num2 > LargestNumber:
        LargestNumber = num2

    if num3 > LargestNumber:
        LargestNumber = num3

    return LargestNumber

#Example 1
print("Example 1")
print("Number1 = 5.7")
print("Number2 = 6.2")
print("Number3 = 1.2")
print("Largest: " + str(largest(5.7,6.2,1.2)))
print("****************")

#Example 2
print("Example 2")
print("Number1 = 4.5")
print("Number2 = 5.6")
print("Number3 = 5.6")
print("Largest: " + str(largest(4.5,5.6,5.6)))
print("****************")




    
