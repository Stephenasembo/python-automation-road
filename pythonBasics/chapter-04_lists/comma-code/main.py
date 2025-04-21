import copy

def createString(listArg):
  listCopy = copy.copy(listArg)
  step = 1
  if not listArg:
    return ''
  
  elif len(listCopy) == 1:
    string = listCopy[0]
    print(string)
    return string
  
  else:
    for i in range(len(listCopy) - 1):
      listCopy.insert(step, ',')
      step += 2

    string = listCopy[0]
    listCopy = listCopy[1:]
    listCopy[-2] = ' and '
    for item in listCopy:
      string += item
    return string

example = ['apples', 'bananas', 'tofu', 'cats']
print(createString(example))
