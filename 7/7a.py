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

vs = map(lambda x: int(x), line.split(","))
vs = list(vs)

s = 0
for v in vs:
    s += v

print(s)
print(len(vs))

def fuel(vs, x):
    t = 0
    for v in vs:
        d = abs(v-x)
        t += d * (d +1) / 2
    return t

prevf = 9999999999999999
x = 0
while True:
    f = fuel(vs, x)
    if f > prevf:
        break
    x += 1
    prevf = f

print(x)
print(prevf)
