import sys
input = sys.stdin.readline

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [INF] * (1 << N)
dp[0] = 0  # 아무것도 할당되지 않은 상태

for mask in range(1 << N):
    k = bin(mask).count('1')  # 현재 몇 명까지 할당되었는지
    if k >= N:
        continue
    for j in range(N):
        if not (mask & (1 << j)):
            dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + D[k][j])

print(dp[(1 << N) - 1])