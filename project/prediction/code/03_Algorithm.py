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
    y = logr.predict([X_train[0]])
    z = logr.predict_proba([X_train[0]])
    joblib.dump(logr,'''data/train_model_old.m''')

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

def main(inpath,refpath):
    '''
    '''
    X = []
    Y = []
    with open(inpath) as read_object:
        for line in read_object:
            sig = []
            info = line.strip().split('\t')
            for num in info:
                sig.append(float(num))
            X.append(sig)
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            label = int(info[-1])
            Y.append(label)
    LR(X,Y) 

if __name__ == '__main__':
    #main('data/source_data/K562_82_matrix_siteprof1','data/source_data/K562_1a_logLR_matrix_siteprof1','data/source_data/hg19_gene3k_sorted.bed')
    #main('data/source_data/K562_82_matrix_siteprof1','data/source_data/K562_1a_score_matrix.txt','data/source_data/hg19_gene3k_sorted.bed')
    inpath='data/source_data/G4_motif_TEST_matrix_siteprof1'
    refpath='data/source_data/motif_mix_sorted.bed'
    main(inpath,refpath)
    

