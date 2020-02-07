#File to tell whether an entered number is even or odd.
#Written by: Jeff Brusoe
#Last Updated: February 7, 2020
#
#Note:  There is no error handling with this code. It assumes that
#       number entered is valid. See ver 2 for error handlng code.

InputNumber = input("Please enter an integer: ")
print("Entered Number: ",InputNumber)

if int(InputNumber)%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
