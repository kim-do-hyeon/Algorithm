# 백준 28353 - 고양이 카페
# 분류 : 투포인터

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
start, end = 0, N - 1

count = 0
while start < end :
    if A[start] + A[end] <= K :
        count += 1
        start += 1
        end -= 1
    else :
        end -= 1

print(count)
