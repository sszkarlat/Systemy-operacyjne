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

# Znajdowanie plikow o zadanej liczbie dowiazan (>1)
pliki_dowiazan=$(find "$katalog" -type f -links +1)

if [ -z "$pliki_dowiazan" ]; then
    echo "Brak plikow z twardymi dowiazaniami w podanym katalogu."
    exit 0
fi

# Wyswietlenie informacji o przypadkach hardlinkowania
echo "Przypadki hardlinkowania:"

while IFS= read -r plik; do
    liczba_dowiazan=$(stat -c %h "$plik")

    echo -e "\nLiczba dowiazan: $liczba_dowiazan"
    echo "Plik: $plik"

done <<< "$pliki_dowiazan"
