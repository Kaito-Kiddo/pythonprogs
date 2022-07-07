#%%
""""
    Coursera Week 4 assignment
    Extract link and name from a url
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def retr(url, count, pos):

    elt = []
    for i in range(count):
        p=0
        html = urllib.request.urlopen(url).read()
        print("Retrieving:",url)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for tag in tags:
            p+=1
            if p==pos:
                url=tag.get('href',None)
                elt= re.findall(">([a-zA-Z]+)<",str(tag))
    return elt

# url = input('Enter URL:')
count = int(input('Enter Count:'))
pos = int(input('Enter Position:'))


url="http://py4e-data.dr-chuck.net/known_by_Rowan.html"
# url="http://py4e-data.dr-chuck.net/known_by_Fikret.html"
result=retr(url,count,pos)
print(*result)


# %%
