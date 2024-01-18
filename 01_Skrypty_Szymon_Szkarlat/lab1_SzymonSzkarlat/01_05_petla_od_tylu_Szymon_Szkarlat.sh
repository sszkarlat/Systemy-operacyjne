#!/bin/bash

if [ $# -eq 0 ]
then
	echo "Brak argumentow"
	exit 1
fi

for ((i=$#; i>0; i--))
do
	echo -n "${!i} "
done

echo
