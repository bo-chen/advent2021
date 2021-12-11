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

b = []
for l in ls:
    nr = []
    for c in l:
        nr.append(int(c))
    b.append(nr)

h = len(b)
w = len(b[0])

def cstr(i, j):
    return str(i) + "," + str(j)

def incr(b, i, j, ms):
    cs = cstr(i,j)
    if i < 0 or i >= h or j < 0 or j >= w or cs in ms:
        return

    b[i][j] += 1
    if b[i][j] > 9:
        b[i][j] = 0
        ms.add(cs)
        incr(b, i-1, j-1,ms)
        incr(b, i-1, j,ms)
        incr(b, i-1, j+1,ms)
        incr(b, i, j-1,ms)
        incr(b, i, j+1,ms)
        incr(b, i+1, j-1,ms)
        incr(b, i+1, j,ms)
        incr(b, i+1, j+1,ms)
        return

    return

def step(b):
    ms = set()
    for i in range(h):
        for j in range (w):
            incr(b, i, j, ms)
    return len(ms)

tt = 0
for s in range(100000000):
    t = step(b)
    if t == w*h:
        print(s+1)
        break


