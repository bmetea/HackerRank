#!/bin/python3

import sys

s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


def calculate(fruits, tree_pos):
    counter = 0
    for fruit_pos in fruits:
        if (s <= tree_pos + fruit_pos <= t):
            counter += 1
    print(counter)


calculate(apple, a)
calculate(orange, b)



