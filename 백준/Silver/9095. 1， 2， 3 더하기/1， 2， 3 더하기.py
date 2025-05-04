# 백준 9095 - 1, 2, 3 더하기
# 분류 : 코딩 테스트 준비 - 기초 ) 브루트 포스

T = int(input())
dp = [0] * 12
dp[1] = [1]
dp[2] = [2]
dp[3] = [4]

for i in range(4, 12) :
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(T) :
    n = int(input())
    print(sum(dp[n]))