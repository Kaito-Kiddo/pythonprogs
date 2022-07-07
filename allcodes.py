#%%
from cmath import isnan
from curses.ascii import isalpha, isspace
from operator import contains
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
