#! /usr/bin/python3

# Console Canvas - Prints the user desired shape to the terminal.

# TODO: Inform user of possible options for shape
shapes = ['square', 'triangle', 'pyramid']

# Number the options printed starting from one
def print_supported_shapes():
  print('The program currently prints these shapes: ')
  for i in range(1, len(shapes) + 1):
    print(str(i) + '. ' + shapes[i - 1])

# TODO: Ask user for desired shape
while True:
  print_supported_shapes()
  try:
    user_shape = (input('Which shape do you want to print?\n')).lower()
    if user_shape not in shapes:
      raise Exception('\nError: Sorry ' + user_shape + ' is not supported.\n')
    break
  except Exception as err:
    print(err)


# TODO: Ask user for shape's size
while True:
  try:
    user_size = input('Which size do you want your ' + user_shape + ' to be?\n')
    user_size = int(user_size)
    break
  except:
    print('\nError: Please input a valid number!\n')

# TODO: Print the shape to the console
print_symbol = '#'

def print_square(size, symbol):
  print('Here is your square  of size ' + str(size) + '.\n')
  for i in range(size):
    for j in range(size):
      print(symbol, end='')
    print()

def print_triangle(size, symbol):
  print('Here is your triangle of size ' + str(size) + '.\n')
  for i in range(1, size + 1):
    for j in range(i):
      print(symbol, end='')
    print()

def print_pyramid(size, symbol):
  print('Here is your pyramid of size ' + str(size) + '.\n')
  padding = size - 1
  space = ' '
  pyramid_symbol = symbol
  for row in range(size):
    print((space * padding) + pyramid_symbol)
    pyramid_symbol += symbol * 2
    padding -= 1

if user_shape == 'square':
  print_square(user_size, print_symbol)
elif user_shape == 'triangle':
  print_triangle(user_size, print_symbol)
elif user_shape == 'pyramid':
  print_pyramid(user_size, print_symbol)
else:
  print('Error: Sorry ' + user_shape + ' can\'t be printed.')