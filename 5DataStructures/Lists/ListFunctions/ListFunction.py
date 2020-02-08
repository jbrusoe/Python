#List Functions
#
#This problem comes from page 145 of this book:
#https://www.amazon.com/Practical-Programming-Introduction-Computer-Science/dp/1680502689/ref=sr_1_2?keywords=practical+programming&qid=1581125837&sr=8-2


def GetList(Print=False):
    ids =  [4353, 2314, 2956, 3382, 9362, 3900]

    if Print:
        print("Original List:")
        print(ids)

    return ids

#Part a - Remove 3382 from the list
WorkingList = GetList(True)

print("\nRemove 3382 from the list")
WorkingList.remove(3382)
print(WorkingList)

#Part b - Get the index of 9362
WorkingList = GetList()

print("\nGet the index of 9362")
index = WorkingList.index(9362)
print("Index:",index)

#Part c - Insert 4499 in the list after 9362.
print("\nInsert 4499 in the list after 9362.")
WorkingList.insert(index+1,4499)
print(WorkingList)

#Part d - Extend the list by adding [5566, 1830] to it
print("\nExtend the list by adding [5566, 1830] to it")
WorkingList += [5546,1830]
print(WorkingList)

#Part e - Reverse the list.
print("\nReverse the list.")
WorkingList.reverse()
print(WorkingList)

#Part 4 - Sort the list
print("\nSort the list")
WorkingList.sort()
print(WorkingList)








