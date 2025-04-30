# 백준 10211 - Maximum Subarray
# 분류 : 누적합

T = int(input())
for _ in range(T) :
    N = int(input())
    X = list(map(int, input().split()))

    psum = [0] * N
    psum[0] = X[0]
    for i in range(1, N) :
        psum[i] = psum[i - 1] + X[i]

    max_sum = -1e9
    for i in range(N) :
        for j in range(i, N) :
            range_sum = psum[j]
            if i > 0 :
                range_sum -= psum[i - 1]

            if max_sum < range_sum :
                max_sum = range_sum
    
    print(max_sum)