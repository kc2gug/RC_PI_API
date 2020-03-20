#!/bin/bash

cd $(dirname $0)

./cleanup.py

python -m SimpleHTTPServer &
simple_pid="$!"
./controlpadserver.py
echo "Stopping HTTP server : pid = $simple_pid"
kill $simple_pid
