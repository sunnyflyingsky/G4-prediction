
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
    #matrix = [[0]*3000 for _ in range(44218)]
    t = 0
    with open(outpath,'w') as write_object:
        for line in read_object2:
            info = line.strip().split('\t')
            chrom = info[0]
            j = 0
            res = list(range(int(info[1]),int(info[2]),1))
            for i in range(int(info[1]),int(info[2]),1):
                while chrom in ref.keys() and j<len(ref[chrom]):
                    if int(ref[chrom][j][0])>i:
                        break
                    elif int(ref[chrom][j][1])<i:
                        j+=1
                    else:
                        res.remove(i)
                        break
            if res==[]:continue
            start = res[0]
            end = res[0]
            for k in range(len(res)-1):
                if res[k+1]==res[k]+1:
                    end+=1
                else:
                    write_object.write('{}\t{}\t{}\n'.format(chrom,start,end))
                    start = res[k+1]
                    end+=1
            t+=1
            print(t/50838)


    



if __name__ == '__main__':
    compare('data/source_data/G4_TEST_predict_region_sorted.bed','data/source_data/K562_BG4-ChIP_peaks_comp.narrowPeak','data/source_data/NoG4_TEST_predict_region.bed')




