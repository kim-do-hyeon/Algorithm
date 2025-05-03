from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    visited = [[False] * C for _ in range(R)]
    answer = []
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(R) :
        for c in range(C) :
            if maps[r][c] != 'X' and not visited[r][c] :
                queue = deque()
                queue.append((r, c))
                visited[r][c] = True
                total = int(maps[r][c])
                
                while queue :
                    cr, cc = queue.popleft()
                    for i in range(4) :
                        nr, nc = cr + dr[i], cc + dc[i]
                        if 0 <= nr < R and 0 <= nc < C :
                            if not visited[nr][nc] and maps[nr][nc] != 'X' :
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                total += int(maps[nr][nc])
                answer.append(total)
                
    return sorted(answer) if answer else [-1]