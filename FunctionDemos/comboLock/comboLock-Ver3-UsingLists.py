#comboLock
#Purpose: Select the largest of three floating point numbers
#Based on problem 5 from -
#http://www.mathcs.emory.edu/~valerie/courses/fall10/155/hw/hw05-functions.pdf
#
#Written by: Jeff Brusoe
#Last Updated: May 2, 2019
#
#Note: This would be better done with Python lists. However, the problem
#statement states to do this with the individual variables.
#
#Lock is opened if all numbers are between 1 and 9.
#Number order should be odd,even,odd,even,odd

def comboLock(InputNumbers):

    print("Input List: " + str(InputNumbers))

    Length = len(InputNumbers)
    if Length == 5:
        print("Valid number of parameters passed to function")
    else:
        print("Invalid number of parameters passed to function")
        print("You are locked out!")
        return

    for i in range(0,Length):
        print("Current Number: " + str(InputNumbers[i]))
        if InputNumbers[i] < 10 and InputNumbers[i] > 0:
            print("Element " + str(i) + " is valid")

            if i%2 == 0 and InputNumbers[i]%2 == 1:
                print("Element " + str(i) + " is odd")
            elif i%2 ==1 and InputNumbers[i]%2 == 0:
                print("Element " + str(i) + " is even")
            elif i%2 == 0:
                #Should be an odd number
                print("Element " + str(i) + " is not odd") 
                print("You are locked out!")
                return
            else:
                print("Element " + str(i) + " is not even") 
                print("You are locked out!")
                return
        else:
            print("Number out of range...")
            print("You are locked out!")
            return
        
    print("You opened the lock!")

comboLock([9,2,5,4,1])
print("************************")
comboLock([9,2,5,4,1,7])
print("************************")
comboLock([1,8,3,6,8])
print("************************")
comboLock([2,2,5,6,4])
print("************************")
comboLock([9,8,7,8,10])
    
