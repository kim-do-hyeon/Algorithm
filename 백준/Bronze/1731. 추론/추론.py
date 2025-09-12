# [브론즈 2] 백준 1731 - 추론

import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

calc_results = []
for i in range(1, len(A)) :
    calc_results.append(A[i] / A[i - 1])
    
if len(list(set(calc_results))) == 1 :
    print(int(A[-1] * (A[-1] / A[-2])))
else :
    print(int(A[-1] + (A[-1] - A[-2])))