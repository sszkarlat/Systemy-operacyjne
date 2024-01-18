# sprawdz czy podany ciag jest arytmetyczny lub geometryczny

cGeo=0
cAryt=0
cnt=0
wynik=0
for i in $@;do
	if (( $cnt == 0 ));then
		j=$i
		(( cnt++ ))
	elif (( $cnt == 1 ));then
		cGeo=$(( $i/$j ))
		cAryt=$(( $i-$j ))
		(( cnt++ ))
		j=$i
	else
		if (( cGeo != $(( $i/$j )) ));then
			wynik=1
		elif (( cAryt != $(( $i-$j )) ));then
			wynik=2
		elif (( cAryt != $(( $i-$j )) && cGeo != $(( $i/$j )) ));then
			wynik=3
		fi
		j=$i
	fi
done
if (( $wynik == 0 )) && (( $# != 0));then
	echo "Ciag jest i geometryczny i arytmetyczny"
elif (( $wynik == 1 ));then
	echo "Ciag jest arytmetyczny"
elif (( $wynik == 2 ));then
	echo "Ciag jest geometryczny"
else
	echo "Ciag nie jest ani geometryczny, ani arytmetyczny"
fi
