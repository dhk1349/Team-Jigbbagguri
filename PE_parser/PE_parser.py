# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:52:50 2019

@author: dhk13
"""
import pefile
import binascii
#PEheader=pefile.PE('C:\\Windows\\System32\\notepad.exe')

fd=open('C:\\Windows\\System32\\notepad.exe', 'rb')
file_data=fd.read()
fd.seek(2, 0)
seek_data=fd.read()
print(seek_data)   #read를 하면 b'가 같이 저장되는데 
#print(binascii.b2a_hex(file_data))
