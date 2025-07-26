# 백준 1182 - 부분수열의 합

import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for i in range(1, N + 1) :
    combination = combinations(A, i)
    for x in combination :
        if sum(x) == S :
            answer += 1

print(answer)