#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:13:03 2019

@author: ssn-9
"""
"""
f=open("intermediate_relevant.txt","r")
lines = f.read()
l1=lines.split('\n\n')
for i in range(1,1001):
    f1= open ('inter/data_lstm'+str(i)+'.txt','w+',encoding = "ISO-8859-1")
    f1.write(l1[i-1])
"""    
import glob
f1= open ('data_relevant.txt','w+',encoding = "ISO-8859-1")
path = 'inter/*.txt' 
files = glob.glob(path)
for name in files:
    with open(name,encoding = "ISO-8859-1") as f:
        lines = f.read()
        l2=lines.replace('\n','')
        l3=l2.replace(']','')
        l4=l3.replace('[','')
        l5=l4.replace('   ',',')
        l6=l5.replace('  ',',')
        l7=l6.replace(' ',',')
        f1.write(l7)
        f1.write('\n')
