#/bin/bash
val1=0
val2=1
somme=$(( $val1 + $val2 ))
if [[ $1 == 1 ]];then
	echo "la valeur "$1" de la suite de Fibonnaci est "$val1
elif [[ $1 == 2 ]];then
	echo "la valeur "$1" de la suite de Fibonnaci est "$val2 
else
	echo -e $val1"\n"$val2"\n"$somme
	for (( i = 3 ; i < $1 ; i++ ));do
		val1=$val2
		val2=$somme
		somme=$(( $val1 + $val2 ))
		echo $somme
	done
	echo "la valeur "$1" de la suite de Fibonnaci est "$somme 
fi

