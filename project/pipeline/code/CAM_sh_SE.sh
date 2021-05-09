output_path=/mnt/Storage/home/zhangjiasheng/data/Nuc_data/CAM_re 
data_path=/mnt/Storage/home/zhangjiasheng/data/Nuc_data/GSE78984/fastq_file 
ref_path=/mnt/Storage/home/zhangjiasheng/data/Bowtie2 

for i in `seq 71 73`;
do
CAM.py simple -a $data_path/SRR33994${i}.fastq -n SRR33994${i} -t SE -s hg19 --fa $ref_path/hg19.fa --mapindex $ref_path/hg19
done &