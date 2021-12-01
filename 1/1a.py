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
t = 0
for i in ls:
    if last == None or i <= last:
        1 + 1
    else:
        t += 1
    last = i

print(t)


