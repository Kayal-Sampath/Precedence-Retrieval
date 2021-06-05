from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import nltk

def process(file):
    raw=open(file).read()
    tokens=word_tokenize(raw)
    words= [w.lower() for w in tokens]
    porter = nltk.PorterStemmer()
    stemmed_tokens = [porter.stem(t) for t in words]
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in stemmed_tokens if not w in stop_words]
    count = nltk.defaultdict(int)
    for word in filtered_tokens:
        count[word] +=1
    return count;

def cos_sim(a,b):
    dot_product = np.dot(a,b)
    norm_a =np.linalg.norm(a)
    norm_b =np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

def getSimilarity(dict1,dict2):
    all_words_list = []
    for key in dict1:
        all_words_list.append(key)
    for key in dict2:
        all_words_list.append(key)
    all_words_list_size = len(all_words_list)
    #print(all_words_list_size)
    v1=np.zeros(all_words_list_size, dtype=np.int)
    v2=np.zeros(all_words_list_size, dtype=np.int)
    i=0
    
    for (key) in all_words_list:
        v1[i] = dict1.get(key, 0)
        try:
            v2[i] = dict2.get(key, 0)
        except AttributeError:
            pass
        i = i + 1
    return cos_sim(v1,v2)
if __name__ == '__main__': 
    f1= open ('/home/kayal/Desktop/Dataset/Task_2/Catch_score.txt','w+',encoding = "ISO-8859-1")
    dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_0001.txt'
    dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_0200.txt'
    getSimilarity(process(dict1),process(dict2))
"""
    #dict2=process('/home/kayal/Desktop/b.txt')
def filesearch(dict1):
    print("function called")    
    for i in range(1,10):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_000'+ str(i) +'.txt' 
        f1.write('000'+str(i)+'  ')
        f1.write(str(getSimilarity(process(dict1),process(dict2))))
        f1.write('\n')
        print("written:"+str(i))
    for i in range(10,100):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_00'+ str(i) +'.txt' 
        f1.write('00'+str(i)+'  ')
        f1.write(str(getSimilarity(process(dict1),process(dict2))))
        f1.write('\n')
        print("written:"+str(i))
    for i in range(100,1000):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_0'+ str(i) +'.txt' 
        f1.write('0'+str(i)+'  ')
        f1.write(str(getSimilarity(process(dict1),process(dict2))))
        f1.write('\n')
        print("written:"+str(i))
    for i in range(1000,2001):
        dict2= '/home/kayal/Desktop/Dataset/Task_2/Prior_Cases/prior_case_'+ str(i) +'.txt' 
        f1.write(str(i)+'  ')
        f1.write(str(getSimilarity(process(dict1),process(dict2))))
        f1.write('\n')
        print("written:"+str(i))
if __name__ == '__main__':
    for j in range(0,201):
        print("for loop:"+str(j))
        f1.write(",")
        f1.write("Current_Case_00"+str(j)+"\n")
        dict1 = '/home/kayal/Desktop/Dataset/Task_2/C/c'+str(j)+'.txt'
        filesearch(dict1) 
fout=open('/home/kayal/Desktop/Dataset/Task_2/current_catch','r')
if __name__ == '__main__': 
    for j in range(1,10):
        print("for loop:"+str(j))
        f1.write(",")
        f1.write("Current_Case_000"+str(j)+"\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_000'+str(j)+'.txt'
        filesearch(dict1)
    for j in range(10,100):
        print("for loop:"+str(j))
        f1.write(",")
        f1.write("Current_Case_00"+str(j)+"\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_00'+str(j)+'.txt'
        filesearch(dict1)
    for j in range(100,201):
        print("for loop:"+str(j))
        f1.write(",")
        f1.write("Current_Case_0"+str(j)+"\n")
        dict1='/home/kayal/Desktop/Dataset/Task_2/Current_Cases/current_case_0200.txt'
        filesearch(dict1)
"""
"""
for i in range(1,201):
    f2 = open('/home/kayal/Desktop/Dataset/Task_2/C1/c'+str(i)+'.txt','w+')       
    fo = open('/home/kayal/Desktop/Dataset/Task_2/Catch_Score.txt','r')
    x = fo.read()
    t=x.split(',')
    f2.write(str(t[i]))   
"""    