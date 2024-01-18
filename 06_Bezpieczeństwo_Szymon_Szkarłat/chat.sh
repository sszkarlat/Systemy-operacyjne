#!/bin/bash

if [ -z "$2" ] ; then
    echo "Need names of chat pipes (yours and other's), eg $0 bob john"
    exit 1
fi

P1=/tmp/chatpipe${1}
P2=/tmp/chatpipe${2}
KEY_FILE=./secret.key

[ -p "$P1" ] || mkfifo $P1
[ -p "$P2" ] || mkfifo $P2

# Check if the key file exists
if [ ! -f "$KEY_FILE" ]; then
    echo "Key file not found. Please generate the key file first."
    exit 1
fi

# Background cat of incoming pipe,
# also prepend current date to each line)
(cat $P2 | sed "s/^/$(date +%H:%M:%S)> /" | openssl enc -aes-256-cbc -d -base64 -kfile $KEY_FILE) &

# Feed one notice and then STDIN to outgoing pipe
(echo "$1 joined" ; cat) | openssl enc -aes-256-cbc -e -base64 -kfile $KEY_FILE >> $P1

# Kill all background jobs (the incoming cat) on exit
trap 'kill -9 $(jobs -p)' EXIT
# (Probably should delete the fifo files too)
