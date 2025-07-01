import sys
sys.setrecursionlimit(10 ** 7)

N, P, Q, X, Y = map(int, input().split())

cache = {}

def dp(n):
    if n <= 0:
        return 1
    if n in cache:
        return cache[n]
    
    # n // P - X 와 n // Q - Y 로 int 계산
    cache[n] = dp(n // P - X) + dp(n // Q - Y)
    return cache[n]

print(dp(N))