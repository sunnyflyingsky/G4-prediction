import matplotlib.pyplot as plt
import numpy as np

def main(inpath1,inpath2,refpath,outpath):
    '''
    绘制位点信号相关性图谱
    针对每个基因TSS位点或者G4 summits位点绘制MNase-seq和ATAC-seq的相关性散点图
    '''
    X = []
    Y = []
    strand = []
    with open(refpath) as read_object:
        for line in read_object:
            s = line.strip().split('\t')[-1]
            if s == '-':strand.append(-1)
            elif s == '+': strand.append(1)
            else:strand.append(1)
            
    t = 0
    with open(inpath1) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            t+=1
            X.append(float(info[1000])*strand[t-1])
            #int(float(info[1000])*100)/100
    t = 0 
    with open(inpath2) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            t += 1
            Y.append(float(info[1000])*strand[t-1])
    #print(X)
    #print(X[1000:1100])
    #print(Y[1000:1100])
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('relationship between MNase-seq and G4 peak in TSS',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('MNase-seq signal',fontsize=24)
    plt.ylabel('G4 ChIP-seq signal',fontsize=24)
    plt.scatter(X,Y,c='r',marker='.',label='G4 ChIP-seq & MNase-seq')
    plt.xlim(-0.5,0.5)
    plt.ylim(-10,25)
    plt.legend(loc='upper right')
    #plt.savefig(outpath, dpi=300)
    plt.show()


 


if __name__=='__main__':
    main('data/source_data/K562_82_matrix_siteprof1','data/source_data/K562_1a_logLR_matrix_siteprof1','data/source_data/hg19_gene3k_sorted.bed','comparasion/ATAC&Nuc')