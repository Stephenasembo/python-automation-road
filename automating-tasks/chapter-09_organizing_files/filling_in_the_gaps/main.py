#! /usr/bin/python3

''' Filling in the gaps - Searches for gaps in file naming in a specified folder.
    If gaps are found, the program renames the file and all proceeding files to close
    the gap between the filenames.
'''

import os, re, shutil

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
foundFiles.sort()
fileNum.sort()

number = int(fileNum[0])
nextFileIndex = 0

for num in fileNum:
  num = int(num)
  if num == number:
    number += 1
    nextFileIndex += 1
  else:
    gap = number
    gapSize = int(fileNum[nextFileIndex]) - number
    # print('Gap found: ' + str(gap) + ' is missing.')
    # print('The gap size is: ' + str(gapSize))
    # print('Rename the value at index: ' + str(nextFileIndex))
    break

# TODO: If gap found rename the file and files after it
rectifyFiles = foundFiles[nextFileIndex:]
for i in range(len(rectifyFiles)):
  numRegex = re.compile(r'\d+')
  num = numRegex.search(rectifyFiles[i]).group()
  numLen = len(num)
  renamedNum = str((int(num)) - gapSize)
  renamedNum = renamedNum.rjust(numLen, '0')
  rectifyFiles[i] = numRegex.sub(renamedNum, rectifyFiles[i])

rightOrder = foundFiles[:nextFileIndex] + rectifyFiles
print(foundFiles)
print(rightOrder)

for i in range(len(foundFiles)):
  foundFiles[i] = os.path.join(folder, foundFiles[i])
  rightOrder[i] = os.path.join(folder, rightOrder[i])
  print('Moving %s to %s' % (foundFiles[i], rightOrder[i]))
  shutil.move(foundFiles[i], rightOrder[i])


# for folderName, subfolders, files in os.walk(folder):
#   for fileName in files:
#     fileNamePath = os.path.join(folder, fileName)
#     for foundFile in foundFiles:
#       foundFilePath = os.path.join(folder, foundFile)
#       print('Moving %s to %s' % (fileNamePath, foundFilePath))
