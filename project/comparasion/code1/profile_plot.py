import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(x):
    return 1 /(1 + math.exp(-x))

def main(inpath1,refpath,outpath):
    '''
    '''
    strand = []
    with open(refpath) as read_object:
        for line in read_object:
            s = line.strip().split('\t')[-1]
            if s == '-':strand.append(-1)
            elif s == '+': strand.append(1)
            else:strand.append(1)
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('G4_TSS_Profile',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('Relative distance to TSS',fontsize=24)
    plt.ylabel('Average signal',fontsize=24)
    X = [x for x in range(-1000,2000,1)]
    #print(len(X))
    Y = [0]*3000
    t = 0
    with open(inpath1) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            t+=1
            for i in range(len(Y)):
                Y[i] += float(info[i])#*strand[t-1]
    for i in range(len(Y)):
        Y[i] = Y[i]/t
    #ym = min(Y)
    #for i in range(len(Y)):
    #    if Y[i]==ym:print(i)
    plt.plot(X,Y,'r',label='G4 profile')
    """
    Y = [0]*2000
    t = 0
    with open(inpath2) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            t+=1
            for i in range(len(Y)):
                Y[i]+=float(info[i])
    for i in range(len(Y)):
        Y[i] = Y[i]/t
    plt.plot(X,Y,'b',label='ATAC-seq')
    """
    plt.xticks([X[0],X[len(X)//3],X[-1]],labels=['-1kb','TSS','2kb'],fontsize=24)
    plt.legend(loc='upper right')
    plt.show()

if __name__=='__main__':
    main('data/source_data/G4_2a_3k_matrix_siteprof1','data/source_data/hg19_gene3k_sorted.bed','comparasion/ATAC&Nuc')