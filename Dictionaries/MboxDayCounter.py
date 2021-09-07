# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:00:29 2021

@author: Blair Hicks
"""

def MboxDayCounter(sourceFile):
    fhandle = open(sourceFile)
    
    dow = dict()
    for line in fhandle:
        if line.find('From ') == -1: continue
        line = line.split()
        dow[line[2]] = dow.get(line[2], 0) + 1
        
    print(dow)
        
MboxDayCounter('mbox-short.txt')