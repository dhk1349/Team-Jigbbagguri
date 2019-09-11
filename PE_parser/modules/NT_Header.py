
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
        
#This part is File Header
        
    Machine = libs.little(data[4:6])
    NumbersOfSection = libs.little(data[6:8])
    TimeDateStamp = libs.little(data[8:12])
    SizeOfOptionalHeader = libs.little(data[20:22])
    Chars = libs.little(data[22:24])
    
    print("[NT_Header]-File Header")
    print("{}\t\t{}\t\t{} ".format("offset","value","description"))
    print("============================================")
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+4, Machine, "Machine"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+6, NumbersOfSection, "NumbersOfSection"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+8, TimeDateStamp, "TimeDateStamp"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+20, SizeOfOptionalHeader, "SizeOfOptionalHeader"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+28, Chars, "Characteristics"))
    print("\n")
    
#This part is Optional Header 
#This part is not tested
    fd.seek(NT_Offset+24, 0)
    data=fd.read(224)  #need to check exact number
    Magic=libs.little(data[0:2]) #010B or 020B
    BitStructure = "NONE"
    if (Magic==0x010B):
        BitStructure = "32bits" #determine if its 32 bits or 64 bits
    elif(Magic==0x020B):
        BitStructure = "64bits"
    
    AddressOfEntryPoint 
    ImageBase
    SectionAlignment
    FileAlignment
    SizeOfImage
    SizeOfHeader
    Subsystem
    NumbersOfRvaAndSizes
    """
    print("[NT_Header]-Optional Header")
    print("{}\t\t{}\t\t{} ".format("offset","value","description"))
    print("============================================")
    print("{:x}".format(Magic))
    print(BitStructure)
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+4, Magic, "Magic"))
    #find location of IMAGE_DATA_DIRECTORY