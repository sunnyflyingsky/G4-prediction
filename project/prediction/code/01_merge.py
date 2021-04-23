def merge(inpath,outpath):
    '''
    将G4Hunter没有merge起来的序列merge起来
    '''
    read_object = open(inpath)
    flag=0
    with open(outpath,'w') as write_object:
        for line in read_object:
            if line.startswith('>'):
                if flag:
                    write_object.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(start,end,sequence,len(sequence),score/NBR,t+1))
                    flag = 0
                write_object.write(line)
                start,end,score,NBR = 0,0,0,0
                t = 0
                sequence = ''
            elif line.startswith('Start'):
                pass
            else:
                info = line.strip().split('\t')
                if len(info)==6:flag=1
                if end>=int(info[0]):
                    end = int(info[1])
                    score+=float(info[4])
                    sequence=sequence[:int(info[0])-start]+info[2].strip()
                    NBR+=1
                else:
                    if start!=0 and end!=0:
                        write_object.write('{}\t{}\t{}\t{}\t{}\n'.format(start,end,sequence,len(sequence),score/NBR))
                        t+=1
                        score,NBR=0,0
                    start=int(info[0])
                    end=int(info[1])
                    score+=float(info[4])
                    sequence=info[2].strip()
                    NBR+=1

def merge_peak(file_list,outpath):
    '''
    '''
    write_object = open(outpath,'w')
    res = {}
    for name in file_list:
        print(name)
        inpath = 'data/source_data/'+name
        with open(inpath) as read_object:
            for line in read_object:
                info = line.strip().split('\t')
                chrom = info[0]
                if chrom in res.keys():
                    flag = 1
                    for i,peak in enumerate(res[chrom]):
                        if int(peak[0])>int(info[2]):
                            pass
                        elif int(peak[1])<int(info[1]):
                            pass
                        else:
                            res[chrom][i]=[str(min(int(peak[0]),int(info[1]))),str(max(int(peak[1]),int(info[2])))]
                            flag = 0
                    if flag:
                        res[chrom].append([info[1],info[2]])
                else:
                    res[chrom]=[[info[1],info[2]]]
    print('end!')
    for key,value in res.items():
        for i in range(len(value)):
            write_object.write('{}\t{}\t{}\n'.format(key,value[i][0],value[i][1]))




if __name__=='__main__':
    #inpath = 'data/source_data/hg19-Merged.txt'
    #outpath = 'data/source_data/hg19-Merged_complete.txt'
    #merge(inpath,outpath)
    file_list = ['K562_BG4-ChIP_peaks.narrowPeak','peak_all.list']
    outpath = 'data/source_data/K562_BG4-ChIP_peaks_comp.narrowPeak'
    merge_peak(file_list,outpath)