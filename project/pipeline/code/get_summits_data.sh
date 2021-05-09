
infile="/mnt/Storage/home/zhangjiasheng/project/G4/data"
outfile="/mnt/Storage/home/zhangjiasheng/project/G4/data"
ref_genome="/mnt/Storage/home/zhangjiasheng/data/Bowtie2"

file=("AB521M" "AB551" "AB555M" "AB580" "HCI005" "HCI009" "STG139" \
"STG139M_181" "STG139M_284" "STG143_284" "STG143_317" "STG195M" \
"STG201_181" "STG201_284" "STG282M" "STG316" "VHIO179_181" \
"VHIO179_284" "VHIO098_181" "VHIO098_284")

for model in ${file[@]}
do
	cd $infile/$model/07_macs2
	mkdir tmp
	for k in `seq 1 4`;
	do
		python ~/data/script/get_bin.py -i $infile/$model/07_macs2/${model}_rep${k}.hg19_summits.bed -U 200 -D 200 -f ${model}_summits_windows_rep${k} -o $outfile/$model/07_macs2/tmp
		wait;
		bedtools getfasta -fi ~/data/Bowtie2/hg19.fa -bed $outfile/$model/07_macs2/tmp/${model}_summits_windows_rep${k}.bed -fo $outfile/$model/07_macs2/tmp/G4_${model}_rep${k}.txt
		wait;
		python ~/Toolkit/G4Hunter/G4Hunter.py -i $outfile/$model/07_macs2/tmp/G4_${model}_rep${k}.txt -o $outfile/$model/07_macs2/tmp -w 25 -s 1.5
	done &
done



