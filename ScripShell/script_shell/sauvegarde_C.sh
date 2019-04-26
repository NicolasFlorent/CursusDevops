#!/bin/bash
extension=$1
for i in *.c;
do
	cp $i $i.$extension
done
