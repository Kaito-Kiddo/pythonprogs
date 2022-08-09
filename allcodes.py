#%%
from cmath import isnan
from curses.ascii import isalpha, isspace
from itertools import count
from operator import contains
from statistics import mean
from tokenize import group


print("MAY the Force B with U")

def computepay(hrs,rate):
    
    if hrs > 40:
        p =(40*rate + (hrs-40)*rate*1.5)
    else:
        p =(hrs*rate)
    return p
h,r = input("Enter Hours and rate of hours : ").split()
h,r = float(h),float(r)
p = computepay(h,r)  
print("Pay",p,sep=" ")

# %%
x = -2
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
# %%
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

# %%
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)

# %%
# score = float(input("Enter Score: "))
score = 0.85
if score > 1.0 or score < 0 :
    print("Out of range")
else:
    if score >= 0.9 : grade = "A"
    elif score >= 0.8  : grade = "B"
    elif score >= 0.7 : grade = "C"
    elif score >= 0.6 : grade = "D"
    elif score < 0.6 : grade = "F"

    print(grade)

# %%
nums =[]
while(True):
    num=input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
        nums.append(num)
    except:
        print("Invalid input")
        continue

nums.sort()
smallest=nums[0]
largest=nums[-1]
print("Maximum is", largest)
print("Minimum is", smallest)
# %%
x = '40'
y = int(x) + 2
print(y)
# %%
x = 'From marquard@uct.ac.za'
print(x[14:17])
# %%
greet = 'Hello Bob'
print(greet.upper())
# %%
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
# %%
x = 'From marquard@uct.ac.za'
print(x[8])


# %%
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
print(pos,len(text))
num=text[pos:]
print(num)
num=float(num)
print(num)
# %%
fname = input("Enter file name: ")
# fh = open(fname,"r")
with open(fname) as fh:
    for line in fh:
        line=line.rstrip().upper()
        print(line)


# %%
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fname = "mbox-short.txt"
with open(fname,"r") as f:
    c=0
    t=0
    for line in f:
        line=line.strip()
        if line.startswith("X-DSPAM-Confidence:"):
            pos = line.find("0")
            # print(pos,len(text))
            nums=line[pos:]
            # print(num)
            no=float(nums)
            t+=no
            c+=1
    # print("Count :",c,"total :",t)  
    print("Average spam confidence: ",t/c)

# %%


"""
    Important
    Re module 
    Split function
    caps first letter of every word

"""
import re
s=re.split('(\W)', input())
for j,i in enumerate(s):
    if i.isalpha():
        s[j]=i[0].upper()+i[1:]
print(*s,sep="")    #print(''.join(s))

# %%
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
# %%
fruit = 'Banana'
fruit[0] = 'b'
# ERRORRR!!!!!!!
print(fruit)

# %%

fname="romeo.txt"
uni_words = []
with open(fname,"r") as f:
    for line in f:
        words = line.rstrip().split()

        for x in words:
            if x not in uni_words:
                uni_words.append(x)
    uni_words.sort()
    print(uni_words)


# %%
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
fname = "mbox-short.txt"
with open(fname,"r") as f:
    c=0
    for line in f:
        line=line.strip()
        if line.startswith('From '):
            words=line.split()
            print(words[1])
            c+=1

    print("There were ",c," lines in the file with From as the first word")
# %%


# fname = input("Enter file:")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

fname = "mbox-short.txt"
with open(fname,"r") as f:
    c=0
    words=list()
    counts=dict()
    for line in f:
        line=line.strip()
        if line.startswith('From '):
            words.append(line.split()[1])

    for word in words:
        counts[word] = counts.get(word,0) + 1

    for key,value in counts.items():
        print(key,value)
    max_key = max(counts,key = counts.get)
    print(max_key,counts[max_key])


# %%
data = (1,3,6,5,2,5,2,4,6,3,4,2,6,1)
data_set=set(data)
for i in data_set:
    print(i,data.count(i))

# %%
""" Dict count freq  """
fname = "mbox-short.txt"
words =[]
counts = dict()
with open(fname,"r") as f:
    for line in f:
        line=line.strip()
        if line.startswith('From '):
            word= (line.split()[5].split(':')[0])
            counts[word] = counts.get(word,0) + 1

    for k,v in sorted(counts.items()):
        print(k,v)



        
# %%
print("big">"small")

# %%
for x in range(1, 10, 3):
    print(x)
# %%
for x in range(10):
    for y in range(x):
        print(y)
# %%
"""
    PALINDROME APPROACH
"""
s = "Never Odd or Even"
# s="kayak"
s=s.lower().replace(" ","")
l=len(s)
print(s[0::1],s[l::-1],sep="\n")
if(s[0:l:1] == s[l::-1]):
    print("True")
else: print("False")
# %%
f,l = "Jane","Smith"
f"{f} {l[0]}."
# %%
s,o,r= "abcabcabc", "abc", "xyz"
if s.endswith(o):
    n=s[:-len(o)]+r
    print(n)
# %%
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

[x.replace('.hpp',".h") for x in filenames]

# %%
text = "programming in python is fun"
say=""
words = text.split()
new_words =[]
for word in words:
    new_words.append(word[1:]+word[0]+"ay")

say=' '.join(new_words)
print(say)
# %%

"""
    code to convert a file permission
    in octal format
    into a string format
    eg  755 : rwxr-xr-x
"""
keys = ["0","1","2","3","4","5","6","7"]
values = ['---','--x','-w-','-wx','r--','r-x','rw-','rwx']

mydict = dict(zip(keys,values))

# print(mydict)
s=""
y=755
for x in str(y):
    s += mydict.get(x)

print(s)


# %%

g,glist="Marketing", ["Mike", "Karen", "Jake", "Tasha"]

s=f"{g}: {', '.join(glist)}"
print(s)
# %%

guest_list = [('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")]

for x in guest_list:
    s=f"{x[0]} is {x[1]} years old and works as {x[2]}"
    print(s)
# %%

email_dict = {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}

emails = []

for k,v in email_dict.items():
    l = len(v)
    for i in range(l):
        emails.append(f"{v[i]}@{k}")
print(emails)

# %%
"""
reverse key n value_lists of dict to make new dict
"""
gp_dict = {"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }
user_groups = {}
for k,v in gp_dict.items():
    for i in v:
        user_groups[i] = user_groups.get(i,[])+[k]

print(user_groups)

# %%
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
# %%

addr="1001 1st Ave"
hn,*st = addr.split()
print(hn)
f"house number {hn} on street named {' '.join(st)}"
# %%

s = "Have a nice day"
r = "nice"
# s[:s.find(r)]+r.upper()+s[s.find(r)+len(r):]
s.replace(r,r.upper(),1)
# %%
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
Jamies_list.reverse()
mylist = Drews_list + Jamies_list
mylist
# %%


def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
    guests2.update(guests1)
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# %%


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():
    # Check if the letter needs to be counted or not
        if letter.isalpha():
            result[letter] = result.get(letter,0) + 1
    # Add or increment the value in the dictionary
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
# %%

animal = "Hippopotamus"

print(animal[3:6])
print(animal[-5])
print(animal[10:])
# %%
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
colors
# %%
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()


# %%

def get_events_date(events):
    print(events.date)

# %%
test_dic = {'a': 2, 'b': 3, 'c': 4}
test_new_dic= {}
i = 4
if i in test_dic.values():
    print(test_dic.get())

# %%
""""
    Important re module
"""
import re

common_words=("a","it","the","to","if")

s = "!! it is a== string.! 2 3 123 the; words,;; are to good- hi-= , cool;; With.! !; ;#$ %^ Punctuation? ? yes?"
s = re.sub(r'[^\w\s]','',s)
s= s.split()
print(s)
words = [word for word in s if word not in common_words]
print(words)  


# %%



fname = "romeo.txt" #mbox-short.txt"

common_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
with open(fname,"r") as f:
    c=0
    words=[]
    counts={}

    for line in f:
        line=line.strip().lower()
        line = re.sub(r'[^\w\s]','',line).split()
        words = [word for word in line if word not in common_words]
        for word in words:
            if word.isalpha():
                counts[word] = counts.get(word,0) + 1
    

    for key,value in counts.items():
        print(key,value)

    # cloud = wordcloud.WordCloud()
    # cloud.generate_from_frequencies(counts)
    # cloud.to_file("myfile.jpg")

#%%
import os
fname="romeo.txt"
os.path.getsize(fname)
#%%
import os

# os.mkdir("new_dir")
# os.chdir("new_dir")
os.getcwd()
print(os.listdir("new_dir"))
print(os.rmdir("new_dir"))
# os.mkdir("new_dir")

#%%
import os
import datetime
# print(os.path.getsize(filename))
# print(os.path.getmtime("romeo.txt"))
timestamp=os.path.getmtime("romeo.txt")
print(timestamp)
print(type(timestamp))
timestamp=datetime.datetime.fromtimestamp(timestamp)
print(timestamp)
print(type(timestamp))
timestamp=str(timestamp)
print(timestamp)
timestamp = timestamp.split()
print(type(timestamp))
print(timestamp[0])
# print(datetime.datetime.fromtimestamp(timestamp))
# os.path.abspath("romeo.txt")
# %%
import os
cwd = os.getcwd()
print(cwd)
pwd = os.pardir
print(f'{os.path.abspath(cwd+"/"+pwd)}')
# %%
vals = [25, 30, 33, 35, 40, 180]
new_vals = [i + 32 for i in vals]

print(new_vals)
# %%
def hours_to_seconds(hours):
    return hours * 60 * 60

hours_to_seconds(8)
#%%
def time_to_seconds(hours,minutes):
    print(hours * 60 * 60 + minutes * 60)

time_to_seconds(1,50)
# %%
d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

d['two']

# %%
import random
random.seed(2427)
def efficient_sample(n):
  x = [random.random() for i in range(n)]
  return x

efficient_sample(20)
# %%
[
i for i in range(5) if i > 2
]
# %%
[i * 3 for i in range(5)]

# %%
[i * 2 for i in range(5)]
# %%
d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

d.get('three')

# %%
import numpy as np
age=[1,2,3,4,5,6,7,8]
average_age = np.mean(age)
spread_age = np.std_dev(age)

print(average_age)
print(spread_age.round(2))
# %%
import pandas as pd
data={'temperature':[1,2,3],
  'luminosity':[1,2,3],
  'radius':[7,8,9]}


column_names = [
  'temperature',
  'luminosity',
  'radius'
]
stars = pd.DataFrame(data,
columns=['A','B','C'])
# stars = stars.set_index()
print(stars.describe)

# %%
import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if re.match('^[a-zA-Z]', username):
        return True
    return False



print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
# %%
import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase 
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,;:-']"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  #DEBUG CODE GOES HERE
  print(string1)

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False

# %%

import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails, 
    # which means that we're making a Leap Year calculation
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
  next_date_obj = add_year(date_obj)

  # Convert the datetime object to string, 
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today))) 
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29
# %%
import turtle

Tex=turtle.Turtle()
window = turtle.Screen()
for i in range(6):
    Tex.forward(100)
    Tex.left(60)
window.exitonclick()
# turtle.done()
# %%
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
l=len(sports)
last = sports[l-3:]
print(last)
# %%
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = f"{by} {az}{io}, {qy}"
print(message)  
# %%
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
# for n in range(5):
#     print(n, fruits[n])
for i,j in enumerate(fruits):
    print(i," : ",j)
# %%
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

same_letter_count=0
for i in sentence.split(' '):
    if i.startswith(i[0]) == i.endswith(i[0]):
        same_letter_count+=1
print(same_letter_count)
# %%
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for i in items:
    if 'w' in i:
        acc_num+=1
print(acc_num)

#%%
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e=0
for i in sentence.split():
    if 'a' in i or 'e' in i:
        num_a_or_e+=1
print(num_a_or_e)
# %%
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
for i in s:
    if i in vowels:
        num_vowels+=1
print(num_vowels)
# %%
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
print(b)
# %%
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2,'horseback')
print(sports)
# %%
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.pop(len(trav_dest)-2)
print(trav_dest)
# %%

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars =[]
for i in str1:
    chars.append(i)
print(chars)
# %%

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds =[]
for wrd in wrds:
    wrd+='ed'
    past_wrds.append(wrd)
print(past_wrds)
# %%
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

a_scores=0
for score in scores.split():
    if int(score) >= 90:
        a_scores+=1
print(a_scores)
# %%
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=""
for i in org.split():
    if i not in stopwords:
        acro+=i[0].upper()
print(acro)
# %%
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro=[]
for i in sent.split():
    if i not in stopwords:
        acro.append(i[0:2].upper())
acro='. '.join(acro)
print(acro)
# %%
# palindrome
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(p_phrase,r_phrase,sep="\n")

# %%

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for i in inventory:
    item,stock,cost=i.split(', ')
    print(f"The store has {stock} {item}, each for {cost} USD.")
# %%
"""
    Count number of 
    chars, words and lines
    in a file
"""
with open("travel_plans.txt","r") as f:
    num_chars=num_words=num_lines=0
    for line in f:
        num_lines += 1
        num_chars += len(line)
        line=line.split()
        num_words += len(line)
    print(f"Total \n Characters : {num_chars} \n Words : {num_words} \n Lines : {num_lines}")  
# %%
""" Print first 33 chars of the file """
with open("travel_plans.txt","r") as f:
    line=f.read()
    msg=line[:33]
    print(msg)
# %%
""" assign 2nd word of each line to list """
with open("travel_plans.txt","r") as f:
    three=[]
    for line in f:
        line=line.split()
        three.append(line[1])

    print(three)

# %%

with open("travel_plans.txt","r") as f:
    p_words=[]
    for line in f:
        line=line.split()
        for word in line:
            if 'p' in word:
                p_words.append(word)

    print(p_words)
# %%
""" find avg price and max-rate in SP500.txt 
 col - 2 is  price, col - 5 is rate 
 only read data June 2016 to May 2017 
 i.e, lines 6:18
"""
 
with open("SP500.txt","r") as f:
    rates = []
    avg=0
    count=0
    lines = f.readlines()[6:18]
    for line in lines:
        line=line.split(',')
        # print(line[0]," : ",line[1]," : ",line[7])
        avg+=float(line[1])
        count+=1
        rates.append(line[5])

    mean_SP = avg/count
    max_interest = max([float(i) for i in rates])
    print(mean_SP,max_interest)
# %%
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}

swimmers["Phelps"] = 23
# %%
""" Max key and Max value """

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

k = max(d, key=d.get) #key
print("key " + k + " has the highest value,",d[k])

# %%
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3,
 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = Junior.values()
print(sum(credits))
# %%
""" count chars freq 
    removing spaces """
str1 = "peter piper picked a peck of pickled peppers".replace(" ", "")
freq={}
for char in str1:
    freq[char] = freq.get(char,0) + 1
for k,v in freq.items():
    print(k,v)
# %%
""" freq words in string """
str1 = "I wish I wish with all my heart to fly with dragons in a land apart".split()

freq_words={}
for word in str1:
    freq_words[word] = freq_words.get(word,0) + 1
print(freq_words)
# %%
""" most adn least freq char """
sally = "sally sells sea shells by the sea shore"

characters ={}
for char in sally:
    characters [char] = characters .get(char,0) + 1
best_char = max(characters, key=characters.get)
worst_char = min(characters, key=characters.get)
print(
    "Most Freq -",best_char,"with Freq =",
    characters[best_char],
    "\nLeast Freq -",worst_char,"with Freq =",
    characters[worst_char]
)


# %%

tuples_lst = [('Beijing', 'China', 2008),
 ('London', 'England', 2012),
  ('Rio', 'Brazil', 2016, 'Current'),
   ('Tokyo', 'Japan', 2020, 'Future')]
country = ([i[1] for i in tuples_lst])
print(country)
# %%
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp
# %%
"""
STOP when u reach 7 in a list
return sublist upto number 7
not include 7
using BREAK
"""
def sublist(lst):
    i=0
    sublist = []
    while lst[i] != 7:
        sublist.append(lst[i])
        i+=1
        if i == len(lst):
            break
    return sublist
print(sublist([1, 6, 2, 3, 9]))
#%%
""" 
STOP when u reach 7 in a list
return sublist upto number 7
not include 7
USING SLICES"""
def sublist(lst):
    i=0

    while i < len(lst):
        if lst[i] == 7:
            return lst[:i]
        i+=1
    return lst[:i]
print(sublist([1, 6, 2, 7, 3, 9]))

# %%
""" USING WHile and break"""
def sublist(string_lst):
    i=0
    sublist = []
    while string_lst[i] != "bye":
        sublist.append(string_lst[i])
        i+=1
        if i == len(string_lst):
            break
    return sublist
print(sublist(["hi","bye","STOP"]))


# %%
"""
USING Slices
"""
def sublist(string_lst):
    i=0
    while i < len(string_lst):
        if string_lst[i] == "STOP":
            return string_lst[:i]
        i+=1
    return string_lst[:i]
print(sublist(["hi","bye","STOP"]))

#%%

def beginning(string_lst):
    i=0
    sublist = []
    while string_lst[i] != "bye":
        sublist.append(string_lst[i])
        i+=1
        if i == len(string_lst):
            break
    return sublist
print(beginning(["hi","bye"]))
# %%
"""" LAMBDA func ANONYMOUS func """
print((lambda s:s[::-1])("hello world"))
# %%
"""  non-default argument (b)
 follows default argument (a) """
def sum(x,z=5):
    return z + x

# def sum(z=5, x):    
#     #error x is non default and 
#     # it cannot come after default arg
#     return z + x  

#%%
def test(x,bool=True,dict1={2:3, 4:5, 6:8}):
    if bool == True:
        if x in dict1.keys():
            return dict1[x]
    return False
    
#%%

def checkingIfIn(s,direction=True,d = {
    'apple': 2,
     'pear': 1,
      'fruit': 19,
       'orange': 5,
        'banana': 3,
         'grapes': 2,
          'watermelon': 7}):
    if direction == True:
        if s in d.keys():
            return True
        return False
    else :
        if s not in d.keys():
            return True
        return False
# %%
def checkingIfIn(a, direction = True, d={
    'apple': 2,
    'pear': 1,
    'fruit': 19,
    'orange': 5,
    'banana': 3,
    'grapes': 2,
    'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]
c_false = checkingIfIn('hello')
print(c_false)
c_true = checkingIfIn('hello',direction=False)
print(c_true)
fruit_ans = checkingIfIn('fruit')
print(fruit_ans)
param_check=checkingIfIn('HI',d={'HI':8})
print(param_check)
# %%

""" Sorting list.sort and sorted(list) """
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(s):
    return s[1]
# using func
# sorted_by_second_let = sorted(ex_lst,key=second_let)

# using lambda
sorted_by_second_let = sorted(ex_lst,key=lambda x:x[1])

print(sorted_by_second_let)
# %%
""" sort list """
nums = ['1450', '33', '871',
 '19', '14378', '32',
  '1005', '44', '8907', '16']

def last_char(s):
    # print(s[-1],end=" ")
    return s[-1]
# using function as key parameter
nums_sorted = sorted(nums,key=last_char,reverse=True)
# using Lambda
nums_sorted_lambda = sorted(nums,key=lambda x:x[-1],reverse = True)
print("\n",nums_sorted)
print("\n",nums_sorted_lambda)
#%%
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners =sorted(winners,key=lambda x:x.split()[-1])

# %%
""" Sort freq dict """
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    d[x] = d.get(x,0)+1 # create freq dict of list L

# d.keys() is same as d where d is dict, both returns list of keys
for x in sorted(d,key=lambda k: d[k],reverse=True):
    print(f"{x} appears {d[x]} times")

# %%
"""" Sort breaking ties"""
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# %%
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
print(sorted_weather)

# %%
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_three=sorted(medals,key=lambda x:medals[x],reverse=True)[:3]
print(top_three)
# %%
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed = sorted(groceries,key=lambda x:groceries[x],reverse=True)
# %%
