outpath=/mnt/Storage/home/zhangjiasheng/data/TMP_data/GSE123292
inpath=/mnt/Storage/home/zhangjiasheng/data/TMP_data/GSE123292

for i in `seq 22 56`;
do
fasterq-dump -e 8 --split-files -O $outpath/fastq_file $inpath/SRR89552${i}
done &
