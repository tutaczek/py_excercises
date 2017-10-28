inventory = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}

def displayInventory(inventory):
    print('Inwentarz:')
    item_total = 0
    for k, v in inventory.items():
        print(v,k)  
        item_total = item_total + v
    print("Całkowita liczba przedmiotów: " + str(item_total))

displayInventory(inventory)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory

inv = {'złote monety': 42, 'lina': 1}
dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'rubin']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
