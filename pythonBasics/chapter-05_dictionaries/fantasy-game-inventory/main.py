def displayInventory(inventory):
  totalItems = 0
  print('Inventory:')
  for key, value in inventory.items():
    totalItems += value
    print(str(value) + ' ' + str(key))
  print('Total number of items: ' + str(totalItems))

def addToInventory(inventory, addedItems):
  for listValue in addedItems:
    inventory.setdefault(listValue, 0)
    inventory[listValue] += 1
  return inventory

inventoryExample = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Example of a list to be added to the inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'knife']

inventoryExample = addToInventory(inventoryExample, dragonLoot)

displayInventory(inventoryExample)