# 백준 1303 - 전쟁 - 전투
# 분류 : DFS/BFS

from collections import deque

N, M = map(int, input().split())

A = [""] * M

for i in range(M) :
    A[i] = input()

def solve(color) :
    result = 0
    visit = [[False] * N for _ in range(M)]
    queue = deque()

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(M) :
        for j in range(N) :
            if A[i][j] != color :
                continue

            if not visit[i][j] :
                queue.append((i, j))
                visit[i][j] = True
                count = 1

                while len(queue) != 0 :
                    r, c = queue.popleft()

                    for k in range(4) :
                        nr, nc = r + dr[k], c + dc[k]
                        if nr < 0 or M <= nr or nc < 0 or N <= nc :
                            continue
                        
                        if A[nr][nc] != color :
                            continue

                        if not visit[nr][nc] :
                            queue.append((nr, nc))
                            visit[nr][nc] = True
                            count += 1
                
                result += count * count
    return result

print(solve('W'), solve('B'))
