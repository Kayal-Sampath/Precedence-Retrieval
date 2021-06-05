from sklearn.metrics.pairwise import cosine_similarity
import numpy
def execute(f,m,pi):
    f1=f.read()
    f1s=f1.split(']\n[')
    len1=len(f1s)-1
    for j in range(1,len1):
        list2=str(f1s[j]).split(' ')
        list13=[]
        for i in range(0,len(list2)):
            try:
                list13.append(float(list2[i]))
            except ValueError:
                pass;
        loop(list13,j,len1,m,pi)
def loop(l,j,len1,m,pi):
    fin2=open('prior_embedding/vector'+str(pi)+'.txt','r')
    #print(pi)
    execute1(l,fin2,j,len1,m,pi)
    
def execute1(l,p,j,len1,m,pi):
    p1=p.read()
    p1s=p1.split(']\n[')
    len2=len(p1s)-1
    for y in range(1,len2):
        listp2=str(p1s[y]).split(' ')
        listp13=[]
        for z in range(0,len(listp2)):
            try:
                listp13.append(float(listp2[z]))
            except ValueError:
                pass;  
        s=cosine_similarity([l],[listp13])
        matrix(s,j,y,len1,len2,m,pi)
def matrix(v,j,y,len1,len2,m,pi):
    for q in range (0,len1-1):
        for r in range (0,len2-1):
            m[j-1,y-1]=v
def input1(pi):
    f31=open('current_embedding/vector142.txt','r')
    len1=calculate_length(f31)
    print(len1)
    f32=open('prior_embedding/vector'+str(pi)+'.txt','r')
    len2=calculate_length(f32)
    print(len2)
    m = numpy.zeros(shape=(len1-2,len2-2), dtype=float)
    return m
def calculate_length(f):
    a1=f.read()
    a1s=a1.split(']\n[')
    len1=len(a1s)
    return len1;
def inputfile(m,pi):
    file1=open('current_embedding/vector142.txt','r')
    execute(file1,m,pi)
def write_result(m1,b):
    o=open('irrelevant_mat/142'+'-'+str(b)+'.txt','w+')
    numpy.set_printoptions(threshold=numpy.nan)
    o.write(str(m1))
if __name__ == '__main__':
    print('CC142')
    prior=['1195']
    for pi in prior:
        print('Prior case:'+pi)
        m=input1(pi)
        inputfile(m,pi)
        write_result(m,pi)
