#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:38:35 2019

@author: pulkitwadhwa
"""


import os
import javalang
import csv

fieldnames=[]

def findFiles(fpath):
    
    fileList=list()
    
    isDirectory = os.path.isdir(fpath)
    if(isDirectory):
        for root, dirs, files in os.walk(fpath):
            for file in files:
                if(file.endswith(".java")):
                    fileList.append(os.path.join(root,file))
    else:
        fileList.append(fpath)

    return fileList




def tokenzier(filelist):     
    List=[]
    for file in filelist:
        file1 = open(file, 'r') 
        print(file)
        lines = file1.read()
        lines=lines.strip()
    
       
       
        Map={}
          
        
        
      
        if(lines[0]=="﻿"):
            lines=lines[1:]
            
        tokens=list(javalang.tokenizer.tokenize(lines))
        for token in tokens:
            token=str(token)
                
            x = token.split()
            key=x[0]
            if key not in Map.keys():
                Map[key]=1
            else:
                val=Map[key]
                Map[key]=val+1
        print(Map)
        for i in Map.keys():
            if i not in fieldnames:
                fieldnames.append(i)
        List.append(Map)
    
    return List
    
def csvWrite(tokenList):    
    with open('CodeClone.csv', 'w') as csv_file:  
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
             
            writer.writeheader()
            for row in tokenList:
                    writer.writerow(row)
                
                
                
if __name__ == '__main__':
    filePath=input("enter file Path")
    fileList=findFiles(filePath)
    tokenList=tokenzier(fileList)
    csvWrite(tokenList)
    
    
    
                    
                