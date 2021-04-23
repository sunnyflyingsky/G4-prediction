
def Seq2Region(inpath,outpath):
    '''
    '''
    read_obejct = open(inpath)
    with open(outpath,'w') as write_object:
        for line in read_obejct:
            if line.startswith('>'):
                chrom = line.strip().replace('>','')
            else:
                info = line.strip().split('\t')
                write_object.write('{}\t{}\t{}\t{}\t{}\n'.format(\
                    chrom,info[0],info[1],info[2],info[4]))

def mapping(inpath,refpath,outpath):
    '''
    '''
    motif = []
    with open(inpath) as read_obejct:
        read_obejct.readline()
        for line in read_obejct:
            info = line.strip().split('\t')
            motif.append(info)
            #print(motif)
    write_object = open(outpath,'w')
    for k,info in enumerate(motif):
        flag = 0
        m = info[1]
        l = len(info[1])
        with open(refpath) as read_obejct:
            for line in read_obejct:
                if line.startswith('>'):
                    chrom = line.strip().replace('>','')
                    print(chrom)
                    loci = 0
                    sequence = ''
                else:
                    sequence+=line.strip()
                    for i in range(0,len(sequence)-l+1,1):
                        if sequence[i:i+l]==m:
                            write_object.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(\
                                info[0],info[1],chrom,loci,loci+l,info[2],info[3],info[4],info[5]))
                            flag = 1
                        loci+=1
                    sequence = sequence[i:]
                if flag:break
        print(k/len(motif))



if __name__=='__main__':
    inpath = 'data/source_data/hg19-Merged_complete.txt'
    outpath = 'data/source_data/hg19_G4_predict_region.bed'
    Seq2Region(inpath,outpath)
    #inpath = 'data/source_data/S1_S2_g4_motif.txt'
    #refpath = 'data/source_data/hg19.fa'
    #outpath = 'data/source_data/S1_S2_g4_motif_region.bed'
    #mapping(inpath,refpath,outpath)
