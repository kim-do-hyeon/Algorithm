# 백준 1697 - 숨바꼭질
# 분류 : BFS
# 문제집 - 0x09강 - BFS

from collections import deque

N, K = map(int, input().split())
MAX = 1000001

dist = [-1] * MAX
dist[N] = 0

queue = deque([N])

while queue :
    current = queue.popleft()

    if current == K :
        break

    for next in (current - 1, current + 1, current * 2) :
        if 0 <= next < MAX and dist[next] == -1 :
            dist[next] = dist[current] + 1
            queue.append(next)

print(dist[K])