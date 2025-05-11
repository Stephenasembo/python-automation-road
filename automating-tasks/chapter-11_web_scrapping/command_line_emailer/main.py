#! /usr/bin/python3

# Command line emailer - Sends an email from the command line

import sys, logging

logging.basicConfig(level=logging.DEBUG, filename='./logs.txt', format='%(asctime)s - %(levelname)s - %(message)s')

# TODO: Take email address and email messsage from command line
logging.info('Program started.')
if len(sys.argv) < 3:
  print('Error: python recipient-email-address message\n')
  logging.error('Program ended not enough command line arguments provided.')
  sys.exit()
else:
  recipient = sys.argv[1]
  message = sys.argv[2:]

logging.info('Program reached end of execution.')

# TODO: Ask for user's account details

# TODO: Send email to specified address

# TODO: Exit program