# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:09:20 2019

@author: dhk1349
"""
import modules.PE_libs as libs

def find(fd, offset, sections):
    print("[Section header]")
    print("============================================")

    print("{}\t\t{}\t\t{} ".format("offset","value","description"))
    Section_offset=offset
    for i in range(sections):
        Section_offset=section_iterator(Section_offset, fd)
        
    
def section_iterator(offset,fd):
    fd.seek(offset)
    data=fd.read(40)
    Name = libs.big(data[0:6])
    VirtualSize = libs.little(data[8:12])
    VirtualAddress = libs.little(data[12:16])
    SizeOfRawData = libs.little(data[16:20])
    PointerToRawData = libs.little(data[20:24])
    Chars = libs.little(data[36:40])

    print("{:08x}\t{:05x}\t{}".format(offset+0, Name, "Name"))
    print("{:08x}\t{:04x}\t{}".format(offset+8, VirtualSize, "VirtualSize"))
    print("{:08x}\t{:04x}\t{}".format(offset+12, VirtualAddress, "VirtualAddress"))
    print("{:08x}\t{:04x}\t{}".format(offset+16, SizeOfRawData, "SizeOfRawData"))
    print("{:08x}\t{:04x}\t{}".format(offset+20, PointerToRawData, "PointerToRawData"))
    print("{:08x}\t{:04x}\t{}".format(offset+36, Chars, "Characteristics"))
    print("\n")
    return offset+40