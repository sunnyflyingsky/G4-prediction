
def score(inpath,outpath):
    write_object = open(outpath,'w')
    with open(inpath) as read_object:
        for line in read_object:
            label = line.strip().split('\t')[-1]
            if int(label):
                write_object.write(line)

def score_s(inpath,refpath,outpath):
    '''
    '''
    Positive_peak = {}
    write_object = open(outpath,'w')
    with open(refpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            try:Positive_peak[info[0]].append([info[1],info[2],info[-1]])
            except:Positive_peak[info[0]] = [[info[1],info[2],info[-1]]]
    with open(inpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            chrom = info[0]
            start,end=int(info[1]),int(info[2])
            if int(info[-1]):
                write_object.write(line)
                continue
            if chrom=='chrM':
                continue
            for peak in Positive_peak[chrom]:
                if end<int(peak[0]):
                    pass
                elif start>int(peak[1]):
                    pass
                else:
                    if abs(float(info[-2]))>=1.6:
                        write_object.write(line)
                    break

def pipline(inpath,outpath):
    '''
    '''
    write_object = open(outpath,'w')
    with open(inpath) as read_object:
        for line in read_object:
            label = line.strip().split('\t')[-1]
            num = int(line.strip().split('\t')[-2])
            if num>=4 or int(label):
                write_object.write(line)




if __name__=='__main__':
    #inpath = 'prediction/res2/hg19_G4_predict_region.bed'
    #outpath = 'prediction/res2/G4_positive_4.bed'
    #refpath = 'data/source_data/K562_BG4-ChIP_peaks_comp.narrowPeak'
    #score_s(inpath,refpath,outpath)
    #inpath = 'prediction/res2/G4_positive_3.bed'
    #outpath = 'prediction/res2/G4_positive_4.bed'
    #pipline(inpath,outpath)
    inpath = 'prediction/res_Last/G4_hg19_predict_region.bed'
    outpath = 'prediction/res_Last/G4_positive_hg19.bed'
    score(inpath,outpath)

