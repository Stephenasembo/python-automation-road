#! /usr/bin/python3

import re

def stripRegex(string, character = None):
  # Check if second argument passed to function
  # Create Regex to look for whitespace or characters
  if character == None:
    stringRegex = re.compile(r'\s')
  else:
    stringRegex = re.compile(character)
  # Substitute matches with blank strings
  return stringRegex.sub('', string)

print(stripRegex('  hello'))