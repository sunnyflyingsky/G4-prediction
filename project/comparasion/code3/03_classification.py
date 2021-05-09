
def classification(file_list):
    '''
    '''
    outpath1='comparasion/G4_second/res/S_motif_greed.txt'
    outpath2='comparasion/G4_second/res/M_motif_greed.txt'
    outpath3='comparasion/G4_second/res/N_motif_greed.txt'
    res = {}
    for k,name in enumerate(file_list):
        inpath='data/G4_analysis_data/'+name+'/07_macs2/tmp/motif_hit.txt'
        with open(inpath) as read_object:
            for line in read_object:
                flag = 1
                info = line.strip().split('\t')
                chrom = info[0]
                if chrom in res.keys() and res[chrom]:
                    for i in range(len(res[chrom])):
                        if int(info[1])>=res[chrom][i][1]:
                            pass
                        elif int(info[2])<=res[chrom][i][0]:
                            pass
                        else:
                            res[chrom][i]=[min(int(info[1]),res[chrom][i][0]),max(int(info[2]),res[chrom][i][1]),\
                                res[chrom][i][2]+float(info[3]),res[chrom][i][3]]
                            res[chrom][i][-1].append(int(info[4]))
                            flag = 0
                            break
                if flag:
                    try:res[chrom].append([int(info[1]),int(info[2]),float(info[3]),[int(info[4])]])
                    except:res[chrom]=[[int(info[1]),int(info[2]),float(info[3]),[int(info[4])]]]
        print(k/20)
    print('ok!')
    write_object1 = open(outpath1,'w')
    write_object2 = open(outpath2,'w')
    write_object3 = open(outpath3,'w') 
    for chrom,motif in res.items():
        for i in range(len(motif)):
            if 4 in motif[i][-1]:
                write_object1.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom,motif[i][0],motif[i][1],motif[i][2],motif[i][3]))
            elif 2 in motif[i][-1] or 3 in motif[i][-1]:
                write_object2.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom,motif[i][0],motif[i][1],motif[i][2],motif[i][3]))
            else:
                write_object3.write('{}\t{}\t{}\t{}\t{}\n'.format(chrom,motif[i][0],motif[i][1],motif[i][2],motif[i][3]))

def classificationAll(): 
    outpath1='comparasion/G4_second/res/S_motif_80rep.txt'
    outpath2='comparasion/G4_second/res/M_motif_80rep.txt'
    outpath3='comparasion/G4_second/res/N_motif_80rep.txt'
    write_object1 = open(outpath1,'w')
    write_object2 = open(outpath2,'w')
    write_object3 = open(outpath3,'w')
    with open('comparasion/G4_second/res/motif_hit_all.txt') as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            if int(info[-1])<=1:
                write_object3.write(line)
            elif int(info[-1])<=4:
                write_object2.write(line)
            else:
                write_object1.write(line)

if __name__ =='__main__':
    '''
    '''
    """
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    classification(file_list)
    """
    classificationAll()