#Exercise 4 from https://www.machinelearningplus.com/python/101-numpy-exercises-python/
#Get odd elements from array
#
#Written by: Jeff Brusoe

import numpy as np

print("Goal: Remove odd elements from an array\n")

x=np.array([3,7,25,24,26,33,-1,-2])
print("Original Array:","\n",x,"\n")

OddArray = x[x%2==1]
print("Odd Array: ",OddArray,"\n")

print("Output from np.mod()")
remainders = np.mod(x,2)
print(remainders)
