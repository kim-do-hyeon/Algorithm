# 백준 14003 - 가장 긴 증가하는 부분 수열 5
# 분류 : 이분 탐색

import sys
import bisect

input = sys.stdin.readline

A = int(input())
S = list(map(int, input().split()))

dp = []
lis_indices = []
parent = [-1] * A

for i in range(A) :
    num = S[i]
    pos = bisect.bisect_left(dp, num)

    if pos == len(dp) :
        dp.append(num)
        if lis_indices :
            parent[i] = lis_indices[-1]
        lis_indices.append(i)
    else :
        dp[pos] = num
        lis_indices[pos] = i
        if pos > 0 :
            parent[i] = lis_indices[pos - 1]

lis_length = len(dp)
print(lis_length)

lis_sequence = []
cur_index = lis_indices[-1]

while cur_index != -1 :
    lis_sequence.append(S[cur_index])
    cur_index = parent[cur_index]   

print(*reversed(lis_sequence))