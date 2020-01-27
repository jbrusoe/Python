#Fantasy Game Inventory
#Written by: Jeff Brusoe
#Last Updated: January 27, 2020
#
#Based on end of chapter 5 exercises from Automate the Boring Stuff with Python
#https://automatetheboringstuff.com/

CurrentStuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def DisplayInventory(SummaryTitle,inventory):
    print(SummaryTitle + ":")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    print("Total number of items: " + str(item_total) + "\n")

def AddToInventory(Inventory, AddedItems):
    
    for i in range(len(AddedItems)):
        print("Adding Item: " + AddedItems[i])

        ItemTotal = Inventory.get(AddedItems[i],0)

        Inventory[AddedItems[i]] = ItemTotal + 1
        
    return Inventory


DisplayInventory("Initial Inventory",CurrentStuff)

DragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
CurrentStuff = AddToInventory(CurrentStuff, DragonLoot)

DisplayInventory("\nFinal Inventory", CurrentStuff)
