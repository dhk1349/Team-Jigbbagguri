# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:17:20 2019

@author: dhk13
"""

import modules.PE_libs as libs
import struct
def find(fd):
    
    print("[DOS_Header]")
    print("{}\t{}\t{} ".format("offset","value","description"))
    print("============================================")
    
    e_magic=fd.read(2) #e_magic
    
    var=struct.pack('<|', e_magic)
    print(var)
    fd.seek(0x40-4)
    lfanew=fd.read(4)
    e_magic = libs.big(e_magic)
    lfanew = libs.little(lfanew)
    
    print("{:08x}\t{:04x}\t{}".format(0x00000000, e_magic, "DOS Signature"))
    print("{:08x}\t{:08x}\t{}".format(0x0000003C, lfanew, "Offset to NT Header"))
    print("\n\n")
    
    return lfanew