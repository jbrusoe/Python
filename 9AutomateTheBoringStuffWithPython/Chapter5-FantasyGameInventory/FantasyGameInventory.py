stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(SummaryTitle,inventory):
    print(SummaryTitle + ":")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(Inventory, AddedItems):
    print("\nItems to add to inventory:")
    for i in range(len(AddedItems)):
        print(AddedItems[i])

    print("\n")
    
    #Now add items to inventory
    for i in range(len(AddedItems)):
        print("Additen item: " + AddedItems[i])
        
    return Inventory


displayInventory("Initial Inventory",stuff)

DragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, DragonLoot)

displayInventory("\nFinal Inventory", stuff)
