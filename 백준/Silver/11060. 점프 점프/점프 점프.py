# 백준 11060 - 점프 점프
# 분류 : 다이나믹 프로그래밍

N = int(input())
A = list(map(int ,input().split()))

D = [1e9] * N
D[N - 1] = 0
for i in range(N - 2, -1, -1) :
    D[i] = 1e9
    for j in range(1, A[i] + 1) :
        if i + j >= N :
            break

        D[i] = min(D[i], 1 + D[i + j])

if D[0] == 1e9 :
    print(-1)
else :
    print(D[0])