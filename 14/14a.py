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

template = ls[0]

ls = ls[2:]

rs = dict()
for l in ls:
    [k, v] = l.split(" -> ")
    rs[k] = v

def count_ps(template):
    pf = dict()
    for i in range(len(template) - 1):
        p = template[i:i+2]
        if p in pf:
            pf[p] += 1
        else:
            pf[p] = 1
    return pf

def fstep(pf,rs):
    npf = dict()
    for k in pf:
        v = rs[k]

        p = k[0] + v
        if p in npf:
            npf[p] += pf[k]
        else:
            npf[p] = pf[k]

        p = v + k[1]
        if p in npf:
            npf[p] += pf[k]
        else:
            npf[p] = pf[k]

    return npf

pf = count_ps(template)

for i in range(40):
    pf = fstep(pf, rs)

fcount = dict()
fcount[template[0]] = 1
fcount[template[-1]] = 1

for p in pf:
    if p[0] in fcount:
        fcount[p[0]] += pf[p]
    else:
        fcount[p[0]] = pf[p]

    if p[1] in fcount:
        fcount[p[1]] += pf[p]
    else:
        fcount[p[1]] = pf[p]


mao = 0
mio = fcount[template[0]]

for k in fcount:
    if fcount[k] > mao:
        mao = fcount[k]
    if fcount[k] < mio:
        mio = fcount[k]

print(mao /2 - mio /2)
