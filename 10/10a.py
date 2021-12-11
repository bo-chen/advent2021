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

pt = {")" : "(", "]": "[", "}": "{",">": "<"}
ev = {")" : 3, "]": 57, "}": 1197,">": 25137}
iv = {"(" : 1, "[": 2, "{": 3,"<": 4}

et = 0
lts = []
for l in ls:
    st = []
    good = True
    for c in l:
        if c in pt.values():
            st.append(c)
        else:
            b = st.pop()
            if pt[c] != b:
                et += ev[c]
                good = False
                break

    if good and len(st) > 0:
        rst = st[::-1]
        lt = 0
        for c in rst:
            lt *= 5
            lt += iv[c]
        lts.append(lt)

lts.sort()



print(lts[int(len(lts)/2 - 0.5)])
