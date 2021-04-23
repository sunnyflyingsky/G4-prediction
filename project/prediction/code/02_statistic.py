import matplotlib.pyplot as plt
def statistic(inpath):
    '''
    '''
    res = [0]*100
    with open(inpath) as read_object:
        for line in read_object:
            signals = line.strip().split('\t')
            for sig in signals:
                try:
                    res[int(float(sig)*100)]+=1
                except:
                    res[99]+=1

    
    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('motif hits in rep',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('hits number',fontsize=24)
    plt.ylabel('motif count',fontsize=24)
    plt.bar(range(len(res)),res)
    #plt.bar(range(len(res)),res)
    plt.legend()
    plt.show()
    




if __name__=='__main__':
    inpath = 'data/source_data/K562_1a_logLR_matrix_siteprof1'
    statistic(inpath)



