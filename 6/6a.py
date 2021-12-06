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


freqs = [0] * 9
print(freqs)
for v in ls[0].split(","):
    freqs[int(v)] += 1

print(freqs)

def sim_day(freqs):
    nf = [0] * 9
    # 7..1
    for n in range(7,0,-1):
        nf[n] = freqs[n + 1]
    # 0
    nf[0] = freqs[1]
    nf[6] = freqs[0] + nf[6]
    nf[8] = freqs[0]
    return nf

for i in range(256):
    freqs = sim_day(freqs)
    print(freqs)

t = 0
for i in range(9):
    t += freqs[i]

print(t)

