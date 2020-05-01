#!/bin/bash

cd $(dirname $0)

./cleanup.py
sleep 3

python -m SimpleHTTPServer &
simple_pid="$!"
./controlpadserver.py
echo -e "\nStopping HTTP server : pid = $simple_pid"
sleep 2
kill -9 $simple_pid
./cleanup.py
