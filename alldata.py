"""
All codes of
Python 3 Programming Specialization
Course 3 -
Data Collection and Processing with Python
University of Michigan
"""
#%%
""" Nested DICT Indexing"""
d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}

# %%


info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']
# %%
""" JSON loads and dumps"""

import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

# %%

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names=[]
for name in info:
	last_names.append(name[1])
# %%
info = [['Tina', 'Turner'], 1939,['singer'],['Matt', 'Damon'], 1970, ['actor','Kristen', 'Wiig'], [1973],3452]
for x in info:
	if type(x) == list:
		print(x)
	if type(x)==int:
		print(x,'is int')
