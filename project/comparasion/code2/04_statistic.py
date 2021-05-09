

def main(inpath1,inpath2,file_list):
    '''
    '''
    unique_peak = {}
    with open(inpath1) as read_obejct:
        for line in read_obejct:
            info = line.strip().split('\t')
            try:
                unique_peak[info[0]].append([info[1],info[2],int(info[3]),int(info[4]),float(info[5]),0,[]])
            except:
                unique_peak[info[0]]=[[info[1],info[2],int(info[3]),int(info[4]),float(info[5]),0,[]]]
    res = []
    ##mapping
    for i,name in enumerate(file_list):
        rep = 1
        while rep<=4:
            peak_file_path = inpath2+'/'+name+'/07_macs2/'+name+'_rep'+str(rep)+'.hg19_peaks.narrowPeak'
            summits_file_path = inpath2+'/'+name+'/07_macs2/'+name+'_rep'+str(rep)+'hg19_summits.bed'
            rep+=1
            unique_peak= statistic(peak_file_path,summits_file_path,unique_peak)
            print((i*4+rep-1)/80)
    ##文件的写入
    """
    with open('comparasion/G4/G4_data/Unique_map.txt','w') as write_object:
        for chrom,info in unique_peak.items():
            for t in info:
                write_object.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(\
                    chrom,t[0],t[1],t[2],t[3],t[4],t[5],t[6]))
    with open('comparasion/G4/G4_data/distance.txt','w') as write_object:
        for tmp in res:
            write_object.write('\t'.join(tmp)+'\n')
    """
    with open('comparasion/G4/G4_data/distance_motif.txt','w') as write_object:
        for chrom,info in unique_peak.items():
            for t in info:
                write_object.write('\t'.join(t[-1])+'\n')

def statistic(peak_file_path,summits_file_path,unique_peak):
    '''
    统计这些motif距离summits的距离
    '''
    peak_read_object = open(peak_file_path)
    chrom='chr1'
    i=0
    for line in peak_read_object:
        info = line.strip().split('\t')
        if info[0]=='chrM':continue
        if info[0]==chrom:
            pass
        else:
            chrom = info[0]
            i=0
        start,end = int(info[1]),int(info[2])
        summits = int(info[1])+int(info[9])
        while True:
            if i>=len(unique_peak[chrom]):
                break
            if int(unique_peak[chrom][i][1])<start:
                i+=1
            elif int(unique_peak[chrom][i][0])>end:
                break
            else:
                
                center_site = int(unique_peak[chrom][i][0])+(unique_peak[chrom][i][2]+unique_peak[chrom][i][3])//2
                unique_peak[chrom][i][-1].append(str(abs(summits-center_site)))
                break
    return unique_peak




if __name__=='__main__':
    inpath1='comparasion/G4/G4_data/Unique_map.txt'
    inpath2='data/G4_analysis_data'
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    main(inpath1,inpath2,file_list)






