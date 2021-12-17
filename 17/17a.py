import math
import numpy as np
import os
import re
import sys

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

# x=241..273, y=-97..-63
minx = 241
maxx = 273
miny = -97
maxy = -63

def step(p, v):
    p[0] += v[0]
    p[1] += v[1]

    if v[0] < 0:
        v[0] += 1
    elif v[0] > 0:
        v[0] -= 1

    v[1] -= 1

    return (p, v)

def inTarget(p):
    return p[0] >= minx and p[0] <= maxx and p[1] >= miny and p[1] <= maxy

def project(v):
    p=[0,0]

    maxh = 0

    while True:
        if p[1] > maxh:
            maxh = p[1]

        if inTarget(p):
            return maxh

        if p[0] > maxx or p[1] < miny or v[0] == 0 and p[0] < minx:
            return -1

        (p, v) = step(p, v)


hs = 0
minvx = int(math.sqrt(maxx * 2)) -1

for x in range(minvx, maxx + 1):
    for y in range(miny -1, 1000):
        h = project([x,y])
        if h >= 0:
            hs += 1

print(hs)

