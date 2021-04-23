# coding: utf-8
 
import numpy as np
import math
from sklearn import datasets
from collections import Counter
infinity = float(-2**31)

#逻辑回归的实现

 
def sigmodFormatrix(Xb,thetas):
    params = - Xb.dot(thetas)
    r = np.zeros(params.shape[0])#返回一个np数组
    for i in range(len(r)):
        r[i] = 1 /(1 + math.exp(params[i]))
    return r
 
def sigmodFormatrix2(Xb,thetas):
    params = - Xb.dot(thetas)
    r = np.zeros(params.shape[0])#返回一个np数组
    for i in range(len(r)):
        r[i] = 1 /(1 + math.exp(params[i]))
        if r[i] >=0.5:
            r[i] = 1
        else:
            r[i] = 0
    return r

def sigmod(Xi,thetas):
    params = - np.sum(Xi * thetas)
    r = 1 /(1 + math.exp(params))
    return r
 
class LinearLogsiticRegression(object):
    thetas = None
    m = 0
    #训练
    def fit(self,X,y,alpha = 0.01,accuracy = 0.00001):
        #插入第一列为1，构成xb矩阵
        self.thetas = np.full(X.shape[1]+1,0.5)
        self.m = X.shape[0]
        a = np.full((self.m,1),1)
        Xb = np.column_stack((a,X))
        dimension  = X.shape[1]+1
        #梯度下降迭代
        count = 1
        while True:
            oldJ = self.costFunc(Xb, y)
            #注意预测函数中使用的参数是未更新的
            c = sigmodFormatrix(Xb, self.thetas)-y
            for j in range(dimension):
                self.thetas[j] = self.thetas[j] -alpha * np.sum(c * Xb[:,j])
            newJ = self.costFunc(Xb, y)
            if newJ == oldJ or math.fabs(newJ - oldJ) < accuracy:
                print("代价函数迭代到最小值，退出！")
                print("收敛到:",newJ)
                break
            print("迭代第",count,"次!")
            print("代价函数上一次的差:",(newJ - oldJ))
            count += 1
 
    #预测
    def costFunc(self,Xb,y):
        sum = 0.0
        for i in range(self.m):
            yPre = sigmod(Xb[i,], self.thetas)
            #print("yPre:",yPre)
            if yPre ==1 or yPre == 0:
                return infinity
            sum += y[i]*math.log(yPre)+(1 - y[i])*math.log(1-yPre)
        return -1/self.m * sum
    def predict(self,X):
        a = np.full((len(X),1),1)
        Xb = np.column_stack((a,X))
        return sigmodFormatrix2(Xb, self.thetas)
    def score(self,X_test,y_test):
        y_predict = myLogstic.predict(X_test)
        re = (y_test==y_predict)
        re1 = Counter(re)
        a = re1[True] / (re1[True]+re1[False])
        return a


#if __name__=="main":
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X= iris['data']
y = iris['target']
X = X[y!=2]
y=y[y!=2]
X_train,X_test, y_train, y_test = train_test_split(X,y)
myLogstic = LinearLogsiticRegression()    
myLogstic.fit(X_train, y_train)
y_predict = myLogstic.predict(X_test)
print("参数:",myLogstic.thetas)
 
print("测试数据准确度:",myLogstic.score(X_test, y_test)) 
print("训练数据准确度:",myLogstic.score(X_train, y_train)) 
 
 
'''
2.sklean中的逻辑回归
'''

from sklearn.linear_model import LogisticRegression
print("sklern中的逻辑回归:")
logr = LogisticRegression()
logr.fit(X_train,y_train)
print("准确度:",logr.score(X_test,y_test))    