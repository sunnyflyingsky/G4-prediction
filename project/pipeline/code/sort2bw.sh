nohup zcat ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_71/K562_71.occ.bedgraph.gz|sort -k1,1 -k2n,2 > ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_71/K562_71_sorted.occ.bdg &
wait;
nohup bedGraphToBigWig ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_71/K562_71_sorted.occ.bdg /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_71/K562_71_sorted.occ.bw &
nohup zcat ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_72/K562_72.occ.bedgraph.gz|sort -k1,1 -k2n,2 > ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_72/K562_72_sorted.occ.bdg &
wait;
nohup bedGraphToBigWig ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_72/K562_72_sorted.occ.bdg /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_72/K562_72_sorted.occ.bw &
nohup zcat ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_73/K562_73.occ.bedgraph.gz|sort -k1,1 -k2n,2 > ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_73/K562_73_sorted.occ.bdg &
wait;
nohup bedGraphToBigWig ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_73/K562_73_sorted.occ.bdg /mnt/Storage/home/zhangjiasheng/data/Bowtie2/hg19.len ~/project/compare/ATAC_Nuc/ATAC_analysis/K562_73/K562_73_sorted.occ.bw &

