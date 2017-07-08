#!/bin/python3

import sys



def main():
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    print(n, m)
    edges = dict()
    for line in range(m):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        edges[u] = v
    print(edges)

if __name__ == "__main__":
  main()