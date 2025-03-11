# 백준 1269 - 대칭 차집합
# 분류 : 집합

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = set(A)

count = 0
for b in B :
    if b in A :
        count += 1

print(N + M - 2 * count)
