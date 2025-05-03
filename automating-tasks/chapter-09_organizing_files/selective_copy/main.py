#! /usr/bin/python3

'''Selective copy - Searches for files with certain file extensions.
    The files then get copied to a new folder.'''

import os, re, shutil

# TODO: Get file extensions for files to be searched.

# extension = input('Which type of files do you want to copy ?\n')
# Testing purposes
extension = 'pdf'

# TODO: Walk through the folder searching for the files.
for folder, subFolders, files in os.walk('.'):
  print(folder)
  for subfolder in subFolders:
    print(subfolder)
  for fileName in files:
    print(fileName)

# TODO: Copy found files to a new folder.