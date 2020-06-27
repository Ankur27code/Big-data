#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:28:03 2020

@author: pulkitwadhwa
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import datetime


#function to prepare the training Data

def DataPreparation(dPath):
    df=pd.read_csv(dPath)  
    df=df.fillna(0)
    data = df.iloc[:,:].values
    return data


#function to find the right value of k(number of clusters) using inertia
    
def findK(trainData,n):
    Error =[]
    for i in range(1, n):
        kmeans = KMeans(n_clusters = i).fit(trainData)
        kmeans.fit(trainData)
        Error.append(kmeans.inertia_)
    return Error


#fucntion to plot the elbow

def plotElbow(Error,n):
    plt.plot(range(1, n), Error)
    plt.title('Elbow method')
    plt.xlabel('No of clusters')
    plt.xticks(range(0, n,2))    
    plt.ylabel('Inertia')
    plt.show()    
    
#function to cluster the data and plot the cluster    
def kMeans(trainData,k):
    kmeans = KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=10000,n_clusters=k , n_init=11, n_jobs=1,
                precompute_distances='auto',
 random_state=None, tol=0.0001, verbose=0)
    y_kmeans = kmeans.fit_predict(trainData)
    plt.figure(figsize=(10,5))
    plt.scatter(trainData[:,0],trainData[:,1],c=y_kmeans,cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
    plt.xlim([-100,1500])
    plt.ylim([-100,8000])
    plt.xticks(range(0, 1500,75))
    plt.xlabel('Keyword')
    plt.ylabel('Identifier')
    plt.show() 



    
if __name__ == '__main__':
    dPath=input("enter file Path")
    trainData=DataPreparation(dPath)
    n=21   
    Error=findK(trainData,n)
    plotElbow(Error,n)
    k=5
    kMeans(trainData,k)
    
       

    