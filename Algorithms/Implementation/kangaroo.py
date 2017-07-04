#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    start_diff = x2-x1
    v_diff = v1 -v2
    if (v_diff>0 and (start_diff % v_diff == 0)):
        return 'YES'
    else:
        return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)




