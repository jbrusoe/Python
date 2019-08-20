#Function Demo - Height restrictions
#Written by: Jeff Brusoe

#Based on Problem 1 from this homework set:
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/hw/hw05-functions.pdf

def superman(height):
    print("Height: " + str(height))
    
    if height >= 56:
        print("Have a great ride!")
    else:
        print("Sorry! You must be at least 56 inches to ride.")

superman(30)
print("*************")
superman(70)
