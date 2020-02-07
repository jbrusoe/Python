#File to tell whether an entered number is even or odd.
#Written by: Jeff Brusoe
#Last Updated: February 7, 2020
#
#Note:  This version verifies that the number entered is an integer.

while True:
    try:
        InputNumber = int(input("Please enter an integer: "))
        print("Entered Number:",InputNumber)
        break
    except:
        print("Please enter a valid integer.")

if int(InputNumber)%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
