# 백준 9655 - 돌 게임

N = int(input())

dp = [False] * (N + 4)
dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, N + 1) :
    dp[i] = not dp[i - 1] or not dp[i - 3]

if dp[N] : 
    print("SK")
else :
    print("CY")