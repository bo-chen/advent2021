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

rl = 0
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
        rl += 1 + c

print(rl)


