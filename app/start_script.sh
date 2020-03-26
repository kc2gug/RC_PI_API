#!/bin/bash

cd $(dirname $0)

./cleanup.py

python -m SimpleHTTPServer &
simple_pid="$!"
./controlpadserver.py
echo -e "\nStopping HTTP server : pid = $simple_pid"
sleep 2
kill $simple_pid
