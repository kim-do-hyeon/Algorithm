# 백준 5176 - 대회 자리
import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K) :
    P, M = map(int, input().split())
    A = [int(input()) for _ in range(P)]
    B = [-1 for n in range(M)]
    result = 0
    for i in A :
        if B[i - 1] == -1 :
            B[i - 1] = 1
        else :
            result += 1
    print(result)