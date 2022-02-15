#!/usr/bin/env python3

import hashlib, binascii, getpass
passwd = getpass.getpass("Your password please mouahahah: ")
hash = hashlib.new('md4', passwd.encode('utf-16le')).hexdigest()
print(f"The Windows NT Hash of your string is {hash}")

