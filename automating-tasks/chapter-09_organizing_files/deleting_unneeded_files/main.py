#! /usr/bin/python3

'''Deleting unneeded files - Walks through the entire folder
      tree looking for exceptionally large files.
      The large files' absolute paths are then printed out to the screen.
'''

import os

''' File size conversions:
1KB = 1024bytes
1MB = 1024KB
1GB = 1024MB
'''

# Test folder will be the home folder.
folder = '/home/sain8op/'
maxSize = 100 * 1024 * 1024 #100MB
largeFiles = []

# TODO: Walk entire folder tree provided.
for folderName, subfolderNames, fileNames in os.walk(folder):
  # TODO: Get file size of each file during the walk.
  for file in fileNames:
    filePath = os.path.join(folderName, file)
    if os.path.isfile(filePath):
      fileSize = os.path.getsize(filePath)
      if fileSize > maxSize:
        fileSize = round(fileSize / (1024 * 1024), 2) # store size as MB
        largeFiles.append('File: ' + filePath + '. Size: ' + str(fileSize) + ' MB')

# TODO: Store large file names in a list and print out the list.
if len(largeFiles) != 0:
  for largeFile in largeFiles:
    print(largeFile)
else:
  print('No file larger than ' + str(maxSize) + ' found.')