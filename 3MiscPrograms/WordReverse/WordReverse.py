#Python - Word Reverse
#
#Written by: Jeff Brusoe
#Demo program for Programming Merit Bage class
#
#Sample input: abcdefg
#Sample output: gfedcba

Word = input("Enter a word: ")
print("You entered -",Word)

print("Reversed word - ",end='')

for i in range(len(Word),0,-1):
    print(Word[i-1],end='')

print("")

