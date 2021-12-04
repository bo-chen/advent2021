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

def readf():
    boards = []
    with open('./input.txt') as fp:
        rs = fp.readline().strip().split(",")
        print(rs)
        fp.readline()

        while True:
            board = []
            for i in range(5):
                l = fp.readline()
                if not l:
                    return boards
                ns = l.strip().split()
                ss = list(map(lambda s: {"v" : s, "m": False}, ns))
                board.append(ss)

            boards.append(board)
            l = fp.readline()
            if not l:
                return [rs, boards]

# returns board if won, else None
def checkboards(boards):
    ind = 0
    for b in boards:
        for ri in range(5):
            won = True
            for i in range(5):
                if b[ri][i]["m"] == False:
                    won = False
            if won:
                return [ind, b]

        for ci in range(5):
            won = True
            for i in range(5):
                if b[i][ci]["m"] == False:
                    won = False
            if won:
                return [ind, b]

        ind += 1
    return None

def mark(boards, v):
    for b in boards:
        for i in range(5):
            for j in range(5):
                if b[i][j]["v"] == v:
                    b[i][j]["m"] = True


[rs, boards] = readf()

b = None
finalv = None
for v in rs:
    mark(boards, v)
    r = checkboards(boards)
    while r is not None:
        [i, b] = r
        # print("i " +  str(i))
        boards.pop(i)
        if len(boards) == 0:
            finalv = v
            break
        r = checkboards(boards)

pm(b)

t = 0
for i in range(5):
    for j in range(5):
        if b[i][j]["m"] == False:
            t += int(b[i][j]["v"])

print(t * int(finalv))
