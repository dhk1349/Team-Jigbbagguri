# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:39:19 2019

@author: dhk13
"""
import modules.PE_libs as libs
import sys

def find(fd, NT_Offset):
    fd.seek(NT_Offset,0) #move NT_Offset from the beginning
    data=fd.read(248)
    if(data[0:4]!=b'PE\x00\x00'):
        print("Invalid NT Header")
        sys.exit()
        

    Machine = libs.little(data[4:6])
    NumbersOfSection = libs.little(data[6:8])
    TimeDateStamp = libs.little(data[8:12])
    SizeOfOptionalHeader = libs.little(data[20:22])
    Chars = libs.little(data[22:24])
    
    print("[NT_Header]")
    print("{}\t\t{}\t\t{} ".format("offset","value","description"))
    print("============================================")
    print("{:08x}\t{}\t{}".format(NT_Offset+4, Machine, "Machine"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+6, NumbersOfSection, "NumbersOfSection"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+8, TimeDateStamp, "TimeDateStamp"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+20, SizeOfOptionalHeader, "SizeOfOptionalHeader"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+28, Chars, "Characteristics"))
