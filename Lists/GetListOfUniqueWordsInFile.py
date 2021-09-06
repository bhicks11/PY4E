# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:13:00 2021

@author: Blair Hicks
"""

def GetListOfUniqueWordsInFile(sourceFile):
    fhandle = open(sourceFile)
    wordList = []
    
    for line in fhandle:
        lineList = line.split()
        for word in lineList:
            if word.upper() in wordList: continue
            wordList.append(word.upper())

    wordList.sort()            
    print(wordList)
    
GetListOfUniqueWordsInFile("romeo.txt")