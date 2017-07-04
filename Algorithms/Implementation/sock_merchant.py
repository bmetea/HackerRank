#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    total = 0
    set_socks = set(ar)
    for color in set_socks:
        total+=ar.count(color)//2
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)