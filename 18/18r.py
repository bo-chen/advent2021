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

# Add v to leftmost number in string s
def addl(s, v):
    m = re.search(r"\d+", s)
    if m is None:
        return s
    (li, ri) = m.span()
    return s[:li] + str(int(s[li:ri]) + int(v))  + s[ri:]

def addr(s, v):
    m = None
    for m in re.finditer(r"\d+", s):
        pass
    if m is None:
        return s
    (li, ri) = m.span()
    return s[:li] + str(int(s[li:ri]) + int(v))  + s[ri:]

def expn(s):
    lev = 0
    for i in range(len(s)):
        if s[i] == "[":
            lev += 1
            if lev == 5:
                ri = i + 1 + s[i+1:].find("]")
                [ln, rn] = s[i+1:ri].split(",")
                return (True, addr(s[:i], ln) + "0" + addl(s[ri+1:], rn))
        elif s[i] == "]":
            lev -= 1
    return (False, None)

def splitn(s):
    for m in re.finditer(r"\d+", s):
        v = int(m.group())
        if v >= 10:
            return (True, s[:m.span()[0]] + "[" + str(math.floor(v/2)) + "," + str(math.ceil(v/2)) + "]" + s[m.span()[1]:])
    return (False, None)


def reducen(s):
    while True:
        (r, ns) = expn(s)
        if r:
            s = ns
            continue
        (r, ns) = splitn(s)
        if r:
            s = ns
            continue
        return s

def addn(x, y):
    return reducen("[" + x + "," + y + "]")

def magn(s):
    if s[0] == "[":
        lev = 0
        si = 1
        for i in range(1, len(s) -1):
            if s[i] == "," and lev == 0:
                si = i
                break
            if s[i] == "[":
                lev += 1
            if s[i] == "]":
                lev -= 1
        lst = s[1:si]
        rst = s[si + 1:-1]
        return 3 * magn(lst) + 2 * magn(rst)
    else:
        return int(s)

mm = 0
for i in range(len(ls)):
    for j in range(len(ls)):
        if i == j:
            continue
        m = magn(addn(ls[i], ls[j]))
        if m > mm:
            mm = m
print(mm)

