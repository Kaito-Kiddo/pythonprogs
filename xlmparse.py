#%%

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_1584374.xml"
bdata = urllib.request.urlopen(url).read()
print(f"Retrieving {url}")
# print(type(bdata))
sdata=bdata.decode() # convert byte data to string data
# print(type(sdata))
tree = ET.fromstring(bdata)

counts = tree.findall('.//count')
print('Count:', len(counts))
total=0
for i in counts:
    total+=int(i.text)
    # print(i.text)
print("Sum:",total)

# %%
