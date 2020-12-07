import Levenshtein
import csv
import pickle

#set filename and run
filename="cps-model1.csv"

#--------------------------------
def get_equal_rate(str1, str2):
   return Levenshtein.ratio(str1, str2)

f=open("./full-8092-dataset.pkl","rb")
ansdic=pickle.load(f)


with open(filename,"r") as f:
	row=csv.reader(f,delimiter = ',')
	#next(row) #skiphead
	simlist=[]
	for r in row:
		k=r[0]
		yhat=r[1]
		tempsim=[]#5
		for y in ansdic[k]:
			tempsim.append(get_equal_rate(yhat,y))
		simlist.append(max(tempsim))

re=sum(simlist)/len(simlist)
print(re)

