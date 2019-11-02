# -*- coding: utf-8 -*-
"""
@author: dhk13
"""

def PstreeModule(txtinput):
        """
        input  format
        Name-PID-PPID-threads-handles-time

        Name: "." stands for number of layer, str(addr:name)
        time: (yymmdd) (time) (UTC+0000)

        How it works
        one of (n-1)*.(proc_name) should be parant of (n)*.(proc_name)

        primary key
        str(layer+addr)

        values:
        addr
        #of dots
        PID
        PPID
        handles
        threads
        time
        """
        data=open(txtinput)
        line=data.readline()
        line=data.readline()
        while(True):
            line=data.readline()
            splits=line.split()
            threads=splits[-5]
            handles=splits[-4]
            time=str(splits[-3])+" "+str(splits[-2])+" "+str(splits[-1])
        Insert_req="""대충 insert 명령"""

class PsTree:
    def __init__(self):
        self.Nodelist=[]

    def BuildTree(self):


class Node:
    def __init__(self):
        self.PID
        self.PPID
        self.info

    def GetInfo(self):
        return self.info

    def
