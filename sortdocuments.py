
for i in range(1,201):
    f2 = open('E1/em'+str(i)+'.txt','w+')       
    fo = open('em'+str(i)+'.txt','r')
    x = fo.readlines()
    sort_key = lambda line: float(line.split('  ', 1)[1])
    sorted_x = sorted(x, key=sort_key, reverse=True)
    count=0
    for s in sorted_x:
        if count<5:
            f2.write(s)
            count=count+1  
