import matplotlib.pyplot as plt

def statistic(inpath,refpath):
    '''
    统计预测的准确度
    ''' 
    Positive_peak = {}
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            try:Positive_peak[info[0]].append([info[1],info[2],info[-1]])
            except:Positive_peak[info[0]] = [[info[1],info[2],info[-1]]]
    P = 0
    M = 0
    L = 0
    with open(inpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            chrom = info[0]
            start,end=int(info[1]),int(info[2])
            flag = int(info[-1])
            t = 0
            if chrom=='chrM':
                continue
            L+=1
            for peak in Positive_peak[chrom]:
                if end<int(peak[0]):
                    pass
                elif start>int(peak[1]):
                    pass
                else:
                    t = 1
                    break
            if t==flag and flag==1:
                P+=1
            elif t==flag and flag==0:
                M+=1
            print(L/1411732)
    print(P,M,P+M)
    print((P+M)/L,P/L,M/L)
    #print(P/1411732)

def plot_ROC(inpath,refpath):
    '''
    绘制ROC曲线
    '''

    X,Y = [0],[0]
    Positive_peak = {}
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            try:Positive_peak[info[0]].append([info[1],info[2],info[-1]])
            except:Positive_peak[info[0]] = [[info[1],info[2],info[-1]]]
    P = 0
    L = 0
    with open(inpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            chrom = info[0]
            start,end=int(info[1]),int(info[2])
            flag = int(info[-1])
            t = 0
            if chrom=='chrM':
                continue
            L+=1
            for peak in Positive_peak[chrom]:
                if end<int(peak[0]):
                    pass
                elif start>int(peak[1]):
                    pass
                else:
                    #P += 1
                    t=1
                    break
            if t==flag:P+=1
            X.append(L-P)
            Y.append(P)
    for i in range(len(X)):
        X[i]=X[i]/(L-P)
    for i in range(len(Y)):
        Y[i]=Y[i]/P
    plt.figure(figsize=(12,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('ROC curve for model',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('False Positive Rate',fontsize=24)
    plt.ylabel('True Positive Rate',fontsize=24)
    plt.plot(X,Y)
    T=[]
    for n in range(P):
        T.append(n/P)
    plt.plot(T,T)
    plt.legend()
    plt.show()

def plot_image(inpath,refpath):
    '''
    '''
    Positive_peak = {}
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            try:Positive_peak[info[0]].append([info[1],info[2],info[-1]])
            except:Positive_peak[info[0]] = [[info[1],info[2],info[-1]]]
    L = {}
    P = {}
    with open(inpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            chrom = info[0]
            start,end=int(info[1]),int(info[2])
            if chrom=='chrM':
                continue
            try:L[abs(float(info[-2]))]+=1
            except:L[abs(float(info[-2]))]=1
            for peak in Positive_peak[chrom]:
                if end<int(peak[0]):
                    pass
                elif start>int(peak[1]):
                    pass
                else:
                    try:P[abs(float(info[-2]))]+=1
                    except:P[abs(float(info[-2]))]=1
                    break
    res = [[],[]]
    res[0] = sorted(P.keys())
    for i in res[0]:
        res[1].append(P[i])
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('motif hits in rep',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('hits number',fontsize=24)
    plt.ylabel('motif count',fontsize=24)
    plt.scatter(res[0],res[1],c='r')
    res = [[],[]]
    res[0] = sorted(L.keys())
    for i in res[0]:
        if i in P.keys():
            res[1].append(L[i]-P[i])
        else:
            res[1].append(L[i])
    plt.scatter(res[0],res[1],c='b')
    #plt.bar(range(len(res)),res)
    plt.legend()
    plt.show()


if __name__=='__main__':
    inpath = 'prediction/res_Last/G4_positive.bed'
    #inpath = 'prediction/res_Last/G4_TEST_predict_region.bed'
    refpath = 'data/source_data/K562_BG4-ChIP_peaks_comp.narrowPeak'
    #statistic(inpath,refpath)
    plot_ROC(inpath,refpath)
    #plot_image(inpath,refpath)