# 백준 4179 - 불!
# 분류 : BFS
# 문제집 - 0x09강 - BFS

from collections import deque
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

fire = [[-1] * C for _ in range(R)]
jihun = [[-1] * C for _ in range(R)]

q1 = deque()
q2 = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R) :
    for j in range(C) :
        if board[i][j] == 'F' :
            q1.append((i, j))
            fire[i][j] = 0
        elif board[i][j] == 'J' :
            q2.append((i, j))
            jihun[i][j] = 0

while q1 :
    x, y = q1.popleft()
    for d in range(4) :
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C :
            if board[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                q1.append((nx, ny))

while q2 :
    x, y = q2.popleft()
    if x == 0 or x == R - 1 or y == 0 or y == C - 1 :
        print(jihun[x][y] + 1)
        exit()
    for d in range(4) :
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C :
            if board[nx][ny] != '#' and jihun[nx][ny] == -1:
                if fire[nx][ny] == -1 or fire[nx][ny] > jihun[x][y] + 1:
                    jihun[nx][ny] = jihun[x][y] + 1
                    q2.append((nx, ny))

print("IMPOSSIBLE")