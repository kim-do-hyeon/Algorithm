# 백준 17404 - RGB거리 2
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

INF = 1e9

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

answer = INF

for first in range(3) :
    dp = [[INF] * 3 for _ in range(N)]

    dp[0][first] = A[0][first]

    for i in range(1, N) :
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + A[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + A[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + A[i][2]

    for last in range(3) :
        if last != first :
            answer = min(answer, dp[N - 1][last])

print(answer)
