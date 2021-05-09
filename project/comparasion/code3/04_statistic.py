import matplotlib.pyplot as plt

def statistic(file_list):
    '''
    '''
    res = [0]*80
    sum = 0
    for inpath in file_list:
        with open(inpath) as read_object:
            for line in read_object: 
                info = line.strip().split('\t')
                res[int(info[-1])]+=1
    for i in range(len(res)):
        sum+=i*res[i]
    print(sum)
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('motif hits in rep',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('hits number',fontsize=24)
    plt.ylabel('motif count',fontsize=24)
    plt.bar(range(2,50,1),res[2:50])
    #plt.bar(range(len(res)),res)
    plt.legend()
    plt.show()


if __name__ =='__main__':
    '''
    '''
    
    file_list=['comparasion/G4_second/res/motif_hit_all.txt']
    """
    file_list=["AB521M","AB551","AB555M","AB580","HCI005","HCI009","STG139", \
        "STG139M_181", "STG139M_284", "STG143_284", "STG143_317", "STG195M", \
        "STG201_181", "STG201_284", "STG282M", "STG316", "VHIO179_181", \
        "VHIO179_284", "VHIO098_181", "VHIO098_284"]
    for i,name in enumerate(file_list):
        inpath='data/G4_analysis_data/'+name+'/07_macs2/tmp/motif_hit.txt'
        file_list[i]=inpath
    """
    statistic(file_list)





