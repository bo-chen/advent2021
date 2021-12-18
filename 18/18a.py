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

class Node:
    parent = None
    value = None
    left = None
    right = None
    isr = False
    isl = False

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

def readn(s, parent, isl, isr):
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
        n = Node()
        n.parent = parent
        n.isl = isl
        n.isr = isr
        n.left = readn(lst, n, True, False)
        n.right = readn(rst, n, False, True)
        return n
    else:
        n = Node()
        n.parent = parent
        n.isl = isl
        n.isr = isr
        n.value = int(s)
        return n

def ps(n):
    if n is None:
        return "None"
    if n.value is not None:
        return str(n.value)
    return "[" + ps(n.left) + "," + ps(n.right) + "]"

def addl(n, v):
    if n.value is not None:
        n.value += v
    else:
        addl(n.left, v)

def addr(n, v):
    if n.value is not None:
        n.value += v
    else:
        addr(n.right, v)

def expn(x, lev):
    #print(ps(x))
    c = x
    if c.value is not None:
        return False

    if lev == 3 and c.left.value is None:
        if c.right.value is None:
            addl(c.right, c.left.right.value)
        else:
            c.right.value += c.left.right.value
        p = c
        while p.parent:
            if p.isl:
                p = p.parent
            else:
                addr(p.parent.left, c.left.left.value)
                break
        c.left.value = 0
        c.left.left = None
        c.left.right = None
        return True
    elif lev == 3 and c.right.value is None:
        if c.left.value is None:
            addr(c.left, c.right.left.value)
        else:
            c.left.value += c.right.left.value
        p = c
        while p.parent:
            if p.isr:
                p = p.parent
            else:
                addl(p.parent.right, c.right.right.value)
                break
        c.right.value = 0
        c.right.left = None
        c.right.right = None
        return True

    a = expn(c.left, lev+1)
    if a:
        return True
    return expn(c.right, lev+1)

def splitn(n):
    if n.value is not None:
        if n.value >= 10:
            n.left = readn(str(math.floor(n.value / 2)),n,True,False)
            n.right = readn(str(math.ceil(n.value / 2)),n,False,True)
            n.value = None
            return True
        return False
    r = splitn(n.left)
    if r:
        return True
    return splitn(n.right)

def addn(x, y):
    n = Node()
    x.parent = n
    x.isl = True
    y.parent = n
    y.isr = True
    n.left = x
    n.right = y

    return n

def reducen(n):
    keep = True
    while keep:
        # print(ps(n))
        keep = False
        keep = keep or expn(n, 0)
        if keep:
            continue
        keep = keep or splitn(n)

def magn(n):
    if n.value is not None:
        return n.value
    else:
        return magn(n.left) * 3 + magn(n.right) * 2

tsn = None
for l in ls:
    if tsn is None:
        tsn = readn(l, None, None, None)
    else:
        nn = readn(l, None, None, None)
        tsn = addn(tsn, nn)
        reducen(tsn)

print(magn(tsn))

'''
# tsn = readn(ls[0])
x = readn("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", None, None, None)
y = readn("[1,1]", None, None, None)

print(ps(x))
print(magn(x))
'''
