# 백준 17944 - 퐁당퐁당 1
# 분류 : 구현, 시뮬레이션

N, T = map(int, input().split())

A = []
for i in range(1, 2 * N + 1) :
    A.append(i)
for i in range(2 * N - 1, 1, -1) :
    A.append(i)

T -= 1
T %= (4 * N - 2)

print(A[T])