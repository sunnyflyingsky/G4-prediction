
def alignment(inpath,outpath,name):
    '''
    针对一个模型内的四个rep进行比对，并输出这些motif以及它们的hit数量
    '''
    motif_hit = {}
    for j in range(1,5,1):
        read_object = open(inpath+'/Results_G4_'+name+'_rep'\
            +str(j)+'/G4_'+name+'_rep'+str(j)+'-Merged_complete.txt')
        for line in read_object:
            flag = 1
            if line.startswith('>'):
                info = line.strip().replace('>','').split(':')
                chrom = info[0].strip()
                start = int(info[1].split('-')[0])
            else:
                info = line.strip().split('\t')
                if chrom in motif_hit.keys() and motif_hit[chrom]:
                    for i in range(len(motif_hit[chrom])):
                        if start+int(info[0])>=motif_hit[chrom][i][1]:
                            pass
                        elif start+int(info[1])<=motif_hit[chrom][i][0]:
                            pass
                        else:
                            motif_hit[chrom][i]=[min(motif_hit[chrom][i][0],start+int(info[0])),max(motif_hit[chrom][i][1],start+int(info[1])),\
                                float(info[4])+motif_hit[chrom][i][2],motif_hit[chrom][i][-1]]
                            motif_hit[chrom][i][-1].append(j)
                            flag = 0
                            break
                if flag:
                    try:motif_hit[chrom].append([start+int(info[0]),start+int(info[1]),float(info[4]),[j]])
                    except:motif_hit[chrom] = [[start+int(info[0]),start+int(info[1]),float(info[4]),[j]]]
        read_object.close()
    with open(outpath,'w') as write_object:
        for chrom,motif in motif_hit.items():
            for i in range(len(motif)):
                write_object.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom,motif[i][0],motif[i][1],motif[i][2]/len(motif[i][3]),len(set(motif[i][3]))))

def alignmentAllRep(file_list):
    '''
    '''
    motif_hit = {}
    for k,name in enumerate(file_list):
        for j in range(1,5,1):
            t = k*4+j
            inpath = 'data/G4_analysis_data/'+name+'/07_macs2/tmp'+'/Results_G4_'+name+'_rep'\
                +str(j)+'/G4_'+name+'_rep'+str(j)+'-Merged_complete.txt'
            read_object = open(inpath)
            for line in read_object:
                flag = 1
                if line.startswith('>'):
                    info = line.strip().replace('>','').split(':')
                    chrom = info[0].strip()
                    start = int(info[1].split('-')[0])
                else:
                    info = line.strip().split('\t')
                    if chrom in motif_hit.keys() and motif_hit[chrom]:
                        for i in range(len(motif_hit[chrom])):
                            if start+int(info[0])>=motif_hit[chrom][i][1]:
                                pass
                            elif start+int(info[1])<=motif_hit[chrom][i][0]:
                                pass
                            else:
                                motif_hit[chrom][i]=[min(motif_hit[chrom][i][0],start+int(info[0])),max(motif_hit[chrom][i][1],start+int(info[1])),\
                                    float(info[4])+motif_hit[chrom][i][2],motif_hit[chrom][i][-1]]
                                motif_hit[chrom][i][-1].append(t)
                                flag = 0
                                break
                    if flag:
                        try:motif_hit[chrom].append([start+int(info[0]),start+int(info[1]),float(info[4]),[t]])
                        except:motif_hit[chrom] = [[start+int(info[0]),start+int(info[1]),float(info[4]),[t]]]
            print(t/80)
            read_object.close()
    outpath = 'comparasion/G4_second/res/motif_hit_all.txt'
    with open(outpath,'w') as write_object:
        for chrom,motif in motif_hit.items():
            for i in range(len(motif)):
                write_object.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom,motif[i][0],motif[i][1],motif[i][2]/len(motif[i][3]),len(set(motif[i][3]))))
            


            
if __name__ =='__main__':
    '''
    '''
    
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    """
    #file_list = ['AB521M']
    i=1
    for name in file_list: 
        inpath = 'data/G4_analysis_data/'+name+'/07_macs2/tmp'
        outpath = 'data/G4_analysis_data/'+name+'/07_macs2/tmp/motif_hit.txt'
        alignment(inpath,outpath,name)
        print(i/20)
        i+=1
    """
    alignmentAllRep(file_list)
   




