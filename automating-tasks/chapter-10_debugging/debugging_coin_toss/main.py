#! /usr/bin/python3

'''
Debugging coin toss - The task is to run the program,
find and fix bugs through debugging.
'''

import random
guess = ''
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
  print('You got it!')
else:
  print('Nope! Guess again!')
  guesss = input()
  if toss == guess:
    print('You got it!')
  else:
    print('Nope. You are really bad at this game.')