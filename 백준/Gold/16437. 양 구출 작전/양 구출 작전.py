# 백준 16437 - 양 구출 작전
# 분류 : 다이나믹 프로그래밍

import sys
sys.setrecursionlimit(12345678)

N = int(input())
A = [0] * N
child = [[] for _ in range(N)]

for i in range(1, N) :
    t, a, p = input().split()
    a = int(a)
    p = int(p) - 1
    if t == 'S' :
        A[i] = a
    else :
        A[i] -= a
    
    child[p].append(i)

D = [0] * N

def dfs(u) :
    D[u] = A[u]
    for v in child[u] :
        dfs(v)
        D[u] += D[v]
    
    if D[u] < 0 :
        D[u] = 0

dfs(0)
print(D[0])
    