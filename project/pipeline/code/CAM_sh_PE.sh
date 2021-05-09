output_path=/mnt/Storage/home/zhangjiasheng/data/Nuc_data/CAM_re 
data_path=/mnt/Storage/home/zhangjiasheng/data/Nuc_data/GSE78984/fastq_file 
ref_path=/mnt/Storage/home/zhangjiasheng/data/Bowtie2 

cd $output_path

for i in `seq 73 78`;
do
CAM.py simple -a $data_path/SRR32116${i}_1.fastq -b $data_path/SRR32116${i}_2.fastq -n SRR32116${i} -t PE -s mm9 --fa $ref_path/mm9.fa --mapindex $ref_path/mm9
done &