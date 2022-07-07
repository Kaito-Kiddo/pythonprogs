#%%
import json
import urllib.request, urllib.parse, urllib.error

sum = 0
url = input("Enter Url - ")
print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)
print(json.dumps(js, indent=4))
print('count:', len(js['comments']))
for i in js['comments']:
    sum = sum + i['count']
print ("Sum : ",sum)   
# %%
