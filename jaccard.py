from nltk.corpus import stopwords
import nltk

def process(file):
    raw=open(file).read()
    words= raw.split()
    porter = nltk.PorterStemmer()
    stemmed_tokens = [porter.stem(t) for t in words]
    stop_words = set(stopwords.words('english'))
    voc = [w for w in stemmed_tokens if not w in stop_words]
    #print(type(r))
    return voc;


def jaccard_similarity(list1,list2):
    intersec = len(set(list1) & set(list2))
    #print(intersec)
    union = (len(list1) + len(list2)) - intersec
    #print(union)
    return float(intersec / union)

def findfile(a):    
    for i in range(1,10):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_000'+ str(i) +'.txt'
        b=process(dict2)
        print('p'+str(i))
        f1.write('000'+str(i)+'  ')
        f1.write(str(jaccard_similarity(a,b)))
        f1.write('\n')
        #print(c)       
    for i in range(10,100):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_00'+ str(i) +'.txt'
        b=process(dict2)
        print('p'+str(i))
        f1.write('00'+str(i)+'  ')
        f1.write(str(jaccard_similarity(a,b)))
        f1.write('\n')        
    for i in range(100,1000):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_0'+ str(i) +'.txt'
        b=process(dict2)
        print('p'+str(i))
        f1.write('0'+str(i)+'  ')
        f1.write(str(jaccard_similarity(a,b)))
        f1.write('\n')        
    for i in range(1000,2001):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_'+ str(i) +'.txt' 
        print('p'+str(i))
        b=process(dict2)
        f1.write(str(i)+'  ')
        f1.write(str(jaccard_similarity(a,b)))
        f1.write('\n')
if __name__ == '__main__':
    f1=open('/home/kayal/Desktop/Dataset/Task_2/j_fullscore.txt','w+')
    for j in range(1,10):
        print("for loop:"+str(j))
        f1.write(",\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_000'+str(j)+'.txt'
        a=process(dict1)
        findfile(a)
    for j in range(10,100):
        print("for loop:"+str(j))
        f1.write(",\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_00'+str(j)+'.txt'
        a=process(dict1)
        findfile(a)   
    for j in range(100,201):
        print("for loop:"+str(j))
        f1.write(",\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_0'+str(j)+'.txt'
        a=process(dict1)
        findfile(a)

for i in range(1,201):
    f2 = open('/home/kayal/Desktop/Dataset/Task_2/project/jaccard/J/j'+str(i)+'.txt','w+')       
    fo = open('/home/kayal/Desktop/Dataset/Task_2/project/jaccard/fullscore.txt','r')
    x = fo.read()
    t=x.split(',')
    f2.write(str(t[i])) 