# 백준 20159 - 동작 그만. 밑장 빼기냐?
# 분류 : 누적합

N = int(input())
A = list(map(int, input().split()))

psum0 = [0] * N
psum1 = [0] * N
psum0[0] = A[0]
psum1[0] = 0

for i in range(1, N) :
    if i % 2 == 0 :
        psum0[i] = psum0[i - 1] + A[i]
        psum1[i] = psum1[i - 1]
    else :
        psum0[i] = psum0[i - 1]
        psum1[i] = psum1[i - 1] + A[i]

def range_sum0(l, r) :
    if l > r :
        return 0
    ret = psum0[r]
    if l > 0 :
        ret -= psum0[l - 1]
    return ret

def range_sum1(l, r) :
    if l > r :
        return 0
    ret = psum1[r]
    if l > 0 :
        ret -= psum1[l - 1]
    return ret

answer = psum0[N - 1]
for i in range(N) :
    score = range_sum0(0, i - 1) + range_sum1(i, N - 2)
    if i % 2 == 0 :
        score += A[N - 1]
    
    answer = max(answer, score)

print(answer)