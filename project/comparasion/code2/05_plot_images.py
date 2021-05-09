import matplotlib.pyplot as plt

def main():
    '''
    '''
    res = []
    """
    ##计算全体distance
    with open('comparasion/G4/G4_data/distance_rep.txt') as read_object:
        for line in read_object:
            dis = line.strip().split('\t')
            while '' in dis:
                dis.remove('')
            for d in dis:
                while int(d)>=len(res):
                    res.append(0)
                res[int(d)]+=1
    l = 1000
    k = (95*sum(res))//100
    for i in range(len(res)):
        k=k-res[i]
        print(k)
        if k<=0:
            print(i)
            break
    res = res[:1000]
    """
    """
    ##计算map计数
    with open('comparasion/G4/G4_data/Unique_map.txt') as read_object:
        for line in read_object:
            num = line.strip().split('\t')[-1]
            while int(num)>=len(res):
                res.append(0)
            res[int(num)]+=1
    """
    """
    """
    ##计算每个motif的distance
    with open('comparasion/G4/G4_data/distance_motif.txt') as read_object:
        for line in read_object:
            t = line.strip().split('\t')
            while '' in t:
                t.remove('')
            if t:
                res.append([])
            for i in t:
                res[-1].append(int(i))
    thresh = []
    for numbers in res:
        #k = (8*len(numbers))//10
        numbers = sorted(numbers,reverse=False)
        thresh.append(numbers[len(numbers)//2])
        #print(numbers)
        #for i in range(k+1):
        #    thresh.append(numbers[i])

    res = []
    for d in thresh:
        while int(d)>=len(res):
            res.append(0)
        res[int(d)]+=1

    res = res[:1000]
    thresh = sorted(thresh,reverse=False)
    k = (95*len(thresh))//100
    print(thresh[k])
    

    plt.figure(figsize=(20,12))
    ax = plt.gca()
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.title('G4 motif distance to summits under threshold',loc='center',fontsize=36,fontweight='black')
    plt.xlabel('relative distance',fontsize=24)
    plt.ylabel('count',fontsize=24)
    plt.bar(range(len(res)),res)
    plt.legend()
    plt.show()


    


if __name__=='__main__':
    main()


