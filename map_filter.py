"""" All map, filter and List Comprehension
    Python 3 Programming Specialization
    Course 3 - W2
    Data Collection and Processing with Python
    University of Michigan
     """

#%%
L = {'usa','india','jpn'}
L = list(map(lambda x:x[:2].upper(),L))
print(L)


# %%
""" FILTER """
nums = [3,4,6,7,0,1]
new_nums = list(filter(lambda num: num % 2 == 0,nums))
print(new_nums)


# %%
lst_check = ['plums', 
'watermelon', 
'kiwi', 
'strawberries', 
'blueberries', 
'peaches', 
'apples', 
'mangos', 'papaya']

filter_testing  = list(filter(lambda x:'w' in x,lst_check))
print(filter_testing)
# %%


lst = ["witch", "halloween", "pumpkin",
 "cat", "candy", "wagon", "moon"]
lst2 = list(filter(lambda x:'o' in x,lst))
print(lst2)


# %%

""" LIST Comprehension 
[<transformer_expression>
    for <loop_var> in <sequence>
        if <filtration_expression>]
   """

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
    {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
    {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
    {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
    {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
    {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri = [ d["name"] for d in tester['info']]
print(compri)
# %%
""" Nested Dict 
save values of name key in each outer key """
tester = {'info1': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
    {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
    {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}],

    'info2': [{'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
    {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
    {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
names = []
keys = ['info1','info2']
for key in tester:
    names += [ d["name"] for d in tester[key] ]

print(names)


# %%
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3  = [x1+x2 for (x1,x2) in zip(L1,L2) if (x1 > 10 and x2 < 5) ]
print(L3)


# %%
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
for (x1,x2) in list(zip(L1,L2)):
    if (x1 > 10 and x2 < 5):
        print(x1+x2)


# %%
""" Assessment C3 Week2 
    map filter list zip
"""


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
# map_testing = list(map(lambda x : "Fruit: "+x,lst_check))
map_testing = ["Fruit: " + x for x in lst_check]
print(map_testing)


# %%
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda x : x[0] == 'B',countries))


# %%
""" print only first name """
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [y for (x,y) in people]
print(first_names)

# %%

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2=[x*2 for x in lst]


# %%
"""print names whr marks >= 70 """
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [x for x,y in students if y>=70]


# %%
""" use zip n filter to 
print string of len > 3
use append and not '+=' operator
"""
 
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
print(list(zip(l1,l2)))
opposites = []
for (x1,x2) in list(zip(l1,l2)):
    if len(x1) > 3 and len(x2) > 3: 
        opposites.append((x1,x2))
print(opposites)

# %%
""" use zip n filter to print string of len > 3
    using zip na dfilter 
    important
"""
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']


opposites = list(filter(lambda  x : len(x[0]) > 3 and len(x[1]) > 3,zip(l1,l2)))
print(opposites)

# %%

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species,population))
endangered = [ x for x,y in list(filter(lambda x : x[1] < 2500,pop_info))]
print(endangered)
# %%
