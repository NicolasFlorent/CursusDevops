#!/bin/bash
echo "Hello toi !"
while :
do
    bool_continue=true;
    echo -e "Quelle opération voulez vous faire ????\n(choix possible : add sous mult div)\n(si vous voulez quitter le calculateur : quitter)";read op_choice
    case $op_choice in
        add)
            somme=0
            echo "entrez les nombres a additionner: (stop pour arrêter)";
            while $bool_continue;do
                read valeur
                if [[ $valeur == stop ]];then
                    bool_continue=false
                else
                    somme=$(( $somme + $valeur ))
                fi
            done
            echo -e "Le resultat de l'opération est "$somme"\n"
        ;;
        sous)
            echo "entrez les nombres à soustraire: ";
            read difference
            while $bool_continue;do
                read valeur
                if [[ $valeur == stop ]];then
                    bool_continue=false
                else
                    difference=$(( $difference - $valeur ))
                fi
            done
            echo -e "Le resultat de l'opération est "$difference"\n"
        ;;
        mult)
            produit=1
            echo "entrez les nombres à multiplier: ";
            while $bool_continue;do
                read valeur
                if [[ $valeur == stop ]];then
                    bool_continue=false
                else
                    produit=$(( $produit * $valeur ))
                fi
            done
            echo -e "Le resultat de l'opération est "$produit"\n"
        ;;
        div)
            echo "entrez les nombres à diviser: ";
			read diviseur
            while $bool_continue;do
                read valeur
                if [[ $valeur == stop ]];then
                    bool_continue=false
                else
                    diviseur=$(( $diviseur / $valeur ))
                fi
            done
            echo -e "Le resultat de l'opération est "$diviseur"\n"
        ;;
        quitter)
            echo "A bientôt !"
            break
        ;;
        *)
            echo "Ressayer je ne comprends pas ce que vous voulez faire ! :) "
        ;;
    esac
done


