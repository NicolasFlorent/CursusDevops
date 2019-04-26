#!/bin/bash
echo "Saisissez votre âge :";read age; echo "Vous avez donc "$age" ans."
if [ $age -ge 18 ];then 
	echo "Vous êtes majeur(e)"
else 
	echo "Vous n'êtes pas majeur(e)"
fi

