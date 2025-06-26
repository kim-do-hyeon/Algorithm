# 백준 1113 - 수영장 만들기
# 분류 : BFS

import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

heap = []
# 외곽 테두리 넣기
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            heapq.heappush(heap, (board[i][j], i, j))
            visited[i][j] = True

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0

while heap:
    h, r, c = heapq.heappop(heap)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            # 지금 보고 있는 외벽 높이 h보다 낮다면 물 채우기
            if board[nr][nc] < h:
                answer += h - board[nr][nc]
                board[nr][nc] = h
            heapq.heappush(heap, (board[nr][nc], nr, nc))

print(answer)