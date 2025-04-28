#! /usr/bin/python3

import re, sys

def isPasswordStrong():
  # User inputs password as a command line argument
  if len(sys.argv) != 2:
    print('Usage: python main.py password')
    sys.exit()
  userPassword = sys.argv[1]

  # Regexes check if password is strong
  passwordLenRegex = re.compile(r'(\w){8,}')
  digitRegex = re.compile(r'\d')
  lowerCaseRegex = re.compile(r'[a-z]')
  upperCaseRegex = re.compile(r'[A-Z]')

  if passwordLenRegex.search(userPassword) == None:
    return 'The password is weak. The password should have at least 8 characters.'
  if lowerCaseRegex.search(userPassword) == None:
    return 'The password is weak. The password should have at least 1 lowercase character.'
  if upperCaseRegex.search(userPassword) == None:
    return 'The password is weak. The password should have at least 1 uppercase character.'
  if digitRegex.search(userPassword) == None:
    return 'The password is weak. The password should have at least 1 digit.'
  
  return 'The password is strong.'

print(isPasswordStrong())