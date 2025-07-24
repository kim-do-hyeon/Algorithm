# 백준 17103 - 골드바흐 파티션
# 분류 : 약수

import sys
input = sys.stdin.readline

primes = [True for _ in range(1000001)]

for i in range(2, 1000001) :
    if primes[i] == True :
        for j in range(i * 2, 1000001, i) :
            primes[j] = False

T = int(input())
for i in range(T) :
    N = int(input())
    partition = 0
    for num in range(2, N // 2 + 1) :
        if primes[num] and primes[N - num] :
            partition += 1

    print(partition)