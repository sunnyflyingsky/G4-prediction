
def main():
    '''
    '''
    gene_position = []
    chrom='chr1'
    read_obejct = open('~/data/Nuc_data/CAM_re/SRR3211679/summary/SRR3211679_geneLevel_nucarrayAnnotation.bed')
    with open('~/data/Bowtie2/hg19_gene_res.bed','w') as write_object:
        for line in read_obejct:
            info = line.strip().split('\t')
            if info[0]!=chrom:
                chrom=info[0]
                gene_position = []
            if int(info[1]) not in gene_position:
                gene_position.append(int(info[1]))
                write_object.write('{}\t{}\t{}\n'.format(chrom,gene_position[-1]-3000,gene_position[-1]+3000))
    read_obejct = open('~/data/Bowtie2/hg19.len')
    with open('~/data/Bowtie2/hg19_bin_res.bed','w') as write_object:
        for line in read_obejct:
            info = line.strip().split('\t')
            chrom = info [0]
            length = info[1]//100+1
            start = 0
            while start<info[1]:
                if start+length<info[1]:
                    write_object.write('{}\t{}\t{}\n'.format(chrom,start,start+length))
                else:
                    write_object.write('{}\t{}\t{}\n'.format(chrom,start,length))
                start+=length


if __name__=='__main__':
    main()