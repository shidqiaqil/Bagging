import csv
import math
import random
import statistics 
from sklearn.naive_bayes import GaussianNB

jummodel=15
jumtranmodel=150
train=[]
test=[]
datatrain=[]
datatest=[]
x1=[]
x2=[]
y=[]

#membaca data train
with open('TrainsetTugas4ML.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        train.append(row)

#membaca data test
with open('TestsetTugas4ML.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        test.append(row)

#membuang header
train.pop(0)
test.pop(0)

#membuat float data
train=([[float(x) for x in a] for a in train])

def potongtrain():
    x=[]
    for i in range (jumtranmodel):
        x.append(train[random.randint(0,len(train)-1)])
    return [([[a[0],a[1]] for a in x]),([a[2] for a in x])]

# #Fungsi Bayes dengan Library
def bayes(a,b,c):
    bys= GaussianNB()
    bys.fit(a,b)
    return bys.predict(c)[0]
tranformodel=([potongtrain() for i in range(jummodel)])
x2=([[float(a[0]),float(a[1])] for a in test])
with open('TebakanTugas4ML.csv','w', newline='\n') as writefile:
    writer=csv.writer(writefile,dialect='excel')
    for a in x2:
        hasil=[]
        for model in tranformodel:
            hasil.append(bayes(model[0],model[1],[a]))
        writer.writerow([1]) if hasil.count(1)>=hasil.count(2) else writer.writerow([2])
writefile.close()


