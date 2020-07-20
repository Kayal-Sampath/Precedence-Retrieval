#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:53:22 2019

@author: kayal
"""

import glob
f1= open ('data_relevant.txt','w+',encoding = "ISO-8859-1")
path = 'matrix/relevant/*.txt' 
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
f2= open ('data_irrelevant.txt','w+',encoding = "ISO-8859-1")
path = 'matrix/irrelevant/*.txt' 
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
        f2.write(l7)
        f2.write('\n')
"""
f1= open ('/home/kayal/Desktop/Dataset/pr/datalabel_cnn.txt','w+',encoding = "ISO-8859-1")
path = '/home/kayal/Desktop/Dataset/pr/data/relevant/*.txt' 
files = glob.glob(path)
for name in files:
    with open(name,encoding = "ISO-8859-1") as f:
        lines = f.read()
        f1.write("1")
        f1.write('\n')


path = '/home/kayal/Desktop/Dataset/pr/data/irrelevant/*.txt' 
files = glob.glob(path)
for name in files:
    with open(name,encoding = "ISO-8859-1") as f:
        lines = f.read()
        f1.write("0")
        f1.write('\n')
"""      