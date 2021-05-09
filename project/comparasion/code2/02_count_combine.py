

def main(inpath,outpath):
    '''
    '''
    name = ['None','Unique','Major Similar','Major Different']
    all_line,all_motif,all_peak = 0,0,0
    write_object = open('comparasion/G4/G4_data/05_Class_Identify.txt','w')
    for i,file_name in enumerate(inpath):
        with open('comparasion/G4/G4_data/'+file_name+'.txt') as read_object:
            for line in read_object:
                t = count(line,i)
                all_line+=t[0]
                all_motif+=t[1]
                all_peak+=t[2]
                if i==1:
                    info = line.strip().split('\t')
                    write_object.write('{}\t{}\t{}\t{}\n'.format(info[0],info[1],info[2],info[5]))
                elif i==2 and line.startswith('>'):
                    info = line.strip().replace('>','').split(':')
                    write_object.write('{}\t{}\t{}\t{}\n'.format(\
                        info[0],info[1].split('\t')[0],info[1].split('\t')[1],info[1].split('\t')[2]))
        print(all_line,all_motif,all_peak)
              
def count(line,flag):
    '''
    '''
    if flag==0:
        return (1,0,1)
    elif flag==1:
        return (1,1,1)
    elif flag>=2 and line.startswith('>'):
        return (0,0,1)
    else:
        return (1,1,0)


if __name__=='__main__':
    file_list = ['01_Class_None','02_Class_Unique','03_Class_MS','04_Class_MD']
    main(file_list,'comparasion/G4')


