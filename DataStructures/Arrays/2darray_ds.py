import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max = -9 * 9
# print('Maxmin=' + str(max))
for i in range(0, 4):
    for j in range(0, 4):
        temp = 0
        # print()
        for x in range(j, j + 3):
            # print()
            for y in range(i, i + 3):
                if not ((x - j == 1) and ((y - i == 0) or (y - i == 2))):
                    temp += arr[x][y]
                    # print(arr[x][y], end=' ')
                # else:
                #     print(' ', end=' ')
        if(temp > max):
            max = temp
print(max)
