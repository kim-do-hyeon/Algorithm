# 백준 1932 - 정수 삼각형
# 분류 : 다이나믹 프로그래밍

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

D = [[0] * (i + 1) for i in range(N)]
D[0][0] = A[0][0]

for i in range(1, N) :
    for j in range(i + 1) :
        left, right = 0, 0
        if j > 0 :
            left = A[i][j] + D[i - 1][j - 1]
        if j < i :
            right  = A[i][j] + D[i - 1][j]

        D[i][j] = max(left, right)

print(max(D[N - 1]))