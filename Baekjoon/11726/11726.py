# 백준 11726 - 2 x n 타일링
# 분류 : 다이나믹 프로그래밍

N = int(input())
mod = 10007

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod

print(dp[N])