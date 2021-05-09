import matplotlib.pyplot as plt
def map(inpath,refpath,outpath):
    '''
    '''
    gene6k = {}
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            try:gene6k[info[0]].append([info[1],info[2],info[3]])
            except:gene6k[info[0]]=[[info[1],info[2],info[3]]]
    read_object=open(inpath)
    print('run!')
    res = [0]*6000
    chrom = 'chr1'
    t = 0 
    i=0
    with open(outpath,'w') as write_object:
        for line in read_object:
            info = line.strip().split('\t')
            print(t/1400000)
            t+=1
            if info[0]!=chrom:
                chrom = info[0]
                i = 0
            start,end=int(info[1]),int(info[2])
            score = float(info[4])
            while chrom in gene6k.keys() and i<len(gene6k[chrom]):
                if start > int(gene6k[chrom][i][1]):
                    i+=1
                elif end < int(gene6k[chrom][i][0]):
                    break
                else:
                    s = max(start,int(gene6k[chrom][i][0]))
                    e = min(end,int(gene6k[chrom][i][1]))
                    for j in range(s-int(gene6k[chrom][i][0]),e-int(gene6k[chrom][i][0]),1):
                        if gene6k[chrom][i][2]=='-':
                            res[j]+=score*(-1)
                        else:res[j]+=score
                    break
        for k in range(len(res)):
            write_object.write(str(res[k])+'\t')
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('motif hits in TSS',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('distance to TSS',fontsize=24)
    plt.ylabel('motif count',fontsize=24)
    plt.plot(range(len(res)),res,'r',label='G4 profile')
    plt.xticks([0,3000,6000],labels=['-3kb','TSS','3kb'],fontsize=24)
    plt.legend(loc='upper right')
    plt.show()




if __name__=='__main__':
    inpath = 'prediction/res2/hg19_G4_predict_region.bed'
    refpath = 'data/source_data/hg19_gene6k_sorted.bed'
    outpath = 'comparasion/G4_third/res/hg19_G4_motif_profile'
    map(inpath,refpath,outpath)














