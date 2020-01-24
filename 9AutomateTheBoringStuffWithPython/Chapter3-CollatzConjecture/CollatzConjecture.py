#Collatz Conjection
#Written by: Jeff Brusoe
#Last Updated: January 24, 2020

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

#Main program
while True:
    try:
        #int() converts string input to a number. An error will be raised
        #if the input is not a number as well as not an integer.
        CurrentNumber = int(input("Enter a positive integer: "))

        if CurrentNumber < 1:
            print("Please enter an integer which is greater than 0")
        else:
            print("Beginning Number: " + str(CurrentNumber))
            break
    except:
        print("Please enter an integer which is greater than 0.")


while CurrentNumber != 1:
    CurrentNumber = collatz(CurrentNumber)
