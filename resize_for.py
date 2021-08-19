from PIL import Image,ImageFilter
import sys
import os

import pdb

def convert(img_name):
    img = Image.open(img_name)
    file_size = os.path.getsize(img_name)
    width = img.size[0]
    height = img.size[1]
    if height >= 1920 or width >= 1920 or file_size >= 2 * 1024 * 1024:
        MIN = min(width/1920,height/1920)
        img_resize = img.resize((int(width),int(height)),Image.LANCZOS)
        img_resize = img_resize.convert("RGB")
        img_name = img_name[:-3]+"jpg"
        print(img_name)
        img_resize.save("resized_"+img_name,quality=90)
    
arg = sys.argv
if len(arg) == 1:
    sys.exit()

for img_name in arg[1:]:
    print(img_name)
    if img_name[-3:] == "png" or img_name[-3:] == "PNG":
        convert(img_name)
    else:
        continue

    """
print(arg)
img = Image.open(arg[1])
file_size = os.path.getsize(arg[1])
print(img.format,img.size,img.mode)
print('File Size:', file_size, 'bytes')
width = img.size[0]
height = img.size[1]

if height >= 1920 or width >= 1920 or file_size >= 2 * 1024 * 1024:
    print("BIG!!")
    print("height:" + str(height / 1920))
    print("width:" + str(width / 1920))
    MIN = min(height/1920,width/1920)
    print(MIN)
    width//=MIN
    height//=MIN
    print(width)
    print(height)
    img_resize = img.resize((int(width),int(height)),Image.LANCZOS)
    #img_resize.save(arg[1])
    #img.thumbnail((,),resample=3)
    print(img_resize.size)
    arg[1] = arg[1][:-3]+"jpg"
    print(arg[1])
    img_resize.save("resized_"+arg[1],quality=90)
"""
