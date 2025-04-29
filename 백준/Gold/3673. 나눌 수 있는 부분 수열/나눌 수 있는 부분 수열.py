# 백준 3673 - 나눌 수 있는 부분 수열
# 분류 : 누적 합

T = int(input())

for _ in range(T) :
    D, N = map(int, input().split())
    A = list(map(int, input().split()))

    psum = [0] * N
    psum[0] = A[0]
    for i in range(1, N) :
        psum[i] = psum[i - 1] + A[i]
    
    answer = 0
    count = {}
    count[0] = 1 # psum[i] % D == 0 0~i
    for i in range(N) :
        if psum[i] % D not in count :
            count[psum[i] % D] = 0
        answer += count[psum[i] % D]
        count[psum[i] % D] += 1
    
    print(answer)