# 백준 9506 - 약수들의 합
# 문제집 : Python 배우기 (1 ~ 50)

def isPrime(N) :
    data = []
    for i in range(1, N) :
        if N % i == 0 :
            data.append(i)
    return data

while True :
    N = int(input())
    if N == -1 :
        break
    primeNumber = isPrime(N)
    if sum(primeNumber) == N :
        print(f"{N} =", end = " ")
        for i in range(len(primeNumber) - 1) :
            print(primeNumber[i], end = " + ")
        print(primeNumber[-1])
    else :
        print(f"{N} is NOT perfect.")