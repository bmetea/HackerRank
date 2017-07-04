#!/bin/python3

import sys

def bonAppetit(k,n,  b, ar):
    actual =(sum(ar)-ar[n])/2
    if (b != actual):
        return int(b-actual)
    else:
        return('Bon Appetit')

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)