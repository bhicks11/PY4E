# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:25:34 2021

@author: Blair Hicks
"""

def ListAndCountSenders(sourceFile):
    fHandle = open(sourceFile)
    
    senderCount = 0
    
    for line in fHandle:
        line = line.rstrip()
        if line.find('From ') == -1: continue
        senderCount += 1
        lineWords = line.split()
        print(lineWords[1])
        
    print("There were", senderCount, "lines in the file with From as the first word")

ListAndCountSenders('mbox-short.txt')