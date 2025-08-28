# 백준 11052 - 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1) :
    best = 0
    for k in range(1, i + 1) :
        cand = dp[i - k] + P[k]
        if cand > best :
            best = cand
    dp[i] = best

print(dp[N])