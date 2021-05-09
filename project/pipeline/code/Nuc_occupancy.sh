inpath=/mnt/Storage/home/zhangjiasheng/data/Nuc_data/CAM_re
outpath=/mnt/Storage/home/zhangjiasheng/project/compare/ATAC_Nuc/Nuc_analysis
name=SRR3211680

mkdir ${outpath}/${name}
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr1 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr10 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr11 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr12 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr13 &
wait;
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr14 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr15 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr16 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr17 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr18 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr19 &
wait;
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr2 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr20 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr21 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr22 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr3 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr4 &
wait;
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr5 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr6 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr7 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr8 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chr9 &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chrX &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chrY &
nohup python /mnt/Storage/home/chenxiaolan/bin/nuc_profile_to_occupancy_bw.py -g /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len -p ${inpath}/${name}/summary/${name}_profile.bw -n ${outpath}/${name}/${name} -c chrM &
wait;
cat ${outpath}/${name}/${name}_occupancy_chr1.bdg ${outpath}/${name}/${name}_occupancy_chr10.bdg ${outpath}/${name}/${name}_occupancy_chr11.bdg ${outpath}/${name}/${name}_occupancy_chr12.bdg ${outpath}/${name}/${name}_occupancy_chr13.bdg ${outpath}/${name}/${name}_occupancy_chr14.bdg \
${outpath}/${name}/${name}_occupancy_chr15.bdg ${outpath}/${name}/${name}_occupancy_chr16.bdg ${outpath}/${name}/${name}_occupancy_chr17.bdg ${outpath}/${name}/${name}_occupancy_chr18.bdg ${outpath}/${name}/${name}_occupancy_chr19.bdg ${outpath}/${name}/${name}_occupancy_chr2.bdg \
${outpath}/${name}/${name}_occupancy_chr20.bdg ${outpath}/${name}/${name}_occupancy_chr21.bdg ${outpath}/${name}/${name}_occupancy_chr22.bdg ${outpath}/${name}/${name}_occupancy_chr3.bdg ${outpath}/${name}/${name}_occupancy_chr4.bdg ${outpath}/${name}/${name}_occupancy_chr5.bdg \
${outpath}/${name}/${name}_occupancy_chr6.bdg ${outpath}/${name}/${name}_occupancy_chr7.bdg ${outpath}/${name}/${name}_occupancy_chr8.bdg ${outpath}/${name}/${name}_occupancy_chr9.bdg ${outpath}/${name}/${name}_occupancy_chrX.bdg ${outpath}/${name}/${name}_occupancy_chrY.bdg \
${outpath}/${name}/${name}_occupancy_chrM.bdg > ${outpath}/${name}/${name}_occupancy.bdg
bedGraphToBigWig ${outpath}/${name}/${name}_occupancy.bdg /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len ${outpath}/${name}/${name}_occupancy.bw
wait;


