
def filter(inpath1,inpath2,outpath):
    '''
    利用06内计算的到0.95分位数作为阈值，针对MS和MD两组motif进行筛选剔除，然后重新计数新的MS和MD
    '''
    distance = []
    with open(inpath2) as read_object:
        for line in read_object:
            dis = line.strip().split('\t')
            while '' in dis:
                dis.remove('')
            re = []  
            for num in dis:
                re.append(int(num))
            distance.append(sorted(re))
    
    read_object = open(inpath1)
    i=0
    with open(outpath,'w') as write_object:
        for line in read_object:
            if line.startswith('>'):
                write_object.write(line)
            else:
                if i >=len(distance):break
                if distance[i] and int(distance[i][len(distance[i])//2])<=328:
                    write_object.write(line)
                i+=1




def statistic_summary(inpath):
    '''
    统计两个阈值所导致的数据的剔除情况概要
    '''
    sum_list=[0,0,0]
    with open(inpath) as read_object:
        for line in read_object:
            dis = line.strip().split('\t')
            while '' in dis:
                dis.remove('')
            for num in dis:
                if int(num)<=296:
                    sum_list[0]+=1
                    sum_list[1]+=1
                elif int(num)<=328:
                    sum_list[1]+=1
                sum_list[2]+=1
    print(sum_list[0]/sum_list[2])
    print(sum_list[1]/sum_list[2])

def summary(inpath):
    '''
    统计筛选后的四组文件motif以及peak的变化情况
    '''
    flag = 0
    #None,Unique,MS,MD,MSpeak,MDpeak
    res_summary=[0,0,0,0,0,0]
    all_re =[0,0] 
    with open(inpath) as read_object:
        for line in read_object:
            if line.startswith('>'):
                if flag:
                    if len(score)==0:
                        res_summary[0]+=1
                        all_re[1]+=1
                    elif len(score)==1:
                        res_summary[1]+=1
                        all_re[0]+=1
                        all_re[1]+=1
                    elif score_flag:
                        res_summary[2]+=len(score)
                        res_summary[4]+=1
                        all_re[0]+=len(score)
                        all_re[1]+=1
                    else:
                        res_summary[3]+=len(score)
                        res_summary[5]+=1
                        all_re[0]+=len(score)
                        all_re[1]+=1
                score = []
                score_flag = 1
                flag = 1
            else:
                info = line.strip().split('\t')
                if score:
                    if float(info[2])*score[-1]<0:
                        score_flag=0
                score.append(float(info[2]))
    if len(score)==0:
        res_summary[0]+=1
        all_re[0]+=1
        all_re[1]+=1
    elif len(score)==1:
        res_summary[1]+=1
        all_re[0]+=1
        all_re[1]+=1
    elif score_flag:
        res_summary[2]+=len(score)
        res_summary[4]+=1
        all_re[0]+=len(score)
        all_re[1]+=1
    else:
        res_summary[3]+=len(score)
        res_summary[5]+=1
        all_re[0]+=len(score)
        all_re[1]+=1
    print(res_summary,all_re)






if __name__=='__main__':
    #inpath1='comparasion/G4/G4_data//04_Class_MD.txt'
    #inpath2='comparasion/G4/G4_data/distance_MD_motif.txt'
    #outpath='comparasion/G4/G4_data/04_Class_MD_filter.txt'
    #filter(inpath1,inpath2,outpath)
    #inpath='comparasion/G4/G4_data/distance_MD_rep.txt'
    #statistic_summary(inpath)
    inpath = 'comparasion/G4/G4_data/03_Class_MS_filter.txt'
    summary(inpath)