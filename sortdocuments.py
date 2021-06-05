
for i in range(200,201):
    f2 = open('/home/kayal/Desktop/Dataset/Task_2/embed/E1/em'+str(i)+'.txt','w+')       
    fo = open('/home/kayal/Desktop/Dataset/Task_2/embed/E/em'+str(i)+'.txt','r')
    x = fo.readlines()
    sort_key = lambda line: float(line.split('  ', 1)[1])
    sorted_x = sorted(x, key=sort_key, reverse=True)
    count=0
    for s in sorted_x:
        if count<5:
            f2.write(s)
            count=count+1  
""" 
ff=open('/home/kayal/Desktop/Dataset/Task_2/embed/whole_emb.txt','w+')
for i in range(1,201):
    f = open('/home/kayal/Desktop/Dataset/Task_2/embed/E1/em'+str(i)+'.txt','r')
    k=f.read()
    ff.write('Current_Case_'+str(i)+'\n')
    ff.write(str(k))
    ff.write('\n')    
"""   