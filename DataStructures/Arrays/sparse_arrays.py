import sys

strings = []
queries = []
# occurences = []


# get the number of strings from input
n_strings = int(input().strip())
# read strings from input
for i in range(n_strings):
    arr_s = input().strip()
    strings.append(arr_s)

# get the number of queries from input
n_queries = int(input().strip())
# get strings from input
for i in range(n_queries):
    arr_q = input().strip()
    queries.append(arr_q)


for x in queries:
    count = 0
    for y in strings:
        if x == y:
            count += 1
    print(count)
# print(occurences)
