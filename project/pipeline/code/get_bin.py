import sys
import os
import getopt


def main(file_path,Upstream,Downstream,name,outputpath):
    '''
    '''
    gene_position = []
    try:read_obejct = open(file_path)
    except:
        print('false input path or not bed file')
        sys.exit(Usage)
    with open(outputpath+'/'+name+'.bed','w') as write_object:
        for line in read_obejct:
            info = line.strip().split('\t')
            if '_' in info[0]:continue
            value = (info[0],int(info[1]))
            if value not in gene_position:
                gene_position.append((info[0],int(info[1])))
                #write_object.write('{}\t{}\t{}\t{}\n'.format(gene_position[-1][0],gene_position[-1][1]-Upstream,gene_position[-1][1]+Downstream,info[5]))
                write_object.write('{}\t{}\t{}\n'.format(gene_position[-1][0],gene_position[-1][1]-Upstream,gene_position[-1][1]+Downstream))

Usage = 'Usage: ' + sys.argv[0]
Usage += '''
    <Requires>
    -i input bed file path
    -U upstream
    -D downstream
    -n name of output file
    -o output file folder

    [Options]
    None
'''
Usage += "EX: " + sys.argv[0] + ' -i bed -U 3000 -D 3000 -f FileName -o outfile.'
if len(sys.argv)<5 or not sys.argv[1].startswith('-'):sys.exit(Usage)
if __name__=='__main__':
    print('run!')
    oplist,alist = getopt.getopt(sys.argv[1:],'hi:U:D:f:o:')
    #print(oplist)
    for opt in oplist:
        if opt[0] == '-h':sys.exit(Usage)
        elif opt[0] == '-i':file_path = opt[1]
        elif opt[0] == '-U':
            try:Upstream = int(opt[1])
            except:
                print('please input int value!')
                sys.exit(Usage)
        elif opt[0] == '-D':
            try:Downstream = int(opt[1])
            except:
                print('please input int value!')
                sys.exit(Usage) 
        elif opt[0] == '-f':name = opt[1]
        elif opt[0] == '-o':outputpath = opt[1]
    main(file_path,Upstream,Downstream,name,outputpath)
    print('end!')
