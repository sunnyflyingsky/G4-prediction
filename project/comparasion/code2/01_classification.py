

def classify(inpath1,inpath2,outpath):
    '''
    将peak分类
    '''
    count=0
    read_object = open(inpath1)
    with open(outpath+'/01_Class_None.txt','w') as write_object_None:
        for line in read_object:
            if line.startswith('>'):
                if count==1:
                    write_object_None.write('{}\t{}\t{}\n'.format(chrom,start,end))
                info = line.strip().replace('>','').split(':')
                chrom = info[0]
                start,end=info[1].split('-')[0],info[1].split('-')[1]
                count=0
            else:
                count+=1
    read_object.close()
    #########################################################
    read_object = open(inpath2)
    write_object_unique = open(outpath+'/02_Class_Unique.txt','w')
    write_object_MS = open(outpath+'/03_Class_MS.txt','w')
    write_object_MD = open(outpath+'/04_Class_MD.txt','w')
    for line in read_object:
        if line.startswith('>'):
            info = line.strip().replace('>','').split(':')
            chrom = info[0]
            start,end=info[1].split('-')[0],info[1].split('-')[1]
            score,flag = 0,1
            res = []
            read_object.readline()
        else:
            info = line.strip().split('\t')
            if len(info)==5:
                if res and float(res[-1][4])*float(info[4])<0:
                    flag=0
                res.append(info)
                score+=float(info[4])
            elif len(info)==6:
                if int(info[5])==1:
                    write_object_unique.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(\
                        chrom,start,end,int(info[0]),int(info[1]),info[4]))
                else:
                    if res and float(res[-1][4])*float(info[4])<0:
                        flag=0
                    res.append(info[:5])
                    score+=float(info[4])
                    if flag:
                        write_object_MS.write('>{}:{}\t{}\t{}\t{}\n'.format(chrom,start,end,score/len(res),len(res)))
                        for r in res:
                            write_object_MS.write('{}\t{}\t{}\n'.format(\
                                int(r[0]),int(r[1]),r[4]))
                    else:
                        write_object_MD.write('>{}:{}\t{}\t{}\t{}\n'.format(chrom,start,end,score/len(res),len(res)))
                        for r in res:
                            write_object_MD.write('{}\t{}\t{}\n'.format(\
                                int(r[0]),int(r[1]),r[4]))
    
    write_object_unique.close()
    write_object_MS.close()
    write_object_MD.close()




if __name__=='__main__':
    print('run!')
    classify(inpath1='data/source_data/G4_all-W25-S1.2.txt',\
        inpath2='data/source_data/G4_all-Merged.txt',outpath='comparasion/G4/G4_data')
    print('end!')




