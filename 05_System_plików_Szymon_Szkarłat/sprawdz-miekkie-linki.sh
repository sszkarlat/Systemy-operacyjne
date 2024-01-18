#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Nieprawidlowa liczba argumentow. Uzyj: $0 <katalog>"
    exit 1
fi

katalog="$1"

# Sprawdzenie, czy katalog istnieje
if [ ! -d "$katalog" ]; then
    echo "Podany argument nie jest katalogiem."
    exit 1
fi

# Znajdowanie wszystkich plikow dowiazan miekkich w podanym katalogu
pliki_dowiazan=$(find "$katalog" -type l)

if [ -z "$pliki_dowiazan" ]; then
    echo "Brak plikow dowiazan miekkich w podanym katalogu."
    exit 0
fi

# Wyswietlanie informacji o przypadkach zapetlonego linkowania
echo "Przypadki zapetlonego linkowania miekkiego:"

while IFS= read -r plik; do
    link="$plik"
    dlugosc=0
    linki=()

    # Sprawdzenie dlugosci zapetlenia
    while [ "$(readlink "$link")" != "" ]; do
        linki+=("$link")
        dlugosc=$((dlugosc+1))
        link=$(readlink "$link")
    done

    if [ "$dlugosc" -gt 1 ]; then
        echo -e "\nLiczba zapetlen: $dlugosc"
        echo "Dlugosci zapetlen:"
        for id in "${linki[@]}"; do
            echo "$id"
        done
    fi

done <<< "$pliki_dowiazan"
