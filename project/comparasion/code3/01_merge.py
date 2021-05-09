
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

if __name__ =='__main__':
    '''
    '''
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    #file_list = ['AB521M']
    for name in file_list:
        for i in range(1,5,1):
            inpath = 'data/G4_analysis_data/'+name+'/07_macs2/tmp/Results_G4_'+name+'_rep'\
                +str(i)+'/G4_'+name+'_rep'+str(i)+'-Merged.txt'
            outpath = 'data/G4_analysis_data/'+name+'/07_macs2/tmp/Results_G4_'+name+'_rep'\
                +str(i)+'/G4_'+name+'_rep'+str(i)+'-Merged_complete.txt'
            merge(inpath,outpath)
