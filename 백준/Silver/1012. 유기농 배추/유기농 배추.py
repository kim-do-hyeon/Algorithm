# 백준 1012 - 유기농 배추
# 분류 : BFS

from collections import deque


T = int(input())
for _ in range(T) :
    M, N, K = map(int, input().split())

    
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K) :
        x, y = map(int, input().split())
        field[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y) :
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue : 
            cx, cy = queue.popleft()
            for i in range(4) :
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < M and 0 <= ny < N :
                    if field[ny][nx] == 1 and not visited[ny][nx] :
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    count = 0
    for y in range(N) :
        for x in range(M) :
            if field[y][x] == 1 and not visited[y][x] :
                bfs(x, y)
                count += 1
    
    print(count)
