#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import os
import sys
import socket

import config as cfg

from cgi import parse_qs


def getPostData ():
        package_string=""
        if os.environ.has_key('QUERY_STRING'):
                package_string=os.environ['QUERY_STRING']
        elif len(sys.argv) == 2:
                package_string=sys.argv[1]
        else:
                sys.exit()
	f = open('workfile', 'a')
	f.write(package_string+'\n')
        return package_string


def main(argv=None):
	parseDictionary = parse_qs(getPostData())

	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = socket.gethostname()
		client.connect((host, cfg.PORT))
		client.send(getPostData())
		client.shutdown(socket.SHUT_RDWR)
		client.close()
	except Exception as msg:
		print msg

if __name__ == "__main__":
        sys.exit(main())

