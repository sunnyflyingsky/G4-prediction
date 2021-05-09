import matplotlib.pyplot as plt
res = [[],[]]
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
k = [0,0,0,0]
with open('comparasion/G4/G4_data/04_MD_map.txt') as read_object:
    for line in read_object:
        info = line.strip().split('\t')
        score = abs(float(info[5]))
        if distance[i]:  
            dis = distance[i][len(distance[i])//2]
        #for dis in distance[i]:
            res[1].append(score)
            res[0].append(dis)
            if score>=1.2 and dis<=100:
                k[0]+=1
            elif score>=1.2 and dis>100:
                k[1]+=1
            elif score<1.2 and dis<=100:
                k[2]+=1
            else:k[3]+=1
        i+=1
for num in k:
    print(num/i)
print(k,i)



plt.figure(figsize=(20,12))
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
plt.title('G4 motif distance to summits under threshold',loc='center',fontsize=36,fontweight='black')
plt.xlabel('relative distance',fontsize=24)
plt.ylabel('count',fontsize=24)
plt.scatter(res[0],res[1])
plt.legend()
plt.show()



