#!/bin/bash

read -p "Avez vous un prenom ? (oui ? non ?) " reponse_prenom
if [[ $reponse_prenom == "non" ]];then
    echo "OOOOh c'est dommage ça ! Je vous en donne un alors ! ça sera Bob !"
    name="Bob"
    elif [[ $reponse_prenom == 'oui' ]];then
    read -p "Quel est-il alors ??? " name
else
    echo "Je ne comprends ce que vous avez dit ! Je vous appellerai Bran alors !"
    name="Bran"
fi

read -p "Avez vous un nom de famille ? (oui ? non ?) " reponse
if [[ $reponse == "non" ]];then
    echo "OOOOh c'est dommage ça ! Je vous en donne un alors ! ça sera Smith !"
    nom_famille="Smith"
    elif [[ $reponse == "oui" ]];then
    read -p "Quel est-il alors ??? " nom_famille
else
    echo "Je ne comprends ce que vous avez dit ! Je vous appellerai Hodor alors !"
    nom_famille="Hodor"
fi

echo "Du coup, bonjour "$name" "$nom_famille" !"