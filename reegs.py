#%%
""""
    Important re module QUESTIONS
"""
from http.client import NETWORK_AUTHENTICATION_REQUIRED
import re

common_words=("a","it","the","to","if")

s = "!! it is a== string.! 2 3 123 the; words,;; are to good- hi-= , cool;; With.! !; ;#$ %^ Punctuation? ? yes?"
s = re.sub(r'[^\w\s]','',s)
s= s.split()
print(s)
words = [word for word in s if word not in common_words]
print(words)  
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

Regex_Pattern = r'^hack$'	# Do not delete 'r'.
import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))


# %%
s = "From: xyzcorp@google.com sat sun 14:20"
y = re.findall("^From: (\S*)",s)
z = re.findall("^From: .*@(\S*)",s)
print(z) 
# %%
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
# %%
s="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
re.findall('\S+?@\S+',s)

# %%
fname ="regex_sum.txt"
with open(fname,"r") as f:
    lines = f.read()
# print(lines)
total=0
y=re.findall('([0-9]+)',lines)
# print(y)
for t in y:
    total+=int(t)
print(total)
# %%
import re
s ="12-34-56-87"
ss="12345678"
regex = "^(\d{8})|(\d{2}-\d{2}-\d{2}-\d{2})$"
l=re.findall(regex,s)
print(l)
# %%
# Only works in php or perl
s="tactactic"
ss="tactactictactic"
regex = "^(\2tic|(tac))+$"
re.findall(regex,s)
# %%
""""
    Hackerrank match html links,name
"""
import re
s = r'<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
s=r'<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>'
n=int(input())
for i in range(n):
    s = input()
    print(s)
    url = re.findall('href="(.+)"',s)
    url_name =re.findall('(?<=>)([a-zA-Z\. ]+)</',s) 
    print(*url,",",*url_name,sep="")
# %%

import re
def transform_record(record):
    # pno = re.split(",",record)[1]
    # new_record = re.sub(pno,"+1-"+pno,record)
    new_record= re.sub()
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

# %%
import re
def multi_vowel_words(text):
  pattern = r"\w+[aeiou]{3}\w+"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
# %%

import re
def transform_comments(line_of_code):
  result = re.sub('#{1,}','//',line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
# %%

import re
def convert_phone_number(phone):

    result = re.sub(r"\W(\d{3})-(\d{3}-\d{4}\W)",r" (\1) \2",phone)
    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
# %%

import re
def change_domain(file):

    result = re.sub(r"\W(\d{3})-(\d{3}-\d{4}\W)",r" (\1) \2",phone)
    return result