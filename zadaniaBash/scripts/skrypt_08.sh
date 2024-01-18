#!/bin/bash

# tworzenie kopii pliku

if [[ $# < 3 ]];then
	echo "Brak jakiegos argumentu"
fi
if [[ -f $1 && -d $3 && $2 -gt 0 ]];then
	for (( i=1; i<="$2"; i++ ));do
		dd conv=noerror if=$1 of=$3/$1.$i bs=$2 skip=$((i - 1)) count=1 2>/dev/null
	done
fi
