""" UMICH specilization py3 coursera
    Python Classes and Inheritance
    C4 """

#%%
from asyncore import poll3


print("Hello Class")
# %%
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point - {self.x} {self.y}"

p1 = Point(2,4)
p2 = Point()
print(p2)
# %%
class Animal:
    def __init__(self,arms=0,legs=0):
        self.arms=arms
        self.legs=legs
    def limbs(self):
        return self.arms+self.legs
    def __str__(self):
        return f"Animal - {self.arms} {self.legs}"
spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spider)


# %%
class Cereal:
    cereal=" HI Fruit" #class variable
    def __init__(self,n="",b="",f=0):

        self.name = n
        self.brand = b
        self.fiber = f
    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"

c1 = Cereal("Corn Flakes","Kellogg's",2)
c2 = Cereal("Honey Nut Cheerios","General Mills",3)
print(c1,c2,sep="\n")


# %%
class Fruit():

    def __init__(self, name, price):
        self.name = name
        self.price = price
    def sort_priority(self):
        return self.price
L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
# Using Lambda as key
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)
# Using class function as key
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)


# %%
class AppleBasket:
    def __init__(self,c,q):
        self.apple_color = c
        self.apple_quantity = q
    def increase(self):
        self.apple_quantity+=1
        return self.apple_quantity
    def __str__(self):
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."

testOne = AppleBasket('blue',10)
testTwo = AppleBasket('purple',25)
        
# %%
class BankAccount:
    def __init__(self,n,a):
        self.name = n
        self.amt = a

    def __str__(self):
        return f"Your account, {self.name}, has {self.amt} dollars."

t1 = BankAccount("Bob",100)
t2 = BankAccount('purple',25)

# %%



class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    def opponent(self):
        currtype = {'Grass':('Fire', 'Water'),'Ghost':('Dark','Psychic'),'Fire':('Water','Grass'),'Flying':('Electric','Fighting')}
        return currtype.get(self.p_type)



class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type='Grass'
    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return f"{self.name} knows a lot of different moves!"

p1 = Grass_Pokemon("Belle")
p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika",10)

p3.train()


# %%
""" C4 Final W2 """
class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)
    def opponent(self):
        currtype = {'Grass':('Fire', 'Water'),'Ghost':('Dark','Psychic'),'Fire':('Water','Grass'),'Flying':('Electric','Fighting')}
        return currtype.get(self.p_type)


    
class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"



#%%
""" try except codes """

numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []
for i in numb:
    try:
        remainder += [36 % i]
    except Exception as e:
        remainder += ['Error']

print(remainder)


# %%

lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except ZeroDivisionError:
        continue


# %%
res = input("""
        xy has $ x and y

        Category: aaa
        Phrase:  aaa
        Guessed: aaa

        Guess a letter, phrase, or type 'exit' or 'pass':
        """)
print(res)
# %%
v='AEIOU'
import random

random.choice(v)
# %%
