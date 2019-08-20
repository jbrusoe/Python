#comboLock - Version 1
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

def comboLock(num1,num2,num3,num4,num5):

    #First check that all numbers are between 1 and 9

    ##First Number
    print("num1: " + str(num1))
    if num1 < 10 and num1 > 0:
        print("num1 is valid")

        if num1%2 == 1:
            print("num1 is odd")
        else:
            print("num1 is even")
            print("You are locked out!")
            return
    else:
        print("num1 is invalid")
        print("You are locked out!")
        return

    ##Second Number
    print("num2: " + str(num2))    
    if num2 < 10 and num2 > 0:
        print("num2 is valid")
        
        if num2%2 == 0:
            print("num2 is even")
        else:
            print("num2 is odd")
            print("You are locked out!")
            return
    else:
        print("num2 is invalid")
        print("You are locked out!")
        return

    ##Third Number
    print("num3: " + str(num3))
    if num3 < 10 and num3 > 0:
        print("num3 is valid")

        if num3%2 == 1:
            print("num3 is odd")
        else:
            print("num3 is even")
            print("You are locked out!")
            return
    else:
        print("num3 is invalid")
        print("You are locked out!")
        return

    ##Fourth Number
    print("num4: " + str(num4))
    if num4 < 10 and num4 > 0:
        print("num4 is valid")
 
        if num4%2 == 0:
            print("num2 is even")
        else:
            print("num4 is odd")
            print("You are locked out!")
            return
        
    else:
        print("num4 in invalid")
        print("You are locked out!")
        return

    ##Fifth Number
    print("num5: " + str(num5))
    if num5 < 10 and num5 > 0:
        print("num5 is valid")

        if num5%2 == 1:
            print("num5 is odd")
            print("You opened the lock!")
        else:
            print("num5 is even")
            print("You are locked out!")
            return
        
    else:
        print("num5 is invalid")
        print("You are locked out!")
        return

    return

comboLock(9,2,5,4,1)
print("************************")
comboLock(1,8,3,6,8)
print("************************")
comboLock(2,2,5,6,4)
print("************************")
comboLock(9,8,7,8,10)
    
