import math
import numpy as np
import os
import re
import sys
from queue import PriorityQueue

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

def wrap(x):
    while x > 9:
        x -= 9
    return x

def ingestonce(board, ls, o):
    for l in ls:
        nr = []
        for i in range(5):
            for c in l:
                nr.append(wrap(int(c) + i + o))
        board.append(nr)

for i in range(5):
    ingestonce(board, ls, i)

p = [0, 0]

h =len(board)
w =len(board[0])

def inbounds(x, y):
    return x >= 0 and x < w and y > 0 and y < h

def k(x,y):
    return str(x) + "," + str(y)

def search(board, p):
    done = set()
    q = PriorityQueue()
    q.put((0,p))
    done.add(k(p[0],p[1]))
    while True:
        o =q.get()
        (r, [x, y]) = o
        if x == w-1 and y == h-1:
            return r

        if inbounds(x+1, y) and k(x+1, y) not in done:
            nr = r + board[y][x+1]
            q.put((nr, [x+1,y]))
            done.add(k(x+1, y))
        if inbounds(x-1, y) and k(x-1, y) not in done:
            nr = r + board[y][x-1]
            q.put((nr, [x-1,y]))
            done.add(k(x-1, y))
        if inbounds(x, y-1) and k(x, y-1) not in done:
            nr = r + board[y-1][x]
            q.put((nr, [x,y-1]))
            done.add(k(x, y-1))
        if inbounds(x, y+1) and k(x, y+1) not in done:
            nr = r + board[y+1][x]
            q.put((nr, [x,y+1]))
            done.add(k(x, y+1))

    print("ended with end")


print(search(board,p))






