# 백준 2637 - 장난감 조립
# 분류 : 위상정렬

from collections import deque
N = int(input())
M = int(input())

adj = [[] for _ in range(N)]
count = [0] * N

for i in range(M) :
    X, Y, K = map(int, input().split())
    X -= 1
    Y -= 1

    adj[X].append((Y, K))
    count[Y] += 1

answer = [0] * N
answer[N - 1] = 1

queue = deque()
for i in range(N) :
    if count[i] == 0 :
        queue.append(i)

while len(queue) != 0 :
    u = queue.popleft()

    for v, w in adj[u] :
        answer[v] += w * answer[u]
        count[v] -= 1

        if count[v] == 0 :
            queue.append(v)

for i in range(N) :
    if len(adj[i]) == 0 :
        print(i + 1, answer[i])