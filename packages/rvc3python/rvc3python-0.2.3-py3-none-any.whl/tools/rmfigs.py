#!/usr/bin/env python3

# find all genfigs actually used, and delete the rest
# assumes an genfigs folder exists
#
# searches for usage in kapitelbild and includegraphics

import re
import sys
from pathlib import Path

# path of folder holding the Python generated figures
figs_path = Path(sys.argv[1])

# get list of all the figures
figs = [f for f in figs_path.iterdir()]
figdict = dict()
for fig in figs:
    if fig.stem in figdict:
        print('duplicate', figdict[fig.stem], fig)
    else:
        figdict[fig.stem] = fig

# print(figdict)
# re for the figure
includegraphics = re.compile(r'''\\includegraphics(?:\[[^]]*\])?{([^}]+)}''')

# for each figure actually used in the chapter, remove it from the list
with open(sys.argv[2], 'r') as f:
    for fig in includegraphics.findall(f.read()):
        if '/' in fig:
            fig = fig.split('/')[1]
        if '.' in fig:
            fig = fig.split('.')[0]
        # print('using ', fig)

        if fig in figdict:
            # print('keeping ', fig)
            del figdict[fig]

            # all = list(figs_path.glob(fig + ".*"))
            # if len(all) > 1:
            #     print("multiple versions: ", all)

# all those that are left in the list are unneeded, nuke them
for file in figs:
    for f in figs_path.glob(f"{file}.*"):
        print('unlinking', f)
        # f.unlink()

