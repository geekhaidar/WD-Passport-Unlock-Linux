#!/bin/sh
if [ -z "$1" ]; then
	echo "please supply target device" >&2
	exit 1
fi
if [ -z "$2" ]; then
	echo "please supply a password" >&2
	exit 1
fi
python cookpw.py $1 --unset | sudo sg_raw -s 72 $2 c1 e2 00 00 00 00 00 00 48 00
