import pprint

def displayInventory(inventory):
  totalItems = 0
  print('Inventory:')
  for key, value in inventory.items():
    totalItems += value
    print(str(value) + ' ' + str(key))
  print('Total number of items: ' + str(totalItems))

example = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(example)