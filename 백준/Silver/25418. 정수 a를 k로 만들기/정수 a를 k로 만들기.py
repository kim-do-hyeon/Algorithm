# 백준 25418 - 정수 a를 k로 만들기
# 분류 : BFS

from collections import deque
A, K = map(int, input().split())

adj = [[] for _ in range(K + 1)]
for i in range(1, K + 1) :
    if i + 1 <= K :
        adj[i].append(i + 1)
    if 2 * i <= K :
        adj[i].append(2 * i)

visit = [False] * (K + 1)
dist = [-1] * (K + 1)
queue = deque()

queue.append(A)
visit[A] = True
dist[A] = 0

while len(queue) != 0 :
    u = queue.popleft()

    for v in adj[u] :
        if not visit[v] :
            queue.append(v)
            visit[v] = True
            dist[v] = dist[u] + 1

print(dist[K])