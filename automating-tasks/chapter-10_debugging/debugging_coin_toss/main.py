#! /usr/bin/python3

'''
Debugging coin toss - The task is to run the program,
find and fix bugs through debugging.
'''

import random, logging

logging.basicConfig(filename = 'logs.txt', level = logging.DEBUG,
  format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess = input()

logging.debug('The user\'s choice is: ' + guess)

guessList = ['tails', 'heads']
toss = guessList[random.randint(0, 1)] # 0 is tails, 1 is heads

logging.debug('The coin toss is currently: ' + str(toss))
logging.warning('The toss is a number between 1 and 0')

if toss == guess:
  print('You got it!')
  logging.debug('End of program')

else:
  print('Nope! Guess again!')
  logging.debug('An extra attempt awarded to player.')
  guesss = input()
  logging.debug('The second guess from the player is: ' + guess)

  if toss == guess:
    print('You got it!')
    logging.debug('End of program')

  else:
    print('Nope. You are really bad at this game.')
    logging.debug('End of program')