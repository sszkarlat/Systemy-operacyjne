#!/bin/bash

# podawanie uprawnien do pliku

plik="$@"
if [[ $# == 0 ]];then
	echo "Podaj plik"
	read plik
fi
for i in $plik;do
	uprawnienia=""
	if [[ -r $i ]];then
		uprawnienia+="r"
	fi
	if [[ -w $i ]];then
		uprawnienia+="w"
	fi
	if [[ -x $i ]];then
		uprawnienia+="x"
	fi
	echo "$uprawnienia $i"
done
