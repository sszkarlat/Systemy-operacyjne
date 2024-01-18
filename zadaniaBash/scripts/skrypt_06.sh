#!/usr/bin/env bash

# ls, ale mowi co jest katalogiem oraz ma odpowiedni komunikat jesli to jest ten plik

lista=$(ls)

nazwaPliku=$(awk -F/ '{print $(NF)}'<<<"$0")

for i in $lista;do
	if [[ -d $i  ]];then
		echo "$i jest katalogiem"
	elif [[ $i == $nazwaPliku ]];then
		echo "nie wypisujemy tego pliku"
	elif [[ -f $i ]];then
		ls -l | grep "$i"
	fi
done
