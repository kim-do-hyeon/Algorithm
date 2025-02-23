# 백준 10844 - 쉬운 계단 수
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())
mod = 1000000000

dp = [[0] * (N + 1) for _ in range(10)] # 10 x (n + 1) 배열

dp[0][1] = 0
for i in range(1, 10) :
    dp[i][1] = 1

for i in range(2, N + 1) :
    for j in range(10) :
        dp[j][i] = 0

        if j > 0 :
            dp[j][i] += dp[j - 1][i - 1]
            dp[j][i] %= mod
        if j < 9 :
            dp[j][i] += dp[j + 1][i - 1]
            dp[j][i] %= mod

answer = 0
for i in range(10) :
    answer += dp[i][N]
    answer %= mod

print(answer)
