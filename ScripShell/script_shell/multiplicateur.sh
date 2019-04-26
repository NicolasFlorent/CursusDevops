#/bin/bash
total=1
for i in $*;do
	total=$(( $total * $i ))
done
echo "Le produit des nombres est égal à "$total

