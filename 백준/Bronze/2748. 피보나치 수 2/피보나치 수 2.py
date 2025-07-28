# 백준 2748 - 피보나치 수 2

N = int(input())
dp = [0] * (N + 1)
if N > 0 :
    dp[1] = 1

for i in range(2, N + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])