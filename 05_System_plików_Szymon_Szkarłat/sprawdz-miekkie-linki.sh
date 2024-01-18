#!/bin/bash

if [[ $# != 1 ]]; then
  echo -e "Nieodpowiednia liczba argumentów, spróbuj\n./sprawdz-miekkie-linki.sh SCIEZKA"
  exit 1
elif [[ ! -d $1 ]]; then
  echo "Podany argument nie jest ścieżką"
  exit 1
fi

ctr=0

for file in $(find "$1" -type l); do
  echo "--------------------"
  link=$file
  i=0
  arr=()

  # lecimy w głąb linku
  while [[ $(readlink "$link") != "" ]]; do
    arr[i]=$link
    i=$((i+1))
    link=$(readlink "$link")
  done

  if ((i > 1)); then
    ctr=$((ctr+1))
  fi

  echo -e "Wszystkie dowiązania z danego pliku:\n"
  for id in "${arr[@]}"; do
    echo "$id"
  done
  echo -e "\nLiczba $i\n"

done

echo "+--------------------+"
echo "+ Łącznie pętli: $ctr   +"
echo "+--------------------+"
