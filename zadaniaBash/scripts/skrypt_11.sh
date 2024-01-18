#!/bin/bash

if [[ $# < 2 ]]; then
	echo "Powinny byc 2 argumenty"
	exit
elif [[ ! -r $1 ]];then
	echo "Nie mozna odczytac pliku"
	exit
elif [[ ! -f $1 ]]; then
	echo "Pierwszy argument nie jest plikiem"
	exit
elif [[ ! -d $2 ]]; then
	echo "Drugi argument nie jest sciezka"
	exit
elif [[ ! -w $2 ]]; then
	echo "Nie mozna zapisac w podanej sciezce pliku"
	exit
else
	cp "$1" "$2"
	echo "done"
fi