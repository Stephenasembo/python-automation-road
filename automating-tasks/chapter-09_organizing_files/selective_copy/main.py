#! /usr/bin/python3

'''Selective copy - Searches for files with certain file extensions.
    The files then get copied to a new folder.'''

import os, re, shutil

# TODO: Get file extensions for files to be searched.

extension = input('Which type of files do you want to copy ?\n')
extensionRegex = re.compile(extension)

# TODO: Walk through the folder searching for the files.
foundFiles = []
for folder, subFolders, files in os.walk('.'):
  name = os.path.join(os.getcwd(), folder)  
  for fileName in files:
    fileMatch = extensionRegex.search(fileName)
    if fileMatch != None:
      filePath = os.path.join(name, fileName)
      foundFiles.append(filePath)

# TODO: Copy found files to a new folder.
folderLocation = os.path.join(os.getcwd(), 'foundFiles')
if not (os.path.isdir(folderLocation)):
  os.makedirs(folderLocation)
  folderLocation = os.path.join(os.getcwd(), 'foundFiles')
for file in foundFiles:
  shutil.copy(file, folderLocation)
