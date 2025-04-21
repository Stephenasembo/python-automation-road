def createString(list):
  step = 1
  for i in range(len(list) - 1):
    list.insert(step, ',')
    step += 2
  string = list[0]
  list = list[1:]
  list[-2] = ' and '
  for item in list:
    string += item
  print(string)

example = ['apples', 'bananas', 'tofu', 'cats']
createString(example)
