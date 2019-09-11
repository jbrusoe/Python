import numpy as np

print("NumPy Version: " + np.__version__)

print("Create Integer Array")
IntArray = np.array([1,4,2,5,3])
print(IntArray)

print("Create array of integers from 0 to 9")
IntArray = np.arange(10)
print(IntArray)

print("Create a 3x3 NumPy array")
NumPyArray = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(NumPyArray)

print("Create an array of zeros")
ArrayOfZeros = np.zeros(10,dtype="int")
print(ArrayOfZeros)

