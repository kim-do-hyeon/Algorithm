# 백준 2667 - 단지번호붙이기
# 분류 : BFS

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(G, a, b) :
    n = len(G)
    queue = deque()
    queue.append((a, b))
    G[a][b] = 0
    count = 1

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            if G[nx][ny] == 1 :
                G[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    
    return count

N = int(input())
G = []
for i in range(N) :
    G.append(list(map(int, input())))

cnt = []
for i in range(N) :
    for j in range(N) :
        if G[i][j] == 1 :
            cnt.append(BFS(G, i, j))

cnt.sort()
print(len(cnt))
for i in cnt :
    print(i)
