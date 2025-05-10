#! /usr/bin/python3

# Console Canvas - Prints the user desired shape to the terminal.

# TODO: Inform user of possible options for shape
shapes = ['square', 'triangle', 'pyramid']
print('The program currently prints these shapes: ')

# Number the options printed starting from one
for i in range(1, len(shapes) + 1):
  print(str(i) + '. ' + shapes[i - 1])

# TODO: Ask user for desired shape
user_shape = input('Which shape do you want to print?\n')

# TODO: Ask user for shape's size
user_size = input('Which size do you want your ' + user_shape + ' to be?\n')
user_size = int(user_size)

# TODO: Print the shape to the console
symbol = '#'

def print_square():
  for i in range(user_size):
    for j in range(user_size):
      print(symbol, end='')
    print()

def print_triangle():
  for i in range(1, user_size + 1):
    for j in range(i):
      print(symbol, end='')
    print()

def print_pyramid():
  padding = user_size - 1
  space = ' '
  pyramid_symbol = symbol
  for row in range(user_size):
    print((space * padding) + pyramid_symbol)
    pyramid_symbol += symbol * 2
    padding -= 1
