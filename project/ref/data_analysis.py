import matplotlib.pyplot as plt

def cov_analysis(inpath):
    '''
    '''
    X = [0]*500
    with open(inpath) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            cov = int(info[-1])
            count = int(info[2])-int(info[1])
            while len(X)<=cov:
                X.append(0)
            X[cov]+=count
    X = X[50:100]
    plt.figure(figsize=(12,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('Coverage in sample',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('Cov number',fontsize=24)
    plt.ylabel('count',fontsize=24)
    plt.plot(range(50,100,1),X,'y')
    plt.legend()
    plt.show()



if __name__=='__main__':
    inpath1 = 'data/source_data/37_cov.bedgraph'
    inpath2 = 'data/source_data/72_cov.bedgraph'
    inpath3 = 'data/source_data/82_cov.bedgraph'
    cov_analysis(inpath2)



