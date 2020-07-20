#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fout=open('c_concat_ir.txt','w+')

fin1=open("irr1.txt",'r')
f1=fin1.readlines()
def file_compare(i,c1):
    fin2=open('ans/t'+str(i+1)+'.txt','r')
    f2=fin2.readlines()
    f3=f2[c1-1].split('  ')[1]
    print(f3)
    fout.write(str(f3))
for i in range(0,200):
    for j in range(0,4):
        c1=f1[i].split('   ')[j]
        print(c1)
        file_compare(i,int(c1))
    for j in range(4,5):
        c1=f1[i].split('   ')[j]
        c2=c1.rstrip('\n')
        print(c2)
        file_compare(i,int(c1))

    