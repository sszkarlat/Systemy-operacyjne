#!/usr/bin/env bash

# wypisanie 5 kolumny usera z podanym UUID

uid="$@"
if (( $#==0 )); then
       	echo "Podaj UID"
	read uid
fi
for i in $uid;do
	awk -F: "{if (\$3==$i) {print \$5}}" /etc/passwd
done
