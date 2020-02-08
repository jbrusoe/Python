#List as Stack(Last in, First out) Demo

def PrintStack(stack):
    print("Current Stack:")
    print(stack)
          
stack = [3,4,5]
PrintStack(stack)

print("\nAdding 6 to stack")
stack.append(6)
PrintStack(stack)

print("\nAdding 7 to stack")
stack.append(7)
PrintStack(stack)

for i in range(0,3):
    print("\nPopping from stack")
    print("Element removed from stack:",stack.pop())
    PrintStack(stack)

