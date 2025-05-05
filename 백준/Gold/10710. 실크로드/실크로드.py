# 백준 10710 - 실크로드
# 분류 : 다이나믹 프로그래밍

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[1e9] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(1, M + 1) :
    for j in range(0, N + 1) :
        dp[i][j] = dp[i - 1][j]

        if j > 0 :
            dp[i][j] = min(
                dp[i][j],
                dp[i - 1][j - 1] + C[i - 1] * D[j - 1]
            )

print(dp[M][N])