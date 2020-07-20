#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:07:21 2019

@author: ssn-9
"""

fin=open("irr.txt",'r')
f1=fin.readlines()
fout=open('irr1.txt','w')
for i in range(0,1185,5):
    for j in range(i,i+4):
        c1=f1[j]
        c2=c1.rstrip('\n')
        print(c2)
        fout.write(str(c2)+'   ')
    for j in range(i+4,i+5):
        c1=f1[j]
        print(c1)
        fout.write(str(c1))