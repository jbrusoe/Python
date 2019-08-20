#Replace Odd Numbers in Array with -1
#Problem 5 from - https://www.machinelearningplus.com/python/101-numpy-exercises-python/

#Written by: Jeff Brusoe
#Last Updated: February 4, 2019

import numpy as np

print("Goal: Replace odd elements with -1\n")

x=np.array([3,7,25,24,26,33,-1,-2])
print("Original Array:","\n",x,"\n")

x[x%2==1] = -1
print("New Array Array:","\n",x,"\n")