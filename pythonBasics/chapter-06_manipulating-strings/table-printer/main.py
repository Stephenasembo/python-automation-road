#! /usr/bin/python3

sample = [['apples', 'oranges', 'cherries', 'banana'],
          ['Alice', 'Bob', 'Carol', 'David'],
          ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
  # Find longest string for each column
  colWidths = [0] * len(tableData)
  for i in range(len(tableData)):
    longestStr = len(tableData[i][0])
    for value in range(len(tableData[i]) - 1):
      if longestStr < len(tableData[i][value + 1]):
        longestStr = len(tableData[i][value + 1])
    colWidths[i] = longestStr
  
    # Justify each string
    for row in range(len(tableData[i])):
      tableData[i][row] = (tableData[i][row].rjust(colWidths[i]))

printTable(sample)