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

# TODO: Ask for user's account details
print('\nEnter your account details to log in to you email account.\n')

while True:
  try:
    email_account = input('Email address: ')
    if email_account == '':
      raise Exception('\nError: Email address can not be empty! Please try again.\n')
    else:
      break
  except Exception as err:
    print(err)

while True:
  try:
    email_password = input('Password: ')
    if email_password == '':
      raise Exception('\nError: Password can not be empty! Please try again.\n')
    else:
      break
  except Exception as err:
    print(err)

# TODO: Send email to specified address

# TODO: Exit program
sys.exit()
logging.info('Program reached end of execution.')