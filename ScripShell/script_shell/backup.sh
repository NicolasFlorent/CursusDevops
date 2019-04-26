#!/bin/bash
if [[ -e ../backup/ ]];then
	rm -r ../backup/
fi
mkdir ../backup/
touch ../backup/backup_files.txt

for i in *;do
	echo $i
	echo $i >> ../backup/backup_files.txt
	cp $i ../backup/$i
done
