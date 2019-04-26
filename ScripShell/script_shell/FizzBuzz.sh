#!/bin/bash

read -p "Vous voulez afficher jusqu'à quel nombre ???? " n

for((i=1;i<=$n;i++)); do
    if [[ $i%3 -eq 0 ]] && [[ $i%5 -eq 0 ]]; then
        echo "FizzBuzz"
    elif [[ $i%5 -eq 0 ]]; then
        echo "Buzz"
    elif [[ $i%3 -eq 0 ]]; then
        echo "Fizz"
    else
        echo $i
    fi
done
