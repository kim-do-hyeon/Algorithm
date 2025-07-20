# 백준 25214 - 크림 파스타
# 분류 : 다이나믹 프로그래밍

N = int(input())
A = list(map(int, input().split()))

D = [0] * N
E = [0] * N

D[0] = A[0]
for i in range(1, N) :
    D[i] = min(D[i - 1], A[i])

E[0] = 0
for i in range(1, N) :
    E[i] = max(E[i - 1], A[i] - D[i])

print(*E)