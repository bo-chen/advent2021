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

bs = []
for c in ls[0]:
    bs.append(format( int(c,16), "04b"))

bs = "".join(bs)

def readv(bs):
    nstr = []
    stop = False
    while not stop:
        if bs[0] == "0":
            stop = True
        nstr.append(bs[1:5])
        bs = bs[5:]

    x = int("".join(nstr), 2)

    return (bs, x)

def readp(bs):
    tv = 0
    version = int("".join(bs[0:3]), 2)
    tv += version
    type = int("".join(bs[3:6]), 2)
    bs = bs[6:]

    if type == 4:
        (bs, x) = readv(bs)
        vd = {"v":version, "t":type, "x":x}
        return (bs, vd, tv)

    lt = bs[0]
    bs = bs[1:]
    cs =[]

    if lt == "0":
        #then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
        npbits = int("".join(bs[0:15]), 2)
        bs = bs[15:]
        npbs = bs[0:npbits]
        bs = bs[npbits:]
        while len(npbs) > 5:
            (npbs, c, v) = readp(npbs)
            tv += v
            cs.append(c)
    else:
        # then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
        nps = int("".join(bs[0:11]), 2)
        bs = bs[11:]
        for i in range(nps):
            (bs, c, v) = readp(bs)
            tv += v
            cs.append(c)

    return (bs, {"t": type, "cs":cs, "v":version}, tv)

def calc(d):
    if d["t"] == 4:
        return d["x"]
    elif d["t"] == 0: #0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet,
        t = 0
        for c in d["cs"]:
            t += calc(c)
        return t
    elif d["t"] == 1: #1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        t = 1
        for c in d["cs"]:
            t *= calc(c)
        return t
    elif d["t"] == 2: #2 are minimum packets - their value is the minimum of the values of their sub-packets.
        t = 9999999999999999999999
        for c in d["cs"]:
            v = calc(c)
            if v < t:
                t = v
        return t
    elif d["t"] == 3: #3 are maximum packets - their value is the maximum of the values of their sub-packets.
        t = 0
        for c in d["cs"]:
            v = calc(c)
            if v > t:
                t = v
        return t
    elif d["t"] == 5: #5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if calc(d["cs"][0]) > calc(d["cs"][1]):
            return 1
        else:
            return 0
    elif d["t"] == 6: #6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if calc(d["cs"][0]) < calc(d["cs"][1]):
            return 1
        else:
            return 0
    elif d["t"] == 7: #7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
        if calc(d["cs"][0]) == calc(d["cs"][1]):
            return 1
        else:
            return 0

(bs, d, tv) = readp(bs)
print(calc(d))

