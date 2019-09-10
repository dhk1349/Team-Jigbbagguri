# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:41:33 2019

@author: dhk13
"""

def little(var): #little endian transition
    result=0
    for i in reversed(var):
        result*256
        result+=i
    return result

def big(var):
    result=0
    for i in var:
        result*256
        result+=i
    return result

