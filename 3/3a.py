import math
import numpy as np
import os
import re
import sys

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())

t =0
counts = [0] * len(ls[0])
for l in ls:
    i = 0
    for c in l:
        if c == '1':
            counts[i] += 1
        i += 1
    t += 1

g = [0] * len(ls[0])
e = [0] * len(ls[0])
i = 0
for count in counts:
    if count < t / 2:
        g[i] = "1"
        e[i] = "0"
    else:
        g[i] = "0"
        e[i] = "1"
    i += 1

print("".join(g))


print("".join(e))
print(int("".join(g), base=2)
     * int("".join(e), base=2))




