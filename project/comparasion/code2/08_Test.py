import math
from scipy.stats import pearsonr,shapiro,normaltest,anderson,mannwhitneyu,ttest_ind

def TestOfIndependence(matrix:list):
    '''
    '''
    res = 0
    for i in range(len(matrix)):
        matrix[i].append(sum(matrix[i]))
    matrix.append([0]*len(matrix[0]))
    for j in range(len(matrix[0])):
        for i in range(len(matrix)-1):
            matrix[-1][j]+=matrix[i][j]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            t = matrix[-1][j]*matrix[i][-1]/matrix[-1][-1]
            res = res+((matrix[i][j]-t)*(matrix[i][j]-t))/t
    print(res)

def TestOfBehrens(X,Y):
    '''
    '''
    X_avg = sum(X)/len(X)
    Y_avg = sum(Y)/len(Y)
    X_sv,Y_sv = 0,0
    for num in X:
        X_sv = X_sv+(num-X_avg)*(num-X_avg)
    X_sv = X_sv/len(X)
    for num in Y:
        Y_sv = Y_sv+(num-Y_avg)*(num-Y_avg)
    Y_sv = Y_sv/len(Y)
    print((X_avg-Y_avg)/math.sqrt(X_sv/len(X)+Y_sv/len(Y)))




if __name__=='__main__':
    #matrix = [[27433, 7782],[21723, 6496]]
    #matrix = [[8902, 26313],[7268, 20951]]
    #matrix = [[14145, 1005],[10629, 779]]
    #matrix = [[24774,49156],[1784,14278]]
    #TestOfIndependence(matrix)
    res_X = [[],[]]
    res_Y = [[],[]]
    distance=[]
    with open('comparasion/G4/G4_data/04_distance_MD_motif.txt') as read_object:
        for line in read_object:
            dis = line.strip().split('\t')
            while '' in dis:
                dis.remove('')
            re = []
            for num in dis:
                if int(num)<=1000:
                    re.append(int(num))
            distance.append(sorted(re))
    i = 0
    with open('comparasion/G4/G4_data/04_MD_map.txt') as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            score = abs(float(info[5]))
            if distance[i]:  
                dis = distance[i][len(distance[i])//2]
            #for dis in distance[i]:
                res_X[1].append(score)
                res_X[0].append(dis)
            i+=1
    distance=[]
    with open('comparasion/G4/G4_data/03_distance_MS_motif.txt') as read_object:
        for line in read_object:
            dis = line.strip().split('\t')
            while '' in dis:
                dis.remove('')
            re = []
            for num in dis:
                if int(num)<=1000:
                    re.append(int(num))
            distance.append(sorted(re))
    i = 0
    with open('comparasion/G4/G4_data/03_MS_map.txt') as read_object:
        for line in read_object:
            info = line.strip().split('\t')
            score = abs(float(info[5]))
            if distance[i]:  
                dis = distance[i][len(distance[i])//2]
            #for dis in distance[i]:
                res_Y[1].append(score)
                res_Y[0].append(dis)
            i+=1
    #TestOfBehrens(res_X[1],res_Y[1])
    #corr,p = pearsonr(res_X[0],res_X[1])
    corr,p = ttest_ind(res_X[0],res_Y[0])
    print(corr,p)



