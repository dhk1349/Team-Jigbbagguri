# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:34:42 2019

@author: dhk13
"""
import pslist
import re
location="C:\\Users\\dhk13\\Desktop\\직박구리\\memory.dmp"
location2="C:\\Users\\dhk13\\Desktop\\직박구리\\자료\\volatility_2.6_win64_standalone\\volatility_2.6_win64_standalone\\training.vmem"

fd=open(location2, 'rb')
data=fd.read()

kdbg=b'KDBG'
INITkdbg=b'INITKDBG'
result=[]
result2=[]
num=0

while True:
    num=data.find(kdbg, num+1)
    if(num==-1):
        break;
    result.append(num)

while True:
    num=data.find(INITkdbg, num+1)
    if(num==-1):
        break;
    result2.append(num+4)
   
for i in result2:
    indexnum=result.index(i)+1
    fd.seek(result[indexnum]-50)
    data=fd.read(100)
    for i in range(len(data)):
        if(data[i]==248):
            if(data[i+1]==255 and data[i+2]==255):
                print("offset: ",hex(result[indexnum]))
                #print(data)
                break;

print("done")