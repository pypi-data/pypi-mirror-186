#!/usr/bin/env python3

import re
from pathlib import Path
import argparse
import os
from colored import attr

parser = argparse.ArgumentParser(description='a grep like tool that searches over all RVC3 tex source files')
parser.add_argument('query', type=str, nargs='?', default=None,
	help='Python regexp query, suitably escaped.  If not given it is prompted for, which can be less hassle than escaping')
parser.add_argument('--list', '-l', action='store_const', const=True,
	help='just list the files that match')
parser.add_argument('--sublime', '-e', action='store_const', const=True,
	help='spawn sublime with a tab for each file that matches')
args = parser.parse_args()

root = Path('/Users/corkep/book/Python-version/latex')

files = [root / f"chapter{i}/chap{i}.tex" for i in range(1, 17)]
# files += [root / f"chapter-appendices/Z_0_{i:03d}_Appendix.tex" for i in range(1, 11)]

if args.query is None:
	query = input('regexp: ')
	print(query)
else:
	query = args.query
query = re.compile(query)

relevant_files = []

def boldify(m):
	return attr(1) + m.group(0) + attr(0)

for file in files:
	header = False

	with open(file, 'r') as f:
		for lineno, line in enumerate(f):
			m = query.search(line)
			if m is not None:
				if args.list or args.sublime:
					relevant_files.append(file)
					break
				if not header:
					print('\n' + file.name)
					header = True
				line = query.sub(boldify, line)
				print(f"{lineno:4d}: {line.rstrip():s}")

if args.list:
	for file in relevant_files:
		print(file.name)
if args.sublime:
	os.system('tcsh -c "sublime ' + ' '.join([str(file) for file in relevant_files]) + '"')

