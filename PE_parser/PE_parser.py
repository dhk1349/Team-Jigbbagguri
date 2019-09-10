# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:52:50 2019

@author: dhk13
"""
#import pefile
import modules.DOS_Header as DOS_Header
import modules.NT_Header as NT_Header

#PEheader=pefile.PE('C:\\Windows\\System32\\notepad.exe')

'''
functions you need to know
f.seek(n) n번째 바이트로 이동
f.seek(n,1) 현재 위치 기준으로 n바이트 이동x`s
f.seek(n,2) 맨 마지막에서 n바이트 이동
f.tell() 현재 파일 포인터 위치 반환

f.read(n) n만큼 읽기

#fd.seek(2, 0)
seek_data=fd.read(2)        
print(seek_data)   #read를 하면 b'가 같이 저장되는데 
#print(binascii.b2a_hex(file_data))

'''

def main():
    fd=open('C:\\Windows\\System32\\notepad.exe', 'rb')
    
    NT_Offset=DOS_Header.find(fd)
    NT_Header.find(fd, NT_Offset)
if __name__=="__main__":
    main()