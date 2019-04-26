#!/bin/bash

if ping -c 1 google.com;then
	firefox www.google.com
else
	echo "Vous ne pouvez pas vous connecter à google"
fi
