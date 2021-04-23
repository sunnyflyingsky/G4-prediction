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
def predict(inpath,refpath,modelpath,outpath):
    '''
    '''
    strand = []
    PredictModel = joblib.load(filename=modelpath)
    Y = []
    with open(refpath) as read_object:
        for line in read_object:
            score = float(line.strip().split('\t')[-1])
            if score>0:
                strand.append(1)
            else:strand.append(-1)
    t=0
    print('step1')
    with open(inpath) as read_object: 
        for line in read_object: 
            t+=1
            info = line.strip().split('\t')
            X = [[]]
            for num in info:
                X[0].append(float(num))#*strand[t-1])
            Y.append(PredictModel.predict(X))
            print(t/141173)
    print('step2')
    read_object = open(refpath)
    t = 0 
    with open(outpath,'w') as write_object:
        for line in read_object:
            info = line.strip().split('\t')
            write_object.write('\t'.join(info)+'\t'+str(Y[t][0])+'\n')
            t+=1




if __name__=='__main__':
    print('run!')
    inpath = 'data/source_data/G4Hunter_TEST_82_matrix_siteprof1'
    refpath = 'data/source_data/G4_TEST_predict_region_sorted.bed'
    modelpath1 = 'data/train_model_18.m'
    #modelpath2 = 'data/train_model_TrueLable.m'
    outpath = 'prediction/res2/G4_TEST_predict_region_2.bed'
    predict(inpath,refpath,modelpath1,outpath)
    print('end!')




