from PIL import Image,ImageFilter
import sys
import os
import zipfile
import io

def img_convert(img_bin,img_name):
    img = Image.open(img_bin)
    file_size = len(img_bin.getvalue())/1024**2
    width = img.size[0]
    height = img.size[1]
    if height >= 1920 or width >= 1920 or file_size >= 2 * 1024 * 1024:
        MIN = min(width/1920,height/1920)
        img_resize = img.resize((int(width/MIN),int(height/MIN)),Image.LANCZOS)
        img_resize = img_resize.convert("RGB")
        #os.remove(img_name)
        output = io.BytesIO()
        img_resize.save(output,format="JPEG",quality=90)
        return  output.getvalue()
        
arg = sys.argv
if len(arg) == 1:
    print("No ZIP file exist")
    sys.exit()
    
zfi = zipfile.ZipFile(arg[1])
lst = zfi.namelist()


for img_name in lst:
    if img_name[-3:] == "png" or img_name[-3:] == "PNG":
        img_file = zfi.open(img_name)
        img_bin = io.BytesIO(img_file.read())
        print(img_name)
        img_jpg=img_convert(img_bin,img_name)
        img_name = img_name[:-3]+"jpg"
        img_path = img_name.split("/")
        #print(img_path[-1])
        zfi.close()
        with zipfile.ZipFile(arg[1],"a") as zfo:
            zfo.write(img_path[-1])
        #inf = zipfile.ZipInfo(img_path[-1])
        #zfi.writestr(inf,img_jpg)
        zfi = zipfile.ZipFile(arg[1])
