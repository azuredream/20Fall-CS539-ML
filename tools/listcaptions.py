#imglists -> captions
import os
f=open("./GCCdata_text/captions.txt","r",encoding="UTF-8")
newf=open("./GCCdata_text/newcaptions.txt","w",encoding="UTF-8")
d={}
r=""
for root,dirs,files in os.walk("./GCCdata_Dataset/GCCdata_Dataset/"):
	pass
for line in f:
	tokens=line.split(",")
	r+=line if tokens[0] in files else ""

newf.write(r)
newf.close()
f.close()
