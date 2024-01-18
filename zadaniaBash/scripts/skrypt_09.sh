#!/bin/bash

# printowanie ilosci procesow od wszystkich userow

while (( 1==1 ));do
	ps -eo user | sort | uniq -c
	echo ""
	sleep 2
done
