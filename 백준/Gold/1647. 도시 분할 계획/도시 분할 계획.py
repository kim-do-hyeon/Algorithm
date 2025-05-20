# 백준 1647 - 도시 분할 계획

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G = []
for i in range(M) :
    A, B, C = map(int, input().split())
    G.append((C, A, B))

G.sort()

parent = [i for i in range(N + 1)]

def get_parent(x) :
    if parent[x] == x :
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b) :
    a = get_parent(a)
    b = get_parent(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def same_parent(a, b) :
    return get_parent(a) == get_parent(b)

total_cost = 0
max_edge = 0

for cost, a, b in G :
    if not same_parent(a, b) :
        union_parent(a, b)
        total_cost += cost
        max_edge = cost

print(total_cost - max_edge)