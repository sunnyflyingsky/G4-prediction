cp /mnt/Storage/home/chenxiaolan/project/G4_NUC/ChIP-seq_merged/rawdata/hg19.wgEncodeDukeMapabilityRegionsExcludable.whitelist.bed .


cutadapt -f fastq -e 0.1 -q 20 -O 3 -a CTGTCTCTTATACACATCT -o ${1}_cut.fastq ${1}.fastq


bwa mem -t 30 -M /mnt/Storage/home/chenxiaolan/Data/bwa/hg19.fa ${1}_cut.fastq > ${2}.sam
samtools view -S -u -b  -F2304 -q 10 -L hg19.wgEncodeDukeMapabilityRegionsExcludable.whitelist.bed ${2}.sam | samtools sort - -o ${2}.hg19.tmp 
java -Xmx5g -jar /home/compbio/ServerPackages/java/picard.jar MarkDuplicates REMOVE_DUPLICATES=true I=${2}.hg19.tmp O=bamclean/${2}.clean.bam M=logdir/${2}.md.txt


samtools view -H bamclean/${2}.clean.bam > bamclean/${2}_filtered.sam 
samtools view -h bamclean/${2}.clean.bam |awk '{if($5>=10 && substr($3,1,3)=="chr" && $3!="chrM") print $0;}' >>  bamclean/${2}_filtered.sam
samtools view -bS bamclean/${2}_filtered.sam > bamclean/${2}.filtered.bam
rm bamclean/${2}_filtered.sam 
