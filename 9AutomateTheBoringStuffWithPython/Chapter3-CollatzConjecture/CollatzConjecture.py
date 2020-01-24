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

while True:
    try:
        CurrentNumber = int(input("Enter a positive integer: "))
        print("Beginning Number: " + str(CurrentNumber))
        break
    except:
        print("Invalid input")


while CurrentNumber != 1:
    CurrentNumber = collatz(CurrentNumber)
