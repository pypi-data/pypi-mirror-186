#!/usr/bin/env python3

import re
import sys

text = open(sys.argv[1], 'r').read()

pat = re.compile(r'''\\INDEX\{[^}\n]*\n[^}]*\}''')

deblank = re.compile('\s+')

def fixup(m):
	x = m.group(0)
	# print(x)
	y = deblank.sub(' ', x) + '\n'
	# print(y)
	return y

# m = pat.findall(text)

m = pat.sub(fixup, text)

print(m)
