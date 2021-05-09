#example:nohup bash PDTX_run_model.sh &
# "AB521M","AB551","AB555M","AB577M","AB580","AB636M","AB790","AB863M","HCI005","HCI009",
# "PAR1006","PAR1022","STG139","STG139M_181","STG139M_284","STG143_284","STG143_317","STG195M","STG201_181","STG201_284",
# "STG282M","STG316","STG331","VHIO098_181","VHIO098_284","VHIO179_181","VHIO179_284"

# AB521M,AB551,AB555M,AB577M,AB580,AB636M,AB790,AB863M,HCI005,HCI009,
# PAR1006,PAR1022,STG139,STG139M_181,STG139M_284,STG143_284,STG143_317,STG195M,STG201_181,STG201_284,
# STG282M,STG316,STG331,VHIO098_181,VHIO098_284,VHIO179_181,VHIO179_284

infile="/mnt/Storage/home/houshuang/g4/chipseq/PDTX/01_raw_data/fastq_file"
ref_genome="/mnt/Storage/home/houshuang/ref_genome"

file=("AB521M" "AB551" "AB555M" "AB580" "HCI005" "HCI009" "STG139" \
"STG139M_181" "STG139M_284" "STG143_284" "STG143_317" "STG195M" \
"STG201_181" "STG201_284" "STG282M" "STG316" "VHIO179_181" \
"VHIO179_284" "VHIO098_181" "VHIO098_284")

file2=("AB521M" "AB551" "AB555M" "AB580" "HCI009" "STG139" \
"STG139M_181" "STG139M_284" "STG143_284" "STG195M" \
"STG201_181" "STG201_284" "STG282M" "STG316" "VHIO179_181" \
"VHIO179_284" "VHIO098_284")

for model in ${file2[@]}
do
	mkdir $model
	cd $model
	
	# === trimming ===
	mkdir 01_trimmed
	for rep in {input,rep1,rep2,rep3,rep4}
	do
		tmp=`ls $infile/$model/${model}_${rep}_r?.fastq.gz` && \
		echo ${model}_${rep}"_raw_fastq: "$tmp && \
		all=`echo $tmp | tr " " ","` && \
		echo ${model}_${rep}"_raw_fastq: "$all && \
		zcat $tmp | gzip > ./01_trimmed/${model}_${rep}.fastq.gz
		
	  f=`basename $fo`
	  cutadapt -q 20 -O 3 -a CTGTCTCTTATACACATCT -o ./01_trimmed/${model}_${rep}.trimmed.fq.gz ./01_trimmed/${model}_${rep}.fastq.gz && \
  	echo "01_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done
	
	# == align ==
	g=${ref_genome}/hg19_mm10_dm6/hg19_mm10_dm6
	mkdir 02_aligned
	for fo in ./01_trimmed/*.trimmed.fq.gz
	do
		f=`basename $fo`
		(bwa mem -t 10 -M ${g}.fa $fo | samtools view -@ 10 -Sb > ./02_aligned/${f%%.trimmed.fq.gz}.hg19_mm10_dm6.bam) 2>./02_aligned/${f%%.trimmed.fq.gz}_mapping.log && \
  	echo "02_time: "`date +'%Y-%m-%d %H:%M:%S'`
		#bowtie2 -p 10 --mm -x $g --no-unal -U $fo | samtools view -Sb -F2308 -q 10 > ./02_aligned/${f%%.trimmed.fastq.gz}.hg19_mm10_dm6.bam
	done
	
	mkdir 03_bam_sort
	for fo in ./02_aligned/*bam
	do
		f=`basename $fo`
	  samtools view -b -F2308 -q 10 $fo | samtools sort -@ 10 -O BAM - > ./03_bam_sort/${f%%.bam}.sort.bam && \
  	echo "03_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done
	
	# === species splitting ===
	mkdir 04_split_bam
	# awk '{$1=$1"_hg19";for(i=1;i<NF;i++) printf("%s\t",$i);print $NF}' hg19.refseq.bed > test
	hg19_genome=${ref_genome}/hg19_mm10_dm6/hg19.chrom.sizes.bed
	mm10_genome=${ref_genome}/hg19_mm10_dm6/mm10.chrom.sizes.modi.bed
	dm6_genome=${ref_genome}/hg19_mm10_dm6/dm6.chrom.sizes.modi.bed
	for fo in ./03_bam_sort/*bam
	do
		f=`basename $fo`
	  #hg19
	  samtools view -b -@10 $fo -L $hg19_genome > ./04_split_bam/${f%%.hg19_mm10_dm6.sort.bam}.hg19.bam && \
	  #dm6
		#samtools view -b -@10 $fo -L $dm6_genome > ./04_split_bam/${f%%.hg19_mm10_dm6.sort.bam}.dm6.bam && \
	  #mm10
	  #samtools view -b -@10 $fo -L $mm10_genome > ./04_split_bam/${f%%.hg19_mm10_dm6.sort.bam}.mm10.bam && \
	  echo "04_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done
	
	# === merge files of same condition and same sequencing run === 
#	mkdir 05_merge_bam
#	rep=(input rep1 rep2 rep3 rep4)
#	for i in ${rep[@]}
#	do
#		f=${model}_$i
#		#hg19
#	  samtools merge -@10 ./05_merge_bam/${f}.hg19.merged.bam ./04_split_bam/${f}*hg19.bam && \
#	  #dm6
#	  samtools merge -@10 ./05_merge_bam/${f}.dm6.merged.bam ./04_split_bam/${f}*dm6.bam && \
#	  #mm10
#	  samtools merge -@10 ./05_merge_bam/${f}.mm10.merged.bam ./04_split_bam/${f}*mm10.bam && \
#	  echo "05_time: "`date +'%Y-%m-%d %H:%M:%S'`
#	done
	
	# === markduplicates (picard) and recover stats on number of reads == 
	mkdir 06_rmdup
	for fo in ./04_split_bam/*.bam
	do
	  #java -Xmx7g -jar ~/applications/picard-2.20.3.jar MarkDuplicates I=$f O=${f%%.bam}.nodup.bam M=${f%%.bam}.md.txt AS=true REMOVE_DUPLICATES=true
		f=`basename $fo`
		sambamba markdup -t 10 -r $fo ./06_rmdup/${f%%.bam}.nodup.bam && \
	  echo "06_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done
	
	rm -rf 03_bam_sort
	rm -rf 04_split_bam
	
	# === call peaks == 
	mkdir 07_macs2
	for fo in ./06_rmdup/*rep*bam
	do
		f=`basename $fo`
		echo "call_peak_bam: "$fo
  	macs2 callpeak --keep-dup all -t $fo -c ./06_rmdup/${model}_input*hg19*bam -n ./07_macs2/${f%%.nodup.bam} --format=BAM --gsize hs --qvalue 0.05 2> ./07_macs2/${f%%.nodup.bam}_MACS.log && \
  	echo "07_hg19_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done
	
	mkdir 07_macs14
	for fo in ./06_rmdup/*rep*hg19*bam
	do
		f=`basename $fo`
		echo "call_peak_bam: "$fo
  	macs14 callpeak -p 1e-5 -t $fo -c ./06_rmdup/${model}_input*hg19*bam -n ./07_macs14/${f%%.nodup.bam}_macs14 --format=BAM --gsize hs 2> ./07_macs14/${f%%.nodup.bam}_macs14.log && \
  	echo "07_hg19_time: "`date +'%Y-%m-%d %H:%M:%S'`
	done

#	for fo in ./06_rmdup/*rep*bam
#	do
#		f=`basename $fo`
#		if [[ $fo == *"dm6"* ]]
#		then
#	  	macs2 callpeak --keep-dup all -B -t $fo -c ./06_rmdup/${model}_input_*dm6* -n ./07_macs/${f%%.nodup.bam} --format=BAM --gsize 'dm' --bw=300 --qvalue 0.05 2> MACS.log && \
#	  	echo "07_dm6_time: "`date +'%Y-%m-%d %H:%M:%S'`
#	  else
#	  	macs2 callpeak --keep-dup all -B -t $fo -c ./06_rmdup/${model}_input_*hg19* -n ./07_macs/${f%%.nodup.bam} --format=BAM --gsize 'hs' --bw=300 --qvalue 0.05 2> MACS.log && \
#	  	echo "07_hg19_time: "`date +'%Y-%m-%d %H:%M:%S'`
#		fi
#	done
	
	# === generate bw file === 
#	mkdir 08_bw_file
#	cd 08_bw_file
#	for fo in ../07_macs/*.hg19*bdg
#	do
#		f=`basename $fo`
#		grep -v _ $fo | awk '{if($1 != "chrM") print $0}' > ${f%%.bdg}.tmp.bdg && \
#		bedSort ${f%%.bdg}.tmp.bdg ${f%%.bdg}.sort.bdg && \
#		bedGraphToBigWig ${f%%.bdg}.sort.bdg ${ref_genome}/hg19/chromInfo.txt ${f%%.bdg}.bw && \
#		rm ${f%%.bdg}.tmp.bdg && \
#		rm ${f%%.bdg}.sort.bdg
#	done
#	cd ..
	
	mkdir 09_merge_rep
	cd 09_merge_rep
	rep_all=`ls ../06_rmdup/*rep*hg19*bam` && \
	echo "merge_rep_bam_files: "${rep_all} && \
	samtools merge -@ 10 ${model}.hg19.merged.bam ${rep_all} && \
	samtools sort -@ 10 -O BAM ${model}.hg19.merged.bam > ${model}.hg19.merged.sort.bam
	rm ${model}.hg19.merged.bam
	ln ${model}.hg19.merged.sort.bam ../06_rmdup/${model}.hg19.merged.sort.bam
  macs14 callpeak -p 1e-5 -t ${model}.hg19.merged.sort.bam -c ../06_rmdup/${model}_input*hg19*bam -n ${model}_macs14 --format=BAM --gsize hs 2> macs14.log && \
	macs2 callpeak --keep-dup all -t ${model}.hg19.merged.sort.bam -c ../06_rmdup/${model}_input*hg19*bam -n ${model}_macs2 --format=BAM --gsize 'hs' --bw=300 --qvalue 0.05 2> MACS.log
	cd ..
	
	source /mnt/Storage/home/houshuang/miniconda3/etc/profile.d/conda.sh && \
	conda activate chipseq
	
	mkdir 10_bw_from_bam
	for fo in ./06_rmdup/*hg19*bam
	do
		f=`basename $fo`
		tot_num=`samtools view -c -F 260 $fo` && \
		echo $tot_num && \
		c=`bc -l <<< "1000000 / $tot_num"` && \
		echo $c && \
		bamCoverage --scaleFactor $c -bs 10 -p 15 -b $fo -of "bigwig" -o ./10_bw_from_bam/${f%%.bam}.bw
	done
	
	conda deactivate

	cd ..
done

# === Generate consensus peaks ===
mkdir macs2_multi2_bed
cd macs2_multi2_bed
for i in ${file[@]}
do
	peak_files=`ls ../${i}/07_macs2/*hg19*_peaks.narrowPeak` && \
	echo "multi2_narrowpeak: "${peak_files} && \
	multiIntersectBed -i ${peak_files} | awk '{if($4>=2) print $0}' | sortBed -i | mergeBed -i - > $i.hg19.multi2.bed && \
	echo "end_time: "`date +'%Y-%m-%d %H:%M:%S'`
done

multi2_peaks=`ls *hg19.multi2.bed` && \
cat $multi2_peaks | sortBed -i - | mergeBed -i - > hg19.consensus.bed && \
awk '{if (($3-$2) >= 100) print $0}' hg19.consensus.bed | sortBed -i - > hg19.consensus.filter.sort.bed

cd ..
# === Generate consensus peaks ===
mkdir macs14_multi2_bed
cd macs14_multi2_bed

for i in ${file[@]}
do
	peak_files=`ls ../${i}/07_macs14/*rep*hg19_macs14_peaks.bed` && \
	echo "multi2_narrowpeak: "${peak_files} && \
	multiIntersectBed -i ${peak_files} | awk '{if($4>=2) print $0}' | sortBed -i | mergeBed -i - > ${i}.hg19.multi2.bed && \
	echo "end_time: "`date +'%Y-%m-%d %H:%M:%S'`
done

multi2_peaks=`ls ./*hg19.multi2.bed` && \
echo "merge_one: "$multi2_peaks
cat $multi2_peaks | sortBed -i - | mergeBed -i - > hg19.consensus.bed && \
awk '{if (($3-$2) >= 100) print $0}' hg19.consensus.bed | sortBed -i - > hg19.consensus.filter.sort.bed
