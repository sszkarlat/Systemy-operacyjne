#!/bin/bash

if [ -z "$2" ] ; then
    echo "Podaj imiona (nadawca i odbiorca) $0 szymon kamil"
    exit 1
fi

P1=/tmp/chatpipe${1}
P2=/tmp/chatpipe${2}

[ -p "$P1" ] || mkfifo $P1
[ -p "$P2" ] || mkfifo $P2

# Uruchomienie w tle procesu cat dla przychodzacego potoku,
(cat $P2) &

(echo "$1 dolaczyl" ; cat) >> $P1

# Zakonczenie tego co dzieje sie w tle
trap 'kill -9 $(jobs -p)' EXIT
