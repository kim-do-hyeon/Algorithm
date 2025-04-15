# 백준 23253 - 자료구조는 정말 최고야
# 분류 : 구현

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

possible = True
for _ in range(M) :
    K = int(input())
    A = list(map(int, input().split()))

    for i in range(1, len(A)) :
        if A[i - 1] < A[i] :
            possible = False
            break

if possible :
    print("Yes")
else :
    print("No")