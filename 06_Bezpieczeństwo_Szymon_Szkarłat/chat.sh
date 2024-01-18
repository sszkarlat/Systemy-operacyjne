#!/bin/bash

if [ -z "$2" ] ; then
    echo "Podaj imiona (nadawca i odbiorca) $0 szymon kamil"
    exit 1
fi

P1=/tmp/chatpipe${1}
P2=/tmp/chatpipe${2}

[ -p "$P1" ] || mkfifo $P1
[ -p "$P2" ] || mkfifo $P2

# Klucz do szyfrowania/deszyfrowania (moze lepiej zmienic na bezpieczniejszy)
KEY="tajnyKlucz"

# Uruchomienie w tle procesu cat dla przychodzacego potoku,
(cat $P2 | openssl enc -d -aes-256-cbc -pass pass:$KEY) &

# Szyfrowanie wiadomosci i przekazywanie jej do potoku
(echo "$1 dolaczyl" ; cat) | openssl enc -aes-256-cbc -pass pass:$KEY > $P1

# Zakonczenie procesu w tle
trap 'kill -9 $(jobs -p)' EXIT
