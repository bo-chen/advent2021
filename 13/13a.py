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

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

ds = dict()
def dk(x,y):
    return y * 1000000 + x

folds = []

for l in ls:
    if l == "":
        continue
    if l[0:11] == "fold along ":
        [d, v] = l[11:].split("=")
        folds.append([d,int(v)])
    else:
        [xst, yst] = l.split(",")
        x = int(xst)
        y = int(yst)
        ds[dk(x,y)] = [x,y]

def foldx(cds, fx):
    nds = dict()
    for [x, y] in cds.values():
        nx = x
        if x > fx:
            nx = fx + fx - x
        nds[dk(nx, y)] = [nx, y]
    return nds

def foldy(cds, fy):
    nds = dict()
    for [x, y] in cds.values():
        ny = y
        if y > fy:
            ny = fy + fy - y
        nds[dk(x, ny)] = [x, ny]
    return nds

for [d, v] in folds:
    if d == "x":
        ds = foldx(ds, v)
    else:
        ds = foldy(ds, v)
    print(len(ds))

print("")
for y in range(10):
    for x in range(100):
        if dk(x,y) in ds:
            print("$",end="")
        else:
            print(" ",end="")
    print("")
