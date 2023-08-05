#!/usr/bin/env python3

# find all oldfigs actually used, and delete the rest
# assumes an oldfigs folder exists
#
# searches for usage in kapitelbild and includegraphics

import re
import sys
from pathlib import Path

# path of folder holding the old figures from Springer
oldfigs_path = Path("oldfigs")

# get list of all the old figures
oldfigs = [str(f.stem) for f in oldfigs_path.iterdir()]


# re for the figure
figure = re.compile(r'''\\includegraphics(?:\[[^]]*\])?{([^}]+)}|\\kapitelbild{([^}]+)}''')

# for each figure actually used in the chapter, remove it from the list
with open(sys.argv[1], 'r') as f:
    for fig in figure.findall(f.read()):

        fig = [f for f in fig if f != ''][0]
        if fig in oldfigs:
            print('keeping ', fig)
            oldfigs.remove(fig)

# all those that are left in the list are unneeded, nuke them
for file in oldfigs:
    for f in oldfigs_path.glob(f"{file}.*"):
        print('unlinking', f)
        f.unlink()

