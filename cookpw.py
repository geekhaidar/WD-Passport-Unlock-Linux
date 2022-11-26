#!/usr/bin/env python

import sys
import argparse
import codecs

def wdc(password):
	password = "WDC." + password
	password = password.encode("utf-16")[2:]
	from hashlib import sha256
	for _ in range(1000):
		password = sha256(password).digest()
	return password

def raw(password):
	if password == 'NULL':
		password = ''
	return bytes(password.ljust(32, '\0').encode('ascii'))

def generate_password(password, cook_method, cmd, changepw):
	password = cook_method(password)

	if cmd == 'unlock':
		field = b'00'
	elif cmd == 'change':
		field = b'00'
		password = password + cook_method(changepw)
	elif cmd == 'unset':
		field = b'10'
		password = password + b'\00' * 32
	elif cmd == 'set':
		field = b'01'
		password = b'\00' * 32 + password

	header = b'450000' + field + b'00000020'
	header = codecs.getdecoder('hex')(header)[0]

	return header + password

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("passwd", type=str)
	parser.add_argument("--raw", action="store_true",
		help="use raw ascii input, length must be under 32, use 'NULL' for empty input")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("--unset", action="store_true",
		help="set the password")
	group.add_argument("--set", action="store_true",
		help="unset the password")
	group.add_argument("--change", action="store", type=str, metavar="topw",
		help="change the password")

	args = parser.parse_args()

	if args.raw:
		if len(args.raw) > 32:
			sys.exit('Password length cannot be larger than 32!')
		method = raw
	else:
		method = wdc

	changepw = None
	if args.unset:
		# sg_raw -s 72 -i OUTPUT_FILE DEVICE c1 e2 00 00 00 00 00 00 48 00
		cmd = 'unset'
	elif args.set:
		# sg_raw -s 72 -i OUTPUT_FILE DEVICE c1 e2 00 00 00 00 00 00 48 00
		cmd = 'set'
	elif args.change:
		# sg_raw -s 72 -i OUTPUT_FILE DEVICE c1 e2 00 00 00 00 00 00 48 00
		cmd = 'change'
		changepw = args.change
	else:
		# sg_raw -s 40 -i OUTPUT_FILE DEVICE c1 e1 00 00 00 00 00 00 28 00
		cmd = 'unlock'

	password = generate_password(args.passwd, method, cmd, changepw)

	out = getattr(sys.stdout, 'buffer', sys.stdout)
	out.write(password)

if __name__ == '__main__':
	main()
