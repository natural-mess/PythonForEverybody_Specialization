# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take input
url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

track = 0

# Create request
for i in range(int(count)+1):
    print ('Retrieving: ' + url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        track = track + 1
        if track == int(position):
            url = tag.get('href', None)
            track = 0;
            break
