import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score

data_train = np.loadtxt('subs_train.csv', delimiter=',')
x_train=data_train[:,0:100]
y_train=data_train[:,100]

data_test = np.loadtxt('subs_test.csv', delimiter=',')
x_test=data_test[:,0:100]
y_test=data_test[:,100]

data =svm.SVC(kernel='linear', C=0.1,probability=True )
data.fit(x_train,y_train)
#print("training Accuracy")
predicted=data.predict(x_test)
a=accuracy_score(y_test,predicted)
fout=open('subs_final_out.txt','w+',encoding = "UTF-8")
def checkdigits(c2):
    return len(str(c2))
def insert(i,fout):
    fin=open('r_ir.txt','r')
    f2=fin.readlines()
    try:
        c1=f2[i-1]
        c2=c1.rstrip('\n')
        return c2;
    except IndexError:
        print(i)

for i in range(0,500):
    print(i)
    #print(data.classes_)
    print(data.predict_proba(x_test)[i][0])
    print(data.predict_proba(x_test)[i][1])
    if(data.predict_proba(x_test)[i][0]<=data.predict_proba(x_test)[i][1]):
        print('relevant')
        c2=insert(i+1500,fout)
        n=checkdigits(c2)
        #print(n)
        if n==1:
            fout.write('000'+str(c2))
            fout.write('\n') 
        elif n == 2:
            fout.write('00'+str(c2))
            fout.write('\n')
        elif n == 3:
            fout.write('0'+str(c2))
            fout.write('\n')
        else:
            fout.write(str(c2))
            fout.write('\n')
#    elif(data.predict_proba(x_test)[i][1]>0.7):
#        print('relevant')
#        c2=insert(i,fout)
#        n=checkdigits(c2)
#        #print(n)
#        if n==1:
#            fout.write('000'+str(c2))
#            fout.write('\n') 
#        elif n == 2:
#            fout.write('00'+str(c2))
#            fout.write('\n')
#        elif n == 3:
#            fout.write('0'+str(c2))
#            fout.write('\n')
#        else:
#            fout.write(str(c2))
#            fout.write('\n')            
    else:
        #print(data.predict_proba(x_test)[i][1])
        fout.write('-ir-')
        fout.write('\n')
        print('irrelevant')
        #insert1(i,fout)
        
