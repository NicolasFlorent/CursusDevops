#!/bin/bash
if [ "$PWD" == "$HOME" ];then
	echo "Vous êtes dans le répertoire d'accueil"
else
	echo "Vous n'êtes pas dans le répertoire d'accueil"
fi
