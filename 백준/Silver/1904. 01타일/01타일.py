# 백준 1904 - 01타일
# 분류 : 다이나믹 프로그래밍

N = int(input())

mod = 15746

D = [0] * 1000001

D[1] = 1
D[2] = 2

for i in range(3, N + 1) :
    D[i] = D[i - 1] + D[i - 2]
    D[i] %= mod

print(D[N])