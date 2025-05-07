from collections import deque

R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
N = int(input())
H = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def throw(turn, height):
    row = R - height
    if turn % 2 == 0:
        for col in range(C):
            if B[row][col] == 'x':
                B[row][col] = '.'
                return
    else:
        for col in range(C - 1, -1, -1):
            if B[row][col] == 'x':
                B[row][col] = '.'
                return

def bfs(r, c, visited):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    cluster = [(r, c)]
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and B[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
                cluster.append((nr, nc))
    return cluster

def drop(cluster):
    cluster.sort(reverse=True)
    for r, c in cluster:
        B[r][c] = '.'

    fall = 0
    while True:
        for r, c in cluster:
            nr = r + fall + 1
            if nr >= R or (B[nr][c] == 'x' and (nr, c) not in cluster):
                return fall
        fall += 1

def apply_drop(cluster, fall):
    for r, c in cluster:
        B[r + fall][c] = 'x'

for i in range(N):
    throw(i, H[i])
    
    visited = [[False] * C for _ in range(R)]
    for c in range(C):
        if B[R - 1][c] == 'x' and not visited[R - 1][c]:
            bfs(R - 1, c, visited)

    found = False
    for r in range(R - 1, -1, -1):
        for c in range(C):
            if B[r][c] == 'x' and not visited[r][c]:
                cluster = bfs(r, c, visited)
                f = drop(cluster)
                apply_drop(cluster, f)
                found = True
                break
        if found:
            break

for row in B:
    print(''.join(row))