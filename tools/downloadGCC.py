# coding: utf8
import requests
import random

def download_img(img_url, savepath, imgname, api_token=None):
	succ=1
	print (img_url)
	#header = {"Authorization": "Bearer " + api_token} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
	r=None
	try:
		r = requests.get(img_url,timeout=5)
	except:
		succ=-1
		print("timeout")
	if r:
		print(r.status_code) # 返回状态码
		if r.status_code == 200:
		    open(savepath+imgname, 'wb').write(r.content) # 将内容写入图片
		    #print("done")
		else:
			succ=-1
		del r
	return succ


#pp=0.0632*1.3 #for val
pp=0.0006*1.03*1 #for train
imgnum=53458
targetpath='E:\\20fall\\ML\\final\\GCCdata'
failedimg=[]
proddata=""
with open("Train_GCC-training.tsv","r",encoding='UTF-8') as f:
	for l in f:
		if random.random()>pp:
			continue
		l=l.strip()
		tokens=l.split("http")
		#imgname=l.split("/")[-1].split("?")[0]
		img_url="http"+tokens[1]
		caption=tokens[0]
		if ".png" in l:
			imgname=str(imgnum)+".png"
		else:
			imgname=str(imgnum)+".jpg"
		imgnum+=1
		d=download_img(img_url,targetpath+"\\trainimg\\",imgname)
		if d==-1:
			failedimg.append(img_url)
		else:
			proddata+=imgname+","+caption+"\n"

# with open("failedimg.txt","a") as f:
# 	for l in failedimg:
# 		f.write(str(l))
with open("trainimgcaption.txt","w",encoding='UTF-8') as f:
	f.write(proddata)