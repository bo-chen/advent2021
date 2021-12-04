import math
import numpy as np
import os
import re
import sys

ls = []
with open('./input.txt') as fp:
    for line in fp:
        ls.append(line.strip())


def filter(nums, filter):

    i = 0
    while True:
        t =0
        count =0
        for l in nums:
            if l[i] == '1':
                count += 1
            t += 1

        if count >= t / 2:
            most = "1"
            least = "0"
        else:
            most = "0"
            least = "1"

        if filter == "most":
            f = most
        elif filter == "least":
            f = least

        nnums = []
        for n in nums:
            if n[i] == f:
                nnums.append(n)

        if len(nnums) == 1:
            return nnums[0]
        nums = nnums
        i += 1


g =filter(ls, "most")
e =filter(ls, "least")
print(g)
print(int("".join(g), base=2))
print(e)
print(int("".join(e), base=2))


print(int("".join(g), base=2)
     * int("".join(e), base=2))




