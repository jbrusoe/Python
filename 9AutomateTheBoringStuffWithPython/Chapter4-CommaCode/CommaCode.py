#CommaCode.py
#Written by: Jeff Brusoe
#Last Updated: Jaunary 24, 2020
#
#Purpose:   Convert a list into a comma separated string with the word "and"
#           used before the last word. This is from the end of chapter 4 of
#           "Automate the Boring Stuff with Python".

def ListToString(InputList):
    print("Input List: ", InputList)

    OutputString = ""
    
    for i in range(len(InputList)):

        if i == (len(InputList) - 1):
            OutputString = OutputString + "and " + InputList[i]
        else:
            OutputString = OutputString + InputList[i] + ", "

    return OutputString

print(ListToString(['apples', 'bananas', 'tofu', 'cats']))
    
