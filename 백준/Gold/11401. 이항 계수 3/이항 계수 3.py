# 백준 11401 - 이항 계수 3
# 분류 : 수학
# 문제집 : 단기간 성장 - 4번

MOD = 1_000_000_007

def factorial(N) :
    result = [1] * (N + 1)
    for i in range(2, N + 1) :
        result[i] = result[i - 1] * i % MOD
    return result

def mod_inverse(X) :
    return pow(X, MOD - 2, MOD)

N, K = map(int, input().split())

fact = factorial(N)
numerator = fact[N]
denominator = fact[K] * fact[N - K] % MOD
result = numerator * mod_inverse(denominator) % MOD

print(result)
