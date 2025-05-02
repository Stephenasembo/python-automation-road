#! /usr/bin/python3

# regex-search - Search for line matching a user-supplied regex expression

''' Search for any line in all .txt files that matches the user supplied
    regex expression. Print the results to the screen.
'''

import re, os

# TODO: Receive regex expression from user as input
userRegex = re.compile(input('Enter the regex expression:\n'))

# TODO: Open all .txt files in a folder
contentArray = []
for fileName in os.listdir('./sampleFolder'):
    # Open only .txt files
    if fileName.endswith('.txt'):
        file = open(os.path.join('./sampleFolder', fileName))
        fileContent = file.readlines()
        contentArray += fileContent
        file.close()

# TODO: Search for a line match
for line in contentArray:
    matchObject = userRegex.search(line)

    # TODO: Print the line to the screen
    if matchObject != None:
        print(line)
