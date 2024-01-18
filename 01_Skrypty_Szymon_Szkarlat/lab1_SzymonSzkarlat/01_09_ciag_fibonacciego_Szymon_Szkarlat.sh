#!/bin/bash

fibonacci() {
	n=$1
	a=0
	b=1
	i=0

	while [ $i -lt $n ]
	do
		echo -n "$a "
		tmp=$a
		a=$b
		b=$((tmp + b))
		i=$((i + 1))
	done
}

if [ $# -ne 1 ]
then
	echo "Uzycie $0 <n>"
	exit 1
fi

n=$1

fibonacci $n
echo
