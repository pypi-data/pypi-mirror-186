#! /usr/bin/env python3
import re
import sys
from pathlib import Path

filename = sys.argv[1]
#filename = "/Users/corkep/book/Python-version/latex/chapter10/chap10.tex"

re_section = re.compile(r"\\(?P<level>(?:sub)*)section{(?P<title>[^}]+)}")
m = re.match(".*chap([0-9]+).tex", filename)
try:
    chapnum = m.group(1)
except AttributeError:
    chapnum = 'APP'

secnumbers = [0,]
lastlevel = 0

filename = Path(filename).expanduser()

outfile = filename.with_suffix('.py')
out = open(outfile, "w")

with open(filename, "r") as file:
    for line in file:
        if line.startswith(">>> ") or line.startswith("... "):
            print(line[4:], end="", file=out)
            continue
        
        if line.startswith(r"\end{lstlisting}"):
            print(file=out)
            continue
            
        m = re_section.match(line)
        if m is not None:
            level = m.group("level").count('sub')

            if level == lastlevel:
                secnumbers[level] += 1
            elif level > lastlevel:
                secnumbers.append(1)
            else:
                secnumbers = secnumbers[:level+1]
                secnumbers[level] += 1
            lastlevel = level

            secnum = ".".join([str(i) for i in [chapnum] + secnumbers])
            header = "# " + "#" * (level+1) + " " + secnum + " " + m.group('title') + "\n#\n"
            print(header, file=out)

out.close()