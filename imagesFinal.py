#%%
""" --------------------------------------  """
from PIL import Image, ImageFont,ImageDraw
from IPython.display import display
# Opening Image
im = Image.open(r"Kaito.png")
im = im.convert('RGB')
(w,h) = (im.width,im.height)
new_images = []
for z in range(3):
    for i in [0.1,0.5,0.9]:
        picture_new = Image.new('RGB', (w,h+50))
        for x in range(w):
            for y in range(h):
                r,g,b= im.getpixel((x,y))
                if z == 0 : r = int (i*r)
                elif z == 1 : g = int(i*r)
                elif z == 2 : b = int(i*b)
                picture_new.putpixel((x,y),(r,g,b))
        picture_txt = ImageDraw.Draw(picture_new)
        # picture_txt.text((100,465),"channel 1.0 intensity {}.".format (i),font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40) ,fill=(255,255,255,0))

        picture_txt.text((0,h+15),f"channel {z} intensity {i}.",fill=(255,255,255,0))
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
""" FINAL ONly works in COursera lab"""
from PIL import Image, ImageFont,ImageDraw
from IPython.display import display
# Opening Image
im = Image.open("readonly/msi_recruitment.gif")
im = im.convert('RGB')
(w,h) = (im.width,im.height)
new_images = []
for z in range(3):
    for i in [0.1,0.5,0.9]:
        picture_new = Image.new('RGB', (w,h+50))
        for x in range(w):
            for y in range(h):
                r,g,b= im.getpixel((x,y))
                if z == 0 : r = int (i*r)
                elif z == 1 : g = int(i*r)
                elif z == 2 : b = int(i*b)
                picture_new.putpixel((x,y),(r,g,b))
        picture_txt = ImageDraw.Draw(picture_new)
        picture_txt.text((0,h+15),f"channel {z} intensity {i}.",font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40) ,fill=(255,255,255,0))

#         picture_txt.text((0,h+15),f"channel {z} intensity {i}.",fill=(255,255,255,0))
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
""" another better approach"""

import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont
from IPython.display import display
# read image and convert to RGB
# image=Image.open("readonly/msi_recruitment.gif")
image=Image.open("Kaito.png")
image=image.convert('RGB')
#r, g, b = image.getpixel((1, 1))
#print(r, g, b)
# build a list of 9 images which have different brightnesses
#enhancer=ImageEnhance.Brightness(image)
#draw = ImageDraw.Draw(image)
#fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", 75)
#draw.text((10, 400), "Hello world!", font = fnt)
images = []
lables = []
for i in range(3):
    for j in (0.1,0.5,0.9):
        source = image.split()
        x = source[i].point(lambda x:x*j)
        source[i].paste(x)
        im = Image.merge(image.mode, source)
        lables.append('channel {} intensity {}'.format(i,j))
        images.append(im)
for img in images:
    display(img)
# Recombine back to RGB image
# %%
