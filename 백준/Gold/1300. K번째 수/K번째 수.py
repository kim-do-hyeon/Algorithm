# 백준 1300 - K번째 수
# 분류 : 이분 탐색

N = int(input())
K = int(input())

low = 1
high = N * N
answer = -1

while low <= high :
    mid = (low + high) // 2

    count = 0
    for i in range(1, N + 1) :
        # i, 2 * i, 3 *i, ..., N * i
        count += min(N, (mid - 1) // i)
    
    if count < K :
        answer = mid
        low = mid + 1
    else :
        high = mid - 1

print(answer)