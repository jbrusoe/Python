import math
import cmath

print("Method 1 to create complex number - Add j to a number")
z1 = 2 + 3j
print(z1)

print("\nMethod 2 to create complex number - complex(real,img)")
z2 = complex(2,3)
print(z2)

print("\nComplex conjugate")
print(z1.conjugate())


print("\nCreating complex number i*pi")
z3 = complex(0,math.pi)
print(z3)

print("\nexp(i*pi) = " + str(cmath.exp(z3)))
