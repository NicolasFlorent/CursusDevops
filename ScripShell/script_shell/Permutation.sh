#!/bin/bash

perm_without_temp(){
    echo "Permutation sans variable temporaire: Valeurs données : "
    echo "a = " $a
    echo "b = " $b
    
    a=$(($a+$b))
    b=$(($a-$b))
    a=$(($a-$b))
    
    echo "Permutation des valeur... "
    echo "a = " $a
    echo "b = " $b
    
}

perm_with_temp(){
    echo "Permutation avec variable temporaire: Valeurs données : "
    echo "a = " $a
    echo "b = " $b
    
    tmp=$a
    a=$b
    b=$tmp
    
    echo "Permutation des valeur... "
    echo "a = " $a
    echo "b = " $b
    echo "tmp = " $tmp
    
}


read -p "Donner deux valeurs à permuter a et b : " a b
read -p "Voulez-vous faire une permutation avec ou sans variables temporaire ? (avec ? ou sans ? ) " choix
if [[ $choix == "avec" ]];then
    perm_with_temp
elif [[ $choix == "sans" ]];then
    perm_without_temp
else
    echo "ça ne fait pas partie des choix possible... tant pis pour vous...."
fi


