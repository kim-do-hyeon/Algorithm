# 백준 2629 - 양팔저울
# 분류 : 다이나믹 프로그래밍

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

D = [[False] * 80002 for _ in range(N)]

# D[i][j] 0 ~ i -> j
# j < 0, 0 -> 40001

zero = 40001

D[0][zero] = True
D[0][zero + A[0]] = True
D[0][zero - A[0]] = True

for i in range(1, N) :
    for j in range(0, 80002) :
        D[i][j] = D[i - 1][j]

        if j - A[i] >= 0 :
            D[i][j] |= D[i - 1][j - A[i]]
        if j + A[i] < 80002 :
            D[i][j] |= D[i - 1][j + A[i]]

for i in range(M) :
    if D[N - 1][zero + B[i]]  :
        print("Y")
    else :
        print("N")