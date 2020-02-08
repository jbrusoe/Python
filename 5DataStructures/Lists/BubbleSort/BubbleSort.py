#Python Bubble Sort Demonstration
#Written by: Jeff Brusoe
#Last Updated: May 23, 2019

#For students to try/consider:
#1. Can you rewrite this to put the bubble sort piece into a function?
#2. How would this change if you used a numpy array?
#3. Is bubble sort a good idea to use on this list? What happens
#   if there are a million integers? Why or why not?
#3a. If the answer to number 3 is no, what algorithm should be used.
#4. Is there a better way to implement this?

import random

#Part 1: Generated a random list of 20 numbers between 1 and 100
UnsortedList = []

for i in range (1,20):
    UnsortedList.append(random.randint(1,100))

print("Original List:\n", UnsortedList)

#Now pass that list through the bubble sort algorithm
print("Begin Sorting")

LoopCount = 1
NoSwap = False

while NoSwap == False:
    print("Pass " + str(LoopCount))
    LoopCount += 1

    NoSwap = True
    
    for i in range(0,len(UnsortedList)-1):
        if UnsortedList[i+1] < UnsortedList[i]:
            #Need to swap
            Temp = UnsortedList[i+1]
            UnsortedList[i+1] = UnsortedList[i]
            UnsortedList[i] = Temp
            NoSwap = False

    print(UnsortedList)
    print("*******************")
    
    if NoSwap == True:
        break
            
    
    
