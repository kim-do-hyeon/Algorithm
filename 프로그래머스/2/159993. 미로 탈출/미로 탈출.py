from collections import deque

def bfs(maps, start, target) :
    R, C = len(maps), len(maps[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]] = True
    
    while queue :
        r, c, dist = queue.popleft()
        
        if maps[r][c] == target :
            return dist
        for i in range(4) :
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and maps[nr][nc] != 'X' :
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1

def solution(maps):
    R, C = len(maps), len(maps[0])
    start = lever = exit = None
    
    for r in range(R) :
        for c in range(C) :
            if maps[r][c] == 'S' :
                start = (r, c)
            elif maps[r][c] == 'L' :
                lever = (r, c)
            elif maps[r][c] == 'E' :
                exit = (r, c)
    
    to_lever = bfs(maps, start, 'L')
    if to_lever == -1 :
        return -1
    
    to_exit = bfs(maps, lever, 'E')
    if to_exit == -1 :
        return -1
    
    
    return to_lever + to_exit

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))