import numpy as np
import pandas as pd
from sklearn import datasets
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt
import random
import math

def LR(X,y):
    '''
    '''
    X_train,X_test, y_train, y_test = train_test_split(X,y)
    logr = LogisticRegression(C=1)
    logr.fit(X_train,y_train)
    print("测试集准确度:",logr.score(X_test,y_test))
    print("训练集准确度:",logr.score(X_train,y_train))
    joblib.dump(logr,'''data/train_model_18.m''')

def sigmoid(x):
    return 1 /(1 + math.exp(-x))

def plotSigmoid(X,Y):
    X,Y=[],[]
    for i in range(0,100,1):
        a = (random.randint(0,100)-50)/10
        X.append(a)
    X = sorted(X)
    for x in X:
        Y.append(sigmoid(x))
    plt.plot(X,Y,'r',label='sigmoid')
    plt.legend()
    plt.show()

def main(inpath1,inpath2,refpath):
    '''
    '''
    X,Y = [],[]
    strand = []
    MAXl = 0
    with open(refpath) as read_object:
        for line in read_object:
            s = line.strip().split('\t')[-1]
            if s == '-':strand.append(-1)
            elif s == '+': strand.append(1)
            else:strand.append(1)
    a = 0
    with open(inpath2) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            a+=1
            if a%10!=2:continue
            t = int(info[0])
            Y.append(t)
            if X and len(X[-1])>MAXl:MAXl=len(X[-1])
            X.append([])
            for num in info:
                if int(num)!=t:
                    t = int(num)
                    Y.append(t)
                    if X and len(X[-1])>MAXl:MAXl=len(X[-1])
                    X.append([0])
                else:
                    X[-1].append(0)
    print(Y.count(1))
    j,k = 0,0
    a = 0
    with open(inpath1) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            a+=1
            if a%10!=2:continue
            for i in range(len(info)):
                if j >= len(X):break
                if k<len(X[j]):
                    X[j][k] = float(info[i])#*strand[a-1]
                    k+=1
                else:
                    print(j/len(X))
                    j += 1
                    k = 0
    for j in range(len(X)):
        avg = sum(X[j])/len(X[j])
        for i in range(len(X[j]),MAXl,1):
            X[j].append(avg)
            #print(t*100/(44218*2))
    #for i in range(len(info)):
    #    X[i][0] = X[i][0]/t
    """
    t = 0 
    with open(inpath2) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            t += 1
            if t%100!=1:
                continue
            for i in range(len(info)):
                Y.append(float(info[i])*strand[t-1])
            #print((t*100+44218)/(44218*2))
    
    for i in range(len(Y)):
        Y[i]=1 if abs(Y[i])>0.5 else 0
    """
    print(Y.count(1))
    #print(X[1000:2000])
    #print(Y[2000:3000])
    LR(X,Y) 

if __name__ == '__main__':
    #main('data/source_data/K562_82_matrix_siteprof1','data/source_data/K562_1a_logLR_matrix_siteprof1','data/source_data/hg19_gene3k_sorted.bed')
    main('data/source_data/K562_82_matrix_siteprof1','data/source_data/K562_1a_score_matrix.txt','data/source_data/hg19_gene3k_sorted.bed')
    
    

