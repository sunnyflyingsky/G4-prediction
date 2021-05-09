import os

work_path = "/mnt/Storage/home/zhangjiasheng"
data_path = "/data/ATAC_data/GSE70751/fastq_file"
output_path = "/project/compare/ATAC_Nuc/ATAC_mapping/chrom_access_human_70751"
ref_path = "/data/Bowtie2/hg19"
fastq_file = 'SRR2096437-SRR2096441'
def main():
    with open(work_path + output_path + '/tophat_2.sh','w') as write_object:
        write_object.write('output_path='+work_path+output_path+'\n')
        write_object.write('ref_path='+work_path+ref_path+'\n')
        write_object.write('data_path='+work_path+data_path+'\n\n')
        file_list = []
        for i in range(37,42,1):
            file_list.append('SRR20964'+str(i)+'.fastq')
        for f in file_list:
            write_object.write('tophat2 -m 1 -N 3 --read-edit-dist 3 -p 8 -g 2 -I 50000 --microexon-search --no-coverage-search -G $ref_path/{} -o $output_path/{} /mnt/Storage/home/chenxiaolan/Data/annotation/Bowtie2/hg19  $data_path/{} >> $output_path/{} \n'.format(\
                'hg19_refseq.gtf',f.split('.')[0],f,f.split('.')[0]+'_ATAC_align.log'))


'''
    nohup tophat2 -m 1 -N 3 --read-edit-dist 3 -p 8 -g 2 -I 50000 --microexon-search/
	--no-coverage-search --library-type fr-firststrand -G /home1/lpwang/ann/malaria/PF3D7_32.gtf/
	-o results/03.tophat/T1  /home1/lpwang/ann/bowtie2_index/PF3D7_32 source/DIS3-ADAR-T_1.fq.gz >> ATAC_align.log &
	
	nohup tophat2 -m 1 -N 3 --read-edit-dist 3 -p 8 -g 2 -I 50000 --microexon-search/
	--no-coverage-search --library-type fr-firststrand -G /home1/lpwang/ann/malaria/PF3D7_32.gtf/
	-o results/03.tophat/T2  /home1/lpwang/ann/bowtie2_index/PF3D7_32 source/DIS3-ADAR-T_2.fq.gz >> ATAC_align2.log &
'''
def file_name(file_path):
    return os.listdir(file_path)


if __name__=='__main__':
    main()

