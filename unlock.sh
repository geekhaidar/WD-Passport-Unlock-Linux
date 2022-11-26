#!/bin/sh
if [ -z "$1" ]; then
	echo "please supply target device" >&2
	exit 1
fi
if [ -z "$2" ]; then
	echo "please supply a password" >&2
	exit 1
fi
python cookpw.py $2 | sudo sg_raw -s 40 $1 c1 e1 00 00 00 00 00 00 28 00
