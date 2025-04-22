# 백준 2501 - 약수 구하기
# 단계별로 풀어보기 - 9 - 약수, 배수와 소수
# 분류 : 수학

def prime(N) :
    primeNumber = []
    for i in range(1, N + 1) :
        if N % i == 0 :
            primeNumber.append(i)
    return primeNumber

N, K = map(int, input().split())
primeNumber = prime(N)
if K > len(primeNumber) :
    print(0)
else :
    print(primeNumber[K - 1])
