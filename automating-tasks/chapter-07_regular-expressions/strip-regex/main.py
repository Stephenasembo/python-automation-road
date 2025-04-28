#! /usr/bin/python3

import re, sys

def stripRegex(string, character = None):
  if character == None:
    stringRegex = re.compile(r'\s')
  else:
    stringRegex = re.compile(character)
  # Substitute matches with blank strings acts as deletion of characters
  return stringRegex.sub('', string)

# Take user input from command line
if len(sys.argv) > 3 or len(sys.argv) < 2:
  print('Usage: python string character.')
  sys.exit()
else:
  if len(sys.argv) == 2:
    print(stripRegex(sys.argv[1]))
  else:
    print(stripRegex(sys.argv[1], sys.argv[2]))
