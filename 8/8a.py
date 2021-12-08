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

rows = []
for l in ls:
    [psstr,osstr] = l.split(" | ")
    ps = psstr.split()
    os = osstr.split()
    rows.append({"ps": ps, "os": os})

t = 0
for r in rows:
    ones = None
    fours = None
    sevens = None

    # 1 has len 2
    # 4 has len 4
    # 7 has len 3
    # 8 has len 7
    # 9 diff 4 has len 2
    # 0 diff 1 has len 4
    # 6 diff 1 has len 5
    # 3 diff 1 has len 3
    # 2 diff 4 has len 3
    # 5 diff 4 has len 2

    trans = dict()
    inv = dict()

    for o in r["os"] + r["ps"]:
        le = len(o.strip())
        s = set(o.strip())
        cs = list(o.strip())
        cs.sort()
        cs = "".join(cs)
        if le == 2:
            trans[cs] = "1"
            inv[1] = s
        elif le == 4:
            trans[cs] = "4"
            inv[4] = s
        elif le == 3:
            trans[cs] = "7"
            inv[7] = s
        elif le == 7:
            trans[cs] = "8"
            inv[8] = s

    for o in r["os"] + r["ps"]:
        le = len(o.strip())
        s = set(o.strip())
        cs = list(o.strip())
        cs.sort()
        cs = "".join(cs)
        if le == 6:
            if len(s.difference(inv[4])) == 2:
                trans[cs] = "9"
            elif len(s.difference(inv[1])) == 4:
                trans[cs] = "0"
            elif len(s.difference(inv[1])) == 5:
                trans[cs] = "6"
        elif le == 5:
            if len(s.difference(inv[1])) == 3:
                trans[cs] = "3"
            elif len(s.difference(inv[4])) == 3:
                trans[cs] = "2"
            elif len(s.difference(inv[4])) == 2:
                trans[cs] = "5"

    dig = ""

    for o in r["os"]:
        cs = list(o.strip())
        cs.sort()
        cs = "".join(cs)

        dig += trans[cs]

    t += int(dig)

print(t)
