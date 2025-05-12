#! /usr/bin/python3

# Command line emailer - Sends an email from the command line

# The initial program will only utilize Chrome browser

'''
The program is not functional right now due to bot login restrictions by
email provider platforms.
'''

import sys, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.DEBUG, filename='./logs.txt', format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

browser = None # Web automation disabled
login_status = False

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

def login_user(address, password):
  global login_status
  # Enter email address
  address_input = browser.find_element(By.ID, 'username')
  address_input.send_keys(address)
  address_input.submit()

  # Enter account password
  password_input = browser.find_element(By.ID, 'password')
  password_input.send_keys(password)
  password_input.submit()

  login_status = True
  print('Successfully logged in.')

# TODO: Check if user logged in or not
try:
  print('Checking email account login status...')
  browser.get('https://account.proton.me/mail')
  try:
    element = browser.find_element(By.NAME, 'loginForm')
    if not login_status:
      print('\nEnter your account details to log in to your email account.\n')
      email_address = get_account_details('Email address')
      email_password = get_account_details('Password')

      # Login to user account
      login_user(email_address, email_password)
    else:
      print('You are already logged in to your account.')
      login_status = True

  except NoSuchElementException:
    login_status = True
except:
  print('Error while opening browser.')

# TODO: Send email to specified address

# TODO: Exit program
# sys.exit()
logging.info('Program reached end of execution.')