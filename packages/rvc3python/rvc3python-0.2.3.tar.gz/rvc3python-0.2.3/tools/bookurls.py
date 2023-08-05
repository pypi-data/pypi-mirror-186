#!/usr/bin/env python3

import re
from pathlib import Path
import os
from colored import attr
import urllib.request
import urllib.error


root = Path('/Users/corkep/book/Python-version/latex')

files = [root / f"chapter{i}/chap{i}.tex" for i in range(1, 17)]
# files += [root / f"appendices/Z_0_{i:03d}_Appendix.tex" for i in range(1, 11)]
files += [root / f"appendices/app.tex"]

query = re.compile(r'''\\url{([^}]+)}''')

relevant_files = []

fout = open('book.html', 'w')
fout.write('<html>\n<body>\n')
for file in files:
    header = False

    with open(file, 'r') as f:
        urls = query.findall(f.read())

    if len(urls) > 0:
        name = Path(file).stem
        print('\n' + str(file))
        fout.write(f"<h2>{name}</h2>\n<ul>\n")

        for url in urls:
            print(url, end='')
            try:
                f = urllib.request.urlopen(url, timeout=10)
                status = 200 <= f.status <= 299
                print(' ok')
            except urllib.error.HTTPError as e:
                print(e.code)

                # print(f"ERR2  {url}, {f.status}")
                status = 200 <= e.code <= 299
            except urllib.error.URLError as e:
                print(f"ERR  {url}, {e.reason}")
                status = False
            except ValueError:
                print(" ValueError")
                status = False

            if status:
                style = ""
            else:
                style = "color: red;"
            fout.write(f"<li><p><a href='{url}' style='{style}'>{url}</a></p></li>\n")

            # print(f"{f.status:4d} {url}")

        fout.write(f"\n</ul>\n")

fout.write('</body>\n</html>\n')
fout.close()
