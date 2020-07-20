#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 01:50:52 2019

@author: kayal
"""
fout=open('/home/kayal/Desktop/ans.txt','w+')
fin1=open('/home/kayal/Desktop/a.txt')
fin2=open('/home/kayal/Desktop/b.txt')
f1=fin1.readlines()
f2=fin2.readlines()
def file(f1,i):
    for j in range(0,10):
        print(f1[i+j])
        fout.write(str(f1[i+j]))
for i in range(0,2000,10):
    #fout.write(str(f1[i]))
    file(f1,i)
    file(f2,i)
    #fout.write(str(f2[i]))
