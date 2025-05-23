# 백준 15989 - 1,2,3 더하기 4
# 분류 : 다이나믹 프로그래밍

T = int(input())

D = [[0] *  10001 for _ in range(4)]
D[0][0] = 1
for i in range(1, 4) :
    for j in range(10001) :
        D[i][j] = D[i - 1][j]

        if j >= i :
            D[i][j] += D[i][j - i]
        
for _ in range(T) :
    N = int(input())

    print(D[3][N])