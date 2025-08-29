# 백준 1912 - 연속합
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

for i in range(1, N) :
    A[i] = max(A[i], A[i] + A[i - 1])

print(max(A))