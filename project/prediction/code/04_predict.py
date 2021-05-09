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
    t=0
    print('step1')
    with open(inpath) as read_object: 
        for line in read_object: 
            t+=1
            info = line.strip().split('\t')
            sig = []
            for num in info:
                sig.append(float(num))
            X = [sig]
            Y.append(PredictModel.predict(X)[0])
            print(t/1141173)
    print('step2')
    print(Y.count(1))
    read_object = open(refpath)
    t = 0 
    with open(outpath,'w') as write_object:
        for line in read_object:
            info = line.strip().split('\t')
            write_object.write('\t'.join(info)+'\t'+str(Y[t])+'\n')
            t+=1

if __name__=='__main__':
    print('run!')
    #inpath = 'data/source_data/G4Hunter_TEST_82_matrix_siteprof1'
    inpath = 'data/source_data/G4_motif_hg19_matrix_siteprof1'
    refpath = 'data/source_data/G4Hunter_predict_region.bed'
    #modelpath1 = 'data/train_model_18.m'
    modelpath2 = 'data/train_model_old.m'
    outpath = 'prediction/res_Last/G4_hg19_predict_region.bed'
    predict(inpath,refpath,modelpath2,outpath)
    print('end!')




