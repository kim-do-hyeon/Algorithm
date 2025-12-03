# [골드 4] 백준 1083 - 소트

import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
S = int(input())

for i in range(N) :
    if not S :
        break
    max_value = max(array[i:i + S + 1])
    max_index = array.index(max_value)
    while max_index != i and S :
        array[max_index], array[max_index - 1] = array[max_index - 1], array[max_index]
        max_index -= 1
        S -= 1

print(*array)