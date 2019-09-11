#Python Word Reverse with Function

def WordReverse(Word):
    print("Original Word: " + Word)

    print("Reversed Word: ", end="")
    
    for i in range (len(Word),0,-1):
        print(Word[i-1], end="")

    print("\n\n")


WordReverse("Python")
WordReverse("Computer Programming")
WordReverse("Machine Learning")
