import numpy as np

print("Generating Matrix...")
Matrix = np.arange(6).reshape((2,3))

print("\nOriginal Matrix:")
print(Matrix)

print("\nTransposed Matrix:")
print(np.transpose(Matrix))

