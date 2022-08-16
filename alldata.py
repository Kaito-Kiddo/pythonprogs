"""
All codes of
Python 3 Programming Specialization
Course 3 - W1
Data Collection and Processing with Python
University of Michigan
"""
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


#%%
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = 'data' in nested
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = 24 in nested.values()
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = 'whole' not in nested['window']
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = 'physics' in nested


# %%
"""  Nested Data and Nested Iteration assessment """
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
for olymp in nested_d:
	US_count.append(nested_d[olymp]['USA'])
print(US_count)


# %%
""" Nested Data and Nested Iteration """
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for l in l_of_l:
	third.append(l[2])
print(third)


# %%
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t=[]
other=[]
for athlete in athletes:
	for ath in athlete:
		print(ath)
		if 't' in ath:
			t.append(ath)
		else:
			other.append(ath)
print(t)
print("------------------")
print(other)
# %%
