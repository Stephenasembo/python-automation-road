#! /usr/bin/python3

'''Deleting unneeded files - Walks through the entire folder
      tree looking for exceptionally large files.
      The large files' absolute paths are then printed out to the screen.
'''

import os

# Test folder will be the home folder.
folder = '/home/sain8op/'
maxSize = 1000000
largeFiles = []

# TODO: Walk entire folder tree provided.
for folderName, subfolderNames, fileNames in os.walk(folder):
  # TODO: Get file size of each file during the walk.
  for file in fileNames:
    filePath = os.path.join(folderName, file)
    if os.path.isfile(filePath):
      fileSize = os.path.getsize(filePath)
      if fileSize > maxSize:
        largeFiles.append(filePath)

# TODO: Store large file names in a list and print out the list.
if len(largeFiles) != 0:
  for largeFile in largeFiles:
    print(largeFile)
else:
  print('No file larger than ' + str(maxSize) + ' found.')