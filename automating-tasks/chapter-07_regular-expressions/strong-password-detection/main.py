#! /usr/bin/python3

import re, sys

# Regex to make sure the password is atleast 8 characters long
passwordLenRegex = re.compile(r'(\w){8,}')

digitRegex = re.compile(r'\d')

lowerCaseRegex = re.compile(r'[a-z]')

upperCaseRegex = re.compile(r'[A-Z]')

userPassword = 'stephenmArk22'

lenMatch = passwordLenRegex.search(userPassword)

if lenMatch == None:
  print('''
  The password is weak.
  Please run the program again with a stronger password.
  The password should have at least 8 characters.
  ''')

else:
  lowerCaseMatch = lowerCaseRegex.search(userPassword)
  if lowerCaseMatch == None:
    print('''
    The password is weak.
    Please run the program again with a stronger password.
    The password should have at least 1 lowercase character.
    ''')

  else:
    upperCaseMatch = upperCaseRegex.search(userPassword)
    if upperCaseMatch == None:
      print('''
      The password is weak.
      Please run the program again with a stronger password.
      The password should have at least 1 uppercase character.
      ''')

    else:
      digitMatch = digitRegex.search(userPassword)
      if digitMatch == None:
        print('''
        The password is weak.
        Please run the program again with a stronger password.
        The password should have at least 1 digit.
        ''')
      else:
          print('The password entered is strong.')