# kopiowanie pliku do innego folderu, wiecej niz 1 raz

if (( $# == 3 )); then
	if [[ -r "$1" && -f "$1" && -w "$2" ]]; then
		if (( $3 > 0 )); then
			for (( i=0; i<$3; i++ ))
			do
				plik="$2"
				var=$(awk -F/ '{print $(NF)}'<<< "$1")
				plik+="$var"
				plik+="-kopia-$i"
				cp "$1" "$plik"
			done

		else
			echo "musi byc liczba wieksza od 0"
		fi
	else
		echo "Nie ma takiego pliku/folderu/brak uprawnien"
	fi
else
	echo "Nieprawidlowa liczba argumentow"
fi
