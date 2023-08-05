# crop image

from machinevisiontoolbox import Image
import numpy as np
import sys
from pathlib import Path

def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

margin = 5

filename = Path(sys.argv[1])
a = Image(filename)

im = a.image

print(im.shape)

bg = []

for c in range(im.shape[1]):
    column = im[:,c,:]
    t = np.all(column == (255, 255, 255))
    bg.append(t)

c1 = bg.index(False)
c2 = rindex(bg, False)
c1 -= margin
if c1 < 0:
    c1 = 0
c2 += margin
if c2 >= im.shape[1]:
    c2 = im.shape[1]

bg = []
for r in range(im.shape[0]):
    row = im[r,:,:]
    t = np.all(row == (255, 255, 255))
    bg.append(t)

r1 = bg.index(False)
r2 = rindex(bg, False)
r1 -= margin
if r1 < 0:
    r1 = 0
r2 += margin
if r2 >= im.shape[0]:
    r2 = im.shape[0]

print(f"image: rows {r1}-{r2}, columns {c1}-{c2}")

out = Image(im[r1:r2, c1:c2, :])
outfile = filename.parent / (filename.stem + '-cropped' + filename.suffix)
out.write(str(outfile))