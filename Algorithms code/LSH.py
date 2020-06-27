##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 22 13:21:41 2020
#
#@author: pulkitwadhwa
#"""
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn import random_projection
import time


projections=np.random.randn(2,15)
def dot(a):
    a=np.dot(a,projections.T)
    return a




def DataPreparation(dPath):
    df=pd.read_csv(dPath)  
    df=df.fillna(0)
    data = df.iloc[:,:].values
    return data



def hashing(data,flag):
    bucket={}
    
    for vector in range(len(data)):
        if(flag):    
            a=dot(data[vector])
        else:
            a=data[vector]
        f=(''.join((a).astype(float).astype('str')))    
        fin=hash(str(f))
        if(fin in bucket.keys()):
            bucket[fin].append(vector+2)
        else:
            list1=[]
            list1.append(vector+2)
            bucket[fin]=list1
       
    count=0
    
    for i in bucket.keys():
        if(len(bucket[i])>1):
                    print(bucket[i])   
        count=count+len(bucket[i]) 
    print("***")    
    print('Total Count='+str(count))
    print('Unique Count='+str(len(bucket)))


def gaussData(dPath):
    df=pd.read_csv(dPath)  
    df=df.fillna(0)
    data = df.iloc[:,:].values
    transformer = random_projection.GaussianRandomProjection(n_components=2, eps=0.1, random_state=None)
    transformedData = transformer.fit_transform(data)
    return transformedData



if __name__ == '__main__':
    
    
    dPath=input("enter file Path")
    starttime = time.time()
    trainData=DataPreparation(dPath)
    hashing(trainData,True)
    print("--- %s seconds ---" % (time.time() - starttime))
   
    
    starttime = time.time()
    transformedData=gaussData(dPath)
    hashing(transformedData,False)     
    print("--- %s seconds ---" % (time.time() - starttime))







