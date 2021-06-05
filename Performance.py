import numpy as np
fin1=open('output.txt','r')
fin2=open('ground_truth.txt','r')

f1=fin1.read()
f2=fin2.read()
pre=f1.split('\n')
act=f2.split('\n')

s=[]
score = 0.0000
hit=0


for i in range(0,200):
    hit=0
    score=0
    s=0
    for j in range(0,5):
        p=(pre[i].split(' ')[j])
        for k in range(0,5):
            a=(act[i].split(' ')[k])
            #print(a+' '+p)
            if a==p:
                #print('1')
                hit=hit+1
                score = hit /5

    s=np.mean(score)        
            

