

def main(inpath1,inpath2,file_list):
    '''
    '''
    unique_peak = {}
    with open(inpath1) as read_obejct:
        for line in read_obejct:
            if line.startswith('>'):
                info = line.strip().replace('>','').split(':')
                chrom = info[0]
                start = info[1].split('\t')[0]
                end = info[1].split('\t')[1]
            else:
                info = line.strip().split('\t')
                try:
                    unique_peak[chrom].append([start,end,int(info[0]),int(info[1]),float(info[2]),0,[]])
                except:
                    unique_peak[chrom]=[[start,end,int(info[0]),int(info[1]),float(info[2]),0,[]]]
            """
            info = line.strip().split('\t')
            try:
                unique_peak[info[0]].append([info[1],info[2],int(info[3]),int(info[4]),float(info[5]),0,0])
            except:
                unique_peak[info[0]]=[[info[1],info[2],int(info[3]),int(info[4]),float(info[5]),0,0]]
            """
    res = []
    ##mapping
    for i,name in enumerate(file_list):
        rep = 1
        while rep<=4:
            peak_file_path = inpath2+'/'+name+'/07_macs2/'+name+'_rep'+str(rep)+'.hg19_peaks.narrowPeak'
            #print(peak_file_path)
            summits_file_path = inpath2+'/'+name+'/07_macs2/'+name+'_rep'+str(rep)+'hg19_summits.bed'
            rep+=1
            unique_peak,res_tmp = map(peak_file_path,summits_file_path,unique_peak)
            res.append(res_tmp)
            print((i*4+rep-1)/80)
            #res.append(statistic(peak_file_path,summits_file_path,unique_peak))
    ##文件的写入
    """
    
    with open('comparasion/G4/G4_data/MD_map.txt','w') as write_object:
        for chrom,info in unique_peak.items():
            for t in info:
                write_object.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(\
                    chrom,t[0],t[1],t[2],t[3],t[4],t[5],t[6]))
    with open('comparasion/G4/G4_data/distance_MD_rep.txt','w') as write_object:
        for tmp in res:
            write_object.write('\t'.join(tmp)+'\n')
    """
    with open('comparasion/G4/G4_data/distance_MD_motif.txt','w') as write_object:
        for chrom,info in unique_peak.items():
            for t in info:
                write_object.write('\t'.join(t[-1])+'\n')
    

def map(peak_file_path,summits_file_path,unique_peak):
    '''
    将peak映射到20个sample的summits文件中去
    '''
    #summits_read_object = open(summits_file_path)
    peak_read_object = open(peak_file_path)
    chrom='chr1'
    #i=0
    res = []
    for line in peak_read_object:
        info = line.strip().split('\t')
        if info[0]=='chrM':continue
        if info[0]==chrom:
            pass
        else:
            chrom = info[0]
            #i=0
        start,end = int(info[1]),int(info[2])
        summits = int(info[1])+int(info[9])
        #while True:
        for i in range(len(unique_peak[chrom])):
            #if i>=len(unique_peak[chrom]):
            #    break
            #if int(unique_peak[chrom][i][3])+int(unique_peak[chrom][i][0])<start:
            if int(unique_peak[chrom][i][1])<start:
                continue
                #i+=1
            #elif int(unique_peak[chrom][i][2])+int(unique_peak[chrom][i][0])>end:
            elif int(unique_peak[chrom][i][0])>end:
                break
            else:
                #unique_peak[chrom][i][-1]+=1
                center_site = int(unique_peak[chrom][i][0])+(unique_peak[chrom][i][2]+unique_peak[chrom][i][3])//2
                res.append(str(abs(summits-center_site)))
                unique_peak[chrom][i][-1].append(res[-1])
                if int(res[-1])<=328:
                    unique_peak[chrom][i][-2]+=1
                #break
    return unique_peak,res


if __name__=='__main__':
    #inpath1='comparasion/G4/G4_data/Unique_map.txt'
    inpath1='comparasion/G4/G4_data/04_Class_MD.txt'
    inpath2='data/G4_analysis_data'
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    main(inpath1,inpath2,file_list)