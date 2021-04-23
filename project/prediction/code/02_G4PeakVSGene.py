
def compare(inpath1,inpath2,outpath):
    '''
    '''
    ref = {}
    read_object1 = open(inpath1)
    for line in read_object1:
        info = line.strip().split('\t')
        try:
            ref[info[0]].append((info[1],info[2]))
        except:
            ref[info[0]]=[(info[1],info[2])]
    read_object2 = open(inpath2) 
    matrix = [[0]*3000 for _ in range(44218)]
    t = 0
    with open(outpath,'w') as write_object:
        for line in read_object2:
            info = line.strip().split('\t')
            chrom = info[0]
            j = 0
            for i in range(int(info[1]),int(info[2]),1):
                while chrom in ref.keys() and j<len(ref[chrom]):
                    if int(ref[chrom][j][0])>i:
                        break
                    elif int(ref[chrom][j][1])<i:
                        j+=1
                    else:
                        matrix[t][i-int(info[1])]=1
                        break
            t+=1
            print(t/44218)
        for nums in matrix:
            for num in nums:
                write_object.write(str(num)+'\t')
            write_object.write('\n')



if __name__ == '__main__':
    compare('data/source_data/K562_BG4-ChIP-rep_1a_peaks.narrowPeak','data/source_data/hg19_gene3k_sorted.bed','data/source_data/K562_1a_score_matrix.txt')




