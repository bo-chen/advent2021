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


board = []
for l in ls:
    nr = []
    for c in list(l):
        nr.append(int(c))
    board.append(nr)


h = len(board)
w = len(board[0])

def cs(i, j):
    return str(i) + "," + str(j)


def cbasin(board, si, sj, m):
    s =cs(si,sj)
    if si < 0 or si >= h or sj < 0 or sj >= w or s  in m or board[si][sj] == 9:
        return 0
    m.add(s)
    return 1 + cbasin(board, si -1, sj, m) + cbasin(board, si +1, sj, m) +cbasin(board, si, sj -1, m) +cbasin(board, si, sj+1, m)



rl = 1
bs = []
for i in range(h):
    for j in range(w):
        c = board[i][j]
        if i > 0 and board[i-1][j] <= c:
            continue
        if i < h - 1 and board[i+1][j] <= c:
            continue
        if j > 0 and board[i][j-1] <= c:
            continue
        if j < w - 1 and board[i][j+1] <= c:
            continue
        bs.append(cbasin(board, i, j, set()))

bs.sort(reverse=True)

print(bs[0] * bs[1] * bs[2])


