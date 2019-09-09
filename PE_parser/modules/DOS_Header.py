# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:17:20 2019

@author: dhk13
"""

def find(fd):
    
    print("[DOS_Header]")
    print("{}\t{}\t{} ".format("offset","value","description"))
    print("============================================")
    
    e_magic=fd.read(2) #e_magic
    fd.seek(0x40-4)
    lfanew=fd.read(4)
    lfanew_num=0x00
    for i in reversed(lfanew):
        lfanew_num<<2
        lfanew_num+=i
        
    
    print("{:08x}\t{}\t{}".format(0x00000000, e_magic, "DOS Signature"))
    
    print("{:08x}\t{:08x}\t{}".format(0x0000003C, lfanew_num, "Offset to NT Header"))
    #[print("{:02x}".format(i), end="") for i in reversed(lfanew)]
    #print("\t{}".format("Offset to NT Header"))
    
    
    return hex(lfanew_num) 