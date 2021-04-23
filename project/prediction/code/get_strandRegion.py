
def get_sequence(peak_region,write_folder):
    '''
    '''
    score = 0
    read_object = open(peak_region)
    with open(write_folder+'/'+'G4-all_region4.bed','w') as write_object:
        for line in read_object:
            if line.startswith('>'):
                info = line.strip().replace('>','').split(':')
                if score>0:strand = '1'
                elif score<0:strand = '-1'
                else:strand = '0'
                try:write_object.write('{}\t{}\t{}\t{}\n'.format(chrom,start,end,strand))
                except:pass
                chrom,start,end,score = info[0],info[1].split('-')[0],info[1].split('-')[1],0
                read_object.readline()
            else:
                score+=float(line.strip().split('\t')[4]) 
        if score>0:strand = '1'
        elif score<0:strand = '-1'
        else:strand = '0'
        write_object.write('{}\t{}\t{}\t{}\n'.format(chrom,start,end,strand))






if __name__=='__main__':
    print('run!')
    get_sequence('data/source_data/G4_all-W25-S1.2.txt','data/source_data')
    print('end!')







