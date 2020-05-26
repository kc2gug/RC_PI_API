#!/bin/bash

cd $(dirname $0)

function cleanup (){
	for things in $(ps | grep -e python -e start_script | awk '{print $1}'); 
		do kill -9 $things
	done

	./cleanup.py
	sleep 1
}


python -m SimpleHTTPServer &

if [[ $# != 0 ]]; then
	cleanup
	exit 10
fi

simple_pid="$!"

./controlpadserver.py

echo -e "\nStopping HTTP server : pid = $simple_pid"
kill -9 $simple_pid

cleanup
