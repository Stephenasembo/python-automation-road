#! /usr/bin/python3

# Link_verification - Flags broken links from a provided url to a webpage

import requests, sys, bs4, pprint, re

# Test website
url = 'https://python.org'

# TODO: Open webpage from the provided url
# try:
#   initial_page = requests.get(url)
#   initial_page.raise_for_status()
# except Exception as err:
#   print(f'There was a problem loading: {url}')
#   sys.exit()

# Cache website for testing purposes
# saved_html = open('./test_file.html', 'wb')
# for chunk in initial_page.iter_content(100000):
#   saved_html.write(chunk)
# saved_html.close()

cached_website_html = open('./test_file.html')

# TODO: Get all link elements from the webpage
soup = bs4.BeautifulSoup(cached_website_html, features='html.parser')
cached_website_html.close()
link_tags = soup.select('a')

links = []
for link_element in link_tags:
  links.append(link_element.get('href'))

# TODO: Visit all links from the webpage
# Sanitize links
def sanitize_links():
  sanitized = []
  for i in range(len(links)):
    if (re.compile(r'[0-9a-zA-Z]$').search(links[i]) == None and
      (not (links[i].endswith('#') or links[i].endswith('/')))):
      continue
    elif links[i].startswith('http'):
      sanitized.append(links[i])
    elif links[i].startswith('//'):
      sanitized.append('https:' + links[i])
    elif links[i].startswith('#'):
      sanitized.append(url + '/' + links[i])
    elif re.compile(r'^/.+').search(links[i]) != None:
      sanitized.append(url + links[i])
    elif re.compile(r'^[a-zA-Z0-9]+').search(links[i]):
      sanitized.append('https://' + links[i])
    else:
      sanitized.append(url + links[i])
  return sanitized

links = sanitize_links()

# TODO: Flag 404 Error pages as broken links
broken_links = []
other_errors = []

for link_url in links:
  try:
    res = requests.get(link_url)
  except requests.ConnectionError:
    other_errors.append(f'Connection error occured: Failed to load {link_url}')
  except requests.HTTPError as err:
    if err == 404:
      broken_links.append(link_url)
    else:
      other_errors.append(f'HTTP Error: Failed with status code ${err}')

if len(broken_links > 0):
  print('Broken links found on this webpage:')
  for broken_link in broken_links:
    print(broken_link)
else:
  print('Hooray! No broken link found on this webpage.')

if len(other_errors) != 0:
  print('The following links failed to load due to other errors: ')
  for error in other_errors:
    print(error)

sys.exit()
