import struct
import numpy as np

def main(inpath,annotationpath,outpath):
    '''
    '''
    gene_position = {}
    read_obejct = open(annotationpath)
    for line in read_obejct:
        info = line.strip().split('\t')
        if info[0] not in gene_position.keys():
            gene_position[info[0]]=[]
        gene_position[info[0]].append((int(info[1]),int(info[2])))
    write_obejct = open(outpath,'w')
    read_obejct = open(inpath,'r')
    #print(gene_position[:10])
    y,windows = [],[]
    chrom_flag = 'chr1'
    l,steps,i = 2,10,0
    for line in read_obejct:
        if line.startswith('#'):continue
        info = line.strip().split('\t')
        chrom,start_p,end_p,score = info[0],int(info[1]),int(info[2]),float(info[3])
        if chrom!=chrom_flag:
            chrom_flag=chrom
            i = 0
        if chrom_flag not in gene_position.keys():
            break
        #if i >= len(gene_position[chrom_flag]):break
        #if start_p > gene_position[chrom_flag][i][0]:
        #    start_p = gene_position[chrom_flag][i][0]
        for p in range(start_p,end_p,1):
            if i >=len(gene_position[chrom_flag]):
                break
            if p < gene_position[chrom_flag][i][0]:
                pass
            elif p >= gene_position[chrom_flag][i][0] and p < gene_position[chrom_flag][i][1]:
                windows.append((p,float(score)))
                if len(windows)>=l:
                    y.append(str(sum(list(zip(*windows))[1])/len(windows)))
                    windows = []
            elif p >= gene_position[chrom_flag][i][1]:
                i+=1
                if len(y)>=3000:
                    write_obejct.write('\t'.join(y))
                    write_obejct.write('\n')
                    print(i/len(gene_position[chrom_flag])*100)
                y=[] 


if __name__=='__main__':
    main('data/source_data/SRR3211682_profile.wig','data/source_data/K562_2a.bed','data/82_2a_matrix.csv')



