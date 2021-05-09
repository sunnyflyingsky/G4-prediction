import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
def main(inpath,refpath,outpath):
    '''
    绘制热图
    '''
    strand = []
    with open(refpath) as read_object:
        for line in read_object:
            s = line.strip().split('\t')[-1]
            if s == '-':strand.append(-1)
            elif s == '+': strand.append(1)
            else:strand.append(1)
    #print(strand)
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('G4_peak_heatmap',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('Relative distance to G4 peak summits',fontsize=24)
    plt.ylabel('Average signal',fontsize=24)
    #X = [x for x in range(-4500,4500,3)]
    Y = []
    with open(inpath) as read_obejct:
        for line in read_obejct:
            info = line.strip().split('\t')
            Y.append([])
            for i in range(len(info)):
                Y[-1].append(float(info[i]))

    heat_map = sns.heatmap(Y,cmap='Blues_r',vmin=0,vmax=5)
    plt.xticks([0,1500,3000],labels=['-3kb','center','3kb'],fontsize=24)
    plt.yticks([],fontsize=24)
    #plt.legend(loc='upper right')
    plt.show()    


if __name__=='__main__':
    main('data/source_data/K562_2a_82_matrix_siteprof1','data/source_data/K562_2a.bed','comparasion/ATAC&Nuc')