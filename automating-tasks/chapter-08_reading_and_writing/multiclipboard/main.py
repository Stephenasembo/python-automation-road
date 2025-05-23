#! /usr/bin/python3

# mcb.pyw - Saves and loads data to and from a clipboard

'''Usage: python save <keyword> - Saves clipboard to keyword.
          python <keyword> - Loads keyword to clipboard.
          python list - Loads all keywords to clipboard.
          python delete <keyword> - Deletes keyword from storage.
          python delete - Deletes all keywords from storage.'''
        
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3:
  if sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
  elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
    del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
  # TODO: List keywords and load content.
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])
  elif sys.argv[1].lower() == 'delete':
    for key in list(mcbShelf.keys()):
      del mcbShelf[key]

mcbShelf.close()