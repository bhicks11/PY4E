# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:23:12 2021

@author: Blair Hicks
"""

def StoreWordsInDict(sourceFile):
    fhandle = open(sourceFile)
    wordlist = dict()
    
    for line in fhandle:
        words = line.split()
        for word in words:
            wordlist[word] = wordlist.get(word, 0) + 1
        
    print(wordlist)
    
StoreWordsInDict('words.txt')