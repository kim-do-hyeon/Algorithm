# 백준 12738 - 가장 긴 증가하는 부분 수열 3
# 분류 : 이진탐색

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

dp = [A[0]]

for i in range(1, N) :
    if dp[-1] < A[i] :
        dp.append(A[i])
    else :
        left, right = 0, len(dp) - 1
        while left < right :
            mid = (left + right) // 2
            if dp[mid] < A[i] :
                left = mid + 1
            else :
                right = mid
        dp[right] = A[i]

print(len(dp))