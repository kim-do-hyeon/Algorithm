import sys
sys.setrecursionlimit(10000)

R, C = map(int, input().split())
B = [input().strip() for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

answer = 0
visited = [[set() for _ in range(C)] for _ in range(R)]

def dfs(r, c, used, count):
    global answer
    if used in visited[r][c]:
        return
    visited[r][c].add(used)

    answer = max(answer, count)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            char_bit = 1 << (ord(B[nr][nc]) - ord('A'))
            if not (used & char_bit):
                dfs(nr, nc, used | char_bit, count + 1)

start_bit = 1 << (ord(B[0][0]) - ord('A'))
dfs(0, 0, start_bit, 1)

print(answer)