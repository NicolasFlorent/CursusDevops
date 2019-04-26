#!/bin/bash
echo $PWD
if [[ -e files_concat ]];then
	rm files_concat
else
	touch files_concat
fi
for i in $PWD/*;do
	cat $i >> files_concat
done

