# 백준 2636 - 치즈
# 분류 : BFS

import sys
from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

time, last_cheese = 0, 0

def bfs_air() :
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    melt = []

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                visited[nx][ny] = True
                if matrix[nx][ny] == 0 :
                    q.append((nx, ny))
                elif matrix[nx][ny] == 1 :
                    melt.append((nx, ny))
        
    return melt

def count_cheese() :
    return sum(row.count(1) for row in matrix)

while True :
    melt = bfs_air()
    if not melt :
        break
    last_cheese = len(melt)
    for x, y in melt :
        matrix[x][y] = 0
    time += 1

print(time)
print(last_cheese)
