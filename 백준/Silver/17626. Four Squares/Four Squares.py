# 백준 17626 - Four Squares
# 분류 : DP

''' 시간 초과 '''
# n = int(input())

# dp = [0] * (n + 1)

# for i in range(1, n + 1) :
#     dp[i] = i
#     j = 1
#     while j ** 2 <= i :
#         dp[i] = min(dp[i], dp[i - j ** 2] + 1)
#         j += 1

# print(dp[n])


''' 시간 초과 '''
# N = int(input())

# dp = [4] * (N + 1) # 최악의 경우인 4로 초기화

# for i in range(1, N + 1) :
#     if (i ** 0.5).is_integer() :
#         dp[i] = 1
#         continue
    
#     for j in range(1, N) :
#         if j * j > i :
#             break
#         dp[i] = min(dp[i], 1 + dp[i - j * j])

# print(dp[N])


''' 시간 초과 '''
# import sys
# input = sys.stdin.read

# N = int(input())

# # 초기화
# dp = [i for i in range(N + 1)]  # 최악의 경우 모든 숫자가 1^2로만 이루어진 경우

# for i in range(1, N + 1):
#     j = 1
#     while j * j <= i:
#         dp[i] = min(dp[i], dp[i - j * j] + 1)
#         j += 1

# print(dp[N])

import sys
import math

def four_squares(n):
    # Case 1: n이 제곱수라면 1
    if math.isqrt(n) ** 2 == n:
        return 1

    # Case 2: n이 두 개의 제곱수 합이면 2
    for i in range(1, math.isqrt(n) + 1):
        if math.isqrt(n - i * i) ** 2 == (n - i * i):
            return 2

    # Case 3: n이 세 개의 제곱수 합이면 3
    for i in range(1, math.isqrt(n) + 1):
        for j in range(1, math.isqrt(n - i * i) + 1):
            if math.isqrt(n - i * i - j * j) ** 2 == (n - i * i - j * j):
                return 3

    # Case 4: 위 세 가지 경우가 아니라면 4
    return 4


n = int(input())
print(four_squares(n))
