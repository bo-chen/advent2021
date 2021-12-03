import math
import numpy as np
import os
import re
import sys

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())


f = 0
d = 0
aim = 0
for l in ls:
    ws = l.split(" ")
    v = int(ws[1])
    if ws[0] == "forward":
        f += v
        d += v * aim
    elif ws[0] == "down":
        aim += v
    elif ws[0] == "up":
        aim -= v

print(f*d)
