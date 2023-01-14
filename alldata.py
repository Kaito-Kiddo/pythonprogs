"""
All codes of
Python 3 Programming Specialization
Course 3 - W1 

Data Collection and Processing with Python
University of Michigan

Course 5 - w1 - w3
OpenCV tesseract pillow
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

from dis import dis
import json
from sys import displayhook
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
""" C5 W1  """
print("hello")
# %%
import PIL
PIL.__version__
help(PIL)
dir(PIL)

# %%
from PIL import Image
file="kaito.jpg"
image=Image.open(file)
print(image)


# %%
import inspect
print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))
# %%
image.show()
# %%
from IPython.display import display
display(image)
# %%
from PIL import Image
file="kaito.jpg"
image=Image.open(file)
image.save("kaito.png")

# %%
image =Image.open("kaito.png")
import inspect
inspect.getmro(type(image))

# %%
from PIL import ImageFilter
# help(ImageFilter)
blurred_image=image.filter(PIL.ImageFilter.BLUR)

display(blurred_image)
# %%
print("{}x{}".format(image.width, image.height))
# %%
display(image.crop((200,0,500,250)))




# ----------------------------------
# %%
import PIL
from PIL import Image
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("kaito.png")
image=image.convert('RGB')


# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Color(image)
images=[]
for i in range(1, 10):
    images.append(enhancer.enhance(0.1))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

# %%
import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from PIL import ImageEnhance


# read image and convert to RGB
# image=Image.open("readonly/msi_recruitment.gif")
image=Image.open("kaito.png")
image=image.convert('RGB')

imagesnew=[]




for i in [0.1,0.5,0.9]:
    picture_new = Image.new('RGB', (800, 500))
    for x in range(image.width):
        for y in range(image.height):
            r,g,b= image.getpixel((x,y))
            r= int (i*r)
            picture_new.putpixel((x,y),(r,g,b))
    # get a font
    #fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 15)
    picture_txt = ImageDraw.Draw(picture_new)
    picture_txt.text((100,465),"channel 1.0 intensity {}.".format (i),font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40) ,fill=(255,255,255,0))
    imagesnew.append (picture_new)
    
for i in [0.1,0.5,0.9]:
    picture_new = Image.new('RGB', (800, 500))
    for x in range(image.width):
        for y in range(image.height):
            r,g,b= image.getpixel((x,y))
            g= int (i*g)
            picture_new.putpixel((x,y),(r,g,b))
    picture_txt = ImageDraw.Draw(picture_new)
    picture_txt.text((100,465),"channel 2.0 intensity {}.".format (i),font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40) ,fill=(255,255,255,0))
    imagesnew.append (picture_new)
    
for i in [0.1,0.5,0.9]:
    picture_new = Image.new('RGB', (800, 500))
    for x in range(image.width):
        for y in range(image.height):
            r,g,b= image.getpixel((x,y))
            b= int (i*b)
            picture_new.putpixel((x,y),(r,g,b))
    picture_txt = ImageDraw.Draw(picture_new)
    picture_txt.text((100,465),"channel 3.0 intensity {}.".format (i),font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40) ,fill=(255,255,255,0))
    imagesnew.append (picture_new)

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3+150))
x=0
y=0

for img in imagesnew:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))

    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height+50
    else:
        x=x+first_image.width

        
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

display(contact_sheet)

#%%
""" --------------------------------------  """
from PIL import Image, ImageEnhance
from IPython.display import display
# Opening Image
im = Image.open(r"Kaito.png")
im = im.convert('RGB')
(w,h) = (im.width,im.height)
new_images = []
for z in range(3):
        
    for i in [0.1,0.5,0.9]:
        picture_new = Image.new('RGB', (w,h))


        for x in range(w):
            for y in range(h):
                r,g,b= im.getpixel((x,y))
                if z == 0 : r = int (i*r)
                elif z == 1 : g = int(i*r)
                elif z == 2 : b = int(i*b)
                picture_new.putpixel((x,y),(r,g,b))

        # display(picture_new)
        new_images.append(picture_new)

first_image=new_images[0]
contact_sheet=Image.new(first_image.mode, (w*3,h*3+150))
x=0
y=0

for imgs in new_images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(imgs, (x, y))

    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+w == contact_sheet.width:
        x=0
        y=y+h+50
    else:
        x=x+w

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

display(contact_sheet)


# %%
from PIL import Image
import pytesseract
image = Image.open(r"Kaito.png")
# text = pytesseract.image_to_string(image)
# print(text)
w = image.getpixel((0,0))
# %%
import zipfile
file_name = r".\test\small_img.zip"
unzip = zipfile.ZipFile(file_name, 'r')
unzip.extractall(path=r".\test")    
unzip.close()
# %%
with zipfile.ZipFile(file_name) as zip:
    # zip.printdir()
    info = zip.infolist()
    ext = zip.namelist()
    print(ext)

    #extract 1 file
    zip.extract(ext[1],r".\test")



