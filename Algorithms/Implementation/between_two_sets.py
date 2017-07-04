#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function
    count = 0
    low = max(a)
    high = min(b)
    for x in range(low, high+1):
        it_is = True
        for ai in a:
            if (x%ai!=0): it_is=False
        for bi in b:
            if (bi%x!=0): it_is=False
        # print(str(x) + ":" +str(it_is))
        if it_is : count+=1
    return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
