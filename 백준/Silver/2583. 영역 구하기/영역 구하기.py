# 백준 2583 - 영역 구하기

import sys
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            arr[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def dfs(x, y) :
    global result
    if x < 0 or x >= M or y < 0 or y >= N :
        return 0
    if arr[x][y] == 1 :
        return 0

    arr[x][y] = 1
    result += 1
    for i in range(4) :
        dfs(x + dx[i], y + dy[i])

    return result

answer = []
for i in range(M) :
    for j in range(N) :
        cnt = dfs(i, j)
        if cnt :
            answer.append(cnt)
            result = 0

answer.sort()
print(len(answer))
for i in answer :
    print(i, end = " ")