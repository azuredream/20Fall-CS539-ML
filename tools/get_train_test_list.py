import os
trainf=open("./GCCdata_text/GCC_8k.trainImages.txt","w",encoding="UTF-8")
testf=open("./GCCdata_text/GCC_8k.testImages.txt","w",encoding="UTF-8")
for root, dirs, files in os.walk("./GCCdata_Dataset/GCCdata_Dataset/"):
	pass
testlist=""
trainlist=""
for f in files:
	tokens=f.split(".")
	if int(tokens[0])<20000:#test
		testlist+=f+"\n"
	else:
		trainlist+=f+"\n"
trainf.write(trainlist)
testf.write(testlist)
