import sys

nd = input().strip().split(' ')
# the number of integers
n = int(nd[0])
# the number of rotations
d = int(nd[1])
arr = [int(arr_t) for arr_t in input().strip().split(' ')]

print('********Solution************')


for i in range(d, n):
    print(arr[i], end=' ')
for j in range(0, d):
    print(arr[j], end=' ')
