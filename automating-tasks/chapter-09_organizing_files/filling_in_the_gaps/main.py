#! /usr/bin/python3

''' Filling in the gaps - Searches for gaps in file naming in a specified folder.
    If gaps are found, the program renames the file and all proceeding files to close
    the gap between the filenames.
'''

import os, re

# Test folder
folder = os.path.join(os.getcwd(), 'sample')

foundFiles = []
fileNum = []

prefix = 'spam'
# Use a regex for finding files
fileRegex = re.compile(r'''
  ^spam       # Initial word before number
  (\d)+       # The file number
  (.*)$       # The file extension
  ''', re.VERBOSE)

# TODO: Walk through folder
for folderName, subFolders, files in os.walk(folder):

  # TODO: Find files with specified prefix
  for fileName in files:
    fileMatch = fileRegex.search(fileName)

    # TODO: Store all found files in a list
    if fileMatch != None:
      foundFiles.append(fileName)
      fileNum.append(fileMatch.group(1))

# TODO: Look for gaps in file naming
fileNum.sort()
number = int(fileNum[0])

for num in fileNum:
  num = int(num)
  if num == number:
    number += 1
  else:
    print('Gap found: ' + str(number) + ' is missing.')
    break

# TODO: If gap found rename the file and files after it