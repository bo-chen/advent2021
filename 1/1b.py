import math
import numpy as np
import os
import re
import sys

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(int(line.strip()))


last = None
pp = None
p = None
t = 0
for i in ls:
    if pp != None and p != None:
        w = pp + p + i
        if last != None and w > last:
            t += 1
        last = w
    pp = p
    p = i

print(t)
