from PIL import Image,ImageFilter
import sys
import os
import zipfile
import io
import glob

Compress = False
def img_convert(img_bin,img_name):
    global Compress
    img = Image.open(img_bin)
    file_size = len(img_bin.getvalue())/1024**2
    width = img.size[0]
    height = img.size[1]
    if height > 1920 and width > 1920 or file_size >= 2 * 1024 * 1024:
        Compress = True
        print("\tConverted")
        MIN = min(width/1920,height/1920)
        img_resize = img.resize((int(width/MIN),int(height/MIN)),Image.LANCZOS)
        img_resize = img_resize.convert("RGB")
        output = io.BytesIO()
        img_resize.save(output,format="JPEG",quality=90)
        return  output.getvalue()
    else:
        print("\tSkip")
        img_resize = img.convert("RGB")
        output = io.BytesIO()
        img_resize.save(output,format="JPEG",quality=90)
        return  output.getvalue()
        return output

if os.name == "nt":
    arg = ["zip.py"]
    arg+=glob.glob(sys.argv[1])
    print(arg)
else :
    arg = sys.argv
if len(arg) == 1:
    print("No ZIP file exist")
    sys.exit()

for i in arg[1:]:
    if i[-4:]==".zip" or i[-4:]==".ZIP":
        print(i)
        zfi = zipfile.ZipFile(i)
        lst = zfi.namelist()

        img_jpg=[]
        img_path=[]
        for img_name in lst:
            if img_name[-3:] == "gif":
                    print("GIF Contain!\nQUIT!")
                    sys.exit()
            if img_name[-3:] == "png" or img_name[-3:] == "PNG" or img_name[-3:] == "jpg" or img_name[-4:] == "jpeg":
                
                
                img_file = zfi.open(img_name)
                img_bin = io.BytesIO(img_file.read())
                print("\t"+img_name)
                img_jpg.append(img_convert(img_bin,img_name))
                img_name = img_name[:-3]+"jpg"
                img_path.append(img_name.split("/")[-1])

        if Compress == True:
            with zipfile.ZipFile(i,"w", compression=zipfile.ZIP_LZMA) as zfo:
                for binary,path in zip(img_jpg,img_path):
                    print("\t"+path)
                    inf = zipfile.ZipInfo(path)
                    zfo.writestr(inf,binary)
            zfo.close()
