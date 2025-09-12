# [브론즈 2] 백준 1773 - 폭죽쇼
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

check = [False] * (C + 1)
for i in A :
    for j in range(1, C // i + 1) :
        if (i * j) <= C and (i * j) != 0 :
            check[i * j] = True
print(check.count(True))