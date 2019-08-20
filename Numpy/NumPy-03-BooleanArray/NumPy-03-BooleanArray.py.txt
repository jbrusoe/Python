#Exercise 3 from https://www.machinelearningplus.com/python/101-numpy-exercises-python/
#Create a 3×3 numpy array of all True’s
#
#Written by: Jeff Brusoe

import numpy as np

print("Goal: Create a 3x3 numpy array of all True's\n")

print("Generating Array...","\n")
x = np.full((3,3),True)
print(x,"\n")

print("Array Type: ", x.dtype)
print("Array Shape: ", x.shape)
print("Array Size: ", x.size)