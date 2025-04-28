# 백준 12865 - 평범한 배낭
# 분류 : 다이나믹 프로그래밍
# 문제집 : 단기간 성장 - 1번

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for w, v in items :
    for j in range(K, w - 1, -1) :
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])