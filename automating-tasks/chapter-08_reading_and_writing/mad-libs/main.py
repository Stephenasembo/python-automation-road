#! /usr/bin/python3

# mad-libs -Replace content in text file with user input

''' User enters words which will replace specific word content in the text file.
    String result is printed on the screen and saved to a new text file.'''

import re

# TODO: Open text file
initialFile = open('./sampleText.txt')

# TODO: Read file content
initialFileContent = initialFile.read()

# TODO: Prompt user for input
adjective = input('Enter an adjective:\n')
noun1 = input('Enter a noun:\n')
verb = input('Enter a verb:\n')
noun2 = input('Enter a noun:\n')

# TODO: Perform word search with regex expressions
adjectiveRegex = re.compile('ADJECTIVE')
nounRegex = re.compile('NOUN')
verbRegex = re.compile('VERB')

# TODO: Substitute matches with corresponding input
newContent = adjectiveRegex.sub(adjective, initialFileContent)
newContent = nounRegex.sub(noun1, newContent, count=1)
newContent = verbRegex.sub(verb, newContent)
newContent = nounRegex.sub(noun2, newContent)

# TODO: Create new file for results
resultFile = open('./result.txt', 'w')

# TODO: Write the result to the new file
print(newContent)
resultFile.write(newContent)

# TODO: Close open files
initialFile.close()
resultFile.close()