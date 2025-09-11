# [브론즈 2] 백준 1592 - 영식이와 친구들

N, M, L = map(int, input().split())
A = [0] * N
# A[0] = 1
max_ball = 0
index = 0
result = 0
while max_ball != M :
    A[index] += 1
    max_ball = max(max_ball, A[index])
    if max_ball == M :
        break
    if A[index] < M and A[index] % 2 == 1 :
        index += L
        if index >= N :
            index -= N
    elif A[index] < M and A[index] % 2 == 0 :
        index -= L
        if index < 0 :
            index += N
    
    # print(A)
    result += 1
print(result)