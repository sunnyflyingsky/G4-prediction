output_path=/mnt/Storage/home/zhangjiasheng/data/G4s_data/GSE107690/fastq_file 
data_path=/mnt/Storage/home/zhangjiasheng/data/G4s_data/GSE107690/fastq_file 
ref_path=/mnt/Storage/home/zhangjiasheng/data/Bowtie2 

nohup cutadapt -f fastq -e 0.1 -q 20 -O 3 -a CTGTCTCTTATACACATCT -o $output_path/SRR6347550_cut.fastq $data_path/SRR6347550.fastq &
wait;
for i in `seq 52 57`;
do
cutadapt -f fastq -e 0.1 -q 20 -O 3 -a CTGTCTCTTATACACATCT -o $output_path/SRR63475${i}_cut.fastq $data_path/SRR63475${i}.fastq
done &
