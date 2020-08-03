#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:16:06 2020

@author: ankuraggarwal
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import time

projections=np.random.randn(1,2)

def DataPreparation(dPath):
    df=pd.read_csv(dPath)  
    df=df.fillna(0)
    data = df.iloc[:,:].values    
    data = PCA(n_components=2).fit_transform(data)    
    return data



def kMeans(trainData,k):

    kmeans = KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=10000,n_clusters=k , n_init=11, n_jobs=1,
                precompute_distances='auto',
     random_state=None, tol=0.0001, verbose=0)
    kmeans.fit_predict(trainData)
    
    labels = kmeans.labels_    

    return labels


    


def ClusterIndicesNumpy(clustNum, labels_array): #numpy 
     return (np.where(labels_array == clustNum)[0])
 
    
def hashing(data,labels,n):    
    clusters={}
    for cluster in range(n):
        clusterLabels=ClusterIndicesNumpy(cluster,labels)
        dict2={}
    
        for j in range(len(clusterLabels)):
            element=clusterLabels[j]
            f=(''.join((data[element]).astype(np.float32).astype('str')))

            fin=hash(str(f))
            if(fin in dict2.keys()):
                dict2[fin].append(element+2)
            else:
                list1=[]
                list1.append(element+2)
                dict2[fin]=list1
        for j in dict2.keys():
            if(len(dict2[j])>1):
                print(dict2[j])        
        clusters[cluster]=dict2
        
            
    
    count=0
    for cluster in clusters.keys():
        count=count+len(clusters[cluster]) 
    print(count) 
   





if __name__ == '__main__':
    
    
    dPath=input("enter file Path")
    starttime = time.time()

    trainData=DataPreparation(dPath)
    k=5
    labels=kMeans(trainData,k)
    hashing(trainData,labels,k)
   
    print("--- %s seconds ---" % (time.time() - starttime))





