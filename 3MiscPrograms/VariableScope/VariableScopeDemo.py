#Python - Variable Scope Demo
#Written By: Jeff Brusoe
#Last Updated: February 7, 2020

GlobalVariable1 = "Global definied outside of function"

def ScopeDemo():
    print("Inside the function")
    global GlobalVariable2
    GlobalVariable2 = "Global defined inside of function"
    FunctionLocalVariable = "Local variable in function"
    print(GlobalVariable1)
    print(FunctionLocalVariable)
    print("Leaving function\n")

ScopeDemo()
print("Outside the function:",GlobalVariable1)
print("Outside the function:",GlobalVariable2)

print("Attempting to print local variable from function:")
print(FunctionLocalVariable) # Out of scope, so this gives an error
