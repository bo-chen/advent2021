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

segs = []

for l in ls:
    ws = l.split()
    [x1, y1] = ws[0].split(",")
    [x2, y2] = ws[2].split(",")

    segs.append({"x1":int(x1), "x2":int(x2), "y1":int(y1), "y2":int(y2)})

print(len(segs))

# sparse matrix [x,y] : v
board = dict()

sign = lambda x: x and (1, -1)[x<0]
def add_seg(board, seg):
    dx = seg["x2"] - seg["x1"]
    dy = seg["y2"] - seg["y1"]
    ux = sign(dx)
    uy = sign(dy)
    its = 0
    if dx == 0:
        its = dy * uy + 1
    else:
        its = dx * ux + 1

    for i in range(its):
        coord = [seg["x1"] + i * ux, seg["y1"] + i * uy]
        cs = f'{coord[0]},{coord[1]}'
        if cs in board:
            board[cs] += 1
        else:
            board[cs] = 1

for s in segs:
    add_seg(board, s)

t = 0
for v in board.values():
    if v >= 2:
        t += 1

print(t)

