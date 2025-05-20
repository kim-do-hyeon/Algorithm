# 백준 1562 - 계산 수

MOD = 10 ** 9
N = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10) :
    dp[1][i][1 << i] = 1

for pos in range(1, N) :
    for digit in range(10) :
        for mask in range(1 << 10) :
            if dp[pos][digit][mask] == 0 :
                continue

            for next in [digit - 1, digit + 1] :
                if 0 <= next <= 9 :
                    next_mask = mask | (1 << next)
                    dp[pos + 1][next][next_mask] += dp[pos][digit][mask]
                    dp[pos + 1][next][next_mask] %= MOD

result = 0
for i in range(10) :
    result = (result + dp[N][i][(1 << 10) - 1]) % MOD

print(result)