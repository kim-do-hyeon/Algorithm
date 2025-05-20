# 백준 1806 - 부분합

N, S = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
total = 0
min_length = N + 1

while True :
    if total >= S :
        min_length = min(min_length, end - start)
        total -= A[start]
        start += 1
    elif end == N :
        break
    else :
        total += A[end]
        end += 1

if min_length == N + 1 :
    print(0)
else :
    print(min_length)