data_path=~/data/ATAC_data/GSE66386/fastq_file
ref_path=~/data/Bowtie2
output_path=~/project/compare/ATAC_Nuc/ATAC_mapping/S.cerevisiae

for i in `seq 37 47`;
do
bowtie2 -p 6 --rg-id sample_${i} --rg "PL:ILLUMINA" --rg "SM:SRR18221${i}" -x $ref_path/sacCer3 -1 $data_path/SRR18221${i}_1.fastq -2 $data_path/SRR18221${i}_2.fastq | samtools sort -@ 6 -m 1G -o $output_path/SRR18221${i}_sorted.bam;
done &

