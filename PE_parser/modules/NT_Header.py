
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
    if(BitStructure=="None"):
        print("Something wrong with optional header parser")
        sys.exit()
    AddressOfEntryPoint = libs.little(data[16:20])
    SectionAlignment = libs.little(data[32:36])
    FileAlignment = libs.little(data[36:40])
    SizeOfImage = libs.little(data[56:60])
    SizeOfHeader = libs.little(data[60:64])
    Subsystem = libs.little(data[68:70])
    if (BitStructure=="32bits"):        
        ImageBase = libs.little(data[28:32])
        NumbersOfRvaAndSize = libs.little(data[92:96])
    elif (BitStructure=="64bits"): #64bits
        ImageBase = libs.little(data[24:32])
        NumbersOfRvaAndSize = libs.little(data[108:112])

    print("[NT_Header]-Optional Header {} structure".format(BitStructure))
    print("{}\t\t{}\t\t{} ".format("offset","value","description"))
    print("============================================")

    print("{:08x}\t{:04x}\t{}".format(NT_Offset+24, Magic, "Magic"))
    print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+16   , AddressOfEntryPoint, "Address of Entry  Point"))
    if(BitStructure=="32bits"):
        print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+28   , ImageBase, "ImageBase"))
    elif (BitStructure=="64bits"):
        print("{:08x}\t{:016x}\t{}".format(NT_Offset+24+24   , ImageBase, "ImageBase"))
        
    
    print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+32   , SectionAlignment, "SectionAlignment"))
    print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+36   , FileAlignment, "FileAlignment"))
    print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+56   , SizeOfImage, "SizeOfImage"))
    print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+60   , SizeOfHeader, "SizeOfHeader"))
    print("{:08x}\t{:04x}\t{}".format(NT_Offset+24+68   , Subsystem, "Subsystem"))
    if(BitStructure=="32bits"):
        print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+92   , NumbersOfRvaAndSize, "NumbersOfRvaAndSize"))
    elif (BitStructure=="64bits"):
        print("{:08x}\t{:08x}\t{}".format(NT_Offset+24+108   , NumbersOfRvaAndSize, "NumbersOfRvaAndSize"))
    print("\n")
    return 24+SizeOfOptionalHeader, NumbersOfSection
    #find location of IMAGE_DATA_DIRECTORY