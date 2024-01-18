#!/bin/bash

if [ -z "$2" ] ; then
    echo "Need names of chat pipes (yours and other's), eg $0 bob john"
    exit 1
fi

P1=/tmp/chatpipe${1}
P2=/tmp/chatpipe${2}

[ -p "$P1" ] || mkfifo $P1
[ -p "$P2" ] || mkfifo $P2

# Background cat of incoming pipe,
# also prepend current date to each line)
(cat $P2 | sed "s/^/$(date +%H:%M:%S)> /" ) &

# Feed one notice and then STDIN to outgoing pipe
(echo "$1 joined" ; cat) >> $P1

# Kill all background jobs (the incoming cat) on exit
trap 'kill -9 $(jobs -p)' EXIT
# (Probably should delete the fifo files too)
