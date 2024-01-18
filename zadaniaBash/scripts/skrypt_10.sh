#!/bin/bash

if [[ $# -eq 0 ]];then
	echo "brak argumentow"
	exit
fi
for i in $@;do
	find $i -type f | wc -l
done