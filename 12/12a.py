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

def isSmall(s):
    return s.lower() == s and s != "start"

g = dict()
sns = set()
for l in ls:
    [s, e] = l.split("-")
    if isSmall(e):
        sns.add(e)

    if s in g:
        g[s].append(e)
    else:
        g[s] = [e]
    if e in g:
        g[e].append(s)
    else:
        g[e] = [s]


def travel(g, n, p, m, ssn):
    p = p + "-" + n
    if n == "end":
        ps = set()
        ps.add(p)
        return ps

    if isSmall(n):
        if n == ssn:
            ssn = "nomore"
        else:
            m.add(n)

    ps = set()
    for nn in g[n]:
        if nn == "start" or nn in m:
            continue
        ps = ps.union(travel(g, nn, str(p), set(m), ssn))
    return ps

tt = set()
for sn in sns:
    tt= tt.union(travel(g, "start", "", set(), sn))

print(len(tt))
