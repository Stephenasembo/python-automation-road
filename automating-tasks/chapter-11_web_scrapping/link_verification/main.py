#! /usr/bin/python3

# Link_verification - Flags broken links from a provided url to a webpage

import requests, sys, bs4

# Test website
url = 'https://python.org'

# TODO: Open webpage from the provided url
try:
  initial_page = requests.get(url)
  initial_page.raise_for_status()
except Exception as err:
  print(f'There was a problem loading: {url}')
  sys.exit()

# TODO: Get all link elements from the webpage

# TODO: Visit all links from the webpage

# TODO: Flag 404 Error pages as broken links