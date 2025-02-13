# 백준 2110 - 공유기 설치
# 분류 : 이분 탐색

import sys
input = sys.stdin.readline
N, C = map(int, input().split())

x = [int(input()) for _ in range(N)]

x.sort()

start, end = 1, x[-1] - x[0]
result = 0

while start <= end :
    mid = (start + end) // 2
    value = x[0]
    count = 1

    for i in range(1, N) :
        if x[i] >= value + mid :
            value = x[i]
            count += 1
            if count >= C :
                break
    if count >= C :
        start = mid + 1
        result = mid
    else :
        end = mid - 1
print(result)