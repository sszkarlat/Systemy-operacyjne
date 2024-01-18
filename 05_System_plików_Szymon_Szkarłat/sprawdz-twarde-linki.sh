#!/bin/bash

if [[ $# != 1 ]]; then
  echo -e "Nieodpowiednia liczba argumentów, spróbuj\n./sprawdz-twarde-linki.sh SCIEZKA"
  exit 1
elif [[ ! -d $1 ]]; then
  echo "Podany argument nie jest ścieżką"
  exit 1
fi

# liczba dowiązań nie wliczając tych samych dowiązań
ctr=0

arr=()

while IFS= read -r -d '' file; do
  # liczba linków
  n=$(stat "$file" | awk '/Links/ {print $2}')

  if ((n > 1)); then
    # jeśli nie ma w tablicy
    if ! printf '%s\0' "${arr[@]}" | grep -F -x -z -- "$file" >/dev/null; then
      # dodajemy do tablicy
      j=0
      while IFS= read -r -d '' links; do
        j=$((j+1))
        arr+=( "$links" )
      done < <(find "$1" -type f -links "$n" -print0)
      ctr=$((ctr + (j/n)))
    fi
  fi
done < <(find "$1" -type f -print0)

echo -e "\nLiczba różnych hardlinków: $ctr\n"
