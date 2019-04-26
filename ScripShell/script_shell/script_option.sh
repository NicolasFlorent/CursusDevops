#!/bin/bash
addition(){
	somme=0
	while read line; do
		somme=$(( $somme + $line ))
	done < $name_fichier 
	echo "La somme des nombres dans le fichier est "$somme
}

nlignes(){
	nb_lignes=0
	while read line;do
		nb_lignes=$(($nb_lignes + 1))
	done < $name_fichier
	echo "Le nombre de lignes dans le fichier est "$nb_lignes
}

min(){
	read min < $name_fichier
	while read line;do
		if [[ $min -ge $line ]];then
			min=$line
		fi
	done < $name_fichier
	echo "Le minimun des nombres dans le fichier est "$min
}

max(){
	read max < $name_fichier
	while read line;do
		if [[ $max -le $line ]];then
			max=$line
		fi
	done < $name_fichier
	echo "Le maximum des nombres dans le fichier est "$max
}

name_fichier=$1
if [[ -e $name_fichier ]];then
	echo -e "Le fichier existe bien !\nLes "
else
	echo "Le fichier que vous recherchez n'existe pas ! Je ne peux rien faire d'autre !"
	exit 1
fi

for i in $*;do
	case $i in 
	-somme)
		addition
		;;
	-nblignes)
		nlignes
		;;
	-min)
		min
		;;
	-max)
		max
		;;
	$name_fichier)
		continue
		;;
	*)
		echo $i" n'est pas une option valide !"
		;;
	esac
done
