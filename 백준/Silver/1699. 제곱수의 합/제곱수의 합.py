# 백준 1699 - 제곱수의 합
# 분류 : 다이나믹 프로그래밍

N = int(input())

D = [0] * (N + 1)

for i in range(1, N + 1) :
    if (i ** 0.5).is_integer() :
        D[i] = 1
        continue

    D[i] = 1e9
    j = 1
    while j * j <= i / 2 :
        D[i] = min(D[i], 1 + D[i - j * j])
        j += 1
print(D[N])