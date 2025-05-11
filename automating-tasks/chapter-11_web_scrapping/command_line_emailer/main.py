#! /usr/bin/python3

# Command line emailer - Sends an email from the command line

import sys, logging
from selenium import webdriver
from selenium.webdriver.common.by import By

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

login_status = False

# TODO: Check if user logged in or not
try:
  browser = webdriver.Chrome()
  browser.get('https://gmail.com')
  try:
    element = browser.find_element(By.ID, 'headingText')
  except:
    login_status = True
except:
  print('Error while opening browser.')

# TODO: Ask for user's account details
def get_account_details(field):
  while True:
    try:
      details = input(f'{field}: ')
      if details == '':
        raise Exception(f'\nError: {field} can not be empty! Please try again.\n')
      else:
        logging.info(f'Successfully obtained user\'s: {field}')
        return details
    except Exception as err:
      print(err)

if not login_status:
  print('\nEnter your account details to log in to you email account.\n')
  email_address = get_account_details('Email address')
  email_password = get_account_details('Password')
  # Login to user account
else:
  print('You are already logged in to your account.')

# TODO: Send email to specified address

# TODO: Exit program
sys.exit()
logging.info('Program reached end of execution.')