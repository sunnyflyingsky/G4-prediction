import random
def merge(inpath1,inpath2,inpath3,outpath):
    '''
    '''
    numbers2 = random.sample(list(range(0,40940)),20000)
    #numbers3 = random.sample(list(range(0,76444)),20000)
    write_object = open(outpath,'w')
    with open(inpath1) as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            write_object.write('{}\t{}\t{}\t{}\n'.format(info[0],info[1],info[2],1))
    t = 0
    with open(inpath2) as read_object:
        for line in read_object:
            if t not in numbers2:
                t+=1
                continue
            info = line.strip().split('\t')
            write_object.write('{}\t{}\t{}\t{}\n'.format(info[0],info[1],info[2],0))
            t+=1
    """
    t = 0
    with open(inpath3) as read_object:
        for line in read_object:
            if t not in numbers3:
                t+=1
                continue
            info = line.strip().split('\t')
            write_object.write('{}\t{}\t{}\t{}\n'.format(info[0],info[1],info[2],0))
            t+=1
    """



if __name__=='__main__':
    inpath1='data/source_data/S_motif_80rep.txt'
    inpath2='data/source_data/NoG4_TEST_predict_region.bed'
    inpath3='data/source_data/N_motif_80rep.txt'
    outpath = 'data/source_data/motif_mix.bed'
    merge(inpath1,inpath2,inpath3,outpath)





