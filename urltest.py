#%%
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')

print("Count",len(tags))
tot = 0
for tag in tags:
    total = re.findall('">(\d+)</',str(tag))
    for t in total:
        tot+=int(t)
print("Sum",tot)


# %%
