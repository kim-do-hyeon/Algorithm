# # 백준 17951 - 흩날리는 시험지 속에서 내 평점이 느껴진거야
# 분류 : 이분 탐색

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

low = 0
high = 20 * 100000
answer = -1

while low <= high :
    mid = (low + high) // 2

    sum = 0
    count = 0
    for i in range(N) :
        sum += A[i]
        if sum >= mid :
            count += 1
            sum = 0
    
    if count >= K :
        answer = mid
        low = mid + 1
    else :
        high = mid - 1

print(answer)