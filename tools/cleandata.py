#clean damaged data
import os,shutil
from PIL import Image

def is_valid(file):
    valid = True
    try:
        Image.open(file).load()
    except OSError:
        valid = False
    return valid



dimg=[]
for root,dirs,files in os.walk("./GCCdata_Dataset/GCCdata_Dataset/"):
	pass
for img in files:
	if not is_valid("./GCCdata_Dataset/GCCdata_Dataset/"+img):
		print(img)
		dimg.append(img)
		shutil.move("./GCCdata_Dataset/GCCdata_Dataset/"+img,"./delimg/")    
print(len(dimg))
