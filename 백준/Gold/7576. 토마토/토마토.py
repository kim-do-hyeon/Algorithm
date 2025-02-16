# 백준 7576 - 토마토
# 분류 : 그래프 이론

from collections import deque

M, N = map(int, input().split())

tomatos = []
for _ in range(N) :
    tomatos.append(list(map(int, input().split())))

queue = deque()

for i in range(N) :
    for j in range(M) :
        if tomatos[i][j] == 1 :
            queue.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue :
    x, y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0 :
            tomatos[nx][ny] = tomatos[x][y] + 1
            queue.append((nx, ny))

result = 0
for i in range(N) :
    for j in range(M) :
        if tomatos[i][j] == 0 :
            print(-1)
            exit()
        result = max(result, tomatos[i][j])
print(result - 1)