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
link_tags = soup.select('a')

links = []
for link_element in link_tags:
  links.append(link_element.get('href'))

# TODO: Visit all links from the webpage
# Sanitize links
for i in range(len(links)):
  if links[i].startswith('http'):
    continue
  elif links[i].startswith('//'):
    links[i] = 'https:' + links[i]
  elif links[i].startswith('#'):
    links[i] = url + '/' + links[i]
  else:
    links[i] = url + links[i]

# TODO: Flag 404 Error pages as broken links