# 백준 2749 - 피보나치 수 3

N = int(input())
MOD = 1000000

# # 시간초과 (1. 제귀 방식)
# def fibo(n : int) :
#     if n == 1 or n == 2 :
#         return 1
#     else :
#         return fibo(n - 1) + fibo(n - 2)

# print(fibo(N) % MOD)

# # 시간초과 (2. 이전값 + 전전값 더하는 방식)
# def fibo(n) :
#     a = 1
#     b = 1
#     if n == 1 or n == 2 :
#         return 1
#     for i in range(1, n) :
#         a, b = b, b + a
    
#     return a

# print(fibo(N) % MOD)

n = N % 1500000
fibo = [0] * (n + 2)
fibo[1] = 1

for i in range(2, n + 1) :
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % MOD

print(fibo[n])