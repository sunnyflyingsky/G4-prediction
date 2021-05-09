import os 

work_path = "/mnt/Storage/home/zhangjiasheng"
data_path = "/data/Nuc_data/GSE78984/fastq_file"
output_path = "/data/Nuc_data/CAM_re"
ref_path = "/data/Bowtie2"

def main():
    with open(work_path + output_path + '/CAM_sh.sh','w') as write_object:
        write_object.write('output_path='+work_path+output_path+' \n')
        write_object.write('data_path='+work_path+data_path+' \n')
        write_object.write('ref_path='+work_path+ref_path+' \n\n')
        f_com=[]
        file_list = file_name(work_path+data_path)
        for f in file_list:
            if f.split('.')[1]!='fastq':continue
            if '_' in f:
                if f.split('.')[0][:-2] not in f_com:
                    f_com.append(f.split('.')[0][:-2])
                    write_object.write('CAM.py simple -a $data_path/{} -b $data_path/{} -n {} -t PE -s hg19 --fa $ref_path/{} --mapindex $ref_path/{} \n'.format( \
                        f_com[-1]+'_1.fastq',f_com[-1]+'_2.fastq',f_com[-1],'hg19.fa','hg19'))
                else:
                    pass
            else:
                f_com.append(f.split('.')[0])
                write_object.write('CAM.py simple -a $data_path/{} -n {} -t SE -s hg19 --fa $ref_path/{} --mapindex $ref_path/{} \n'.format(\
                    f_com[-1]+'.fastq',f_com[-1],'hg19.fa','hg19'))
            
        '''CAM.py simple -a ../GSE78984/fastq_file/SRR3211621_1.fastq -b ../GSE78984/fastq_file/SRR3211621_2.fastq -n SRR3211621 -t PE
            -s hg19 --fa /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.fa --mapindex /bowtie2/hg19 \n'''

def file_name(file_path):
    return os.listdir(file_path)

if __name__=='__main__':
    main()