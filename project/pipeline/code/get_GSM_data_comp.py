import sys
import os
import getopt

def main(file_name,input_folder,result_file):
    try:read_object = open(input_folder + '/' + file_name + '.txt')
    except:
        print("can't find the input_path")
        sys.exit(Usage)
    with open(result_file+  '/' + file_name + '.sh','w') as write_object:
        for line in read_object:
            srrnum = line.strip()
            if srrnum.startswith('SRR'):
                write_object.write('wget -c ftp://ftp.sra.ebi.ac.uk/vol1/srr/{}/00{}/{}\n'.format(srrnum[:6],srrnum[-1],srrnum))
            else:
                print('invalid input file!')
                sys.exit(Usage)
        write_object.write('wait;')


Usage = 'Usage: ' + sys.argv[0]
Usage += '''
    <Requires>
    -i input GSE file about SRR list, must be txt file
    -f folder of input file
    -o output file folder 
    
    [Options]
    None
'''
Usage += "EX: " + sys.argv[0] + ' -i GSE78984 -f /mnt/Storage/home/zhangjiasheng/data/Nuc_data   -o outfile.'
if len(sys.argv)<3 or not sys.argv[1].startswith('-'):sys.exit(Usage)
if __name__ == "__main__":
    print('run!')
    oplist,alist = getopt.getopt(sys.argv[1:],'hi:f:o:')
    #print(oplist)
    for opt in oplist:
        if opt[0] == '-h':sys.exit(Usage)
        elif opt[0] == '-i':file_name = opt[1]
        elif opt[0] == '-f':input_folder = opt[1]
        elif opt[0] == '-o':result_file = opt[1]
    main(file_name,input_folder,result_file)
    print('end!')