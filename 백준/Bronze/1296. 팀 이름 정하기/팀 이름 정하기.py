# 백준 1296 - 팀 이름 정하기

import sys

def score(L, O, V, E):
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

input = sys.stdin.readline

base = input().strip()
L0 = base.count('L')
O0 = base.count('O')
V0 = base.count('V')
E0 = base.count('E')

n = int(input())
best_name = None
best_score = -1

for _ in range(n):
    name = input().strip()
    L = L0 + name.count('L')
    O = O0 + name.count('O')
    V = V0 + name.count('V')
    E = E0 + name.count('E')
    s = score(L, O, V, E)

    if s > best_score or (s == best_score and (best_name is None or name < best_name)):
        best_score = s
        best_name = name

print(best_name)